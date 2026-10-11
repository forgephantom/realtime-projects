# Presentation Guide — UTM Campaign Parser: Data Pipeline (Etl)

## 60-Second Pitch

A UTM Campaign Parser ETL pipeline that extracts seeded records, cleans and buckets them, loads a CSV, and reports every stage count. Marketing attribution starts with UTM tags: the parser extracts utm_source/medium/campaign from URLs, normalizes naming conventions, attributes sessions to campaigns, and reports spend efficiency per campaign.

UTM Campaign Parser in two sentences: Marketing attribution starts with UTM tags: the parser extracts utm_source/medium/campaign from URLs, normalizes naming conventions, attributes sessions to campaigns, and reports spend efficiency per campaign. Consistent taxonomy is enforced because 'Email' vs 'email' splits reports. It is unglamorous and essential.

## Architecture Talking Points

- Components: `Pipeline` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extract -> transform -> load over synthetic records; runs in O(n) across all three stages.
- Honest scaling limit: All rows are held in memory between stages, so very large inputs would need chunked or streaming processing instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a UTM Campaign Parser ETL pipeline in Python (stdlib csv) with extract, transform, and load stages; handles corrupt rows with drop counts and reports per-stage statistics to the console.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** Does the pipeline need a real data source?

**A:** No; generate_raw synthesizes deterministic rows from the seed, so the pipeline demonstrates all three stages with zero external input.

**Q:** How are corrupt rows handled?

**A:** clean_rows drops them, counts the drops, and reports the number in the stage report.

**Q:** Does it write files?

**A:** Yes; it is the only file write, and it stays inside the current working directory under demo_workspace/.
