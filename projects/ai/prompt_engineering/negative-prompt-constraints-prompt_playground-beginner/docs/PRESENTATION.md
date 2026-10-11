# Presentation Guide — Negative Prompt Constraints: Prompt_Playground

## 60-Second Pitch

I built a Negative Prompt Constraints that A/B tests prompt variants over seeded inputs and scores them with a transparent rubric. Negative constraints tell the model what to avoid: no jargon, no invented dates, no markdown tables.

Negative Prompt Constraints in two sentences: Negative constraints tell the model what to avoid: no jargon, no invented dates, no markdown tables. Explicit prohibitions work better than hoping the model guesses the boundaries. The lab measures violation rates with and without negative constraints on the same tasks.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Deterministic stub generation keyed by prompt hash, scored by a rubric heuristic over topic terms, required words, and length bounds.; runs in O(V*I) for V variants over I test inputs; scoring is linear in response length..
- Honest scaling limit: The loop is single-threaded and suits hundreds of inputs; thousands would want batched or async model calls.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Negative Prompt Constraints in Python that renders prompt templates, runs A/B variants over seeded inputs, and compares them with rubric scoring.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does the stub model work?

**A:** A zlib CRC32 hash of the prompt picks canned sentences, so the same prompt always yields the same response.

**Q:** What goes into the score?

**A:** One point for the topic term, one per required word found, one for staying within the word-count bounds, divided by the total.

**Q:** Can this drive a real model?

**A:** Swap stub_generate for a real model call; the rendering, scoring, and table code stays the same.
