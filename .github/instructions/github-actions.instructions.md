---
applyTo: ".github/workflows/**/*.yml,.github/workflows/**/*.yaml"
---

When creating or editing GitHub Actions workflows:

## Security
- Keep `permissions` minimal for each workflow and job.
- Never hardcode secrets, tokens, or credentials.
- Prefer pinned SHAs for third-party actions when the action is not maintained by GitHub.

## Reliability
- Add `timeout-minutes` to jobs that could hang.
- Use explicit cache settings only when the dependency manager benefits from them.
- Keep workflow names, job names, and step names descriptive.
- Include `workflow_dispatch` when manual triggering is useful.

## Performance
- Avoid duplicate jobs across `push` and `pull_request` unless behavior differs.
- Use matrices only when multi-version or multi-platform coverage is actually needed.

## Review Standard
- Explain why each trigger exists.
- Prefer the smallest workflow that enforces the intended quality gate.
- If a workflow writes to the repository or opens pull requests, justify that permission clearly.