#!/usr/bin/env python3
"""Property-Based Tester (Lite): Command-Line Tool: a command-line tool for Property-Based Tester (Lite).

Property tests assert invariants over generated inputs (reverse(reverse(x)) == x, serialization round-trips) instead of examples: the generator produces random cases and shrinks failures to minimal repros. Shrinking is the magic that turns random failures into debuggable ones. It finds edge cases humans miss.
Data idea: Tests seeded functions with planted bugs, verifying the tester finds and shrinks failures.

Subcommands: summary (default), top, filter. All work on deterministic
synthetic rows generated from --seed, so every run is reproducible.
"""

import argparse
import json
import random

PARAMS = {'properties': 'invariants tested', 'generators': 'input strategies', 'shrinking': 'failure minimization'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def generate_rows(seed, count):
    """Generate `count` deterministic synthetic Property-Based Tester (Lite) rows."""
    rng = random.Random(seed)
    categories = ["alpha", "beta", "gamma"]
    return [{
        "id": i + 1,
        "category": rng.choice(categories),
        "value": round(rng.uniform(1.0, 1000.0), 2),
    } for i in range(count)]


def cmd_summary(rows, args):
    """Print per-category counts and value statistics."""
    groups = {}
    for row in rows:
        groups.setdefault(row["category"], []).append(row["value"])
    report = {
        "total_rows": len(rows),
        "by_category": {
            cat: {
                "count": len(vals),
                "mean": round(sum(vals) / len(vals), 2),
                "min": min(vals),
                "max": max(vals),
            } for cat, vals in sorted(groups.items())
        },
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("Property-Based Tester (Lite) summary ({} rows)".format(len(rows)))
        print("{:<10} {:>6} {:>10} {:>10} {:>10}".format(
            "CATEGORY", "COUNT", "MEAN", "MIN", "MAX"))
        for cat, stats in sorted(report["by_category"].items()):
            print("{:<10} {:>6} {:>10} {:>10} {:>10}".format(
                cat, stats["count"], stats["mean"],
                stats["min"], stats["max"]))


def cmd_top(rows, args):
    """Print the top-N rows by value."""
    top = sorted(rows, key=lambda r: r["value"], reverse=True)[:args.top_n]
    if args.json:
        print(json.dumps(top, indent=2))
    else:
        print("Top {} Property-Based Tester (Lite) rows by value:".format(args.top_n))
        print("{:>5} {:<10} {:>10}".format("ID", "CATEGORY", "VALUE"))
        for row in top:
            print("{:>5} {:<10} {:>10}".format(
                row["id"], row["category"], row["value"]))


def cmd_filter(rows, args):
    """Print rows whose value is at least --min-value."""
    kept = [r for r in rows if r["value"] >= args.min_value]
    if args.json:
        print(json.dumps(kept, indent=2))
    else:
        print("Property-Based Tester (Lite) rows with value >= {}: {} of {}".format(
            args.min_value, len(kept), len(rows)))
        print("{:>5} {:<10} {:>10}".format("ID", "CATEGORY", "VALUE"))
        for row in kept[:20]:
            print("{:>5} {:<10} {:>10}".format(
                row["id"], row["category"], row["value"]))
        if len(kept) > 20:
            print("  ... and {} more".format(len(kept) - 20))


def main():
    parser = argparse.ArgumentParser(
        description="Property-Based Tester (Lite): Command-Line Tool: CLI for Property-Based Tester (Lite).")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--rows", type=int,
                        default=_num(PARAMS.get("rows"), 200),
                        help="synthetic rows to generate")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON instead of tables")
    sub = parser.add_subparsers(dest="command")

    p_summary = sub.add_parser("summary", help="per-category statistics")
    p_summary.set_defaults(func=cmd_summary)

    p_top = sub.add_parser("top", help="highest-value rows")
    p_top.add_argument("--top-n", type=int, default=5,
                       help="how many rows to show")
    p_top.set_defaults(func=cmd_top)

    p_filter = sub.add_parser("filter", help="rows above a value threshold")
    p_filter.add_argument("--min-value", type=float, default=800.0,
                          help="minimum value to keep")
    p_filter.set_defaults(func=cmd_filter)

    args = parser.parse_args()
    random.seed(args.seed)
    rows = generate_rows(args.seed, args.rows)
    func = getattr(args, "func", None) or cmd_summary
    func(rows, args)


if __name__ == "__main__":
    main()
