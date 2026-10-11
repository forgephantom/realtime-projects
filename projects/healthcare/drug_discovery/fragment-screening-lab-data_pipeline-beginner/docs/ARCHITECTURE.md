# Architecture (HLD) — Fragment Screening Lab: Data Pipeline (Etl)

## Problem & Users

Fragment Screening Lab built as a Data pipeline (ETL). Fragment screening starts from tiny compounds following the rule of three, then grows or links binders into leads. Hit rates are low but the hits that appear are efficient starting points with room to grow. Simulating fragment sets with seeded binders exercises hit detection and fragment-linking logic. Extracts synthetic topic records, transforms them (drop invalid, normalize, bucket), and loads the clean set to CSV.

The intended user is a student or engineer working in healthcare (drug_discovery) who needs a working, runnable reference for Fragment Screening Lab — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| Pipeline | main | Three-stage ETL pipeline for topic records. |
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
generate_raw (extract) -> clean_rows (transform)
clean_rows -> write_csv (load) -> demo_workspace/records_clean.csv
Pipeline.run prints per-stage row counts
```

## Storage

The only persistence is the output CSV written to ./demo_workspace; the raw and intermediate rows exist only in memory during the run.

## Scaling & Limits

All rows are held in memory between stages, so very large inputs would need chunked or streaming processing instead.

## Trade-offs

In-memory batch processing keeps the code simple and fast for demo sizes, at the cost of not streaming arbitrarily large datasets.

## Failure Handling

Corrupt rows (null or negative values) are counted and dropped in the transform stage rather than crashing the pipeline; an empty input writes a header-only CSV.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
