#!/usr/bin/env python3
"""HTTP/3 QUIC Concept Simulator: Simulation (Logistic Growth): a logistic-growth simulation for HTTP/3 QUIC Concept Simulator.

QUIC rebuilds transport on UDP: independent streams eliminate head-of-line blocking, connection migration survives network switches, and TLS 1.3 is integrated into the handshake for faster setup. The simulator models streams multiplexed over one connection with per-stream flow control and packet-loss recovery. It shows why HTTP/3 helps lossy mobile networks most.
Data idea: Simulates seeded transfers over lossy links for QUIC-like vs TCP-like transports, comparing completion times and stall behavior.

Integrates dP/dt = r*P*(1 - P/K) with explicit Euler steps, modeling how a
HTTP/3 QUIC Concept Simulator quantity grows toward its carrying capacity, and prints the
trajectory table plus summary statistics.
"""

import argparse
import random

PARAMS = {'streams': 'concurrent stream count', 'loss': 'simulated packet loss rate', 'migration': 'whether network-switch events occur'}


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
    print("HTTP/3 QUIC Concept Simulator logistic-growth trajectory")
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
        description="HTTP/3 QUIC Concept Simulator: Simulation (Logistic Growth): simulate HTTP/3 QUIC Concept Simulator growth.")
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
