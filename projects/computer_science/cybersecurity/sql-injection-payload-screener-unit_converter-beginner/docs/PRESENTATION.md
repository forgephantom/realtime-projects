# Presentation Guide — SQL Injection Payload Screener: Unit Converter

## 60-Second Pitch

I built a SQL Injection Payload Screener with real conversion factors across six categories, handling temperature offsets correctly. SQL injection happens when untrusted input is concatenated into database queries, letting an attacker alter the query logic with quotes, comments, and stacked statements.

SQL Injection Payload Screener in two sentences: SQL injection happens when untrusted input is concatenated into database queries, letting an attacker alter the query logic with quotes, comments, and stacked statements. The screener is a defensive input validator that scores incoming parameters against patterns for tautologies, union selects, stacked queries, and time-based blind probes without ever executing them. It reports which rule fired and a risk score so developers can find weak validation before attackers do.

## Architecture Talking Points

- Components: `UnitConverter` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Factor-to-base-unit tables; temperature via to/from-Celsius functions; runs in O(1) per conversion.
- Honest scaling limit: A static factor table; adding units is a one-line table edit with no code changes.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a SQL Injection Payload Screener in Python covering six unit categories with exact conversion factors and offset-aware temperature math.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Why is temperature special-cased?

**A:** Temperature scales have offsets, not just ratios, so conversions route through Celsius with dedicated to/from functions.

**Q:** How accurate are the factors?

**A:** Factors are exact definitions (e.g. 1 mi = 1609.344 m, 1 lb = 0.45359237 kg); data sizes offer both SI and binary units.

**Q:** What happens on a bad unit?

**A:** convert() raises ValueError naming the problem, which the CLI turns into exit code 2.
