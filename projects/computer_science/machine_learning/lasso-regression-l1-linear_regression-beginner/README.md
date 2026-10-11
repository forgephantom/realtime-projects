# Lasso Regression (L1): Linear Regression

**Domain:** computer_science | **Subdomain:** machine_learning | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Lasso Regression (L1) built as a Linear regression. Lasso penalizes the sum of absolute coefficient values, which drives some coefficients exactly to zero and performs automatic feature selection. Coordinate descent optimizes it one coefficient at a time with soft thresholding. The sparsity makes lasso a favorite when only a few features truly matter. Fits y = slope*x + intercept by closed-form least squares on seeded synthetic data and reports coefficients, R^2, and predictions.

**Core concept — Lasso Regression (L1):** Lasso penalizes the sum of absolute coefficient values, which drives some coefficients exactly to zero and performs automatic feature selection. Coordinate descent optimizes it one coefficient at a time with soft thresholding. The sparsity makes lasso a favorite when only a few features truly matter.

**Why this matters in the real world:** Gene-expression analysis and sparse signal recovery use lasso for feature selection.

---

## Features

- `generate_data` (`generate_data(seed, n, slope, intercept, noise)`): Generate noisy (x, y) pairs around the true line.
- `fit_least_squares` (`fit_least_squares(xs, ys)`): Closed-form least-squares fit; returns (slope, intercept).
- `r_squared` (`r_squared(xs, ys, slope, intercept)`): Coefficient of determination for the fitted line.
- `main` (`main()`): Parse args, fit, and print coefficients and predictions.

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

The project is built around Ordinary least squares, closed-form normal equations. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n) to fit n points. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/machine_learning/lasso-regression-l1-linear_regression-beginner
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

True vs fitted line coefficients, R^2, and an 8-row prediction table (x, y_true, y_pred, residual).

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
