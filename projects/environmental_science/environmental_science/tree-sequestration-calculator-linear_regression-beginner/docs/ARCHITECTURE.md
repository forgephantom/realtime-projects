# Architecture (HLD) — Tree Sequestration Calculator: Linear Regression

## Problem & Users

Tree Sequestration Calculator built as a Linear regression. A growing tree locks away carbon in its wood, roughly proportional to its biomass, which allometric equations estimate from trunk diameter and species. The calculator converts a tree inventory into tons of CO2 sequestered per year. Fits y = slope*x + intercept by closed-form least squares on seeded synthetic data and reports coefficients, R^2, and predictions.

The intended user is a student or engineer working in environmental_science (environmental_science) who needs a working, runnable reference for Tree Sequestration Calculator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_data (noisy line, known slope/intercept)
(x, y) -> fit_least_squares -> (slope, intercept)
fit -> r_squared + prediction table
```

## Storage

In-memory only: generated points and fitted coefficients exist for the run and are not persisted.

## Scaling & Limits

The closed-form fit is O(n) and single-feature; multi-feature regression would need matrix routines.

## Trade-offs

Closed-form least squares is exact and dependency-free for one feature, but does not generalize to regularization or multivariate fits without numpy.

## Failure Handling

A zero-variance x sample would make the denominator zero; the fit guards this by returning slope 0.0, and an empty y list cannot occur since n >= 1.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
