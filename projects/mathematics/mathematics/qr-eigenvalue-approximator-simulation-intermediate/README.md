# QR Algorithm Eigenvalue Approximator: Simulation (Logistic Growth)

**Domain:** mathematics | **Subdomain:** mathematics | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

QR Algorithm Eigenvalue Approximator built as a Simulation (logistic growth). The QR algorithm repeatedly factors a matrix into orthogonal Q times upper-triangular R and multiplies them back in reverse order; the iterates converge to reveal the eigenvalues on the diagonal. It is the standard dense eigensolver in numerical libraries. This educational version runs it on small symmetric matrices with shift acceleration. Euler-integrates logistic growth dP/dt = r*P*(1-P/K) and prints the trajectory table with summary statistics.

**Core concept — QR Algorithm Eigenvalue Approximator:** The QR algorithm repeatedly factors a matrix into orthogonal Q times upper-triangular R and multiplies them back in reverse order; the iterates converge to reveal the eigenvalues on the diagonal. It is the standard dense eigensolver in numerical libraries. This educational version runs it on small symmetric matrices with shift acceleration.

**Why this matters in the real world:** Eigenvalue solvers drive vibration analysis, quantum chemistry, and Google's original PageRank computations.

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
cd projects/mathematics/mathematics/qr-eigenvalue-approximator-simulation-intermediate
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
