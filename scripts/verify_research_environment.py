from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
STATA_LOG_PATH = ROOT / "stata_smoke.log"


@dataclass
class CheckResult:
    name: str
    ok: bool
    summary: str
    details: list[str]


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify the Stata, PostgreSQL, and Zotero environment for this workspace."
    )
    parser.add_argument(
        "--skip-stata",
        action="store_true",
        help="Skip the Stata batch smoke test.",
    )
    parser.add_argument(
        "--skip-postgres",
        action="store_true",
        help="Skip the PostgreSQL connectivity check.",
    )
    parser.add_argument(
        "--skip-zotero",
        action="store_true",
        help="Skip the Zotero API dry-run check.",
    )
    parser.add_argument(
        "--require-postgis-installed",
        action="store_true",
        help="Fail if the postgis extension is not installed in the connected database.",
    )
    return parser.parse_args()


def trim_output(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) <= 8:
        return lines
    return lines[:8]


def verify_postgres(require_postgis_installed: bool) -> CheckResult:
    command = [sys.executable, str(ROOT / "scripts" / "postgres_verify.py"), "--require-postgis"]
    if require_postgis_installed:
        command.append("--require-postgis-installed")

    result = run_command(command)
    output = result.stdout if result.stdout.strip() else result.stderr
    lines = trim_output(output)

    if result.returncode != 0:
        return CheckResult("PostgreSQL", False, "connectivity check failed", lines)

    summary = "connected"
    if "not installed in the current database" in output:
        summary = "connected; PostGIS available but not installed in current database"
    return CheckResult("PostgreSQL", True, summary, lines)


def verify_stata() -> CheckResult:
    if STATA_LOG_PATH.exists():
        STATA_LOG_PATH.unlink()

    result = run_command([
        str(ROOT / "scripts" / "stata_exec.sh"),
        "-b",
        "do",
        str(ROOT / "scripts" / "stata_smoke.do"),
    ])

    if result.returncode != 0:
        output = result.stdout if result.stdout.strip() else result.stderr
        return CheckResult("Stata", False, "batch smoke test failed", trim_output(output))

    if not STATA_LOG_PATH.exists():
        return CheckResult("Stata", False, "batch smoke test did not produce stata_smoke.log", [])

    log_text = STATA_LOG_PATH.read_text(encoding="utf-8", errors="replace")
    required_markers = ["STATA_SMOKE: START", "STATA_ARITH: 4", "STATA_SMOKE: OK"]
    missing = [marker for marker in required_markers if marker not in log_text]
    if missing:
        return CheckResult("Stata", False, "smoke markers missing from log", missing)

    details = []
    for prefix in ["STATA_VERSION:", "STATA_FLAVOR:", "STATA_PWD:"]:
        for line in log_text.splitlines():
            if prefix in line:
                details.append(line.strip())
                break
    return CheckResult("Stata", True, "batch smoke test passed", details)


def verify_zotero() -> CheckResult:
    result = run_command([
        sys.executable,
        str(ROOT / "scripts" / "zotero_sync.py"),
        "--limit",
        "1",
        "--dry-run",
    ])
    output = result.stdout if result.stdout.strip() else result.stderr
    lines = trim_output(output)

    if result.returncode != 0:
        return CheckResult("Zotero", False, "API dry-run failed", lines)
    return CheckResult("Zotero", True, "API dry-run passed", lines)


def print_result(result: CheckResult) -> None:
    status = "OK" if result.ok else "FAIL"
    print(f"[{status}] {result.name}: {result.summary}")
    for line in result.details:
        print(f"  {line}")


def main() -> int:
    args = parse_args()
    results: list[CheckResult] = []

    if not args.skip_stata:
        results.append(verify_stata())
    if not args.skip_postgres:
        results.append(verify_postgres(args.require_postgis_installed))
    if not args.skip_zotero:
        results.append(verify_zotero())

    for result in results:
        print_result(result)

    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())