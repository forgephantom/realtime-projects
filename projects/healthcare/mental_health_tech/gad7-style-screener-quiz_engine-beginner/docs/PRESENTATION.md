# Presentation Guide — GAD-7-Style Self-Assessment Scorer: Quiz Engine

## 60-Second Pitch

I built a GAD-7-Style Self-Assessment Scorer that quizzes you with shuffled options, scores every answer, and grades the result. Anxiety screening questionnaires follow the same structure as depression screens: frequency-rated items summed into a total with severity bands.

GAD-7-Style Self-Assessment Scorer in two sentences: Anxiety screening questionnaires follow the same structure as depression screens: frequency-rated items summed into a total with severity bands. The tool is strictly educational, showing how scoring works on synthetic data while making clear that results are not a diagnosis. Disclaimer text accompanies every result screen. Includes prominent disclaimer text that the tool is for wellness self-tracking and screening only, never a diagnosis, and encourages consulting a professional.

## Architecture Talking Points

- Components: `Question`, `Quiz` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded shuffle of options; simulated test taker with configurable accuracy; runs in O(q) per session over q questions.
- Honest scaling limit: In-memory question bank; fine for hundreds of questions, no database or multi-user session support.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a GAD-7-Style Self-Assessment Scorer in Python with deterministic option shuffling, auto and interactive answering modes, and letter-grade scoring.
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
