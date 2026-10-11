# Presentation Guide — BGP Route Selector: Config Manager

## 60-Second Pitch

I built a BGP Route Selector that merges defaults, files, environment, and CLI flags into one validated configuration with full provenance. BGP picks routes by policy, not just cost: the selector implements the decision process (local-pref, AS-path length, origin, MED) over seeded announcements and shows how policy overrides shortest-path.

BGP Route Selector in two sentences: BGP picks routes by policy, not just cost: the selector implements the decision process (local-pref, AS-path length, origin, MED) over seeded announcements and shows how policy overrides shortest-path. It explains internet routing's political economy. Route filtering enforces the policy.

## Architecture Talking Points

- Components: `Config` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Layered merge: defaults < ini string < environment < CLI, with typed coercion; runs in O(k) over k config keys.
- Honest scaling limit: Flat key/value schema suits service config; deeply nested configs would want a tree model instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a BGP Route Selector in Python with four-layer precedence, typed coercion, per-key source tracking, and schema validation.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What is the precedence order?

**A:** Later layers win: defaults, then the INI snippet, then PREFIX_* environment variables, then --set overrides.

**Q:** How do you know where a value came from?

**A:** Every set records its layer in _sources, so the demo prints exactly where each value came from.

**Q:** How are booleans parsed?

**A:** Booleans accept true/false/1/0/yes/no/on/off case-insensitively; anything else raises ValueError.
