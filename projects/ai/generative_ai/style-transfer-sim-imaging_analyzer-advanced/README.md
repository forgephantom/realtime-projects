# Neural Style Transfer Simulator: Imaging_Analyzer

**Domain:** ai | **Subdomain:** generative_ai | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Neural Style Transfer Simulator built as a imaging_analyzer. Style transfer rewrites an image in the style of another by matching content features of one image with texture statistics of the other. Gram matrices of convolutional features capture style as feature correlations, while deeper layers preserve content structure. The simulator blends the two losses on seeded feature maps to show the tradeoff. A synthetic scan analyzer that generates a seeded 2D scan with an anomalous blob, segments it by thresholding, and reports the blob centroid and size.

**Core concept — Neural Style Transfer Simulator:** Style transfer rewrites an image in the style of another by matching content features of one image with texture statistics of the other. Gram matrices of convolutional features capture style as feature correlations, while deeper layers preserve content structure. The simulator blends the two losses on seeded feature maps to show the tradeoff.

**Why this matters in the real world:** Photo apps offer artistic filters built on style-transfer research.

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
cd projects/ai/generative_ai/style-transfer-sim-imaging_analyzer-advanced
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
