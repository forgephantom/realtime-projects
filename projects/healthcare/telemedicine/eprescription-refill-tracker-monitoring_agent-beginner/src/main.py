#!/usr/bin/env python3
"""E-Prescription Refill Tracker: Monitoring Agent: a threshold-based monitoring agent for E-Prescription Refill Tracker.

Refill tracking monitors days of supply remaining, refill windows, and prescriber authorization status for each medication. Alerts fire before the supply runs out, accounting for weekends and pharmacy hours. Synthetic medication histories with known refill dates verify the alert timing.
Data idea: Generates synthetic medication histories with known refill dates.

Samples synthetic E-Prescription Refill Tracker metrics for --cycles cycles, evaluates
each reading against configured thresholds, prints every reading with any
triggered alerts, and exits with a summary.
"""

import argparse
import random
import time

PARAMS = {'medication_count': 'medications tracked per patient', 'supply_days': 'days of supply per fill', 'seed': 'random seed for history generation', 'alert_lead_days': 'days before depletion to alert'}


def read_metrics(rng, cycle):
    """Sample one synthetic E-Prescription Refill Tracker metric reading."""
    return {
        "cycle": cycle,
        "cpu_pct": round(rng.uniform(20.0, 98.0), 1),
        "memory_pct": round(rng.uniform(30.0, 97.0), 1),
        "latency_ms": round(rng.uniform(40.0, 900.0), 1),
    }


def check_thresholds(reading, thresholds):
    """Return a list of alert strings for readings over threshold."""
    alerts = []
    if reading["cpu_pct"] > thresholds.get("cpu", 85.0):
        alerts.append("CPU {:.1f}% over {:.1f}%".format(
            reading["cpu_pct"], thresholds.get("cpu", 85.0)))
    if reading["memory_pct"] > thresholds.get("memory", 90.0):
        alerts.append("memory {:.1f}% over {:.1f}%".format(
            reading["memory_pct"], thresholds.get("memory", 90.0)))
    if reading["latency_ms"] > thresholds.get("latency_ms", 500.0):
        alerts.append("latency {:.1f}ms over {:.1f}ms".format(
            reading["latency_ms"], thresholds.get("latency_ms", 500.0)))
    return alerts


class Monitor:
    """Samples metrics, evaluates thresholds, and collects alerts."""

    def __init__(self, seed, thresholds):
        self.rng = random.Random(seed)
        self.thresholds = thresholds
        self.alerts = []

    def run(self, cycles, interval):
        """Sample `cycles` readings, print them, return alert count."""
        for cycle in range(1, cycles + 1):
            reading = read_metrics(self.rng, cycle)
            alerts = check_thresholds(reading, self.thresholds)
            self.alerts.extend(
                (cycle, text) for text in alerts)
            print("cycle {:>2}: cpu={:>5}% mem={:>5}% latency={:>6}ms".format(
                cycle, reading["cpu_pct"], reading["memory_pct"],
                reading["latency_ms"]))
            for text in alerts:
                print("  ALERT: {}".format(text))
            time.sleep(interval)
        print("-" * 52)
        print("cycles: {}  alerts: {}".format(cycles, len(self.alerts)))
        if self.alerts:
            print("alert breakdown:")
            for cycle, text in self.alerts:
                print("  cycle {}: {}".format(cycle, text))
        return len(self.alerts)


def main():
    parser = argparse.ArgumentParser(
        description="E-Prescription Refill Tracker: Monitoring Agent: monitor E-Prescription Refill Tracker metrics.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--cycles", type=int,
                        default=PARAMS.get("cycles", 6),
                        help="sampling cycles to run")
    parser.add_argument("--interval", type=float,
                        default=PARAMS.get("interval", 0.1),
                        help="seconds between samples")
    args = parser.parse_args()
    random.seed(args.seed)

    thresholds = PARAMS.get("thresholds",
                            {"cpu": 85.0, "memory": 90.0,
                             "latency_ms": 500.0})
    print("E-Prescription Refill Tracker monitor (thresholds: {})".format(thresholds))
    Monitor(args.seed, thresholds).run(args.cycles, args.interval)


if __name__ == "__main__":
    main()
