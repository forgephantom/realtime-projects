# Presentation Guide — Document Ingestion Pipeline: File Organizer

## 60-Second Pitch

I built a Document Ingestion Pipeline that tidies a messy folder into categorized subfolders, showing you the plan before it moves anything. A document ingestion pipeline loads raw files, extracts clean text, splits it into chunks, and indexes the embeddings with metadata.

Document Ingestion Pipeline in two sentences: A document ingestion pipeline loads raw files, extracts clean text, splits it into chunks, and indexes the embeddings with metadata. Format handlers deal with PDFs, spreadsheets, and HTML quirks. Idempotent re-ingestion updates changed documents without duplicating the index.

## Architecture Talking Points

- Components: `FileOrganizer` plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Extension-to-folder mapping with a plan-then-execute move pass; runs in O(f) over f files.
- Honest scaling limit: Single-machine, single-threaded moves; fine for thousands of files, not a distributed file pipeline.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Document Ingestion Pipeline in Python that sorts files into extension-mapped folders with a plan-then-execute pass and dry-run mode.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How does it decide which folder a file goes to?

**A:** The extension map comes from {'formats': 'file formats to support', 'metadata_fields': 'metadata extracted per document', 'reingest_mode': 'update or skip unchanged files'}; any extension not listed is routed to a 'misc' folder.

**Q:** What is the point of plan() versus execute()?

**A:** plan() computes every move first, so --dry-run can show the full plan and execute() just carries it out.

**Q:** Is the demo safe to rerun?

**A:** Yes: the demo wipes and recreates ./demo_workspace at startup, so reruns are clean and deterministic.
