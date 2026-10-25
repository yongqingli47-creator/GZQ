---
name: empirical-analysis
description: "Use this skill for empirical research tasks involving data cleaning, variable construction, estimation strategy, robustness checks, reproducibility, or notebook and script review"
argument-hint: "Describe the data, variables, scripts, identification concern, or analysis task"
---

# Empirical Analysis Skill

Use this skill for data cleaning, data construction, empirical analysis, and estimation work.

## Core Priorities

1. Reproducibility before sophistication.
2. Clear mapping from theory to variables.
3. Explicit sample restrictions and missing-data handling.
4. Identification assumptions stated in plain language.
5. Robustness checks chosen to challenge the main claim, not decorate it.
6. Data cleaning choices documented so another researcher can reproduce them.

## Review Checklist

- What is the unit of analysis?
- How are key variables defined and transformed?
- What observations are excluded, and why?
- How are duplicates, outliers, and missing values handled?
- What is the baseline model and why is it appropriate?
- What alternative explanations remain?
- What output or diagnostic would falsify the current claim?

## Implementation Guidance

- Prefer scripts over manual spreadsheet operations.
- Keep paths, seeds, and environment assumptions explicit.
- When reviewing notebooks, separate exploratory cells from reproducible pipeline logic.
- When asked to clean data, propose a pipeline covering import, schema checks, type conversion, duplicate handling, missing values, outlier rules, derived variables, validation, and export.

## Procedure

1. Restate the empirical objective, unit of analysis, and expected output.
2. Separate observed facts from assumptions about the data or identification strategy.
3. Propose the smallest reproducible pipeline that can expose schema, sample, or measurement risks quickly.
4. Define the baseline analysis and the first falsification or robustness checks.
5. End with the exact validation outputs or files needed before widening scope.

## External Tool And Reproducibility Gate

- Choose the estimator and analysis environment from the research design, estimand, and data structure before choosing an MCP server, package, or agent. A tool directory is a discovery aid, not a validated method recommendation.
- Treat MCP servers as interfaces to commands and data, and packages as implementations of specified methods. Neither verifies identification assumptions or makes an analysis reproducible by itself.
- Before connecting a new tool, inspect its primary documentation, license, supported versions, maintenance state, dependencies, data flows, and required credentials or write permissions. Do not send restricted data to an external service without an approved data path.
- Start with a read-only or dry-run check on a small, non-sensitive fixture and compare the output with a known result or the canonical local implementation.
- Preserve the exact script/command, package and runtime versions, input identifiers or hashes, seeds, logs, and machine-readable outputs needed to recreate each reported result. Keep exploratory output separate from the result used in the manuscript.
