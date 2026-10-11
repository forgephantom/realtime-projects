# Pairwise Elo Rating Arena: Web Dashboard

**Domain:** ai | **Subdomain:** model_evaluation | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Pairwise Elo Rating Arena built as a Web dashboard. In a pairwise arena, judges pick the better of two model responses and Elo ratings update from wins and losses, exactly like chess rankings. The expected-score formula turns rating gaps into win probabilities, and the K-factor controls how fast ratings move. Seeded win histories let you verify the ratings converge on the true skill order. Serves a single-page HTML dashboard of topic metrics plus a JSON metrics endpoint.

**Core concept — Pairwise Elo Rating Arena:** In a pairwise arena, judges pick the better of two model responses and Elo ratings update from wins and losses, exactly like chess rankings. The expected-score formula turns rating gaps into win probabilities, and the K-factor controls how fast ratings move. Seeded win histories let you verify the ratings converge on the true skill order.

**Why this matters in the real world:** Public model leaderboards rank chat models from thousands of blind human preference votes.

---

## Features

- **DashboardHandler**: Serves the dashboard HTML page and a JSON metrics endpoint.
- `metric_rows` (`metric_rows(seed, count)`): Generate deterministic synthetic metric rows.
- `render_page` (`render_page(seed, count)`): Render the full dashboard HTML page.
- `start_server` (`start_server(port, seed, count)`): Bind a ThreadingHTTPServer on 127.0.0.1 and serve it in a thread.
- `run_self_test` (`run_self_test(base_url, seed, count)`): Fetch the page and metrics endpoint; print a verification summary.
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

The project is built around Server-side HTML rendering of a metrics table. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) to render n metric rows. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/ai/model_evaluation/pairwise-elo-arena-web_dashboard-beginner
python3 src/main.py --help
python3 src/main.py
```
Add --serve to keep the dashboard running instead of self-testing.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Status lines for GET / and GET /api/metrics, a five-row metric sample, and a SELF-TEST PASSED/FAILED line.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
