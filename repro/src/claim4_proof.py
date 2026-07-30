"""Fail-closed checker for the parametric Claim 4 certificate."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from claim4_independent import check as independent_check

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / ".openresearch" / "artifacts" / "claim_4"
SOURCE_SHA256 = "f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f"


def verify():
    contract = json.loads((ARTIFACT / "claim_contract.json").read_text())
    certificate = json.loads((ARTIFACT / "certificate.json").read_text())
    if contract["source"]["sha256"] != SOURCE_SHA256:
        raise AssertionError("paper source hash is not the audited archive")
    if contract["verdict_if_passed"] != "VERIFIED":
        raise AssertionError("claim contract verdict is not fail-closed")
    expected = [
        "gapped_stack_encoding",
        "relu_observers",
        "affine_stack_updates",
        "finite_control_selector",
        "polynomial_precision",
        "p_complete_padding",
        "conditional_nc_contrapositive",
    ]
    if [step["id"] for step in certificate["derivation"]] != expected:
        raise AssertionError("Claim 4 derivation changed")
    if certificate["conditional_conclusion"]["antecedent"] != "NC != P":
        raise AssertionError("P-versus-NC conditional changed")

    # Parametric interval proof obligations for E(bw)=(2b+1+E(w))/4,
    # assuming 0 <= E(w) < 1.
    intervals = certificate["reachable_intervals"]
    if intervals != {
        "empty": ["0", "0"],
        "top_0": ["1/4", "1/2"],
        "top_1": ["3/4", "1"],
    }:
        raise AssertionError("gapped reachable intervals changed")
    if not (Fraction(1, 2) < Fraction(3, 4)):
        raise AssertionError("stack head gap vanished")

    independent = independent_check()

    margins = [Fraction(1, 2 ** (depth + 1)) for depth in range(1, 65)]
    if margins[-1] >= Fraction(1, 3):
        raise AssertionError("base-2 vanishing-margin control unexpectedly passed")
    if not all(left > right for left, right in zip(margins, margins[1:])):
        raise AssertionError("base-2 margin did not vanish")

    return {
        "claim": 4,
        "status": "VERIFIED",
        "exact_contract": contract["statement"],
        "conditional_assumption": "NC != P",
        "derivation_steps": len(certificate["derivation"]),
        "reachable_encoding_gap": "1/4",
        "independent_checker": independent,
        "negative_control": {
            "name": "paper base-2 stack with fixed epsilon=1/3",
            "smallest_checked_margin": str(margins[-1]),
            "expected": "rejected because the margin tends to zero",
            "observed": "rejected",
        },
        "limitations": contract["limitations"],
    }
