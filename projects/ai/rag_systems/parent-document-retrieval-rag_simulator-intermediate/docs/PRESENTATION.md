# Presentation Guide — Parent Document Retrieval: Rag_Simulator

## 60-Second Pitch

I built a Parent Document Retrieval that chunks documents, retrieves the most relevant passages with TF-IDF scoring, and answers with citations. Parent-document retrieval searches small child chunks for precision but returns the full parent document for context.

Parent Document Retrieval in two sentences: Parent-document retrieval searches small child chunks for precision but returns the full parent document for context. This gives the generator complete surrounding information instead of a fragment. Parent size and child size are tuned together for the corpus.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Fixed-size word chunking with overlap, TF-IDF-weighted term-overlap retrieval, extractive answer from the top chunk with citation.; runs in O(C*T) to score C chunks against T query terms; IDF build is O(total tokens)..
- Honest scaling limit: In-memory chunk list suits thousands of chunks; millions would need an inverted index instead of per-query rescoring.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Parent Document Retrieval in Python implementing chunking, TF-IDF retrieval, and citation-backed extractive answering over a seeded corpus.
```

**Placement tips:**

1. Put this under a "Projects" section near the top of your resume if the project is the strongest evidence of the skill the job asks for; otherwise place it in an appendix or portfolio link and keep the bullet lean.
2. Never put two bullets from the same project on a resume — pick the single bullet that best matches the job description and cut the rest.

## Interview Q&A

**Q:** How is a chunk scored?

**A:** Term frequency inside the chunk times inverse document frequency across chunks; rare query terms count more than common ones.

**Q:** Why do chunks overlap?

**A:** Overlap keeps sentences that straddle a boundary inside at least one chunk, so retrieval does not lose context at cut points.

**Q:** Can this run on real documents?

**A:** Yes: score_chunk is pure, and retrieve just sorts, so any chunk list and IDF table work, including ones from real documents.
