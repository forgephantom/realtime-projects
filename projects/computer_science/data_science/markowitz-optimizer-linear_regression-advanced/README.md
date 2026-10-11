# Markowitz Portfolio Optimizer: Linear Regression

**Domain:** computer_science | **Subdomain:** data_science | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Markowitz Portfolio Optimizer built as a Linear regression. Markowitz balances return against risk: the optimizer finds minimum-variance portfolios for target returns via quadratic programming (lite: grid over weights or analytical two-asset), tracing the efficient frontier. The Sharpe-maximizing tangency portfolio is the headline result. Estimation error is the practical enemy. Fits y = slope*x + intercept by closed-form least squares on seeded synthetic data and reports coefficients, R^2, and predictions.

**Core concept — Markowitz Portfolio Optimizer:** Markowitz balances return against risk: the optimizer finds minimum-variance portfolios for target returns via quadratic programming (lite: grid over weights or analytical two-asset), tracing the efficient frontier. The Sharpe-maximizing tangency portfolio is the headline result. Estimation error is the practical enemy.

**Why this matters in the real world:** Asset allocation, robo-advisors, and fund construction use mean-variance optimization.

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
cd projects/computer_science/data_science/markowitz-optimizer-linear_regression-advanced
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
