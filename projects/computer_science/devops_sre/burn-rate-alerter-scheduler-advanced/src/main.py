#!/usr/bin/env python3
"""Burn Rate Alerter: Task Scheduler: a tiny interval scheduler for Burn Rate Alerter jobs.

Slow budget burns need different urgency than fast ones, so burn-rate alerting watches how quickly the error budget is being consumed. The alerter computes burn over short and long windows, paging for fast burns and ticketing for slow ones, with reset detection to avoid alert fatigue. It catches incidents before the budget is gone.
Data idea: A seeded RNG generates error streams with sudden spikes and slow leaks.

Registers a few Burn Rate Alerter jobs with short intervals, runs the
heap-driven scheduler for --duration seconds, then prints the execution
log and per-job counts and exits.
"""

import argparse
import heapq
import random
import time

PARAMS = {'fast_window_minutes': 'short burn measurement window', 'slow_window_hours': 'long burn measurement window', 'page_threshold': 'burn multiple that pages', 'ticket_threshold': 'burn multiple that tickets'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def make_demo_job(tag):
    """Build a demo job function that counts its own executions."""
    state = {"runs": 0}

    def job(name):
        state["runs"] += 1
        return "{}-run-{}".format(tag, state["runs"])

    return job


class Scheduler:
    """Minimal interval scheduler driven by a heap of next-run times."""

    def __init__(self):
        self.jobs = []
        self.log = []

    def add_job(self, name, interval, func):
        """Register `func` to run every `interval` seconds under `name`."""
        heapq.heappush(self.jobs, (time.monotonic(), name, interval, func))

    def run(self, duration):
        """Run scheduled jobs for `duration` seconds; return the log."""
        deadline = time.monotonic() + duration
        while self.jobs and time.monotonic() < deadline:
            next_run, name, interval, func = self.jobs[0]
            now = time.monotonic()
            if next_run > now:
                time.sleep(min(next_run - now, 0.05))
                continue
            heapq.heappop(self.jobs)
            result = func(name)
            self.log.append((round(now, 2), name, result))
            heapq.heappush(self.jobs,
                           (next_run + interval, name, interval, func))
        return self.log


def main():
    parser = argparse.ArgumentParser(
        description="Burn Rate Alerter: Task Scheduler: schedule Burn Rate Alerter jobs.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--duration", type=float,
                        default=_num(PARAMS.get("duration"), 2.0),
                        help="seconds to run the demo")
    parser.add_argument("--jobs", type=int, default=_num(PARAMS.get("jobs"), 3),
                        help="number of demo jobs to register")
    args = parser.parse_args()
    random.seed(args.seed)

    intervals = [0.3, 0.5, 0.7, 1.0, 1.3]
    sched = Scheduler()
    for i in range(args.jobs):
        sched.add_job("burn-rate-alerter-scheduler-advanced-job-{}".format(i + 1),
                      intervals[i % len(intervals)],
                      make_demo_job("task{}".format(i + 1)))
    log = sched.run(args.duration)

    print("Burn Rate Alerter scheduler ran {} jobs for {}s".format(
        args.jobs, args.duration))
    print("{:>8} {:<22} {}".format("T", "JOB", "RESULT"))
    print("-" * 48)
    for t, name, result in log:
        print("{:>8} {:<22} {}".format(t, name, result))
    print("-" * 48)
    counts = {}
    for _, name, _ in log:
        counts[name] = counts.get(name, 0) + 1
    print("executions: " + ", ".join(
        "{}={}".format(name, counts[name]) for name in sorted(counts)))
    print("total: {} executions".format(len(log)))


if __name__ == "__main__":
    main()
