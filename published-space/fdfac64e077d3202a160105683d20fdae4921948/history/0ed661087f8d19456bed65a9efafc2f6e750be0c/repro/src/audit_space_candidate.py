#!/usr/bin/env python3
"""Fail-closed evaluator-visible audit for a staged Space candidate."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit("usage: audit_space_candidate.py CANDIDATE JUDGED ALLOWLIST")

candidate = Path(sys.argv[1]).resolve()
judged = Path(sys.argv[2]).resolve()
allowlist_path = Path(sys.argv[3]).resolve()


def files(root):
    return {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and ".cache" not in path.parts
    }


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


candidate_files = files(candidate)
judged_files = files(judged)
missing_old = sorted(judged_files - candidate_files)
if missing_old:
    raise AssertionError(f"judged files missing from candidate: {missing_old}")

protected = {
    "pages/overview/page.md",
    "pages/claims/page.md",
    "pages/evidence/page.md",
    "pages/verification-run/page.md",
    "index.html",
    "logbook.css",
    "logbook.js",
    "bucket-icon.svg",
    "trackio-logo-light.png",
    "trackio-logo.png",
    "trackio-wordmark-dark.png",
}
changed_protected = sorted(
    path for path in protected if sha256(candidate / path) != sha256(judged / path)
)
if changed_protected:
    raise AssertionError(f"protected historical files changed: {changed_protected}")

logbook = json.loads((candidate / "logbook.json").read_text())
children = logbook["root"]["children"]
slugs = [child["slug"] for child in children]
expected_current = [
    "release-overview",
    "current-claim-6",
    "current-claim-5",
    "current-claim-4",
    "current-claim-3",
    "current-claim-2",
    "current-claim-1",
]
if slugs[:7] != expected_current:
    raise AssertionError("current evidence is not first in navigation")
if any(
    not child["title"].startswith("Historical rejected baseline")
    for child in children[7:]
):
    raise AssertionError("historical pages are not labeled as rejected baselines")

canonical = [candidate / "README.md", candidate / "pages/index.md"]
canonical.extend(
    candidate / f"pages/current-claim-{claim}/page.md"
    for claim in range(1, 7)
)
canonical.append(candidate / "pages/release-overview/page.md")
link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
broken_links = []
opened = []
for page in canonical:
    opened.append(page.relative_to(candidate).as_posix())
    for target in link_pattern.findall(page.read_text()):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (page.parent / target).resolve()
        if candidate not in resolved.parents and resolved != candidate:
            broken_links.append((page.name, target, "escapes candidate"))
        elif not resolved.is_file():
            broken_links.append((page.name, target, "missing"))
if broken_links:
    raise AssertionError(f"broken evaluator-visible links: {broken_links}")

overview = (candidate / "pages/release-overview/page.md").read_text()
required_overview_phrases = [
    "Previous live judged score: 5/12",
    "Conservative forecast: 5-9/12",
    "Best-supported possible score: 9/12",
    "| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |",
    "| 6 | Current Claim 6 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |",
    "uv run python repro/src/verify.py",
]
missing_phrases = [
    phrase for phrase in required_overview_phrases if phrase not in overview
]
if missing_phrases:
    raise AssertionError(f"overview is missing release facts: {missing_phrases}")

allowlist = [
    line for line in allowlist_path.read_text().splitlines() if line.strip()
]
if allowlist != sorted(allowlist):
    raise AssertionError("upload allowlist is not sorted")
if any(path not in candidate_files for path in allowlist):
    raise AssertionError("upload allowlist names a missing candidate file")
for path in allowlist:
    try:
        (candidate / path).read_text()
    except UnicodeDecodeError as error:
        raise AssertionError(f"upload allowlist is not text-only: {path}") from error

secret_pattern = re.compile(
    r"(hf_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)
secret_hits = []
for path in allowlist:
    if secret_pattern.search((candidate / path).read_text()):
        secret_hits.append(path)
if secret_hits:
    raise AssertionError(f"possible secrets in candidate: {secret_hits}")

result = {
    "passed": True,
    "judged_file_count": len(judged_files),
    "candidate_file_count": len(candidate_files),
    "old_file_set_is_subset": True,
    "protected_historical_files_unchanged": len(protected),
    "canonical_files_opened": opened,
    "upload_file_count": len(allowlist),
    "text_only_upload": True,
    "secret_hits": 0,
    "visibility_matrix_complete": True,
}
print(json.dumps(result, indent=2, sort_keys=True))
