# Presentation Guide — Academic Paper Q&A: Rag_Simulator

## 60-Second Pitch

I built a Academic Paper Q&A that chunks documents, retrieves the most relevant passages with TF-IDF scoring, and answers with citations. Academic paper Q&A retrieves across a corpus of papers, synthesizing findings and noting where papers agree or disagree.

Academic Paper Q&A in two sentences: Academic paper Q&A retrieves across a corpus of papers, synthesizing findings and noting where papers agree or disagree. Citation format follows academic conventions with section references. Contradiction detection flags when sources make opposing claims.

## Architecture Talking Points

- Components: a single module plus the CLI entrypoint — each maps to a real module in `src/`, and the data-flow diagram shows how they connect.
- Algorithm: Fixed-size word chunking with overlap, TF-IDF-weighted term-overlap retrieval, extractive answer from the top chunk with citation.; runs in O(C*T) to score C chunks against T query terms; IDF build is O(total tokens)..
- Honest scaling limit: In-memory chunk list suits thousands of chunks; millions would need an inverted index instead of per-query rescoring.

Use these when someone asks "how does it work?" — start with the problem, then walk the data flow, then name one trade-off. Trade-offs are what interviewers remember.

## Resume Bullet

Copy-paste ready (adapt the verbs to your own voice):

```
Built a Academic Paper Q&A in Python implementing chunking, TF-IDF retrieval, and citation-backed extractive answering over a seeded corpus.
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
