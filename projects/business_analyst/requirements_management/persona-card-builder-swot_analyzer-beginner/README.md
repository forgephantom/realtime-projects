# Persona Card Builder: Swot_Analyzer

**Domain:** business_analyst | **Subdomain:** requirements_management | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

Persona Card Builder built as a swot_analyzer. A persona card compresses a user segment into one page: name, goals, frustrations, and typical tasks. Personas keep design discussions about real humans instead of abstract users. The builder assembles cards from seeded research notes and keeps each persona anchored to observed behaviors. A SWOT and requirements analyzer that scores seeded factor lists per quadrant, finds the dominant quadrant, and generates TOWS action items.

**Core concept — Persona Card Builder:** A persona card compresses a user segment into one page: name, goals, frustrations, and typical tasks. Personas keep design discussions about real humans instead of abstract users. The builder assembles cards from seeded research notes and keeps each persona anchored to observed behaviors.

**Why this matters in the real world:** UX teams pin persona cards in design reviews to keep user needs visible.

---

## Features

- `build_factors` (`build_factors(seed: int) -> dict`): Seeded factor lists per quadrant with weight and impact score.
- `score_quadrant` (`score_quadrant(factors: list) -> float`): Weighted total (sum of weight x score) for one quadrant.
- `categorize` (`categorize(factors: dict) -> dict`): Score all quadrants and name the dominant one.
- `tows_actions` (`tows_actions(factors: dict) -> list`): Pair top factors into SO/WO/ST/WT action items.
- `render_matrix` (`render_matrix(factors: dict, scores: dict) -> str`): Format quadrants and scores as an ASCII 2x2 matrix.
- `run_demo` (`run_demo(seed: int) -> int`): Seeded demo: score quadrants, print matrix and TOWS actions.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Entry point: seeded SWOT analyzer demo.

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

The project is built around Weighted scoring per SWOT quadrant (sum of weight x score), then TOWS pairing of top factors into SO/WO/ST/WT actions.. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(F) over F factors; sorting for top factors is O(F log F).. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/business_analyst/requirements_management/persona-card-builder-swot_analyzer-beginner
python3 src/main.py --help
python3 src/main.py
```
--factors sets how many seeded factors land in each quadrant.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints an ASCII 2x2 SWOT matrix with quadrant scores and a numbered list of TOWS action items.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
