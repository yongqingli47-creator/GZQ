from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not text.startswith("---\n"):
        return {}, [f"{path.relative_to(ROOT)}: missing opening frontmatter delimiter"]

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, [f"{path.relative_to(ROOT)}: missing closing frontmatter delimiter"]

    raw_frontmatter = parts[0].splitlines()[1:]
    data: dict[str, str] = {}
    for line in raw_frontmatter:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{path.relative_to(ROOT)}: invalid frontmatter line '{line}'")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")

    return data, errors


def validate_prompt(path: Path) -> list[str]:
    frontmatter, errors = parse_frontmatter(path)
    if errors:
        return errors

    if not frontmatter.get("description"):
        errors.append(f"{path.relative_to(ROOT)}: missing description")
    if not frontmatter.get("agent"):
        errors.append(f"{path.relative_to(ROOT)}: missing agent")
    return errors


def validate_skill(path: Path) -> list[str]:
    frontmatter, errors = parse_frontmatter(path)
    if errors:
        return errors

    expected_name = path.parent.name
    actual_name = frontmatter.get("name", "")
    if actual_name != expected_name:
        errors.append(
            f"{path.relative_to(ROOT)}: name '{actual_name}' does not match folder '{expected_name}'"
        )
    if not frontmatter.get("description"):
        errors.append(f"{path.relative_to(ROOT)}: missing description")
    return errors


def validate_instruction(path: Path) -> list[str]:
    frontmatter, errors = parse_frontmatter(path)
    if errors:
        return errors
    if not frontmatter.get("applyTo"):
        errors.append(f"{path.relative_to(ROOT)}: missing applyTo")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / ".github" / "prompts").glob("*.prompt.md")):
        errors.extend(validate_prompt(path))

    for path in sorted((ROOT / ".github" / "skills").glob("*/SKILL.md")):
        errors.extend(validate_skill(path))

    github_skills = {
        path.parent.name: path
        for path in (ROOT / ".github" / "skills").glob("*/SKILL.md")
    }
    codex_skills = {
        path.parent.name: path
        for path in (ROOT / ".agents" / "skills").glob("*/SKILL.md")
    }
    for path in sorted(codex_skills.values()):
        errors.extend(validate_skill(path))

    missing_from_codex = sorted(github_skills.keys() - codex_skills.keys())
    missing_from_github = sorted(codex_skills.keys() - github_skills.keys())
    if missing_from_codex:
        errors.append(
            ".agents/skills: missing Codex copies for " + ", ".join(missing_from_codex)
        )
    if missing_from_github:
        errors.append(
            ".github/skills: missing Copilot copies for " + ", ".join(missing_from_github)
        )

    for name in sorted(github_skills.keys() & codex_skills.keys()):
        if github_skills[name].read_bytes() != codex_skills[name].read_bytes():
            errors.append(f"skill '{name}': .github and .agents SKILL.md files differ")

    for path in sorted((ROOT / ".github" / "instructions").glob("*.instructions.md")):
        errors.extend(validate_instruction(path))

    for required in [ROOT / "AGENTS.md", ROOT / ".github" / "copilot-instructions.md"]:
        if not required.exists():
            errors.append(f"{required.relative_to(ROOT)}: required file is missing")

    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("Customization validation failed:\n")
        for entry in errors:
            print(f"- {entry}")
        return 1

    print("Customization validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
