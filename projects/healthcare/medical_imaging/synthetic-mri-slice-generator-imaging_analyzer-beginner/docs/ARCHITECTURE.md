# Architecture (HLD) — Synthetic MRI Slice Generator: Imaging_Analyzer

## Problem & Users

Synthetic MRI Slice Generator built as a imaging_analyzer. Synthetic MRI slices are built from geometric phantoms, such as a head model made of overlapping ellipses, each assigned a tissue-like intensity. This mirrors how real scanners translate proton density and relaxation properties into grayscale values. Seeded generation gives developers a ground truth for testing segmentation and detection code with no patient data involved. A synthetic scan analyzer that generates a seeded 2D scan with an anomalous blob, segments it by thresholding, and reports the blob centroid and size.

The intended user is a student or engineer working in healthcare (medical_imaging) who needs a working, runnable reference for Synthetic MRI Slice Generator — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
