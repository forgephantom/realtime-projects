# Presentation Guide — Mendelian Ratio Chi-Square Analyzer: Quiz Engine

## 60-Second Pitch

I built a Mendelian Ratio Chi-Square Analyzer that quizzes you with shuffled options, scores every answer, and grades the result. Mendel's ratios (3:1, 9:3:3:1, 1:1) are hypotheses tested with chi-square: squared deviations of observed from expected counts, scaled by expectation.

Mendelian Ratio Chi-Square Analyzer in two sentences: Mendel's ratios (3:1, 9:3:3:1, 1:1) are hypotheses tested with chi-square: squared deviations of observed from expected counts, scaled by expectation. The analyzer takes observed offspring counts and a hypothesized ratio, returning the statistic, p-value, and accept/reject verdict. It warns when expected counts are too small.

## Architecture Talking Points

- Components: `Question`, `Quiz` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded shuffle of options; simulated test taker with configurable accuracy; runs in O(q) per session over q questions.
- Honest scaling limit: In-memory question bank; fine for hundreds of questions, no database or multi-user session support.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Mendelian Ratio Chi-Square Analyzer in Python with deterministic option shuffling, auto and interactive answering modes, and letter-grade scoring.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How do you stop the answer always being option 1?

**A:** The option order is shuffled with the seeded RNG and the correct index is remapped, so position carries no information.

**Q:** How does the auto-answered demo work?

**A:** run_auto answers each question correctly with probability accuracy, using a dedicated RNG so the demo is reproducible.

**Q:** How are grades assigned?

**A:** A/B/C/D/F at 90/80/70/60 percent cutoffs, computed from score over total questions.
