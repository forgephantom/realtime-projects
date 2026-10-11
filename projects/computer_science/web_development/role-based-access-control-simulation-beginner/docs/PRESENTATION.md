# Presentation Guide — Role-Based Access Control (RBAC): Simulation (Logistic Growth)

## 60-Second Pitch

A Role-Based Access Control (RBAC) simulation in pure Python that integrates logistic growth with Euler steps and prints the full trajectory toward carrying capacity. RBAC manages permissions through roles: users get roles, roles get permissions, and checks ask 'does this user have permission X'.

Role-Based Access Control (RBAC) in two sentences: RBAC manages permissions through roles: users get roles, roles get permissions, and checks ask 'does this user have permission X'. Role hierarchies and separation-of-duties constraints (no single user may both request and approve) encode policy. Reviews prune stale grants. It scales where per-user ACLs collapse.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Explicit Euler integration of logistic growth; runs in O(steps).
- Honest scaling limit: The trajectory is a plain list, so millions of steps would use noticeable memory; streaming or downsampling would fix that.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Role-Based Access Control (RBAC) simulator in Python (stdlib) implementing Euler integration of logistic growth with seeded parameters; demo runs end-to-end and prints the trajectory table with summary statistics.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** What dynamics does the model show?

**A:** Logistic growth: fast early rise that levels off at the carrying capacity K, a common shape for adoption and saturation processes.

**Q:** How is accuracy controlled?

**A:** --steps and --dt; smaller dt is more accurate, larger dt runs faster but can overshoot.

**Q:** Why Euler instead of RK4?

**A:** Euler is first-order and simple to read; the template favors clarity over the accuracy of higher-order integrators.
