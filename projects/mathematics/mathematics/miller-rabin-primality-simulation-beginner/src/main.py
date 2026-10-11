#!/usr/bin/env python3
"""Miller-Rabin Probabilistic Primality Tester: Simulation (Logistic Growth): a logistic-growth simulation for Miller-Rabin Probabilistic Primality Tester.

The Miller-Rabin test decides primality by checking whether a number behaves like a prime under several random bases, using Fermat-style witnesses on the odd part of n minus 1. Each round halves the chance of a false positive, so a handful of rounds gives near-certainty. It is the workhorse test behind real key generation.
Data idea: The project generates random odd candidates and known Carmichael numbers with a seeded RNG to demonstrate witness detection rates.

Integrates dP/dt = r*P*(1 - P/K) with explicit Euler steps, modeling how a
Miller-Rabin Probabilistic Primality Tester quantity grows toward its carrying capacity, and prints the
trajectory table plus summary statistics.
"""

import argparse
import random

PARAMS = {'candidate': 'odd integer to test', 'rounds': 'number of random bases to try', 'seed': 'RNG seed for reproducible bases'}


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
    print("Miller-Rabin Probabilistic Primality Tester logistic-growth trajectory")
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
        description="Miller-Rabin Probabilistic Primality Tester: Simulation (Logistic Growth): simulate Miller-Rabin Probabilistic Primality Tester growth.")
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
