# Biot Savart Field Calculator: Web Dashboard

**Domain:** physics | **Subdomain:** physics | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Biot Savart Field Calculator built as a Web dashboard. The Biot Savart law adds up the magnetic field contributed by every small segment of a current-carrying wire. For loops, solenoids, and straight wires the integral has clean closed forms, but arbitrary shapes need numerical integration along the path. Serves a single-page HTML dashboard of topic metrics plus a JSON metrics endpoint.

**Core concept — Biot Savart Field Calculator:** The Biot Savart law adds up the magnetic field contributed by every small segment of a current-carrying wire. For loops, solenoids, and straight wires the integral has clean closed forms, but arbitrary shapes need numerical integration along the path.

**Why this matters in the real world:** Magnet designers for MRI machines and particle accelerators compute coil fields with Biot Savart codes.

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
cd projects/physics/physics/biot-savart-field-calculator-web_dashboard-advanced
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
