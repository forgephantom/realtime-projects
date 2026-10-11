# Meta Tag Preview Generator: Web Dashboard

**Domain:** computer_science | **Subdomain:** web_development | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Meta Tag Preview Generator built as a Web dashboard. Social previews come from meta tags: the generator parses Open Graph and Twitter Card tags, validates required fields and image dimensions, and renders a text mock of how the link card will look. Missing or oversized tags produce specific warnings. It catches the 'why does my share look wrong' class of bugs before publishing. Serves a single-page HTML dashboard of topic metrics plus a JSON metrics endpoint.

**Core concept — Meta Tag Preview Generator:** Social previews come from meta tags: the generator parses Open Graph and Twitter Card tags, validates required fields and image dimensions, and renders a text mock of how the link card will look. Missing or oversized tags produce specific warnings. It catches the 'why does my share look wrong' class of bugs before publishing.

**Why this matters in the real world:** Social-share debuggers (Meta, X, LinkedIn) and CMS SEO plugins validate these tags pre-publish.

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
cd projects/computer_science/web_development/meta-tag-preview-generator-web_dashboard-beginner
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
