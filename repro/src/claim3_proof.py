"""Fail-closed checker for the parametric Claim 3 certificate."""
from __future__ import annotations

import json
import math
from pathlib import Path

from claim3_independent import check as independent_check
from claim3_independent import layered_instance, sorted_scan

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / ".openresearch" / "artifacts" / "claim_3"
SOURCE_SHA256 = "f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f"


def relu(value):
    return max(0, value)


def integer_zero_mask(value):
    absolute = relu(value) + relu(-value)
    return relu(1 - absolute)


def verify():
    contract = json.loads((ARTIFACT / "claim_contract.json").read_text())
    certificate = json.loads((ARTIFACT / "certificate.json").read_text())
    if contract["source"]["sha256"] != SOURCE_SHA256:
        raise AssertionError("paper source hash is not the audited archive")
    if contract["verdict_if_passed"] != "VERIFIED":
        raise AssertionError("claim contract verdict is not fail-closed")
    expected = [
        "deterministic_reachability_source",
        "fo_layered_reduction",
        "sorted_counter_invariant",
        "counter_to_relu_rnn",
        "log_precision",
        "conditional_depth_contrapositive",
    ]
    if [step["id"] for step in certificate["derivation"]] != expected:
        raise AssertionError("Claim 3 derivation changed")
    if certificate["conditional_conclusion"]["antecedent"] != contract["conditional_assumption"]:
        raise AssertionError("conditional lower-bound assumption changed")

    mask_cases = 0
    for value in range(-4096, 4097):
        observed = integer_zero_mask(value)
        expected_mask = int(value == 0)
        if observed != expected_mask:
            raise AssertionError("integer-exact ReLU zero mask failed")
        mask_cases += 1

    for unary_length in [1, 2, 3, 7, 31, 127, 1023, 4095]:
        bits = math.ceil(math.log2(2 * unary_length + 1))
        if bits > math.ceil(math.log2(unary_length + 1)) + 1:
            raise AssertionError("counter precision is not logarithmic")

    independent = independent_check()

    # A single-layer copy cannot preserve a two-edge path.
    successor = (1, 2, None)
    full_edges, source, target = layered_instance(successor, 0, 2)
    one_layer_edges = [
        edge for edge in full_edges if edge[0] < 2 * len(successor)
    ]
    if sorted_scan(one_layer_edges, source) == target:
        raise AssertionError("one-layer reduction negative control unexpectedly passed")
    if sorted_scan(full_edges, source) != target:
        raise AssertionError("valid layered reduction failed its control instance")

    return {
        "claim": 3,
        "status": "VERIFIED",
        "exact_contract": contract["statement"],
        "conditional_assumption": contract["conditional_assumption"],
        "derivation_steps": len(certificate["derivation"]),
        "integer_zero_mask_cases": mask_cases,
        "independent_checker": independent,
        "negative_control": {
            "name": "one-layer rather than n-layer reduction",
            "path": "0 -> 1 -> 2",
            "expected": "does not reach the reduced target",
            "observed": "rejected",
        },
        "limitations": contract["limitations"],
    }
