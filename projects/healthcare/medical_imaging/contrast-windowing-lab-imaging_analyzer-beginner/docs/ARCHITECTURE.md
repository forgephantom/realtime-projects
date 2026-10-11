# Architecture (HLD) — Contrast Windowing Lab: Imaging_Analyzer

## Problem & Users

Contrast Windowing Lab built as a imaging_analyzer. Windowing maps a slice of the Hounsfield scale onto display grayscale: the window level sets the center and the window width sets the range. A narrow lung window reveals subtle nodules while a wide bone window shows dense structures. Experimenting with presets builds intuition for why one image can look so different under different windows. A synthetic scan analyzer that generates a seeded 2D scan with an anomalous blob, segments it by thresholding, and reports the blob centroid and size.

The intended user is a student or engineer working in healthcare (medical_imaging) who needs a working, runnable reference for Contrast Windowing Lab — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
seed -> generate_scan (background + anomaly blob) -> grid
 grid -> region_stats -> mean, stdev, min, max
mean + 2*stdev -> threshold -> segment -> binary mask
mask -> connected_components (BFS) -> largest blob -> centroid, size
```

## Storage

No persistence: the scan is regenerated from the seed each run.

## Scaling & Limits

Pixel loops suit demo resolutions; megapixel scans would want numpy or tiled processing.

## Trade-offs

A global threshold is simple and fast but can miss faint anomalies that adaptive methods would catch.

## Failure Handling

If no pixel clears the threshold, the report says no anomaly was found instead of crashing on an empty mask.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
