# HTTP Cache Header Advisor: Api Client Sim

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

HTTP Cache Header Advisor built as a API client sim. Cache-Control, Expires, and validators like ETag decide how long browsers and CDNs may reuse a response without asking again. Immutable hashed assets get long max-age with immutable, while personalized HTML gets no-store or short private caching. The advisor inspects a resource's change frequency and personalization to recommend the right header set. A simulated REST API client that paginates through an in-process fake API, retrying simulated server errors with backoff.

**Core concept — HTTP Cache Header Advisor:** Cache-Control, Expires, and validators like ETag decide how long browsers and CDNs may reuse a response without asking again. Immutable hashed assets get long max-age with immutable, while personalized HTML gets no-store or short private caching. The advisor inspects a resource's change frequency and personalization to recommend the right header set.

**Why this matters in the real world:** CDN cache-rule configuration at Cloudflare, Fastly, and Akamai is this decision encoded as rules.

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
cd projects/computer_science/web_development/http-cache-headers-advisor-api_client_sim-beginner
python3 src/main.py --help
python3 src/main.py
```
--per-page and --max-retries tune the demo; item count and simulated failures come from {'resource_profile': 'change frequency and personalization flags', 'cdn_present': 'whether a shared cache sits in front', 'stale_policy': 'stale-while-revalidate and stale-if-error windows'}.

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
