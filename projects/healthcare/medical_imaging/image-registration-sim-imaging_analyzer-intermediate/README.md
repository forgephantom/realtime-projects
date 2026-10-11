# Image Registration Simulator: Imaging_Analyzer

**Domain:** healthcare | **Subdomain:** medical_imaging | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Image Registration Simulator built as a imaging_analyzer. Rigid registration aligns a moving image to a reference by optimizing translation and rotation parameters against a similarity metric such as sum of squared differences or mutual information. The optimizer must avoid local minima, which is why multi-resolution pyramids start coarse and refine. Recovery error against the known applied transform measures success. A synthetic scan analyzer that generates a seeded 2D scan with an anomalous blob, segments it by thresholding, and reports the blob centroid and size.

**Core concept — Image Registration Simulator:** Rigid registration aligns a moving image to a reference by optimizing translation and rotation parameters against a similarity metric such as sum of squared differences or mutual information. The optimizer must avoid local minima, which is why multi-resolution pyramids start coarse and refine. Recovery error against the known applied transform measures success.

**Why this matters in the real world:** Registration aligns pre- and post-treatment scans so changes can be compared.

---

## Features

- `generate_scan` (`generate_scan(seed: int, size: int = 24) -> tuple`): Seeded NxN scan: gaussian background plus a gaussian anomaly blob.
- `region_stats` (`region_stats(grid: list) -> dict`): Mean, stdev, min, and max over the whole scan.
- `segment` (`segment(grid: list, threshold: float) -> list`): Binary mask of pixels above the threshold.
- `connected_components` (`connected_components(mask: list) -> list`): BFS connected components (4-neighborhood) of the mask.
- `largest_blob` (`largest_blob(components: list) -> dict`): Centroid, pixel count, and bbox of the largest component.
- `render_ascii` (`render_ascii(grid: list, mask: list) -> str`): ASCII heatmap of the scan with the segmented blob marked.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: stats, segmentation, blob report, ASCII map.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded scan analyzer demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random, math, statistics, collections

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Seeded gaussian background plus a gaussian anomaly blob; threshold at mean + 2 sigma; BFS connected components to isolate and measure the blob.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(N^2) for an N x N scan: generation, stats, thresholding, and BFS are each linear in pixels.. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/healthcare/medical_imaging/image-registration-sim-imaging_analyzer-intermediate
python3 src/main.py --help
python3 src/main.py
```
--size sets the scan resolution; the true blob center is seeded and reported for accuracy comparison.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints region statistics, the threshold, the detected blob centroid/size versus the true center, and an ASCII scan map.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
