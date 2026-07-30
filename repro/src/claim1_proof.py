"""Fail-closed checker for the parametric Claim 1 circuit certificate."""
from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path

from claim1_independent import check as independent_check

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / ".openresearch" / "artifacts" / "claim_1"


class Polynomial:
    """Formal sums of noncommutative monomials over Q."""

    def __init__(self, terms):
        self.terms = Counter({tuple(term): coefficient for term, coefficient in terms.items()})
        self.terms += Counter()

    @classmethod
    def symbol(cls, name):
        return cls({(name,): 1})

    def __add__(self, other):
        return Polynomial(self.terms + other.terms)

    def __mul__(self, other):
        terms = Counter()
        for left, left_coefficient in self.terms.items():
            for right, right_coefficient in other.terms.items():
                terms[left + right] += left_coefficient * right_coefficient
        return Polynomial(terms)

    def __eq__(self, other):
        return self.terms == other.terms


def compose(left, right):
    a_left, b_left = left
    a_right, b_right = right
    return a_left * a_right, b_left * a_right + b_right


def tree_metrics(count):
    depth = 0
    products = 0
    width = count
    while width > 1:
        products += width // 2
        width = (width + 1) // 2
        depth += 1
    return depth, products


def nonassociative_control(left, right):
    """Wrong order in the bias term; it must be rejected."""
    a_left, b_left = left
    a_right, b_right = right
    return a_left * a_right, b_right * a_left + b_left


def load_certificate():
    contract = json.loads((ARTIFACT / "claim_contract.json").read_text())
    certificate = json.loads((ARTIFACT / "certificate.json").read_text())
    expected_hash = contract["source"]["sha256"]
    if expected_hash != "f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f":
        raise AssertionError("paper source hash is not the audited archive")
    if contract["verdict_if_passed"] != "VERIFIED":
        raise AssertionError("claim contract verdict is not fail-closed")
    required = {
        "closed_form_parameterization",
        "affine_lift",
        "associative_composition",
        "balanced_product",
        "fixed_layer_closure",
        "positive_gap_gate",
    }
    if set(certificate["lemmas"]) != required:
        raise AssertionError("certificate lemma set changed")
    return contract, certificate


def verify():
    contract, certificate = load_certificate()
    transforms = [
        (Polynomial.symbol("A1"), Polynomial.symbol("b1")),
        (Polynomial.symbol("A2"), Polynomial.symbol("b2")),
        (Polynomial.symbol("A3"), Polynomial.symbol("b3")),
    ]
    left = compose(compose(transforms[0], transforms[1]), transforms[2])
    right = compose(transforms[0], compose(transforms[1], transforms[2]))
    if left != right:
        raise AssertionError("formal affine composition is not associative")

    boundaries = sorted({1, *[value for exponent in range(1, 21)
                              for value in (2**exponent - 1, 2**exponent, 2**exponent + 1)]})
    for count in boundaries:
        depth, products = tree_metrics(count)
        if depth != math.ceil(math.log2(count)) or products != count - 1:
            raise AssertionError(f"balanced-tree resource invariant failed at n={count}")

    broken_left = nonassociative_control(
        nonassociative_control(transforms[0], transforms[1]), transforms[2]
    )
    broken_right = nonassociative_control(
        transforms[0], nonassociative_control(transforms[1], transforms[2])
    )
    if broken_left == broken_right:
        raise AssertionError("negative control unexpectedly remained associative")

    independent = independent_check()
    result = {
        "claim": 1,
        "status": "VERIFIED",
        "exact_contract": contract["statement"],
        "formal_associativity": True,
        "resource_boundary_cases": len(boundaries),
        "largest_checked_boundary": max(boundaries),
        "inductive_resource_rule": certificate["resource_recurrence"],
        "independent_checker": independent,
        "negative_control": {
            "name": "reversed-bias affine composition",
            "expected": "rejected as non-associative",
            "observed": "rejected as non-associative",
        },
        "limitations": contract["limitations"],
    }
    return result
