# Length of Stay Predictor: Linear Regression

**Domain:** healthcare | **Subdomain:** hospital_operations | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Length of Stay Predictor built as a Linear regression. Length-of-stay models predict discharge timing from diagnosis, procedures, age, and comorbidities, helping case managers plan beds and post-acute placement. Since stays are skewed, models often predict log-days or use survival-style approaches. Synthetic admissions with known stay drivers let developers validate the model. Fits y = slope*x + intercept by closed-form least squares on seeded synthetic data and reports coefficients, R^2, and predictions.

**Core concept — Length of Stay Predictor:** Length-of-stay models predict discharge timing from diagnosis, procedures, age, and comorbidities, helping case managers plan beds and post-acute placement. Since stays are skewed, models often predict log-days or use survival-style approaches. Synthetic admissions with known stay drivers let developers validate the model.

**Why this matters in the real world:** Stay predictions help hospitals plan beds and discharges.

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
cd projects/healthcare/hospital_operations/length-of-stay-predictor-linear_regression-intermediate
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
