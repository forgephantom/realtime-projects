# Cipher Suite Negotiator: Api Client Sim

**Domain:** computer_science | **Subdomain:** computer_networks | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Cipher Suite Negotiator built as a API client sim. Cipher suites bundle key exchange, authentication, bulk cipher, and hash: the negotiator intersects client offers with server preferences, selecting the strongest mutual option and failing closed on none. It demonstrates why server preference order matters and how weak suites get excluded. A simulated REST API client that paginates through an in-process fake API, retrying simulated server errors with backoff.

**Core concept — Cipher Suite Negotiator:** Cipher suites bundle key exchange, authentication, bulk cipher, and hash: the negotiator intersects client offers with server preferences, selecting the strongest mutual option and failing closed on none. It demonstrates why server preference order matters and how weak suites get excluded.

**Why this matters in the real world:** TLS servers configure cipher preferences; the handshake negotiates per connection.

---

## Features

- **APIError**: Raised when a simulated request fails after all retries.
- **FakeAPI**: In-process fake HTTP-like API: no sockets, no network; serves paginated items.
- **APIClient**: Tiny REST-style client with retries, pagination helpers, and a request history.
- `FakeAPI.handle` (`handle(self, method: str, path: str, params: dict) -> tuple`): Process one request; return (status_code, body_dict).
- `APIClient.request` (`request(self, method: str, path: str, params: dict = None) -> dict`): Send one request, retrying simulated 500s with a small backoff.
- `APIClient.list_all` (`list_all(self, per_page: int = 5) -> list`): Fetch every page of /items and return the combined item list.
- `run_demo` (`run_demo(seed: int, per_page: int, max_retries: int) -> int`): Paginate through the fake API (surviving simulated 500s) and report.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Parse flags and run the API client demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, time

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Paginated fetching with retry-on-500 and linear backoff. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(pages) requests to list all items. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/computer_networks/cipher-suite-negotiator-api_client_sim-advanced
python3 src/main.py --help
python3 src/main.py
```
--per-page and --max-retries tune the demo; item count and simulated failures come from {'client_offers': 'suites the client proposes', 'server_pref': 'server preference order', 'weak': 'suites considered unacceptable'}.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints the fetched item table, a single-item fetch, and the full request history showing retries after simulated 500s.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
