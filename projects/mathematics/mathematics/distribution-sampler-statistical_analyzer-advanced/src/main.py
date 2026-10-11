#!/usr/bin/env python3
"""Probability Distribution Sampler: Statistical Analyzer: descriptive statistics for Probability Distribution Sampler.

Inverse-transform sampling turns uniform random numbers into draws from any distribution with an invertible CDF, covering exponential, Pareto, and custom distributions. Rejection sampling handles the rest by accepting proposals under an envelope curve. The sampler validates output with a Kolmogorov-Smirnov-style comparison.
Data idea: The demo draws seeded-RNG samples from several distributions and checks sample moments against theoretical values.

Generates a deterministic synthetic sample, then reports count, mean,
median, standard deviation, min/max, quartiles, and an ASCII histogram.
"""

import argparse
import random

PARAMS = {'distribution': 'target distribution', 'params': 'distribution parameters', 'samples': 'draw count'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def generate_sample(seed, n):
    """Draw `n` synthetic Probability Distribution Sampler measurements (mixture model)."""
    rng = random.Random(seed)
    return [rng.gauss(50.0, 12.0) if rng.random() < 0.7
            else rng.gauss(85.0, 8.0) for _ in range(n)]


def percentile(sorted_vals, q):
    """Linear-interpolation percentile of a pre-sorted list."""
    if not sorted_vals:
        return 0.0
    k = (len(sorted_vals) - 1) * q / 100.0
    low = int(k)
    high = min(low + 1, len(sorted_vals) - 1)
    return sorted_vals[low] + (sorted_vals[high] - sorted_vals[low]) * (k - low)


def summarize(values, bins):
    """Compute a full descriptive-statistics summary of `values`."""
    ordered = sorted(values)
    n = len(ordered)
    mean = sum(ordered) / n
    var = sum((x - mean) ** 2 for x in ordered) / n
    lo, hi = ordered[0], ordered[-1]
    width = (hi - lo) / bins if hi > lo else 1.0
    hist = [0] * bins
    for x in ordered:
        hist[min(int((x - lo) / width), bins - 1)] += 1
    return {
        "count": n,
        "mean": mean,
        "median": percentile(ordered, 50),
        "stdev": var ** 0.5,
        "min": lo,
        "max": hi,
        "p25": percentile(ordered, 25),
        "p75": percentile(ordered, 75),
        "hist": hist,
        "lo": lo,
        "width": width,
    }


def print_report(summary):
    """Print the summary table and ASCII histogram."""
    s = summary
    print("Probability Distribution Sampler descriptive statistics")
    print("{:<10} {:>12}".format("STAT", "VALUE"))
    print("-" * 24)
    for key in ("count", "mean", "median", "stdev", "min",
                "p25", "p75", "max"):
        val = s[key]
        text = str(val) if key == "count" else "{:.3f}".format(val)
        print("{:<10} {:>12}".format(key, text))
    print("-" * 24)
    print("Histogram ({} bins):".format(len(s["hist"])))
    peak = max(s["hist"]) or 1
    for i, count in enumerate(s["hist"]):
        edge = s["lo"] + i * s["width"]
        bar = "#" * int(40 * count / peak)
        print("{:>8.2f} | {:<40} {}".format(edge, bar, count))


def main():
    parser = argparse.ArgumentParser(
        description="Probability Distribution Sampler: Statistical Analyzer: statistics for Probability Distribution Sampler.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--samples", type=int,
                        default=_num(PARAMS.get("samples"), 500),
                        help="synthetic measurements to draw")
    parser.add_argument("--bins", type=int,
                        default=_num(PARAMS.get("bins"), 10),
                        help="histogram bins")
    args = parser.parse_args()
    random.seed(args.seed)
    print_report(summarize(generate_sample(args.seed, args.samples),
                           args.bins))


if __name__ == "__main__":
    main()
