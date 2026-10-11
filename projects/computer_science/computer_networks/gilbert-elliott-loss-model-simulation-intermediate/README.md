# Gilbert-Elliott Loss Model: Simulation (Logistic Growth)

**Domain:** computer_science | **Subdomain:** computer_networks | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Gilbert-Elliott Loss Model built as a Simulation (logistic growth). Real packet loss comes in bursts: the Gilbert-Elliott two-state Markov model (good/bad states with transition probabilities) captures burstiness that independent loss misses. The demo fits the model to traces and simulates realistic loss. Codec and FEC design depend on burst statistics. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Gilbert-Elliott Loss Model:** Real packet loss comes in bursts: the Gilbert-Elliott two-state Markov model (good/bad states with transition probabilities) captures burstiness that independent loss misses. The demo fits the model to traces and simulates realistic loss. Codec and FEC design depend on burst statistics.

**Why this matters in the real world:** VoIP/video codec testing and wireless modeling use bursty loss models.

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
cd projects/computer_science/computer_networks/gilbert-elliott-loss-model-simulation-intermediate
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
