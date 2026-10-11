# Model Version Manager: Rest Api Service

**Domain:** ai | **Subdomain:** mlops | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Model Version Manager built as a REST API service. Model versions pin an exact artifact plus its training context: data snapshot, code commit, and hyperparameters. Semantic-style versioning separates breaking changes from improvements, and aliases like champion point at the current production version. The manager resolves aliases and diffs version metadata. Serves a small JSON REST API for the topic records, with health, list, create, and stats endpoints.

**Core concept — Model Version Manager:** Model versions pin an exact artifact plus its training context: data snapshot, code commit, and hyperparameters. Semantic-style versioning separates breaking changes from improvements, and aliases like champion point at the current production version. The manager resolves aliases and diffs version metadata.

**Why this matters in the real world:** Deployment pipelines pin exact model versions for reproducible rollouts.

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
cd projects/ai/mlops/model-version-manager-rest_api-beginner
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
