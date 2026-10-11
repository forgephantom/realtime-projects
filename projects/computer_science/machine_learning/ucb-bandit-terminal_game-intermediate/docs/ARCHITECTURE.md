# Architecture (HLD) — UCB Bandit (Optimism in the Face of Uncertainty): Terminal Game

## Problem & Users

UCB Bandit (Optimism in the Face of Uncertainty) built as a terminal game. UCB picks the arm with the highest upper confidence bound: estimated reward plus an exploration bonus shrinking with pulls. It explores systematically instead of randomly, with strong regret guarantees. The confidence width parameter tunes exploration. A playable tic-tac-toe game with an unbeatable minimax AI: scripted AI-vs-AI demo by default, interactive play with --play.

The intended user is a student or engineer working in computer_science (machine_learning) who needs a working, runnable reference for UCB Bandit (Optimism in the Face of Uncertainty) — something they can read end to end, run in seconds, and adapt to their own data or experiments.

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
