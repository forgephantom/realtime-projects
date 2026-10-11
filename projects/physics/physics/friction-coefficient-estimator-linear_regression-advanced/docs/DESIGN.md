# Design (LLD) — Friction Coefficient Estimator: Linear Regression

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| generate_data | generate_data(seed, n, slope, intercept, noise) | Generate noisy (x, y) pairs around the true line. |
| fit_least_squares | fit_least_squares(xs, ys) | Closed-form least-squares fit; returns (slope, intercept). |
| r_squared | r_squared(xs, ys, slope, intercept) | Coefficient of determination for the fitted line. |
| main | main() | Parse args, fit, and print coefficients and predictions. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Friction Coefficient Estimator:

| Parameter | Meaning |
|---|---|
| incline_angle | ramp angle in degrees |
| slide_distance | measured slide distance in meters |
| timing_noise | standard deviation of synthetic timer error |

## Algorithm & Complexity

The core of this project is Ordinary least squares, closed-form normal equations.

- **Time complexity:** O(n) to fit n points
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/physics/physics/friction-coefficient-estimator-linear_regression-advanced
python3 src/main.py --help
python3 src/main.py
```

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
