# Design (LLD) — Server-Sent Events Feed: Chat Server

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| ChatServer | Tiny TCP chat relay bound to 127.0.0.1 on an ephemeral port, one thread per client. |
| ChatClient | Blocking-line chat client with a background reader thread and a received-message inbox. |

## Functions

| Function | Signature | Description |
|---|---|---|
| ChatServer.start | start(self) -> None | Begin accepting clients in a background thread. |
| ChatServer.broadcast | broadcast(self, data: bytes, exclude=None) -> None | Send raw bytes to every client except exclude. |
| ChatServer.client_count | client_count(self) -> int | Number of currently connected clients. |
| ChatServer.shutdown | shutdown(self) -> None | Stop accepting, disconnect clients, and release the socket. |
| ChatClient.send | send(self, text: str) -> None | Send one chat line, prefixed with this client's name. |
| ChatClient.received | received(self) -> list | A snapshot of every line received so far. |
| ChatClient.close | close(self) -> None | Stop the reader thread and release the socket. |
| run_self_test | run_self_test(messages_per_client: int) -> int | Spin up a server plus two scripted clients, verify the relay, print the transcript. |
| run_serve | run_serve() -> int | Run the server persistently until Ctrl-C. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Self-test by default; persistent server with --serve. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Server-Sent Events Feed:

| Parameter | Meaning |
|---|---|
| events | named event types with payload schemas |
| retry_ms | client reconnection delay hint |
| heartbeat_interval | keep-alive comment cadence |

## Algorithm & Complexity

The core of this project is Thread-per-client TCP relay with line-based broadcast.

- **Time complexity:** O(n) broadcast per message over n clients
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/web_development/server-sent-events-feed-chat_server-beginner
python3 src/main.py --help
python3 src/main.py
```
--serve runs the server persistently; --messages sets the per-client message count for the self-test.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
