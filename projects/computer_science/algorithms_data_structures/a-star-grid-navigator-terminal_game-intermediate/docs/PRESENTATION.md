# Presentation Guide — A-Star Grid Navigator: Terminal Game

## 60-Second Pitch

I built a A-Star Grid Navigator with an unbeatable AI opponent that you can watch play itself or challenge directly. A-star guides Dijkstra with a heuristic estimating remaining distance, exploring far fewer nodes when the heuristic is admissible.

A-Star Grid Navigator in two sentences: A-star guides Dijkstra with a heuristic estimating remaining distance, exploring far fewer nodes when the heuristic is admissible. The navigator compares node expansions of Dijkstra, greedy, and A-star on obstacle grids with Manhattan and Euclidean heuristics. Good heuristics feel like cheating.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Full-depth minimax tic-tac-toe with center-first deterministic move order; runs in O(b^d) minimax per move; trivial for a 3x3 board.
- Honest scaling limit: Minimax is fine for 3x3; larger boards would need depth limits or alpha-beta pruning.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a A-Star Grid Navigator in Python with a full-depth minimax AI, scripted demo games, and an interactive play mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Why full-depth minimax instead of a heuristic?

**A:** Tic-tac-toe is fully solved and tiny: full-depth minimax explores the whole game tree in milliseconds, so no pruning is needed.

**Q:** Is the AI's play deterministic?

**A:** Ties are broken by the fixed MOVE_ORDER (center first), so the AI's choices are identical on every run.

**Q:** How does the scoring work?

**A:** X maximizes (+1 win) and O minimizes (-1 loss); the recursion returns the best achievable score and its move.
