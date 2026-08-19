#!/usr/bin/env python3
"""Check the current six-claim audit and repository identity surfaces."""

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_STATUS = (
    "PARTIAL_C1_C4_VERIFIED_SCOPED_C5_C6_BLOCKED_HISTORICAL_SCORE_4_OF_12_ARCHIVED_BASELINE_5_OF_12_NO_CURRENT_SCORE"
)
EXPECTED_BRANCHES = 14
EXPECTED_COMMITS = 37
CANONICAL_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text())


def branch_names() -> set[str]:
    refs = git(
        "for-each-ref",
        "--format=%(refname)",
        "refs/heads",
        "refs/remotes/origin",
    ).splitlines()
    names = set()
    for ref in refs:
        if ref.endswith("/HEAD"):
            continue
        names.add(ref.removeprefix("refs/heads/").removeprefix("refs/remotes/origin/"))
    return names


def main() -> None:
    manifest = load("EVIDENCE_MANIFEST.json")
    missing = [path for path in manifest["required_evidence"] if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"missing evidence: {', '.join(missing)}")

    verdicts = load("reproduction_verdicts.json")
    if verdicts["overall_status"] != EXPECTED_STATUS:
        raise SystemExit("overall status is inconsistent")
    expected_claims = {
        "C1": "VERIFIED_SCOPED",
        "C2": "VERIFIED_SCOPED",
        "C3": "VERIFIED_SCOPED",
        "C4": "VERIFIED_SCOPED",
        "C5": "BLOCKED",
        "C6": "BLOCKED",
    }
    if verdicts["claims"] != expected_claims:
        raise SystemExit(f"claim statuses are inconsistent: {verdicts['claims']}")
    run = load("evidence/current/formal_run.json")
    if run["statuses"] != {
        "claim_1": "VERIFIED",
        "claim_2": "VERIFIED",
        "claim_3": "VERIFIED",
        "claim_4": "VERIFIED",
        "claim_5": "BLOCKED",
        "claim_6": "BLOCKED",
    }:
        raise SystemExit("current formal run statuses are inconsistent")
    if run["suite_passed"] is not True or run["compute"]["gpu_used"] is not False:
        raise SystemExit("current formal run gate is inconsistent")
    if verdicts["historical_scores"]["published_candidate"]["points"] != 4:
        raise SystemExit("published historical score is inconsistent")
    if verdicts["historical_scores"]["archived_judged_baseline"]["points"] != 5:
        raise SystemExit("archived historical score is inconsistent")
    if verdicts["publication_gate"]["current_review_ready"] is not True:
        raise SystemExit("current review gate is not recorded as ready")
    if verdicts["publication_gate"]["publication_allowed"] is not False:
        raise SystemExit("publication boundary is inconsistent")

    names = branch_names()
    if len(names) != EXPECTED_BRANCHES or "main" not in names or any(name.startswith("orx/") for name in names):
        raise SystemExit(f"unexpected branches: {sorted(names)}")
    commits = int(git("rev-list", "--all", "--count"))
    if commits != EXPECTED_COMMITS:
        raise SystemExit(f"expected {EXPECTED_COMMITS} reachable commits, found {commits}")

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    expected = f"{CANONICAL_IDENTITY} | {CANONICAL_IDENTITY}"
    if identities != {expected}:
        raise SystemExit(f"non-canonical commit identities: {sorted(identities)}")

    print(
        "FINAL_AUDIT=VERIFIED"
        f" branches={len(names)}"
        f" commits={commits}"
        " claims=C1:C4_verified_scoped,C5:C6_blocked"
        " historical_scores=4/12,5/12"
        " current_score_claim=false"
        " publication_allowed=false"
    )


if __name__ == "__main__":
    main()
