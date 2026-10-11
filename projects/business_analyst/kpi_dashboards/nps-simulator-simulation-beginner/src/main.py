#!/usr/bin/env python3
"""Net Promoter Score Simulator: Simulation (Logistic Growth): a logistic-growth simulation for Net Promoter Score Simulator.

Net promoter score comes from a single 0 to 10 question: promoters score 9 or 10, passives 7 or 8, detractors 6 or below, and NPS is promoters minus detractors. The number is simple, but its power is in the trend and the verbatim themes behind it. Simulating responses shows how sample size and sentiment mix move the score.
Data idea: Generates seeded survey responses with score distributions and free-text themes, computes NPS per segment and month, and shows confidence bands by sample size.

Integrates dP/dt = r*P*(1 - P/K) with explicit Euler steps, modeling how a
Net Promoter Score Simulator quantity grows toward its carrying capacity, and prints the
trajectory table plus summary statistics.
"""

import argparse
import random

PARAMS = {'respondents': 'number of survey responses to simulate', 'sentiment_mix': 'share of promoters, passives, detractors', 'trend_months': 'months of trend history to generate'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def simulate(params, steps, dt):
    """Euler-integrate logistic growth; return [(t, value)] rows."""
    r = _num(params.get("r"), 0.4)
    K = _num(params.get("K"), 1000.0)
    value = _num(params.get("P0"), 50.0)
    rows = [(0.0, round(value, 3))]
    t = 0.0
    for _ in range(steps):
        value += dt * r * value * (1.0 - value / K)
        t += dt
        rows.append((round(t, 4), round(value, 3)))
    return rows


def print_trajectory(rows, every):
    """Print every Nth trajectory row plus the final state."""
    print("Net Promoter Score Simulator logistic-growth trajectory")
    print("{:>10} {:>14}".format("t", "value"))
    print("-" * 26)
    for t, value in rows[::every]:
        print("{:>10} {:>14}".format(t, value))
    if rows[-1] != rows[::every][-1]:
        t, value = rows[-1]
        print("  ...")
        print("{:>10} {:>14}".format(t, value))


def main():
    parser = argparse.ArgumentParser(
        description="Net Promoter Score Simulator: Simulation (Logistic Growth): simulate Net Promoter Score Simulator growth.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--steps", type=int,
                        default=_num(PARAMS.get("steps"), 40),
                        help="Euler integration steps")
    parser.add_argument("--dt", type=float, default=_num(PARAMS.get("dt"), 0.1),
                        help="time step size")
    args = parser.parse_args()
    random.seed(args.seed)

    rows = simulate(PARAMS, args.steps, args.dt)
    print_trajectory(rows, every=max(1, len(rows) // 10))
    values = [v for _, v in rows]
    print("-" * 26)
    print("steps: {}  dt: {}".format(args.steps, args.dt))
    print("start: {:.3f}  end: {:.3f}  peak: {:.3f}".format(
        values[0], values[-1], max(values)))
    print("carrying capacity K: {}".format(PARAMS.get("K", 1000.0)))


if __name__ == "__main__":
    main()
