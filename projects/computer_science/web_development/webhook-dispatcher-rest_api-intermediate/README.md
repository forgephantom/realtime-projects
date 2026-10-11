# Webhook Dispatcher with Retries: Rest Api Service

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Webhook Dispatcher with Retries built as a REST API service. Webhooks let a service notify subscribers about events by POSTing JSON to their registered URLs, but the open internet means deliveries fail. A robust dispatcher signs each payload, retries with exponential backoff and jitter, honors Retry-After, and dead-letters endpoints that stay down. Idempotency keys let receivers deduplicate the redeliveries that retries inevitably cause. Serves a small JSON REST API for the topic records, with health, list, create, and stats endpoints.

**Core concept — Webhook Dispatcher with Retries:** Webhooks let a service notify subscribers about events by POSTing JSON to their registered URLs, but the open internet means deliveries fail. A robust dispatcher signs each payload, retries with exponential backoff and jitter, honors Retry-After, and dead-letters endpoints that stay down. Idempotency keys let receivers deduplicate the redeliveries that retries inevitably cause.

**Why this matters in the real world:** Stripe, GitHub, and Shopify webhooks all use signed, retried delivery; receivers implement the verification side.

---

## Features

- **Store**: In-memory record collection backing the API.
- **ApiHandler**: BaseHTTPRequestHandler routing GET/POST to the Store.
- `seed_records` (`seed_records(seed, count)`): Generate deterministic synthetic records.
- `Store.list_records` (`Store.list_records(self)`): Return a copy of all stored records.
- `Store.add_record` (`Store.add_record(self, payload)`): Append a record built from the posted JSON payload.
- `Store.stats` (`Store.stats(self)`): Aggregate record count, mean value, and active count.
- `start_server` (`start_server(port, seed, count)`): Bind a ThreadingHTTPServer on 127.0.0.1 and serve it in a thread.
- `run_self_test` (`run_self_test(base_url, seed)`): Exercise every endpoint with urllib and print a results table.
- `main` (`main()`): Parse args; self-test by default or serve with --serve.

---

## Tech Stack

Python 3.8+, stdlib: argparse, json, http.server, urllib

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around In-memory CRUD over HTTP with JSON bodies. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) per list/stats request, O(1) per create. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/web_development/webhook-dispatcher-rest_api-intermediate
python3 src/main.py --help
python3 src/main.py
```
Add --serve to keep the server running instead of self-testing.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A results table with one line per exercised endpoint (method, path, status code, summary) plus a SELF-TEST PASSED/FAILED line.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
