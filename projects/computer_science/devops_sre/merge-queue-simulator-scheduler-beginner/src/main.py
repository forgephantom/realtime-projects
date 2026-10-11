#!/usr/bin/env python3
"""Merge Queue Simulator: Task Scheduler: a tiny interval scheduler for Merge Queue Simulator jobs.

Merge queues serialize pull requests through tests so main stays green, but sizing and timeouts need tuning. The simulator models PR arrivals, test durations, and failures through queue policies, measuring wait times and main-branch health. It tunes the tradeoff between throughput and safety.
Data idea: A seeded RNG drives PRs through queue policies.

Registers a few Merge Queue Simulator jobs with short intervals, runs the
heap-driven scheduler for --duration seconds, then prints the execution
log and per-job counts and exits.
"""

import argparse
import heapq
import random
import time

PARAMS = {'arrival_rate': 'PRs per hour', 'test_duration': 'validation time', 'batching': 'speculative batches modeled', 'failure_rate': 'flaky PR frequency'}


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
        description="Merge Queue Simulator: Task Scheduler: schedule Merge Queue Simulator jobs.")
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
        sched.add_job("merge-queue-simulator-scheduler-beginner-job-{}".format(i + 1),
                      intervals[i % len(intervals)],
                      make_demo_job("task{}".format(i + 1)))
    log = sched.run(args.duration)

    print("Merge Queue Simulator scheduler ran {} jobs for {}s".format(
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
