# N-Queens Solver: Terminal Game

**Domain:** computer_science | **Subdomain:** algorithms_data_structures | **Difficulty:** beginner | **Est. build time:** 2-4 hours

---

## Overview

N-Queens Solver built as a terminal game. Placing n queens so none attack each other is the classic backtracking problem, with pruning cutting the search dramatically. The solver animates placements and backtracks, counting solutions for each n. Constraint propagation in miniature. A playable tic-tac-toe game with an unbeatable minimax AI: scripted AI-vs-AI demo by default, interactive play with --play.

**Core concept — N-Queens Solver:** Placing n queens so none attack each other is the classic backtracking problem, with pruning cutting the search dramatically. The solver animates placements and backtracks, counting solutions for each n. Constraint propagation in miniature.

**Why this matters in the real world:** Used teaching backtracking and pruning.

---

## Features

- `new_board` (`new_board() -> list`): A fresh 3x3 board as a list of 9 cells.
- `available_moves` (`available_moves(board: list) -> list`): Empty cell indexes, in the fixed MOVE_ORDER.
- `winner` (`winner(board: list)`): 'X', 'O', 'draw', or None when the game is still going.
- `minimax` (`minimax(board: list, player: str) -> tuple`): Full-depth minimax; return (score, best_move) with X maximizing.
- `render` (`render(board: list) -> str`): The board as a printable 3x3 grid.
- `play_game` (`play_game(x_move, o_move) -> tuple`): Play one game between two move functions; return (result, moves).
- `ai_player` (`ai_player(board: list) -> int`): Minimax move for whoever is to move on this board.
- `run_demo` (`run_demo(seed: int, demo_games: int) -> int`): Play scripted AI-vs-AI games and print each final board plus a tally.
- `run_play` (`run_play() -> int`): Interactive mode: you are X, the minimax AI is O.
- `build_parser` (`build_parser() -> argparse.ArgumentParser`): Build the command-line parser for the demo.
- `main` (`main(argv=None) -> int`): Scripted demo by default; --play for interactive mode.

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

The project is built around Full-depth minimax tic-tac-toe with center-first deterministic move order. Input data flows from src/main.py through the processing modules, and the overall approach runs in O(b^d) minimax per move; trivial for a 3x3 board. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the high-level design and [docs/DESIGN.md](docs/DESIGN.md) for the detailed module breakdown.

---

## How to Run

```
cd projects/computer_science/algorithms_data_structures/n-queens-solver-terminal_game-beginner
python3 src/main.py --help
python3 src/main.py
```
--play enables interactive input() mode; --games sets the number of scripted demo games.

All flags are documented in the CLI itself — run with `--help` to see every option with its default value and meaning.

---

## Sample Output

Prints each scripted game's final board, winner, and move count, plus an overall win/draw tally.

---

## Docs

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — high-level design: components, data flow, trade-offs
- [docs/DESIGN.md](docs/DESIGN.md) — low-level design: classes, functions, parameters, extension points
- [docs/RUNBOOK.md](docs/RUNBOOK.md) — how to demo, troubleshoot, and run reliably
- [docs/PRESENTATION.md](docs/PRESENTATION.md) — pitch script, talking points, resume bullet, interview Q&A

## License

MIT — see the repository root `LICENSE` file.
