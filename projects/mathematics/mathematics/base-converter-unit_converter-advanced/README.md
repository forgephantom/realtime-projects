# Arbitrary Base Converter: Unit Converter

**Domain:** mathematics | **Subdomain:** mathematics | **Difficulty:** advanced | **Est. build time:** 8-16 hours

---

## Overview

Arbitrary Base Converter built as a unit converter. Positional notation represents a number as digits times powers of the base, so conversion means repeated division for the integer part and repeated multiplication for the fraction part. The tool handles bases 2 through 36 with digit alphabets and exact fractional expansion up to a precision cap. A unit converter covering length, mass, volume, speed, data sizes, and temperature, with real conversion factors and offset-aware temperature math.

**Core concept — Arbitrary Base Converter:** Positional notation represents a number as digits times powers of the base, so conversion means repeated division for the integer part and repeated multiplication for the fraction part. The tool handles bases 2 through 36 with digit alphabets and exact fractional expansion up to a precision cap.

**Why this matters in the real world:** Base conversion powers hex dumps, URL-safe encodings, and numeral-system teaching tools.

---

## Features

- **UnitConverter**: Converts between units within a category using factor tables; temperature is offset-aware.
- `UnitConverter.convert` (`convert(self, value: float, from_unit: str, to_unit: str) -> float`): Convert value from from_unit to to_unit; raises ValueError on misuse.
- `UnitConverter.categories` (`categories(self) -> list`): Category names, including temperature.
- `UnitConverter.units` (`units(self, category: str) -> list`): Unit names for a category.
- `run_demo` (`run_demo(seed: int) -> int`): Convert the seeded demo list and print a results table.
- `run_single` (`run_single(value: float, from_unit: str, to_unit: str) -> int`): Convert one value supplied on the command line.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Demo table by default; single conversion with --value/--from/--to.

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

The project is built around Factor-to-base-unit tables; temperature via to/from-Celsius functions. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(1) per conversion. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/mathematics/mathematics/base-converter-unit_converter-advanced
python3 src/main.py --help
python3 src/main.py
```
--value/--from/--to converts a single value; the default run prints the demo conversion table.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a conversion results table (value, from, to, result) and the supported category list.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
