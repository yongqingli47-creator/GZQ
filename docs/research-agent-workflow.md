# Research Agent Workflow

This repository now supports literature-grounded AI workflows through repository-local Zotero resources.

## Literature Sources The Agent Should Read

1. `literature/bib/library.bib` when present, otherwise collection-specific `.bib` files in the same folder
2. `literature/metadata/zotero_items.json`
3. `literature/metadata/zotero_items.md`

## Agent Rules Added To The Repository

- `AGENTS.md` now points literature-heavy work to `zotero-library-ops`.
- `.github/instructions/zotero-library.instructions.md` defines source priority and reproducibility rules.
- `.github/skills/zotero-library-ops/SKILL.md` defines how to organize, triage, and synthesize library content.

## Prompt Files For Batch Tasks

Use these prompt files from chat:

- `/zotero-batch-organize`
- `/zotero-review-outline`
- `/literature-review`
- `/literature-matrix`

## Recommended Usage Patterns

### Batch literature organization

Ask for:

```text
Use /zotero-batch-organize and focus on digital innovation and corporate governance.
```

### Literature review drafting

Ask for:

```text
Use /zotero-review-outline and build a review for executive compensation and ESG disclosure.
```

### Paper outline generation

Ask for:

```text
Use /zotero-review-outline and convert the current literature set into a paper outline.
```

## Curated External Stack

Use external tools as extensions to the repository workflow, not as replacements for local evidence, local prompts, or repository literature files.

### 1. Orchestration and stage discipline

- Prefer `Imbad0202/academic-research-skills` when a task needs multi-stage research, writing, and review gates.
- Prefer `AlterLab-IEU/AlterLab-Academic-Skills` as a broad reference library when the task spans disciplines or requires specialized sub-workflows.
- Keep this repository's local skills as the execution layer. External packs should sharpen the stage design, not override repository source rules.

### 2. Economics writing and peer review

- Prefer `hanlulong/econ-writing-skill` for economics-style framing, contribution language, and revision heuristics.
- Prefer `claesbackman/AI-research-feedback`, `poldrack/ai-peer-review`, and `kenwilliford/claude-peer-review` when simulating reviewer heterogeneity or editor arbitration.
- Do not add "humanizer" or de-AI-polish workflows to the core repository workflow. This workspace should improve argument quality, evidence alignment, and readability directly.

### 3. Literature retrieval, grounding, and verification

- Keep local Zotero exports as the first source.
- Add `54yyyu/zotero-mcp` or `cookjohn/zotero-mcp` when the task needs live Zotero interaction beyond the repository snapshot.
- Add `openags/paper-search-mcp`, `oksure/openalex-research-mcp`, or `xiuyechen/semantic-scholar-mcp` when the local library is too narrow for topic expansion.
- Add `JonasBaath/mcp-refchecker` when reference hallucination or metadata inconsistency is the main risk.

### 4. Empirical and causal analysis extensions

- For Stata-heavy workflows, prefer `SepineTam/stata-mcp` or `hanlulong/stata-mcp`.
- For R-heavy workflows, prefer `posit-dev/mcptools` and `gojiplus/r-econometrics-mcp`.
- For notebook control, prefer `datalayer/jupyter-mcp-server`.
- For causal inference or heterogeneous treatment effects, prioritize `py-why/EconML`, `DoubleML/doubleml-for-py`, `py-why/DoWhy`, and `uber/causalml`.
- Treat these tools as estimation or diagnostic layers. The repository still requires explicit variable definitions, sample restrictions, and falsification logic.

### 5. Deep research, systematic review, and writing infrastructure

- Prefer `Stanford STORM`, `PaperQA2`, or `LangChain Open Deep Research` for exploratory evidence collection or multi-perspective literature mapping.
- Prefer `ASReview` for title and abstract screening in systematic review workflows.
- Prefer `mjyoo2/OverleafMCP` when the manuscript workflow must sync with Overleaf through Git.
- Prefer `Microsoft Playwright MCP` or `firecrawl/firecrawl-mcp-server` only when authenticated web retrieval or structured web extraction is unavoidable.

## Adoption Order

1. Start with repository-local prompts, skills, and literature files.
2. Add one external tool only when a concrete bottleneck is clear: live library sync, broader literature search, econometric execution, or review simulation.
3. Validate the output inside the repository workflow before adding a second external layer.
4. Record source boundaries clearly when external tools contribute evidence, citations, screening, or estimation output.

## Quality Control

- Refresh the metadata snapshot before major literature tasks.
- Run the `Repository: validate Copilot customizations` task after changing prompt files, skills, instructions, or agent workflow guidance.
- Treat abstract-based synthesis as a screening layer, not a substitute for full-paper verification.
- Narrow to a collection or topic if the library is too broad for a precise review.
- Prefer official, actively maintained, or field-recognized tools when extending this workflow. If tool quality is uncertain, keep the repository workflow unchanged until the tool has a clear comparative advantage.