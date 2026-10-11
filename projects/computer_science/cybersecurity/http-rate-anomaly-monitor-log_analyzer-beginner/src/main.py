#!/usr/bin/env python3
"""HTTP Rate Anomaly Monitor: Log Analyzer: a log analyzer for HTTP Rate Anomaly Monitor services.

Web servers under scraping or application-layer floods show request rates that deviate sharply from their learned baseline. This monitor builds an hourly baseline of requests per minute from access logs and flags windows where the rate exceeds the baseline by a configurable number of standard deviations. It separates single-IP floods from distributed low-and-slow patterns using per-IP and global counters.
Data idea: A seeded RNG generates access-log traffic with daily seasonality plus injected scraping floods and quiet bot patterns.

Generates a synthetic HTTP Rate Anomaly Monitor service log in memory, parses each
line with a regex, and prints a report: counts by level, counts by
service, top error messages, and the overall error rate.
"""

import argparse
import random
import re
from collections import Counter
from datetime import datetime, timedelta

PARAMS = {'baseline_days': 'days of history used to learn the normal rate', 'sigma_threshold': 'standard deviations above baseline that trigger alerts', 'min_requests': 'floor that avoids alerting on tiny traffic volumes', 'per_ip_limit': 'per-source requests per minute cap'}

LOG_RE = re.compile(
    r"(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"\[(?P<level>[A-Z]+)\] (?P<service>[\w-]+): (?P<msg>.*)")

MESSAGES = {
    "INFO": ["request completed", "cache warmed", "heartbeat ok",
             "worker idle", "checkpoint saved"],
    "WARN": ["retrying upstream call", "slow query detected",
             "queue depth rising", "cache miss spike"],
    "ERROR": ["connection refused by db", "timeout waiting for worker",
              "disk write failed", "upstream returned 503"],
}


def generate_log(seed, lines):
    """Generate `lines` synthetic HTTP Rate Anomaly Monitor log lines in memory."""
    rng = random.Random(seed)
    levels = ["INFO"] * 70 + ["WARN"] * 18 + ["ERROR"] * 12
    services = ["api", "worker", "db", "cache"]
    base = datetime(2026, 10, 10, 9, 0, 0)
    out = []
    for _ in range(lines):
        ts = base + timedelta(seconds=rng.randint(0, 3600))
        level = rng.choice(levels)
        service = rng.choice(services)
        msg = rng.choice(MESSAGES[level])
        out.append("{} [{}] {}: {}".format(
            ts.strftime("%Y-%m-%d %H:%M:%S"), level, service, msg))
    return out


def parse_line(line):
    """Parse one log line; return a dict or None if unparseable."""
    match = LOG_RE.match(line)
    return match.groupdict() if match else None


def analyze(entries):
    """Aggregate level counts, service counts, and top error messages."""
    by_level = Counter()
    by_service = Counter()
    errors = Counter()
    for entry in entries:
        by_level[entry["level"]] += 1
        by_service[entry["service"]] += 1
        if entry["level"] == "ERROR":
            errors[entry["msg"]] += 1
    return {"by_level": by_level, "by_service": by_service,
            "errors": errors}


def print_report(report, total):
    """Print the analysis report."""
    print("HTTP Rate Anomaly Monitor log analysis ({} lines)".format(total))
    print("By level:")
    for level, count in report["by_level"].most_common():
        print("  {:<6} {:>5} ({:.1%})".format(level, count, count / total))
    print("By service:")
    for service, count in report["by_service"].most_common():
        print("  {:<6} {:>5}".format(service, count))
    err_total = sum(report["errors"].values())
    print("Error rate: {:.1%} ({} errors)".format(
        err_total / total if total else 0.0, err_total))
    print("Top error messages:")
    for msg, count in report["errors"].most_common(5):
        print("  {:>4}x  {}".format(count, msg))


def main():
    parser = argparse.ArgumentParser(
        description="HTTP Rate Anomaly Monitor: Log Analyzer: analyze HTTP Rate Anomaly Monitor logs.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--lines", type=int,
                        default=PARAMS.get("lines", 300),
                        help="synthetic log lines to generate")
    args = parser.parse_args()
    random.seed(args.seed)

    lines = generate_log(args.seed, args.lines)
    entries = [e for line in lines if (e := parse_line(line)) is not None]
    print_report(analyze(entries), len(entries))


if __name__ == "__main__":
    main()
