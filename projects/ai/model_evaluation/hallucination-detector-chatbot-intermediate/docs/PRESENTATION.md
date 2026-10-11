# Presentation Guide — Hallucination Detection Simulator: Chatbot

## 60-Second Pitch

I built a Hallucination Detection Simulator that understands what you are asking from keywords and answers from a configurable intent table. Hallucinations are plausible statements that are unsupported or false.

Hallucination Detection Simulator in two sentences: Hallucinations are plausible statements that are unsupported or false. Detection strategies include checking claims against retrieved context, measuring self-consistency across multiple sampled answers, and scoring entity-level factuality. The simulation plants unsupported claims in generated text and measures detector precision and recall at claim granularity.

## Architecture Talking Points

- Components: `Chatbot` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Keyword-overlap intent scoring with a fallback intent; runs in O(i*k) per message over i intents and k keywords.
- Honest scaling limit: Keyword scoring suits tens of intents; hundreds would want TF-IDF or embeddings instead of substring counting.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Hallucination Detection Simulator in Python using keyword-based intent matching with scripted and interactive conversation modes.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How is the intent chosen?

**A:** Each keyword found as a substring adds one point; the highest-scoring intent wins, and the fallback intent wins ties at zero.

**Q:** Why not a machine-learning model?

**A:** Keyword matching is transparent and dependency-free; it handles the demo's small intent set without any model or training data.

**Q:** Can the bot say something wrong?

**A:** It never invents replies; every response comes verbatim from the intent table, so the bot cannot hallucinate.
