# Architecture (HLD) — Hallucination Detection Simulator: Statistical Analyzer

## Problem & Users

Hallucination Detection Simulator built as a Statistical analyzer. Hallucinations are plausible statements that are unsupported or false. Detection strategies include checking claims against retrieved context, measuring self-consistency across multiple sampled answers, and scoring entity-level factuality. The simulation plants unsupported claims in generated text and measures detector precision and recall at claim granularity. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

The intended user is a student or engineer working in ai (model_evaluation) who needs a working, runnable reference for Hallucination Detection Simulator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
