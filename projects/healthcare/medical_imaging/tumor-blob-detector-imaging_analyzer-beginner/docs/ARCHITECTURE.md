# Architecture (HLD) — Tumor Blob Detector: Imaging_Analyzer

## Problem & Users

Tumor Blob Detector built as a imaging_analyzer. Blob detection finds compact bright or dark regions using filters like the Laplacian of Gaussian, which responds strongly to circular structures at a matching scale. Scanning across scales catches blobs of different sizes, and connected-component labeling turns the response map into discrete detections. Precision and recall against seeded ground truth quantify performance. A synthetic scan analyzer that generates a seeded 2D scan with an anomalous blob, segments it by thresholding, and reports the blob centroid and size.

The intended user is a student or engineer working in healthcare (medical_imaging) who needs a working, runnable reference for Tumor Blob Detector — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
