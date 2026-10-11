# Design (LLD) — Edit Script Compressor: File Organizer

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|
| FileOrganizer | Sorts the top-level files of a folder into subfolders by extension. |

## Functions

| Function | Signature | Description |
|---|---|---|
| FileOrganizer.category_for | category_for(self, filename: str) -> str | Folder name for a file's extension, or 'misc' when unknown. |
| FileOrganizer.plan | plan(self) -> list | [(source, destination), ...] for every top-level file in root. |
| FileOrganizer.execute | execute(self, plan: list) -> list | Carry out a plan from plan(); return the moves that happened. |
| FileOrganizer.report | report(self, moves: list) -> str | One-line-per-move human-readable summary. |
| make_sample_files | make_sample_files(root: str, n: int, rng: random.Random) -> list | Create n seeded sample files directly inside root; return their names. |
| list_tree | list_tree(root: str) -> list | Relative paths of everything under root, directories first, sorted. |
| run_demo | run_demo(seed: int, n_files: int, dry_run: bool) -> int | Generate sample files, show before/after, then organize them. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Parse flags and run the organizer demo. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Edit Script Compressor:

| Parameter | Meaning |
|---|---|
| lines_a | original size |
| lines_b | modified size |
| context | hunk context lines |
| group_gap | merge distance |

## Algorithm & Complexity

The core of this project is Extension-to-folder mapping with a plan-then-execute move pass.

- **Time complexity:** O(f) over f files
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/algorithms_data_structures/edit-script-compressor-file_organizer-beginner
python3 src/main.py --help
python3 src/main.py
```
--files sets the sample count; --dry-run prints the move plan without moving anything. Works inside ./demo_workspace.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
