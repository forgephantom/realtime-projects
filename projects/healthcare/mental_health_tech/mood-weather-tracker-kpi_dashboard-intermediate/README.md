# Mood Weather Tracker: Kpi_Dashboard

**Domain:** healthcare | **Subdomain:** mental_health_tech | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Mood Weather Tracker built as a kpi_dashboard. Mood weather metaphors map feelings to weather, sunny, cloudy, stormy, making daily check-ins quick and expressive. Aggregating metaphors over time shows emotional seasons without clinical language. Synthetic check-in series with known metaphor distributions verify the aggregation. A KPI dashboard that computes growth rate, churn, CAC, and LTV from seeded synthetic business data and renders an ASCII dashboard with sparklines.

**Core concept — Mood Weather Tracker:** Mood weather metaphors map feelings to weather, sunny, cloudy, stormy, making daily check-ins quick and expressive. Aggregating metaphors over time shows emotional seasons without clinical language. Synthetic check-in series with known metaphor distributions verify the aggregation.

**Why this matters in the real world:** Metaphor check-ins lower the barrier to daily emotional reflection.

---

## Features

- `generate_business_data` (`generate_business_data(seed: int, months: int = 12) -> dict`): Seeded 12-month synthetic series: revenue, users, adds, churn, spend.
- `compute_kpis` (`compute_kpis(data: dict) -> dict`): Growth rate, churn rate, CAC, and LTV from the series.
- `sparkline` (`sparkline(values: list) -> str`): Map a numeric series to unicode block sparkline characters.
- `render_dashboard` (`render_dashboard(data: dict, kpis: dict) -> str`): Format the KPI values and sparklines as an ASCII dashboard.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: generate data, compute KPIs, print the dashboard.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded KPI dashboard demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, statistics

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Seeded geometric-growth business series; KPIs from period ratios: growth, churn, CAC, and LTV from ARPU over churn.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(M) over M months of synthetic data; all KPI math is O(1) on aggregates.. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/healthcare/mental_health_tech/mood-weather-tracker-kpi_dashboard-intermediate
python3 src/main.py --help
python3 src/main.py
```
--months sets the synthetic history length; values are seeded and reproducible.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints an ASCII dashboard box with four KPIs, monthly revenue/user sparklines, and the raw monthly table.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
