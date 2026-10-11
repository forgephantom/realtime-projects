# Inference Autoscaler Simulator: Simulation (Logistic Growth)

**Domain:** ai | **Subdomain:** mlops | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Inference Autoscaler Simulator built as a Simulation (logistic growth). Inference autoscalers add and remove serving replicas as request rate changes: target metrics like queue depth or GPU utilization drive scaling decisions, with cooldowns preventing flapping. Predictive scaling pre-warms capacity ahead of known peaks. The simulator replays seeded traffic patterns and measures cost versus SLO violations. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Inference Autoscaler Simulator:** Inference autoscalers add and remove serving replicas as request rate changes: target metrics like queue depth or GPU utilization drive scaling decisions, with cooldowns preventing flapping. Predictive scaling pre-warms capacity ahead of known peaks. The simulator replays seeded traffic patterns and measures cost versus SLO violations.

**Why this matters in the real world:** Cloud inference endpoints autoscale replicas to meet demand spikes.

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
cd projects/ai/mlops/resource-autoscaler-simulation-intermediate
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
