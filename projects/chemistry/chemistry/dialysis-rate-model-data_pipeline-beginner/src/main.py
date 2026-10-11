#!/usr/bin/env python3
"""Dialysis Rate Model: Data Pipeline (Etl): an extract-transform-load data pipeline.

Dialysis clears small solutes through a membrane by diffusion while retaining large molecules, with clearance depending on membrane area and the concentration gradient. The model integrates the mass balance to predict solute removal over time.
Data idea: A seeded RNG samples dialyzer parameters, integrates the clearance equations, and logs the concentration decay.

The pipeline extracts deterministic synthetic Dialysis Rate Model records,
transforms them (drop invalid rows, normalize values, bucket them), and
loads the clean set to CSV under ./demo_workspace.
"""

import argparse
import csv
import os
import random

PARAMS = {'membrane_area': 'dialyzer area in square meters', 'blood_flow': 'flow rate in milliliters per minute', 'initial_urea': 'starting urea in milligrams per deciliter'}


def _num(value, fallback):
    """Coerce a descriptive-text PARAMS value to a number, else fallback."""
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback


def generate_raw(seed, n):
    """Extract stage: build `n` synthetic raw Dialysis Rate Model records."""
    rng = random.Random(seed)
    rows = []
    for i in range(n):
        value = rng.gauss(500.0, 200.0)
        if rng.random() < 0.05:
            value = None  # simulate a corrupt source row
        rows.append({
            "id": i + 1,
            "source": rng.choice(["feed-a", "feed-b", "feed-c"]),
            "value": value,
        })
    return rows


def clean_rows(rows):
    """Transform stage: drop invalid rows, normalize, and bucket values.

    Returns (clean_rows, dropped_count).
    """
    valid = [r for r in rows
             if isinstance(r.get("value"), (int, float)) and r["value"] >= 0]
    dropped = len(rows) - len(valid)
    peak = max(r["value"] for r in valid) if valid else 1.0
    clean = []
    for r in valid:
        norm = r["value"] / peak
        bucket = "low" if norm < 0.33 else ("medium" if norm < 0.66 else "high")
        clean.append({
            "id": r["id"],
            "source": r["source"],
            "value": round(r["value"], 2),
            "value_norm": round(norm, 4),
            "bucket": bucket,
        })
    return clean, dropped


def write_csv(path, rows):
    """Load stage: write rows to a CSV file."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["id", "source", "value",
                                                "value_norm", "bucket"])
        writer.writeheader()
        writer.writerows(rows)
    return path


class Pipeline:
    """Three-stage ETL pipeline for Dialysis Rate Model records."""

    def __init__(self, seed, out_dir):
        self.seed = seed
        self.out_dir = out_dir

    def extract(self, n):
        """Run the extract stage and return raw rows."""
        return generate_raw(self.seed, n)

    def transform(self, rows):
        """Run the transform stage and return (clean, dropped)."""
        return clean_rows(rows)

    def load(self, rows):
        """Run the load stage; return the CSV path written."""
        path = os.path.join(self.out_dir, "records_clean.csv")
        return write_csv(path, rows)

    def run(self, n):
        """Run extract -> transform -> load; print a stage report."""
        raw = self.extract(n)
        clean, dropped = self.transform(raw)
        path = self.load(clean)
        print("Dialysis Rate Model: Data Pipeline (Etl) pipeline report")
        print("{:<10} {:>8}".format("STAGE", "ROWS"))
        print("{:<10} {:>8}".format("extract", len(raw)))
        print("{:<10} {:>8}".format("dropped", dropped))
        print("{:<10} {:>8}".format("load", len(clean)))
        print("Wrote: {}".format(path))
        buckets = {}
        for r in clean:
            buckets[r["bucket"]] = buckets.get(r["bucket"], 0) + 1
        print("Buckets: " + ", ".join(
            "{}={}".format(b, buckets.get(b, 0))
            for b in ("low", "medium", "high")))
        print("Sample rows:")
        for r in clean[:5]:
            print("  id={:<4} source={:<7} value={:<9} norm={:<7} bucket={}".format(
                r["id"], r["source"], r["value"], r["value_norm"],
                r["bucket"]))
        return len(clean)


def main():
    parser = argparse.ArgumentParser(
        description="Dialysis Rate Model: Data Pipeline (Etl): ETL pipeline for Dialysis Rate Model.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--rows", type=int,
                        default=_num(PARAMS.get("rows"), 200),
                        help="raw rows to extract")
    parser.add_argument("--out-dir", default="demo_workspace",
                        help="directory for the output CSV")
    args = parser.parse_args()
    random.seed(args.seed)
    Pipeline(args.seed, args.out_dir).run(args.rows)


if __name__ == "__main__":
    main()
