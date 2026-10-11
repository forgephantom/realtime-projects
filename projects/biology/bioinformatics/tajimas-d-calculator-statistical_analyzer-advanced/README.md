# Tajima's D Neutrality Tester: Statistical Analyzer

**Domain:** biology | **Subdomain:** bioinformatics | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Tajima's D Neutrality Tester built as a Statistical analyzer. Tajima's D compares two estimators of mutation rate: pairwise diversity versus segregating sites; negative values signal population expansion or selective sweeps, positive values signal balancing selection or bottlenecks. The statistic normalizes their difference by its theoretical variance. The calculator reports D and an approximate significance flag. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

**Core concept — Tajima's D Neutrality Tester:** Tajima's D compares two estimators of mutation rate: pairwise diversity versus segregating sites; negative values signal population expansion or selective sweeps, positive values signal balancing selection or bottlenecks. The statistic normalizes their difference by its theoretical variance. The calculator reports D and an approximate significance flag.

**Why this matters in the real world:** Tajima's D screens genomes for selective sweeps in evolutionary studies.

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
cd projects/biology/bioinformatics/tajimas-d-calculator-statistical_analyzer-advanced
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
