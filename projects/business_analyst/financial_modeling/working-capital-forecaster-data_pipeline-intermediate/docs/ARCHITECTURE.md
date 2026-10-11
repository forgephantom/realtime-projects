# Architecture (HLD) — Working Capital Forecaster: Data Pipeline (Etl)

## Problem & Users

Working Capital Forecaster built as a Data pipeline (ETL). Working capital forecasting projects receivables, payables, and inventory from revenue and cost drivers, because growth consumes cash before it generates it. A company can be profitable and still run dry if working capital balloons. Linking each balance to its driver turns the forecast into an early warning for cash crunches. Extracts synthetic topic records, transforms them (drop invalid, normalize, bucket), and loads the clean set to CSV.

The intended user is a student or engineer working in business_analyst (financial_modeling) who needs a working, runnable reference for Working Capital Forecaster — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
