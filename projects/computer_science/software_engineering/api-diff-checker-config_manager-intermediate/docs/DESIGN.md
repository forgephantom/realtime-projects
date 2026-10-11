# Design (LLD) — API Diff Checker (Semver): Config Manager

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| Config | Layered configuration with typed coercion, per-key source tracking, and validation. |

## Functions

| Function | Signature | Description |
|---|---|---|
| coerce | coerce(raw: str, kind: type) | Convert a raw string to kind; raises ValueError on bad input. |
| Config.load_defaults | load_defaults(self) -> None | Layer 1: schema defaults. |
| Config.load_ini | load_ini(self, text: str) -> None | Layer 2: parse flat key = value lines from an INI-style string. |
| Config.load_env | load_env(self, prefix: str) -> None | Layer 3: PREFIX_KEY environment variables, e.g. DEMOAPP_PORT. |
| Config.set | set(self, key: str, raw: str) -> None | Layer 4: a single CLI override in key=value form. |
| Config.get | get(self, key: str) | The resolved value for key. |
| Config.as_dict | as_dict(self) -> dict | All resolved values as a plain dict. |
| Config.sources | sources(self) -> dict | Which layer supplied each key. |
| Config.validate | validate(self) -> list | Return a list of human-readable problems; empty means valid. |
| run_demo | run_demo(seed: int, cli_overrides: list, env_prefix: str) -> int | Resolve all four layers, print the table, and validate. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Parse flags and run the config demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for API Diff Checker (Semver):

| Parameter | Meaning |
|---|---|
| old | baseline API surface |
| new | candidate API surface |
| semver | bump recommendation rules |

## Algorithm & Complexity

The core of this project is Layered merge: defaults < ini string < environment < CLI, with typed coercion.

- **Time complexity:** O(k) over k config keys
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/software_engineering/api-diff-checker-config_manager-intermediate
python3 src/main.py --help
python3 src/main.py
```
--set key=value is repeatable for CLI overrides; --env-prefix changes the environment variable prefix.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
