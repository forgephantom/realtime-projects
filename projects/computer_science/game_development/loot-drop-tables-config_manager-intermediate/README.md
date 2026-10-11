# Loot Drop Tables: Config Manager

**Domain:** computer_science | **Subdomain:** game_development | **Difficulty:** intermediate | **Est. build time:** 4-8 hours

---

## Overview

Loot Drop Tables built as a config manager. Drop tables turn kill rewards into weighted random tables with rarity tiers and pity timers. The designer simulates drops verifying rates. Fair randomness, tuned. A layered configuration manager that merges defaults, an INI snippet, environment variables, and CLI overrides with type checking and validation.

**Core concept — Loot Drop Tables:** Drop tables turn kill rewards into weighted random tables with rarity tiers and pity timers. The designer simulates drops verifying rates. Fair randomness, tuned.

**Why this matters in the real world:** Used in loot games.

---

## Features

- **Config**: Layered configuration with typed coercion, per-key source tracking, and validation.
- `coerce` (`coerce(raw: str, kind: type)`): Convert a raw string to kind; raises ValueError on bad input.
- `Config.load_defaults` (`load_defaults(self) -> None`): Layer 1: schema defaults.
- `Config.load_ini` (`load_ini(self, text: str) -> None`): Layer 2: parse flat key = value lines from an INI-style string.
- `Config.load_env` (`load_env(self, prefix: str) -> None`): Layer 3: PREFIX_KEY environment variables, e.g. DEMOAPP_PORT.
- `Config.set` (`set(self, key: str, raw: str) -> None`): Layer 4: a single CLI override in key=value form.
- `Config.get` (`get(self, key: str)`): The resolved value for key.
- `Config.as_dict` (`as_dict(self) -> dict`): All resolved values as a plain dict.
- `Config.sources` (`sources(self) -> dict`): Which layer supplied each key.
- `Config.validate` (`validate(self) -> list`): Return a list of human-readable problems; empty means valid.
- `run_demo` (`run_demo(seed: int, cli_overrides: list, env_prefix: str) -> int`): Resolve all four layers, print the table, and validate.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Parse flags and run the config demo.

---

## Tech Stack

Python 3.8+, stdlib: argparse, os, random

---

## Project Structure

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

---

## How It Works

The project is built around Layered merge: defaults < ini string < environment < CLI, with typed coercion. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(k) over k config keys. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/game_development/loot-drop-tables-config_manager-intermediate
python3 src/main.py --help
python3 src/main.py
```
--set key=value is repeatable for CLI overrides; --env-prefix changes the environment variable prefix.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints a resolved-config table (key, value, type, source layer, description) plus the validation verdict.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
