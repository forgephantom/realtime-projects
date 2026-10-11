# Merger Accretion Dilution Simulator: Simulation (Logistic Growth)

**Domain:** business_analyst | **Subdomain:** financial_modeling | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Merger Accretion Dilution Simulator built as a Simulation (logistic growth). A merger is accretive when the combined earnings per share rise after the deal and dilutive when they fall. The model combines the two income statements, adds synergies, subtracts financing costs and new shares, and compares pro-forma EPS to standalone EPS. Accretion math decides whether a deal creates or destroys shareholder value on paper. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Merger Accretion Dilution Simulator:** A merger is accretive when the combined earnings per share rise after the deal and dilutive when they fall. The model combines the two income statements, adds synergies, subtracts financing costs and new shares, and compares pro-forma EPS to standalone EPS. Accretion math decides whether a deal creates or destroys shareholder value on paper.

**Why this matters in the real world:** Corporate development teams run accretion analysis before recommending acquisitions to the board.

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
cd projects/business_analyst/financial_modeling/merger-accretion-sim-simulation-advanced
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
