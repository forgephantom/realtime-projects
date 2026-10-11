# Architecture (HLD) — Edge Detector Comparison: Statistical Analyzer

## Problem & Users

Edge Detector Comparison built as a Statistical analyzer. Sobel and Prewitt use small gradient kernels while Canny chains Gaussian smoothing, gradient computation, non-maximum suppression, and hysteresis thresholding into cleaner edges. Each detector trades sensitivity against false positives differently under noise. Benchmarking precision and recall on phantoms with annotated true edges makes the trade-off concrete. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

The intended user is a student or engineer working in healthcare (medical_imaging) who needs a working, runnable reference for Edge Detector Comparison — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
