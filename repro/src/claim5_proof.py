"""Fail-closed four-route audit for Claim 5."""
from __future__ import annotations

import json
from pathlib import Path

from claim5_independent import check as independent_check

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / ".openresearch" / "artifacts" / "claim_5"
SOURCE_SHA256 = "f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f"


def verify():
    contract = json.loads((ARTIFACT / "claim_contract.json").read_text())
    routes = json.loads((ARTIFACT / "routes.json").read_text())
    if contract["source"]["sha256"] != SOURCE_SHA256:
        raise AssertionError("paper source hash is not the audited archive")
    if contract["verdict_if_completed"] != "BLOCKED":
        raise AssertionError("Claim 5 verdict changed without resolving the router")
    if [route["id"] for route in routes["routes"]] != [
        "rwkv_exact_architecture",
        "deltanet_arithmetic_program",
        "deltanet_router_primary_audit",
        "falsification_attempt",
    ]:
        raise AssertionError("Claim 5 four-route sequence changed")

    independent = independent_check()
    if independent["route_1_rwkv"]["status"] != "verified_with_bos_repair":
        raise AssertionError("RWKV route did not verify")
    if independent["route_2_deltanet_arithmetic"]["steps_per_matrix"] != 694:
        raise AssertionError("DeltaNet arithmetic route did not verify")
    if independent["route_3_deltanet_router"]["status"] != "invalid_source_lemma":
        raise AssertionError("DeltaNet router obstruction was not reproduced")
    if independent["route_4_falsification"]["status"] != "did_not_falsify_existential_claim":
        raise AssertionError("Claim 5 falsification conclusion changed")

    return {
        "claim": 5,
        "status": "BLOCKED",
        "exact_contract": contract["statement"],
        "routes_completed": 4,
        "independent_checker": independent,
        "blocker": contract["blocker"],
        "unblock_requirement": contract["unblock_requirement"],
        "limitations": contract["limitations"],
    }
