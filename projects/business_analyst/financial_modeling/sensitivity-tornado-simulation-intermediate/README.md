# Sensitivity Tornado Chart: Simulation (Logistic Growth)

**Domain:** business_analyst | **Subdomain:** financial_modeling | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Sensitivity Tornado Chart built as a Simulation (logistic growth). A tornado chart ranks model inputs by how much the output swings when each input moves from low to high. The widest bars sit on top, instantly showing which assumptions deserve diligence. It turns a hundred-line model into a prioritized list of what actually matters. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Sensitivity Tornado Chart:** A tornado chart ranks model inputs by how much the output swings when each input moves from low to high. The widest bars sit on top, instantly showing which assumptions deserve diligence. It turns a hundred-line model into a prioritized list of what actually matters.

**Why this matters in the real world:** Analysts attach tornado charts to investment memos to show which assumptions carry the thesis.

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
cd projects/business_analyst/financial_modeling/sensitivity-tornado-simulation-intermediate
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
