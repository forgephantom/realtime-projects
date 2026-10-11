# Net Promoter Score Simulator: Kpi_Dashboard

**Domain:** business_analyst | **Subdomain:** kpi_dashboards | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Net Promoter Score Simulator built as a kpi_dashboard. Net promoter score comes from a single 0 to 10 question: promoters score 9 or 10, passives 7 or 8, detractors 6 or below, and NPS is promoters minus detractors. The number is simple, but its power is in the trend and the verbatim themes behind it. Simulating responses shows how sample size and sentiment mix move the score. A KPI dashboard that computes growth rate, churn, CAC, and LTV from seeded synthetic business data and renders an ASCII dashboard with sparklines.

**Core concept — Net Promoter Score Simulator:** Net promoter score comes from a single 0 to 10 question: promoters score 9 or 10, passives 7 or 8, detractors 6 or below, and NPS is promoters minus detractors. The number is simple, but its power is in the trend and the verbatim themes behind it. Simulating responses shows how sample size and sentiment mix move the score.

**Why this matters in the real world:** Product and CX teams track NPS quarterly and tie detractor themes to roadmap fixes.

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
cd projects/business_analyst/kpi_dashboards/nps-simulator-kpi_dashboard-beginner
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
