#!/usr/bin/env python3
"""Rate Limit Policy Tester: Rate Limiter.

Rate limits protect backends, but misconfigured ones block legitimate users or let abuse through. The tester fires scripted request patterns at a simulated limiter, verifying allow and deny decisions match policy across burst, sustained, and distributed scenarios. Policy becomes testable code.

Demo dataset idea: A seeded RNG drives request patterns against limiter implementations..
"""

import argparse
import random
import time

SLUG = "rate-limit-policy-tester-rate_limiter-intermediate"
PARAMS = {'policies': 'token bucket, fixed window, sliding', 'scenarios': 'burst, sustained, distributed', 'expectations': 'allowed versus denied per scenario', 'headers': 'retry-after and limit headers checked'}


class FakeClock:
    """A deterministic clock for the demo: time moves only when advanced."""

    def __init__(self):
        self.t = 0.0

    def __call__(self) -> float:
        return self.t

    def advance(self, dt: float) -> None:
        """Move the clock forward by dt seconds."""
        self.t += dt


class TokenBucket:
    """A token-bucket rate limiter.

    Tokens refill continuously at rate_per_sec up to capacity. allow()
    consumes one token when one is available and reports the decision.
    The now callable (default time.monotonic) makes the bucket testable
    with a fake clock, which is what the demo uses for determinism.
    """

    def __init__(self, rate_per_sec: float, capacity: int, now=None):
        if rate_per_sec <= 0 or capacity < 1:
            raise ValueError("rate_per_sec must be > 0 and capacity >= 1")
        self.rate_per_sec = rate_per_sec
        self.capacity = capacity
        self._tokens = float(capacity)
        self._now = now or time.monotonic
        self._last = self._now()
        self.allowed = 0
        self.denied = 0

    def _refill(self) -> None:
        now = self._now()
        self._tokens = min(self.capacity,
                           self._tokens + (now - self._last) * self.rate_per_sec)
        self._last = now

    def peek(self) -> float:
        """Tokens currently available, after refilling up to now."""
        self._refill()
        return self._tokens

    def allow(self) -> bool:
        """Consume one token if available. True means allowed, False denied."""
        self._refill()
        if self._tokens >= 1.0:
            self._tokens -= 1.0
            self.allowed += 1
            return True
        self.denied += 1
        return False

    def stats(self) -> dict:
        """Allowed/denied counters and the admission rate."""
        total = self.allowed + self.denied
        return {
            "allowed": self.allowed,
            "denied": self.denied,
            "admission_rate": self.allowed / total if total else 0.0,
        }


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Rate Limit Policy Tester: Rate Limiter: Rate limits protect backends, but misconfigured ones block legitimate users or let abuse through. The tester fires scripted request patterns at a simulated limiter, verifying allow and deny decisions match policy across burst, sustained, and distributed scenarios. Policy becomes testable code."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--rate", type=float, default=None,
                        help="Refill rate in tokens/second (see the topic params).")
    parser.add_argument("--capacity", type=int, default=None,
                        help="Bucket capacity (see the topic params).")
    parser.add_argument("--requests", type=int, default=None,
                        help="Number of scripted requests (see the topic params).")
    return parser


def run_demo(seed: int, rate: float, capacity: int, n_requests: int) -> int:
    """Replay a seeded bursty arrival schedule against the bucket."""
    clock = FakeClock()
    bucket = TokenBucket(rate, capacity, now=clock)
    rng = random.Random(seed)

    print("Rate Limit Policy Tester: Rate Limiter  (topic: Rate Limit Policy Tester, seed=%d)" % seed)
    print("Token bucket: %.1f tokens/s, capacity %d; %d scripted requests" % (
        rate, capacity, n_requests))
    print("%4s %7s %7s %s" % ("req", "t(s)", "tokens", "decision"))
    elapsed = 0.0
    for i in range(1, n_requests + 1):
        if i > 1:
            gap = rng.choice([0.05, 0.05, 0.10, 0.20, 0.40, 0.05])  # bursty arrivals
            clock.advance(gap)
            elapsed += gap
        tokens_before = bucket.peek()
        decision = "ALLOW" if bucket.allow() else "DENY "
        print("%4d %7.2f %7.2f %s" % (i, elapsed, tokens_before, decision))

    summary = bucket.stats()
    print("\nAllowed %d/%d requests, denied %d (admission rate %.1f%%)." % (
        summary["allowed"], n_requests, summary["denied"],
        100.0 * summary["admission_rate"]))
    return 0


def main(argv=None) -> int:
    """Entry point: parse flags and run the rate-limiter demo."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    rate = args.rate or float(PARAMS.get("rate_per_sec", 5.0))
    capacity = args.capacity or int(PARAMS.get("capacity", 5))
    n_requests = args.requests or int(PARAMS.get("requests", 20))
    return run_demo(args.seed, rate, capacity, n_requests)


if __name__ == "__main__":
    raise SystemExit(main())
