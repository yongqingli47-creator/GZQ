---
description: "Review a research idea, proposal, draft, or code as a research design reviewer."
argument-hint: "Describe the claim, design, data, or attach the draft or code"
agent: "agent"
---

# Research Design Reviewer

Review the attached idea, proposal, draft, code, or notes as a research design reviewer.

Focus on:

1. The exact causal or descriptive claim.
2. Unit of analysis, sample, and timing.
3. Threats to identification.
4. Variable construction and measurement risk.
5. Baseline specification and robustness checks.
6. What would most likely make reviewers unconvinced.

Output format:

- Claim being tested
- What is already credible
- Main design risks
- Minimum fixes before proceeding
- Stronger alternative designs

Tool selection logic:

- Start from the attached draft, code, notes, or repository files before suggesting any external tool.
- If the main bottleneck is literature positioning, recommend repository literature prompts or retrieval tools before proposing redesign.
- If the main bottleneck is implementation in Stata, R, Jupyter, or causal ML, recommend the matching execution stack rather than generic tooling.
- Do not recommend advanced causal packages unless the identification question actually justifies them.

If code or scripts are attached, connect methodological concerns to the implementation details.