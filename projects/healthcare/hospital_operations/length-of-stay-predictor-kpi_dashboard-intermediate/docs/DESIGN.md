# Design (LLD) — Length of Stay Predictor: Kpi_Dashboard

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| generate_business_data | generate_business_data(seed: int, months: int = 12) -> dict | Seeded 12-month synthetic series: revenue, users, adds, churn, spend. |
| compute_kpis | compute_kpis(data: dict) -> dict | Growth rate, churn rate, CAC, and LTV from the series. |
| sparkline | sparkline(values: list) -> str | Map a numeric series to unicode block sparkline characters. |
| render_dashboard | render_dashboard(data: dict, kpis: dict) -> str | Format the KPI values and sparklines as an ASCII dashboard. |
| run_demo | run_demo(seed: int) -> int | Seeded demo: generate data, compute KPIs, print the dashboard. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Entry point: seeded KPI dashboard demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Length of Stay Predictor:

| Parameter | Meaning |
|---|---|
| admission_count | admissions in the training set |
| feature_count | predictor features used |
| seed | random seed for admission generation |
| los_cap_days | maximum stay modeled |

## Algorithm & Complexity

The core of this project is Seeded geometric-growth business series; KPIs from period ratios: growth, churn, CAC, and LTV from ARPU over churn..

- **Time complexity:** O(M) over M months of synthetic data; all KPI math is O(1) on aggregates.
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/healthcare/hospital_operations/length-of-stay-predictor-kpi_dashboard-intermediate
python3 src/main.py --help
python3 src/main.py
```
--months sets the synthetic history length; values are seeded and reproducible.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
