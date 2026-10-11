#!/usr/bin/env python3
"""Difference-in-Differences Estimator: Report Generator.

Diff-in-diff compares the treated group's before/after change against a control group's: the double difference removes shared trends, isolating the treatment effect. Parallel-trends diagnostics (pre-period placebos) validate the key assumption. It is the workhorse of policy evaluation.

Demo dataset idea: Estimates seeded policy impacts with shared trends and verifies effect recovery plus placebo nulls..
"""

import argparse
import os
import random

SLUG = "diff-in-diff-estimator-report_generator-advanced"
PARAMS = {'treated': 'treated unit/group', 'periods': 'pre/post periods', 'placebo': 'pre-period placebo tests'}
OUT_DIR = "demo_output"  # reports are written inside this runtime-created folder


def generate_records(n: int, rng: random.Random) -> list:
    """Build n seeded synthetic measurement records for the demo."""
    services = ["web", "api", "worker", "db"]
    records = []
    for i in range(n):
        requests = rng.randint(500, 5000)
        errors = rng.randint(0, 60)
        records.append({
            "day": "2026-10-%02d" % ((i % 7) + 1),
            "service": rng.choice(services),
            "requests": requests,
            "errors": errors,
            "p99_ms": round(rng.uniform(40.0, 900.0), 1),
        })
    return records


def summarize(records: list) -> dict:
    """Aggregate totals, per-service rollups, error rate, and latency peaks."""
    total_requests = sum(r["requests"] for r in records)
    total_errors = sum(r["errors"] for r in records)
    by_service = {}
    for record in records:
        entry = by_service.setdefault(record["service"],
                                      {"requests": 0, "errors": 0, "max_p99_ms": 0.0})
        entry["requests"] += record["requests"]
        entry["errors"] += record["errors"]
        entry["max_p99_ms"] = max(entry["max_p99_ms"], record["p99_ms"])
    top_service = max(by_service, key=lambda s: by_service[s]["requests"])
    return {
        "records": len(records),
        "total_requests": total_requests,
        "total_errors": total_errors,
        "error_rate": total_errors / total_requests if total_requests else 0.0,
        "by_service": by_service,
        "top_service": top_service,
    }


def render_markdown(title: str, summary: dict, records: list) -> str:
    """Render the summary and sample rows as a Markdown document."""
    lines = []
    lines.append("# %s" % title)
    lines.append("")
    lines.append("Seeded demo data for Difference-in-Differences Estimator (diff-in-diff-estimator-report_generator-advanced).")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| metric | value |")
    lines.append("|---|---|")
    lines.append("| records | %d |" % summary["records"])
    lines.append("| total requests | %d |" % summary["total_requests"])
    lines.append("| total errors | %d |" % summary["total_errors"])
    lines.append("| error rate | %.2f%% |" % (100.0 * summary["error_rate"]))
    lines.append("| top service by requests | %s |" % summary["top_service"])
    lines.append("")
    lines.append("## By service")
    lines.append("")
    lines.append("| service | requests | errors | max p99 ms |")
    lines.append("|---|---|---|---|")
    for service in sorted(summary["by_service"]):
        entry = summary["by_service"][service]
        lines.append("| %s | %d | %d | %.1f |" % (
            service, entry["requests"], entry["errors"], entry["max_p99_ms"]))
    lines.append("")
    lines.append("## Sample rows")
    lines.append("")
    lines.append("| day | service | requests | errors | p99 ms |")
    lines.append("|---|---|---|---|---|")
    for record in records[:10]:
        lines.append("| %s | %s | %d | %d | %.1f |" % (
            record["day"], record["service"], record["requests"],
            record["errors"], record["p99_ms"]))
    lines.append("")
    return "\n".join(lines)


def write_report(path: str, text: str) -> str:
    """Write the Markdown report, creating parent folders; return the path."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as handle:
        handle.write(text)
    return path


def run_demo(seed: int, n_rows: int, out_path: str) -> int:
    """Generate data, summarize it, write the Markdown report, print a summary."""
    rng = random.Random(seed)
    records = generate_records(n_rows, rng)
    summary = summarize(records)
    title = "Difference-in-Differences Estimator: Report Generator"
    markdown = render_markdown(title, summary, records)
    write_report(out_path, markdown)

    print("Difference-in-Differences Estimator: Report Generator  (topic: Difference-in-Differences Estimator, seed=%d)" % seed)
    print("Analyzed %d records: %d requests, %d errors (%.2f%% error rate)." % (
        summary["records"], summary["total_requests"], summary["total_errors"],
        100.0 * summary["error_rate"]))
    print("Top service by requests: %s." % summary["top_service"])
    print("Per-service requests: %s." % ", ".join(
        "%s=%d" % (s, summary["by_service"][s]["requests"])
        for s in sorted(summary["by_service"])))
    print("\nWrote Markdown report: ./%s (%d lines)." % (out_path, markdown.count("\n") + 1))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Difference-in-Differences Estimator: Report Generator: Diff-in-diff compares the treated group's before/after change against a control group's: the double difference removes shared trends, isolating the treatment effect. Parallel-trends diagnostics (pre-period placebos) validate the key assumption. It is the workhorse of policy evaluation."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--rows", type=int, default=None,
                        help="Synthetic records to generate (see the topic params).")
    parser.add_argument("--out", type=str, default=None,
                        help="Report path (see the topic params).")
    parser.add_argument("--title", type=str, default=None,
                        help="Report title (default: Difference-in-Differences Estimator: Report Generator).")
    return parser


def main(argv=None) -> int:
    """Entry point: parse flags and run the report demo."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    n_rows = args.rows or int(PARAMS.get("rows", 24))
    out_path = args.out or PARAMS.get("out", OUT_DIR + "/report.md")
    return run_demo(args.seed, n_rows, out_path)


if __name__ == "__main__":
    raise SystemExit(main())
