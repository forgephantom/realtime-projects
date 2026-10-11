# Few-Shot Sensitivity Probe: Statistical Analyzer

**Domain:** ai | **Subdomain:** model_evaluation | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Few-Shot Sensitivity Probe built as a Statistical analyzer. Few-shot performance swings with the choice, order, and count of examples, sometimes by double digits. The probe sweeps example counts and permutations over a seeded task set and measures score variance, revealing whether a prompt is robust or lottery-like. Reporting the spread instead of a single number is the honest practice. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

**Core concept — Few-Shot Sensitivity Probe:** Few-shot performance swings with the choice, order, and count of examples, sometimes by double digits. The probe sweeps example counts and permutations over a seeded task set and measures score variance, revealing whether a prompt is robust or lottery-like. Reporting the spread instead of a single number is the honest practice.

**Why this matters in the real world:** Researchers report few-shot variance to avoid cherry-picked benchmark numbers.

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
cd projects/ai/model_evaluation/few-shot-sensitivity-statistical_analyzer-intermediate
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
