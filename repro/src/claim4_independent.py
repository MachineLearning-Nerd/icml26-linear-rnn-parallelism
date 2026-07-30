"""Independent exact checker for the gapped Claim 4 stack encoding."""
from __future__ import annotations

from fractions import Fraction
from itertools import product


def encode(bits):
    value = Fraction(0)
    for bit in reversed(bits):
        value = Fraction(2 * bit + 1 + value, 4)
    return value


def relu(value):
    return max(Fraction(0), value)


def head(value):
    return 4 * relu(value - Fraction(1, 2)) - 4 * relu(value - Fraction(3, 4))


def nonempty(value):
    return 4 * value - relu(4 * value - 1)


def pop(value):
    return 4 * value - (2 * head(value) + 1)


def push(value, bit):
    return Fraction(2 * bit + 1 + value, 4)


def check():
    stacks = 0
    for depth in range(15):
        for bits in product((0, 1), repeat=depth):
            value = encode(bits)
            if nonempty(value) != int(bool(bits)):
                raise AssertionError("independent nonempty selector failed")
            if bits:
                if head(value) != bits[0]:
                    raise AssertionError("independent stack head failed")
                if pop(value) != encode(bits[1:]):
                    raise AssertionError("independent stack pop failed")
            for bit in (0, 1):
                if push(value, bit) != encode((bit, *bits)):
                    raise AssertionError("independent stack push failed")
            stacks += 1
    return {"passed": True, "complete_stack_domain_depth": 14, "stacks": stacks}
