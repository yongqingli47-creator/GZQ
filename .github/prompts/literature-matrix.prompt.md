---
description: "Build a structured literature matrix from papers, notes, citations, or a topic description."
argument-hint: "Describe the topic, attach papers, or point to repository literature files"
agent: "agent"
---

# Literature Matrix Builder

Build a structured literature matrix from the attached papers, notes, citations, or topic description.

For each study, extract:

- Citation key or short title
- Research question
- Theory or mechanism
- Data and sample
- Method or identification strategy
- Main finding
- Limitation
- Relevance to my project

Then provide:

- A thematic grouping of the studies
- The most important disagreements in the literature
- Which papers are essential reading first

Tool selection logic:

- Start with repository-local literature files and attached papers before proposing outside search.
- Use live Zotero tooling only when the local library snapshot is clearly outdated or missing a relevant collection.
- Use external search tools only to fill a defined coverage gap, not to widen scope by default.
- Use citation-verification tools when duplicate records, missing metadata, or suspect references would weaken the matrix.

If the attached material is incomplete, infer a provisional matrix structure and state what is still missing.