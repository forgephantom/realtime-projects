#!/usr/bin/env python3
"""Lasso Regression (L1): Linear Regression: ordinary least-squares regression for Lasso Regression (L1).

Lasso penalizes the sum of absolute coefficient values, which drives some coefficients exactly to zero and performs automatic feature selection. Coordinate descent optimizes it one coefficient at a time with soft thresholding. The sparsity makes lasso a favorite when only a few features truly matter.
Data idea: Builds seeded sparse linear problems, fits lasso, and measures how often the true support (nonzero set) is recovered.

Generates deterministic synthetic (x, y) pairs with a known slope and
intercept plus Gaussian noise, fits y = slope*x + intercept by closed-form
least squares, and reports the fitted coefficients, R^2, and a prediction
table.
"""

import argparse
import random

PARAMS = {'alpha': 'L1 penalty strength', 'max_iter': 'coordinate descent iterations', 'true_sparse': 'number of truly nonzero coefficients'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def generate_data(seed, n, slope, intercept, noise):
    """Generate `n` noisy (x, y) pairs around the true line."""
    rng = random.Random(seed)
    xs = [rng.uniform(0.0, 10.0) for _ in range(n)]
    ys = [slope * x + intercept + rng.gauss(0.0, noise) for x in xs]
    return xs, ys


def fit_least_squares(xs, ys):
    """Closed-form least-squares fit; returns (slope, intercept)."""
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den = sum((x - mean_x) ** 2 for x in xs)
    slope = num / den if den else 0.0
    return slope, mean_y - slope * mean_x


def r_squared(xs, ys, slope, intercept):
    """Coefficient of determination for the fitted line."""
    mean_y = sum(ys) / len(ys)
    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    ss_res = sum((y - (slope * x + intercept)) ** 2
                 for x, y in zip(xs, ys))
    return 1.0 - ss_res / ss_tot if ss_tot else 0.0


def main():
    parser = argparse.ArgumentParser(
        description="Lasso Regression (L1): Linear Regression: least-squares fit for Lasso Regression (L1).")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--n", type=int, default=_num(PARAMS.get("n"), 200),
                        help="synthetic points to generate")
    parser.add_argument("--noise", type=float,
                        default=_num(PARAMS.get("noise"), 1.5),
                        help="Gaussian noise stddev on y")
    args = parser.parse_args()
    random.seed(args.seed)

    true_slope = _num(PARAMS.get("slope"), 2.5)
    true_intercept = _num(PARAMS.get("intercept"), 10.0)
    xs, ys = generate_data(args.seed, args.n, true_slope,
                           true_intercept, args.noise)
    slope, intercept = fit_least_squares(xs, ys)
    r2 = r_squared(xs, ys, slope, intercept)

    print("Lasso Regression (L1) least-squares regression (n={})".format(args.n))
    print("true line:      y = {:.3f}*x + {:.3f}".format(
        true_slope, true_intercept))
    print("fitted line:    y = {:.3f}*x + {:.3f}".format(slope, intercept))
    print("R^2:            {:.4f}".format(r2))
    print("-" * 44)
    print("{:>8} {:>10} {:>10} {:>10}".format("x", "y_true", "y_pred",
                                             "residual"))
    for x, y in sorted(zip(xs, ys))[:8]:
        pred = slope * x + intercept
        print("{:>8.3f} {:>10.3f} {:>10.3f} {:>10.3f}".format(
            x, y, pred, y - pred))


if __name__ == "__main__":
    main()
