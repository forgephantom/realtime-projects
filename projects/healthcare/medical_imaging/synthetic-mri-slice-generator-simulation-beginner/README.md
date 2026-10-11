# Synthetic MRI Slice Generator: Simulation (Logistic Growth)

**Domain:** healthcare | **Subdomain:** medical_imaging | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Synthetic MRI Slice Generator built as a Simulation (logistic growth). Synthetic MRI slices are built from geometric phantoms, such as a head model made of overlapping ellipses, each assigned a tissue-like intensity. This mirrors how real scanners translate proton density and relaxation properties into grayscale values. Seeded generation gives developers a ground truth for testing segmentation and detection code with no patient data involved. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — Synthetic MRI Slice Generator:** Synthetic MRI slices are built from geometric phantoms, such as a head model made of overlapping ellipses, each assigned a tissue-like intensity. This mirrors how real scanners translate proton density and relaxation properties into grayscale values. Seeded generation gives developers a ground truth for testing segmentation and detection code with no patient data involved.

**Why this matters in the real world:** Algorithm teams use phantom data to unit-test reconstruction and segmentation pipelines.

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
cd projects/healthcare/medical_imaging/synthetic-mri-slice-generator-simulation-beginner
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
