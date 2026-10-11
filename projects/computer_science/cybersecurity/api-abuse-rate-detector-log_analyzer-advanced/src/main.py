#!/usr/bin/env python3
"""API Abuse Rate Detector: Log Analyzer: a log analyzer for API Abuse Rate Detector services.

Legitimate API clients behave predictably while scrapers and attackers hammer endpoints at inhuman rates or probe for IDOR patterns. The detector profiles per-key request rates, endpoint entropy, and error ratios, flagging keys whose behavior diverges from their historical norm. It separates a viral launch from an attack by looking at error and spread patterns.
Data idea: A seeded RNG synthesizes API gateway logs with normal clients plus scraping and probing keys.

Generates a synthetic API Abuse Rate Detector service log in memory, parses each
line with a regex, and prints a report: counts by level, counts by
service, top error messages, and the overall error rate.
"""

import argparse
import random
import re
from collections import Counter
from datetime import datetime, timedelta

PARAMS = {'rate_sigma': 'deviation that flags a key', 'error_ratio_limit': '4xx share that looks like probing', 'endpoint_spread': 'distinct endpoints touched per window', 'window_minutes': 'observation window'}

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
    """Generate `lines` synthetic API Abuse Rate Detector log lines in memory."""
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
    print("API Abuse Rate Detector log analysis ({} lines)".format(total))
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
        description="API Abuse Rate Detector: Log Analyzer: analyze API Abuse Rate Detector logs.")
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
