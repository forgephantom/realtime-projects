# Presentation Guide — Support Ticket Triage: Chatbot

## 60-Second Pitch

I built a Support Ticket Triage that understands what you are asking from keywords and answers from a configurable intent table. Ticket triage reads an incoming support request, assigns priority and category, and routes it to the right queue with a suggested first response.

Support Ticket Triage in two sentences: Ticket triage reads an incoming support request, assigns priority and category, and routes it to the right queue with a suggested first response. Priority scoring weighs urgency signals like outage language against customer tier. Misrouted tickets are the key metric, tracked per category in the simulation.

## Architecture Talking Points

- Components: `Chatbot` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Keyword-overlap intent scoring with a fallback intent; runs in O(i*k) per message over i intents and k keywords.
- Honest scaling limit: Keyword scoring suits tens of intents; hundreds would want TF-IDF or embeddings instead of substring counting.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Support Ticket Triage in Python using keyword-based intent matching with scripted and interactive conversation modes.
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
