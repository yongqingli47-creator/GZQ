---
name: zotero-library-ops
description: "Use this skill for Zotero API syncing, Better BibTeX grounded reference work, metadata extraction, abstract-based paper triage, and repository-based batch literature workflows"
argument-hint: "Describe the topic, collection, library refresh need, or literature output you want"
---

# Zotero Library Ops Skill

Use this skill when the task depends on repository-local Zotero resources or on refreshing them.

## Core Rules

1. Start from repository sources in `literature/bib/` and `literature/metadata/` before drafting synthesis.
2. Prefer traceable outputs that can be regenerated after Zotero updates.
3. Distinguish what comes from metadata, what comes from abstracts, and what still requires full-text reading.
4. If the request spans many papers, produce structured intermediate artifacts before prose.
5. When source coverage is thin, ask for the minimum additional export or collection refresh needed.

## Typical Inputs

- `literature/bib/library.bib` when present, otherwise other `.bib` exports in `literature/bib/`
- `literature/metadata/zotero_items.json`
- `literature/metadata/zotero_items.md`
- User-provided topic, question, mechanism, or paper set

## Typical Outputs

- Reading priority lists
- Literature matrices
- Theme coding tables
- Consensus versus disagreement maps
- Review section outlines
- Paper or dissertation chapter outlines anchored to specific references

## Workflow

1. Check whether the Zotero metadata snapshot is present and current enough.
2. Check whether the preferred Better BibTeX export exists; if not, fall back to other `.bib` files in `literature/bib/`.
3. Identify the relevant subset of papers.
4. Extract problem, mechanism, method, findings, and limits.
5. Organize before drafting.
6. Surface missing evidence or stale library risks.

## Do Not

- Treat abstracts as substitutes for full-paper causal claims.
- Infer contribution quality from journal prestige alone.
- Produce generic review prose when the repository files support a sharper structure.