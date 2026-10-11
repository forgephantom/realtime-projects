# Design (LLD) — Binary Search Trainer: Terminal Game

## Module Breakdown

| File | Purpose |
|---|---|
| src/main.py | CLI entrypoint (argument parsing + demo orchestration) |

## Classes

| Class | Description |
|---|---|

## Functions

| Function | Signature | Description |
|---|---|---|
| new_board | new_board() -> list | A fresh 3x3 board as a list of 9 cells. |
| available_moves | available_moves(board: list) -> list | Empty cell indexes, in the fixed MOVE_ORDER. |
| winner | winner(board: list) | 'X', 'O', 'draw', or None when the game is still going. |
| minimax | minimax(board: list, player: str) -> tuple | Full-depth minimax; return (score, best_move) with X maximizing. |
| render | render(board: list) -> str | The board as a printable 3x3 grid. |
| play_game | play_game(x_move, o_move) -> tuple | Play one game between two move functions; return (result, moves). |
| ai_player | ai_player(board: list) -> int | Minimax move for whoever is to move on this board. |
| run_demo | run_demo(seed: int, demo_games: int) -> int | Play scripted AI-vs-AI games and print each final board plus a tally. |
| run_play | run_play() -> int | Interactive mode: you are X, the minimax AI is O. |
| build_parser | build_parser() -> argparse.ArgumentParser | Build the command-line parser for the demo. |
| main | main(argv=None) -> int | Scripted demo by default; --play for interactive mode. |

## Data Models & Parameters

The parameters below are the topic's key tunable parameters for Binary Search Trainer:

| Parameter | Meaning |
|---|---|
| array_size | search space size |
| mode | guided or quiz |
| target | value hidden or shown |
| hints | invariant explanations on or off |

## Algorithm & Complexity

The core of this project is Full-depth minimax tic-tac-toe with center-first deterministic move order.

- **Time complexity:** O(b^d) minimax per move; trivial for a 3x3 board
- **Practical behavior:** performance follows the stated complexity in practice; constants depend on input shape and the Python interpreter, so the runbook recommends benchmarking with your own inputs rather than trusting a single measured number.

## CLI Contract

```
cd projects/computer_science/algorithms_data_structures/binary-search-trainer-terminal_game-beginner
python3 src/main.py --help
python3 src/main.py
```
--play enables interactive input() mode; --games sets the number of scripted demo games.

Every flag is documented in `--help`, including its default value and a one-line description of its effect. The default invocation (no flags) runs a complete, seeded demo end to end — that behavior is the contract other documents reference.

## Extension Points

- Persist state in `sqlite3` (stdlib) so results survive restarts instead of living only in memory.
- Load parameters from a JSON config file for repeatable, shareable runs without long flag lists.
- Add an export/serve mode (CSV/JSON export or a small local server) to integrate with other tools.
- Add a `unittest` suite covering the core classes and asserting the seeded demo output.
