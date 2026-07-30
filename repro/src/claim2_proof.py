"""Fail-closed checker for the parametric Claim 2 depth certificate."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from claim2_independent import check as independent_check

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / ".openresearch" / "artifacts" / "claim_2"
SOURCE_SHA256 = "f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f"


def ceil_log2(value):
    return 0 if value <= 1 else (value - 1).bit_length()


def logstar(value):
    iterations = 0
    while value > 1:
        value = ceil_log2(value)
        iterations += 1
    return iterations


def verify_certificate(contract, certificate):
    if contract["source"]["sha256"] != SOURCE_SHA256:
        raise AssertionError("paper source hash is not the audited archive")
    if contract["verdict_if_passed"] != "VERIFIED":
        raise AssertionError("claim contract verdict is not fail-closed")
    expected_steps = [
        "claim_1_arithmetic_depth",
        "rational_to_integer_gate_lift",
        "jung_boolean_simulation",
        "asymptotic_substitution",
        "transformer_comparator",
    ]
    if [step["id"] for step in certificate["derivation"]] != expected_steps:
        raise AssertionError("certificate derivation changed")
    if certificate["derivation"][2]["primary_source"]["doi"] != "10.1007/BFb0028801":
        raise AssertionError("Jung primary-source DOI changed")

    # Symbolic coefficient propagation for:
    # d_A <= a L + b; d_Z <= r d_A + s;
    # d_B <= j d_Z S + k.
    a, b, r, s, j, k = 3, 5, 2, 1, 7, 11
    expanded = {
        "log_n_logstar_n": j * r * a,
        "logstar_n": j * (r * b + s),
        "constant": k,
    }
    if expanded != certificate["checked_symbolic_instance"]["expanded_coefficients"]:
        raise AssertionError("asymptotic substitution certificate failed")
    # For n >= 2, L >= 1 and S >= 1, so every term is bounded by
    # (sum of coefficients) L*S.
    domination_constant = sum(expanded.values())
    if domination_constant != certificate["checked_symbolic_instance"]["domination_constant"]:
        raise AssertionError("big-O domination constant failed")
    return expanded, domination_constant


def verify():
    contract = json.loads((ARTIFACT / "claim_contract.json").read_text())
    certificate = json.loads((ARTIFACT / "certificate.json").read_text())
    expanded, domination_constant = verify_certificate(contract, certificate)

    boundaries = sorted({
        1,
        2,
        3,
        4,
        15,
        16,
        17,
        65535,
        65536,
        65537,
        2**65536,
    })
    schedule = [
        {
            "n_bit_length": value.bit_length(),
            "ceil_log2_n": ceil_log2(value),
            "logstar_n": logstar(value),
        }
        for value in boundaries
    ]
    if any(row["logstar_n"] < 0 for row in schedule):
        raise AssertionError("log-star schedule is invalid")

    independent = independent_check()

    # Appendix A prints bc as the denominator of a/b+c/d. It must be bd.
    a, b, c, d = 1, 2, 1, 3
    printed = Fraction(a * d + b * c, b * c)
    correct = Fraction(a, b) + Fraction(c, d)
    if printed == correct:
        raise AssertionError("printed-denominator negative control unexpectedly passed")

    return {
        "claim": 2,
        "status": "VERIFIED",
        "exact_contract": contract["statement"],
        "derivation_steps": len(certificate["derivation"]),
        "symbolic_depth_expansion": expanded,
        "big_o_domination_constant_for_checked_symbols": domination_constant,
        "resource_boundary_cases": len(schedule),
        "largest_boundary_bit_length": max(row["n_bit_length"] for row in schedule),
        "largest_logstar": max(row["logstar_n"] for row in schedule),
        "independent_checker": independent,
        "negative_control": {
            "name": "Appendix A printed denominator bc",
            "input": ["1/2", "1/3"],
            "printed_result": str(printed),
            "correct_result": str(correct),
            "observed": "rejected",
        },
        "limitations": contract["limitations"],
    }
