# Pub/Sub Message Broker: Chat Server

**Domain:** computer_science | **Subdomain:** computer_networks | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Pub/Sub Message Broker built as a chat server. Message brokers decouple producers and consumers: the broker manages topics, subscriptions, at-least-once delivery with ACKs, and redelivery on timeout. It buffers bursts producers would otherwise drop. The demo shows the reliability contract explicitly. A loopback-only TCP chat server that relays messages between clients, with a default self-test that verifies delivery end to end.

**Core concept — Pub/Sub Message Broker:** Message brokers decouple producers and consumers: the broker manages topics, subscriptions, at-least-once delivery with ACKs, and redelivery on timeout. It buffers bursts producers would otherwise drop. The demo shows the reliability contract explicitly.

**Why this matters in the real world:** RabbitMQ, NATS, and Google Pub/Sub broker messages between services.

---

## Features

- **ChatServer**: Tiny TCP chat relay bound to 127.0.0.1 on an ephemeral port, one thread per client.
- **ChatClient**: Blocking-line chat client with a background reader thread and a received-message inbox.
- `ChatServer.start` (`start(self) -> None`): Begin accepting clients in a background thread.
- `ChatServer.broadcast` (`broadcast(self, data: bytes, exclude=None) -> None`): Send raw bytes to every client except exclude.
- `ChatServer.client_count` (`client_count(self) -> int`): Number of currently connected clients.
- `ChatServer.shutdown` (`shutdown(self) -> None`): Stop accepting, disconnect clients, and release the socket.
- `ChatClient.send` (`send(self, text: str) -> None`): Send one chat line, prefixed with this client's name.
- `ChatClient.received` (`received(self) -> list`): A snapshot of every line received so far.
- `ChatClient.close` (`close(self) -> None`): Stop the reader thread and release the socket.
- `run_self_test` (`run_self_test(messages_per_client: int) -> int`): Spin up a server plus two scripted clients, verify the relay, print the transcript.
- `run_serve` (`run_serve() -> int`): Run the server persistently until Ctrl-C.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Self-test by default; persistent server with --serve.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, socket, threading, time

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Thread-per-client TCP relay with line-based broadcast. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) broadcast per message over n clients. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/computer_networks/pubsub-message-broker-chat_server-beginner
python3 src/main.py --help
python3 src/main.py
```
--serve runs the server persistently; --messages sets the per-client message count for the self-test.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints each client's received transcript plus a PASS/FAIL relay check; --serve prints the bound address and runs until Ctrl-C.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
