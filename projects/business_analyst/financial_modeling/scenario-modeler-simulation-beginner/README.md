# Scenario Model Comparator: Simulation (Logistic Growth)

**Domain:** business_analyst | **Subdomain:** financial_modeling | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Scenario Model Comparator built as a Simulation (logistic growth). Scenario modeling reruns the same financial model under base, upside, and downside assumptions to bound the outcome range. The discipline is keeping scenarios internally consistent: a downside case cannot assume strong pricing and weak volume at once. Comparing scenario outputs shows which decisions are robust and which bet everything on one future. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Scenario Model Comparator:** Scenario modeling reruns the same financial model under base, upside, and downside assumptions to bound the outcome range. The discipline is keeping scenarios internally consistent: a downside case cannot assume strong pricing and weak volume at once. Comparing scenario outputs shows which decisions are robust and which bet everything on one future.

**Why this matters in the real world:** Boards review scenario packs to approve plans that survive the downside, not just the base case.

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
cd projects/business_analyst/financial_modeling/scenario-modeler-simulation-beginner
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
