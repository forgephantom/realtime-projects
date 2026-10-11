# Presentation Guide — Form Validation Engine: Quiz Engine

## 60-Second Pitch

I built a Form Validation Engine that quizzes you with shuffled options, scores every answer, and grades the result. Server-side validation is the real gatekeeper: the engine declares per-field rules (required, type, length, pattern, cross-field matches), runs them in order, and returns structured per-field errors the UI can render.

Form Validation Engine in two sentences: Server-side validation is the real gatekeeper: the engine declares per-field rules (required, type, length, pattern, cross-field matches), runs them in order, and returns structured per-field errors the UI can render. It distinguishes missing vs malformed vs business-rule failures and never trusts client-side checks. Sanitization runs alongside validation, not instead of it.

## Architecture Talking Points

- Components: `Question`, `Quiz` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Seeded shuffle of options; simulated test taker with configurable accuracy; runs in O(q) per session over q questions.
- Honest scaling limit: In-memory question bank; fine for hundreds of questions, no database or multi-user session support.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Form Validation Engine in Python with deterministic option shuffling, auto and interactive answering modes, and letter-grade scoring.
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
