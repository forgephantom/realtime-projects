# Design (LLD) — Service Banner Grabber: Api Client Sim

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| APIError | Raised when a simulated request fails after all retries. |
| FakeAPI | In-process fake HTTP-like API: no sockets, no network; serves paginated items. |
| APIClient | Tiny REST-style client with retries, pagination helpers, and a request history. |

## Functions

| Function | Signature | Description |
|---|---|---|
| FakeAPI.handle | handle(self, method: str, path: str, params: dict) -> tuple | Process one request; return (status_code, body_dict). |
| APIClient.request | request(self, method: str, path: str, params: dict = None) -> dict | Send one request, retrying simulated 500s with a small backoff. |
| APIClient.list_all | list_all(self, per_page: int = 5) -> list | Fetch every page of /items and return the combined item list. |
| run_demo | run_demo(seed: int, per_page: int, max_retries: int) -> int | Paginate through the fake API (surviving simulated 500s) and report. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Parse flags and run the API client demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Service Banner Grabber:

| Parameter | Meaning |
|---|---|
| ports | target ports |
| signatures | banner-to-service mapping |
| timeout | read timeout |

## Algorithm & Complexity

The core of this project is Paginated fetching with retry-on-500 and linear backoff.

- **Time complexity:** O(pages) requests to list all items
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/computer_networks/banner-grabber-api_client_sim-beginner
python3 src/main.py --help
python3 src/main.py
```
--per-page and --max-retries tune the demo; item count and simulated failures come from {'ports': 'target ports', 'signatures': 'banner-to-service mapping', 'timeout': 'read timeout'}.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
