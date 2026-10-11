# Price Elasticity Estimator: Linear Regression

**Domain:** computer_science | **Subdomain:** data_science | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Price Elasticity Estimator built as a Linear regression. Elasticity measures demand's price sensitivity: the estimator fits log-log demand models where the coefficient is the elasticity directly, handling promotions and seasonality as controls. It drives pricing: |elasticity|>1 means cut prices to grow revenue. Identification needs price variation, which the demo plants. Fits y = slope*x + intercept by closed-form least squares on seeded synthetic data and reports coefficients, R^2, and predictions.

**Core concept — Price Elasticity Estimator:** Elasticity measures demand's price sensitivity: the estimator fits log-log demand models where the coefficient is the elasticity directly, handling promotions and seasonality as controls. It drives pricing: |elasticity|>1 means cut prices to grow revenue. Identification needs price variation, which the demo plants.

**Why this matters in the real world:** Revenue management (airlines, retail pricing) estimates elasticities for pricing.

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
cd projects/computer_science/data_science/price-elasticity-estimator-linear_regression-intermediate
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
