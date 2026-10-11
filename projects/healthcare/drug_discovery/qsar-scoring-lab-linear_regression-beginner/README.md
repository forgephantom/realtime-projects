# QSAR Scoring Lab: Linear Regression

**Domain:** healthcare | **Subdomain:** drug_discovery | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

QSAR Scoring Lab built as a Linear regression. Quantitative structure-activity relationship models regress measured activity on molecular descriptors, learning which structural features drive potency. A proper train-test split with R-squared and cross-validation guards against overfitting to the training series. Synthetic data with a known linear activity relationship makes model failures easy to diagnose. Fits y = slope*x + intercept by closed-form least squares on seeded synthetic data and reports coefficients, R^2, and predictions.

**Core concept — QSAR Scoring Lab:** Quantitative structure-activity relationship models regress measured activity on molecular descriptors, learning which structural features drive potency. A proper train-test split with R-squared and cross-validation guards against overfitting to the training series. Synthetic data with a known linear activity relationship makes model failures easy to diagnose.

**Why this matters in the real world:** QSAR prioritizes which compounds chemists should synthesize next.

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
cd projects/healthcare/drug_discovery/qsar-scoring-lab-linear_regression-beginner
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
