# Robots.txt Parser: Api Client Sim

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Robots.txt Parser built as a API client sim. Robots.txt tells crawlers which paths they may fetch: the parser reads user-agent groups, Allow/Disallow rules with longest-match precedence, Crawl-delay, and Sitemap pointers. It answers can-fetch queries for any crawler and URL. Respecting it is voluntary but universal among legitimate search engines. A simulated REST API client that paginates through an in-process fake API, retrying simulated server errors with backoff.

**Core concept — Robots.txt Parser:** Robots.txt tells crawlers which paths they may fetch: the parser reads user-agent groups, Allow/Disallow rules with longest-match precedence, Crawl-delay, and Sitemap pointers. It answers can-fetch queries for any crawler and URL. Respecting it is voluntary but universal among legitimate search engines.

**Why this matters in the real world:** Googlebot, Bingbot, and every SEO crawler consult robots.txt; sites use it to keep staging and admin paths uncrawled.

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
cd projects/computer_science/web_development/robots-txt-parser-api_client_sim-beginner
python3 src/main.py --help
python3 src/main.py
```
--per-page and --max-retries tune the demo; item count and simulated failures come from {'user_agents': 'crawler identities to evaluate', 'default_policy': 'allow vs disallow when no rule matches', 'crawl_delay': 'per-agent delay seconds honored'}.

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
