---
name: literature-synthesis
description: "Use this skill for literature collection, paper comparison, theme coding, gap identification, reference organization, and turning source notes into a structured review"
argument-hint: "Describe the topic, attach papers or notes, or point to repository literature files"
---

# Literature Synthesis Skill

Use this skill when the task is to collect, compare, organize, or synthesize literature.

## Core Rules

1. Organize literature by problem, mechanism, method, and findings.
2. Distinguish seminal papers, mainstream evidence, and peripheral extensions.
3. Treat contradictory findings as an analytical target, not as noise.
4. Do not call something a research gap unless the missing piece matters for theory, identification, or external validity.
5. Prefer structured notes that can be converted into a review section or reading list.

## What To Extract From Each Paper

- Research question
- Theory or mechanism
- Data and sample
- Identification or method
- Main findings
- Limitations
- Usefulness for the current project

## Output Shape

- Topic map
- Key paper clusters
- Agreements and disagreements
- Real gap versus superficial gap
- Reading priority list

## Supervisor Use

- Help reduce reading overload by ranking what must be read now, later, or not at all.
- When reviewing student notes, identify where summary has replaced analysis.

## External Retrieval And Verification Stack

- Start from repository-local Zotero exports before any live retrieval.
- Use `54yyyu/zotero-mcp` or `cookjohn/zotero-mcp` when the task needs live Zotero interaction rather than the local snapshot.
- Use `openags/paper-search-mcp`, `oksure/openalex-research-mcp`, or `xiuyechen/semantic-scholar-mcp` when the local library is too narrow to cover the target question.
- Use `JonasBaath/mcp-refchecker` when citation validity is a binding risk.
- Use `Stanford STORM` or `PaperQA2` for exploratory topic mapping, not as substitutes for source-grounded claims about findings.

## Procedure

1. Define the focal question and the adjacent literatures that genuinely affect it.
2. Extract each study into a compact structure covering question, mechanism, method, findings, and limits.
3. Cluster studies before drafting prose.
4. Separate consensus, disagreement, and unresolved identification issues.
5. End with the most defensible positioning options or next-reading priorities.