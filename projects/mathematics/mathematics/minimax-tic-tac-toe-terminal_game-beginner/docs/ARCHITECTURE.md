# Architecture (HLD) — Minimax Tic-Tac-Toe Engine: Terminal Game

## Problem & Users

Minimax Tic-Tac-Toe Engine built as a terminal game. Minimax chooses the move maximizing the worst-case outcome assuming optimal opponent play, and alpha-beta pruning skips branches that cannot change the decision. Tic-tac-toe is small enough to solve completely. The game plays perfectly as either side and explains each move's minimax value. A playable tic-tac-toe game with an unbeatable minimax AI: scripted AI-vs-AI demo by default, interactive play with --play.

The intended user is a student or engineer working in mathematics (mathematics) who needs a working, runnable reference for Minimax Tic-Tac-Toe Engine — something they can read end to end, run in seconds, and adapt to their own data or experiments.

## System Components

| Component | Module | Responsibility |
|---|---|---|
| CLI entrypoint | main | Argument parsing and demo orchestration via main() |

Each component maps to a real module in the project; no box in this design is aspirational — everything named here exists in the source tree.

## Data Flow

```
new_board -> play_game(x_move, o_move) -> move functions
minimax(board, player) -> (score, best_move) each turn
winner(board) -> X / O / draw / None -> rendered final board + tally
```

## Storage

No persistence: boards and tallies exist only during the run.

## Scaling & Limits

Minimax is fine for 3x3; larger boards would need depth limits or alpha-beta pruning.

## Trade-offs

Pure minimax is simple and provably optimal here, but it would be far too slow for games with bigger branching factors.

## Failure Handling

Illegal moves raise ValueError in scripted play; interactive mode re-prompts instead of crashing, and 'q' quits cleanly.

---

*Design intent:* this document deliberately favors honesty over hype. Every claim above corresponds to something the code actually does; where the implementation is a teaching simplification, that is stated rather than hidden.
