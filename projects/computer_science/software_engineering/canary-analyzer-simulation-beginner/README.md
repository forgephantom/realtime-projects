# Canary Analyzer: Simulation (Logistic Growth)

**Domain:** computer_science | **Subdomain:** software_engineering | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Canary Analyzer built as a Simulation (logistic growth). Canary deploys shift a slice of traffic to the new version and compare metrics: the analyzer runs statistical tests on error rates and latencies between canary and baseline, promoting on success and rolling back on regression. It automates the judgment call. Metric selection decides what 'regression' means. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Canary Analyzer:** Canary deploys shift a slice of traffic to the new version and compare metrics: the analyzer runs statistical tests on error rates and latencies between canary and baseline, promoting on success and rolling back on regression. It automates the judgment call. Metric selection decides what 'regression' means.

**Why this matters in the real world:** Kayenta (Netflix), Argo Rollouts, and Flagger automate canary analysis.

---

## Features

- `simulate` (`simulate(params, steps, dt)`): Euler-integrate logistic growth; return [(t, value)] rows.
- `print_trajectory` (`print_trajectory(rows, every)`): Print every Nth trajectory row plus the final state.
- `main` (`main()`): Parse args, simulate, and print the trajectory and summary.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Explicit Euler integration of logistic growth. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(steps). See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/software_engineering/canary-analyzer-simulation-beginner
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A sampled trajectory table (t, value) plus start, end, peak, and carrying-capacity summary lines.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
