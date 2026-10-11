# Design (LLD) — Predator-Prey Cycle Simulator: Web Dashboard

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| DashboardHandler | Serves the dashboard HTML page and a JSON metrics endpoint. |

## Functions

| Function | Signature | Description |
|---|---|---|
| metric_rows | metric_rows(seed, count) | Generate deterministic synthetic metric rows. |
| render_page | render_page(seed, count) | Render the full dashboard HTML page. |
| start_server | start_server(port, seed, count) | Bind a ThreadingHTTPServer on 127.0.0.1 and serve it in a thread. |
| run_self_test | run_self_test(base_url, seed, count) | Fetch the page and metrics endpoint; print a verification summary. |
| main | main() | Parse args; self-test by default or serve with --serve. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Predator-Prey Cycle Simulator:

| Parameter | Meaning |
|---|---|
| alpha | prey growth rate |
| beta | predation rate |
| years | simulation years |

## Algorithm & Complexity

The core of this project is Server-side HTML rendering of a metrics table.

- **Time complexity:** O(n) to render n metric rows
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/environmental_science/environmental_science/lotka-volterra-simulator-web_dashboard-beginner
python3 src/main.py --help
python3 src/main.py
```
Add --serve to keep the dashboard running instead of self-testing.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
