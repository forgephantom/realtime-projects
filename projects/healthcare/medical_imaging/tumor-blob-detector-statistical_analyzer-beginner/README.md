# Tumor Blob Detector: Statistical Analyzer

**Domain:** healthcare | **Subdomain:** medical_imaging | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Tumor Blob Detector built as a Statistical analyzer. Blob detection finds compact bright or dark regions using filters like the Laplacian of Gaussian, which responds strongly to circular structures at a matching scale. Scanning across scales catches blobs of different sizes, and connected-component labeling turns the response map into discrete detections. Precision and recall against seeded ground truth quantify performance. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

**Core concept — Tumor Blob Detector:** Blob detection finds compact bright or dark regions using filters like the Laplacian of Gaussian, which responds strongly to circular structures at a matching scale. Scanning across scales catches blobs of different sizes, and connected-component labeling turns the response map into discrete detections. Precision and recall against seeded ground truth quantify performance.

**Why this matters in the real world:** Blob detection underlies nodule-finding assists used in lung CT screening.

---

## Features

- `generate_sample` (`generate_sample(seed, n)`): Draw synthetic topic measurements (mixture model).
- `percentile` (`percentile(sorted_vals, q)`): Linear-interpolation percentile of a pre-sorted list.
- `summarize` (`summarize(values, bins)`): Compute a full descriptive-statistics summary.
- `print_report` (`print_report(summary)`): Print the summary table and ASCII histogram.
- `main` (`main()`): Parse args and print the report.

---

## Tech Stack

Python 3.8+, stdlib: argparse, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Descriptive statistics with linear-interpolation percentiles. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(n log n) for the sort; O(n) for the histogram pass. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/healthcare/medical_imaging/tumor-blob-detector-statistical_analyzer-beginner
python3 src/main.py --help
python3 src/main.py
```

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

A statistics table (count, mean, median, stdev, min, p25, p75, max) followed by an ASCII histogram.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
