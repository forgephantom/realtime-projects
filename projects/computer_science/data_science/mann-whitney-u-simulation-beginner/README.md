# Mann-Whitney U Test: Simulation (Logistic Growth)

**Domain:** computer_science | **Subdomain:** data_science | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Mann-Whitney U Test built as a Simulation (logistic growth). The Mann-Whitney U test compares two groups by ranks instead of means, needing no normality: it tests whether one group's values tend to exceed the other's. It is the safe choice for skewed data and ordinal scales. Rank-biserial correlation gives the effect size. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Mann-Whitney U Test:** The Mann-Whitney U test compares two groups by ranks instead of means, needing no normality: it tests whether one group's values tend to exceed the other's. It is the safe choice for skewed data and ordinal scales. Rank-biserial correlation gives the effect size.

**Why this matters in the real world:** Non-normal A/B metrics (revenue, latencies) and ordinal survey data use rank tests.

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
cd projects/computer_science/data_science/mann-whitney-u-simulation-beginner
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
