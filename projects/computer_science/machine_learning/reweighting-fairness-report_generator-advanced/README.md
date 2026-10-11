# Reweighting for Fairness: Report Generator

**Domain:** computer_science | **Subdomain:** machine_learning | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Reweighting for Fairness built as a report generator. Reweighting gives training examples weights inversely proportional to their group-label frequency, so the learner optimizes as if groups were balanced. It is a preprocessing fix needing no model changes. The demo shows disparity metrics improving with small accuracy cost. A report generator that builds seeded synthetic data, aggregates it, and writes a Markdown report with summary and per-service tables.

**Core concept — Reweighting for Fairness:** Reweighting gives training examples weights inversely proportional to their group-label frequency, so the learner optimizes as if groups were balanced. It is a preprocessing fix needing no model changes. The demo shows disparity metrics improving with small accuracy cost.

**Why this matters in the real world:** IBM AI Fairness 360 includes reweighting as a standard bias-mitigation technique.

---

## Features

- `generate_records` (`generate_records(n: int, rng: random.Random) -> list`): Build n seeded synthetic measurement records for the demo.
- `summarize` (`summarize(records: list) -> dict`): Aggregate totals, per-service rollups, error rate, and latency peaks.
- `render_markdown` (`render_markdown(title: str, summary: dict, records: list) -> str`): Render the summary and sample rows as a Markdown document.
- `write_report` (`write_report(path: str, text: str) -> str`): Write the Markdown report, creating parent folders; return the path.
- `run_demo` (`run_demo(seed: int, n_rows: int, out_path: str) -> int`): Generate data, summarize it, write the report, print a summary.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Parse flags and run the report demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, os, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Seeded synthetic data generation, aggregation rollups, Markdown rendering. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) to generate and summarize n records. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/machine_learning/reweighting-fairness-report_generator-advanced
python3 src/main.py --help
python3 src/main.py
```
--rows sets the record count; --out sets the report path (default ./demo_output/report.md); --title sets the heading.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints aggregate stats to stdout and writes a Markdown report with summary, per-service, and sample-row tables.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
