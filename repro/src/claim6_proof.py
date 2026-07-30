"""Fail-closed empirical-evidence audit for Claim 6."""
from __future__ import annotations

import json
from pathlib import Path

from claim6_release_audit import check as release_audit
from claim6_checkpoint_eval import check as checkpoint_evaluation
from claim6_generator_sensitivity import check as generator_sensitivity
from claim6_falsification import check as falsification

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / ".openresearch" / "artifacts" / "claim_6"
SOURCE_SHA256 = "f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f"


def verify():
    contract = json.loads((ARTIFACT / "claim_contract.json").read_text())
    routes = json.loads((ARTIFACT / "routes.json").read_text())
    if contract["source"]["sha256"] != SOURCE_SHA256:
        raise AssertionError("paper source hash is not the audited archive")
    if contract["current_verdict"] != "BLOCKED":
        raise AssertionError("Claim 6 cannot be resolved by the release audit alone")
    if [route["id"] for route in routes["routes"]] != [
        "released_artifact_audit",
        "released_checkpoint_evaluation",
        "generator_repair_sensitivity",
        "falsification_attempt",
    ]:
        raise AssertionError("Claim 6 route plan changed")

    def additional_evidence(local_files):
        return {
            "checkpoint_evaluation": checkpoint_evaluation(local_files),
            "generator_sensitivity": generator_sensitivity(),
            "falsification_attempt": falsification(local_files),
        }

    released = release_audit(extra_check=additional_evidence)
    return {
        "claim": 6,
        "status": "BLOCKED",
        "exact_contract": contract["statement"],
        "routes_completed": 4,
        "release_audit": released,
        "blocker": contract["blocker_after_route_4"],
        "limitations": contract["limitations"],
    }
