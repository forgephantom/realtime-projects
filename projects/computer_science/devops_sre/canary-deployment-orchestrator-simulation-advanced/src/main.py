#!/usr/bin/env python3
"""Canary Deployment Orchestrator: Simulation (Logistic Growth): a logistic-growth simulation for Canary Deployment Orchestrator.

Canary releases shift a small slice of traffic to a new version and watch health signals before rolling forward, limiting blast radius. The orchestrator automates the stages: route 5 percent, compare error rates and latency against the stable version, then promote or roll back automatically. It turns deploy courage into a measured experiment.
Data idea: A seeded RNG simulates two service versions serving traffic with injected regressions in some runs.

Integrates dP/dt = r*P*(1 - P/K) with explicit Euler steps, modeling how a
Canary Deployment Orchestrator quantity grows toward its carrying capacity, and prints the
trajectory table plus summary statistics.
"""

import argparse
import random

PARAMS = {'canary_percent': 'initial traffic share for the new version', 'promotion_steps': 'traffic increments toward full rollout', 'error_rate_guard': 'error threshold that triggers rollback', 'latency_guard_ms': 'p99 latency ceiling during canary'}


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
    print("Canary Deployment Orchestrator logistic-growth trajectory")
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
        description="Canary Deployment Orchestrator: Simulation (Logistic Growth): simulate Canary Deployment Orchestrator growth.")
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
