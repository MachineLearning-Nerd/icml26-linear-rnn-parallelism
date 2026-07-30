"""Independent exact checker for the rational-gate part of Claim 2."""
from __future__ import annotations

from fractions import Fraction


def add_pairs(left, right):
    a, b = left
    c, d = right
    return a * d + b * c, b * d


def multiply_pairs(left, right):
    a, b = left
    c, d = right
    return a * c, b * d


def check():
    cases = 0
    for a in range(-5, 6):
        for b in range(1, 6):
            for c in range(-5, 6):
                for d in range(1, 6):
                    left = (a, b)
                    right = (c, d)
                    numerator, denominator = add_pairs(left, right)
                    if Fraction(numerator, denominator) != Fraction(a, b) + Fraction(c, d):
                        raise AssertionError("independent rational-addition lift failed")
                    numerator, denominator = multiply_pairs(left, right)
                    if Fraction(numerator, denominator) != Fraction(a, b) * Fraction(c, d):
                        raise AssertionError("independent rational-multiplication lift failed")
                    cases += 1
    return {"passed": True, "exact_rational_gate_cases": cases}
