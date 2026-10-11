# PHQ-9-Style Self-Assessment Scorer: Statistical Analyzer

**Domain:** healthcare | **Subdomain:** mental_health_tech | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

PHQ-9-Style Self-Assessment Scorer built as a Statistical analyzer. Depression screening questionnaires ask how often symptoms occurred over two weeks, scoring each answer from zero to three and summing to a total. Score bands suggest minimal through severe symptom levels, but only a clinician can diagnose. This educational tool computes scores from synthetic responses and always displays screening-only disclaimer text. Includes prominent disclaimer text that the tool is for wellness self-tracking and screening only, never a diagnosis, and encourages consulting a professional. Draws a seeded synthetic sample and reports count, mean, median, stdev, quartiles, and an ASCII histogram.

**Core concept — PHQ-9-Style Self-Assessment Scorer:** Depression screening questionnaires ask how often symptoms occurred over two weeks, scoring each answer from zero to three and summing to a total. Score bands suggest minimal through severe symptom levels, but only a clinician can diagnose. This educational tool computes scores from synthetic responses and always displays screening-only disclaimer text. Includes prominent disclaimer text that the tool is for wellness self-tracking and screening only, never a diagnosis, and encourages consulting a professional.

**Why this matters in the real world:** Screening questionnaires are the standard first step in depression screening workflows.

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
cd projects/healthcare/mental_health_tech/phq9-style-screener-statistical_analyzer-beginner
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
