---
description: "Use repository Zotero resources to cluster papers, build a literature matrix, and prioritize reading."
argument-hint: "Describe the topic or ask to infer it from repository literature files"
agent: "agent"
---

# Zotero Batch Organizer

Use the repository literature resources to organize the current paper set.

Task:

1. Read `literature/metadata/zotero_items.json` and `literature/bib/library.bib` when present; otherwise read other `.bib` exports under `literature/bib/`.
2. Build a structured literature matrix grouped by question, mechanism, method, and main findings.
3. Mark each paper as `must-read`, `useful`, or `peripheral` for the stated topic.
4. Flag where abstracts are missing, where metadata is stale, or where full-text reading is still necessary.
5. End with a short action list titled `Next Reading Moves`.

Output format:

- Topic assumption
- Paper clusters
- Literature matrix
- Reading priority
- Missing information
- Next reading moves

Tool selection logic:

- Use repository-local Zotero exports first.
- Suggest live Zotero tooling only when the checked-in snapshot is stale, sparse, or misaligned with the requested topic.
- Suggest external literature search only when the current library cannot support a credible clustering.
- Suggest systematic screening tools only when the paper set is large enough that manual title and abstract triage is inefficient.

If I do not specify a topic, infer one from the most common themes in the repository library files.