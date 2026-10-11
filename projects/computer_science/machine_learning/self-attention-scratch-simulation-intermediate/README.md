# Self-Attention from Scratch: Simulation (Logistic Growth)

**Domain:** computer_science | **Subdomain:** machine_learning | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Self-Attention from Scratch built as a Simulation (logistic growth). Self-attention lets every position attend to every other: queries, keys, and values derive from the same input, scaled dot-products give weights, and multiple heads learn different relations. Implementing it from scratch on a tiny sequence makes transformers legible. Positional encodings add order. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Self-Attention from Scratch:** Self-attention lets every position attend to every other: queries, keys, and values derive from the same input, scaled dot-products give weights, and multiple heads learn different relations. Implementing it from scratch on a tiny sequence makes transformers legible. Positional encodings add order.

**Why this matters in the real world:** The core of GPT/BERT; implementing it once demystifies the architecture.

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
cd projects/computer_science/machine_learning/self-attention-scratch-simulation-intermediate
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
