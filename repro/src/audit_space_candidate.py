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

changed_old = sorted(
    path
    for path in judged_files
    if sha256(candidate / path) != sha256(judged / path)
)
history_root = candidate / "history" / "0ed661087f8d19456bed65a9efafc2f6e750be0c"
missing_history = [
    path
    for path in changed_old
    if not (history_root / path).is_file()
    or sha256(history_root / path) != sha256(judged / path)
]
if missing_history:
    raise AssertionError(f"superseded judged bytes are not preserved: {missing_history}")

logbook = json.loads((candidate / "logbook.json").read_text())
slugs = [child["slug"] for child in logbook["root"]["children"]]
expected = [
    "executive-summary",
    "claim-1",
    "claim-2",
    "claim-3",
    "claim-4",
    "claim-5",
    "claim-6",
    "conclusion",
]
if slugs != expected:
    raise AssertionError(f"canonical navigation mismatch: {slugs}")

canonical = [candidate / "README.md", candidate / "pages/index.md"]
canonical.extend(
    candidate / f"pages/claim-{claim}/page.md" for claim in range(1, 7)
)
canonical.extend(
    [
        candidate / "pages/executive-summary/page.md",
        candidate / "pages/conclusion/page.md",
    ]
)
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

executive = (candidate / "pages/executive-summary/page.md").read_text()
conclusion = (candidate / "pages/conclusion/page.md").read_text()
required = [
    (executive, "Previous live judged score"),
    (executive, "uv run python repro/src/verify.py"),
    (executive, "29,367"),
    (conclusion, "9–11/12"),
    (conclusion, "| 1 | [Claim 1](#/claim-1) | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |"),
    (conclusion, "| 6 | [Claim 6](#/claim-6) | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |"),
]
missing = [phrase for text, phrase in required if phrase not in text]
if missing:
    raise AssertionError(f"canonical pages are missing release facts: {missing}")

for claim in range(1, 7):
    page = (candidate / f"pages/claim-{claim}/page.md").read_text()
    for path in ("raw.json", "checker_output.json", "negative_control_output.json"):
        if f"evidence/current/claim_{claim}/{path}" not in page:
            raise AssertionError(f"Claim {claim} does not expose {path}")

allowlist = [line for line in allowlist_path.read_text().splitlines() if line.strip()]
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
secret_hits = [
    path
    for path in allowlist
    if secret_pattern.search((candidate / path).read_text())
]
if secret_hits:
    raise AssertionError(f"possible secrets in candidate: {secret_hits}")

result = {
    "passed": True,
    "judged_file_count": len(judged_files),
    "candidate_file_count": len(candidate_files),
    "old_file_set_is_subset": True,
    "protected_historical_files_preserved": len(judged_files),
    "superseded_paths_archived": len(changed_old),
    "canonical_files_opened": opened,
    "upload_file_count": len(allowlist),
    "text_only_upload": True,
    "secret_hits": 0,
    "visibility_matrix_complete": True,
}
print(json.dumps(result, indent=2, sort_keys=True))
