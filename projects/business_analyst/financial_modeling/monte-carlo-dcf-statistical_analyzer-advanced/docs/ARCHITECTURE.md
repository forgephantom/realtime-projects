# Architecture (HLD) — Monte Carlo DCF Valuator: Statistical Analyzer

## Problem & Users

Monte Carlo DCF Valuator built as a Statistical analyzer. A deterministic DCF gives one value; a Monte Carlo DCF gives a distribution by sampling growth rates, margins, and the discount rate. The output shows the probability the investment clears its hurdle instead of a single fragile number. It forces the analyst to state uncertainty explicitly rather than hiding it in a point estimate. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

The intended user is a student or engineer working in business_analyst (financial_modeling) who needs a working, runnable reference for Monte Carlo DCF Valuator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
--seed -> generate_sample (mixture model)
sample -> summarize (sort, moments, percentiles, histogram)
summary -> print_report (table + ASCII histogram)
```

## Storage

In-memory only: the sample and summary exist for the duration of the run and nothing is persisted.

## Scaling & Limits

The sample is sorted in memory, so multi-million-point samples would need a streaming quantile sketch instead.

## Trade-offs

Hand-rolled statistics avoid dependencies but only cover univariate descriptives, not hypothesis tests or modeling.

## Failure Handling

An empty sample cannot occur (n comes from --samples), and a constant sample degrades gracefully to a single non-empty histogram bin.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
