# Presentation Guide — AQI Trend Analyzer: Data Pipeline (Etl)

## 60-Second Pitch

A AQI Trend Analyzer ETL pipeline that extracts seeded records, cleans and buckets them, loads a CSV, and reports every stage count. The Air Quality Index compresses pollutant concentrations into a single 0-to-500 scale with color-coded health categories from Good to Hazardous.

AQI Trend Analyzer in two sentences: The Air Quality Index compresses pollutant concentrations into a single 0-to-500 scale with color-coded health categories from Good to Hazardous. Tracking daily AQI over months reveals seasonal patterns, like summer ozone peaks and winter particulate episodes.

## Architecture Talking Points

- Components: `Pipeline` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extract -> transform -> load over synthetic records; runs in O(n) across all three stages.
- Honest scaling limit: All rows are held in memory between stages, so very large inputs would need chunked or streaming processing instead.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a AQI Trend Analyzer ETL pipeline in Python (stdlib csv) with extract, transform, and load stages; handles corrupt rows with drop counts and reports per-stage statistics to the console.
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
