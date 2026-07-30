"""Independent numeric checker for the Claim 1 affine composition certificate."""
from __future__ import annotations

import random


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def vecmat(x, a):
    return [sum(x[i] * a[i][j] for i in range(len(x))) for j in range(len(a[0]))]


def compose(left, right):
    a_left, b_left = left
    a_right, b_right = right
    return matmul(a_left, a_right), [
        x + y for x, y in zip(vecmat(b_left, a_right), b_right)
    ]


def check(seed=260303612):
    rng = random.Random(seed)
    cases = 0
    for dimension in (1, 2, 3, 5):
        for _ in range(64):
            transforms = []
            for _ in range(7):
                matrix = [
                    [rng.randrange(-3, 4) for _ in range(dimension)]
                    for _ in range(dimension)
                ]
                bias = [rng.randrange(-3, 4) for _ in range(dimension)]
                transforms.append((matrix, bias))
            left = compose(compose(transforms[0], transforms[1]), transforms[2])
            right = compose(transforms[0], compose(transforms[1], transforms[2]))
            if left != right:
                raise AssertionError("independent affine associativity check failed")

            state = [rng.randrange(-3, 4) for _ in range(dimension)]
            recurrent = state[:]
            for matrix, bias in transforms:
                recurrent = [
                    x + y for x, y in zip(vecmat(recurrent, matrix), bias)
                ]
            combined = transforms[0]
            for transform in transforms[1:]:
                combined = compose(combined, transform)
            compiled = [
                x + y for x, y in zip(vecmat(state, combined[0]), combined[1])
            ]
            if recurrent != compiled:
                raise AssertionError("independent recurrence/compiler check failed")
            cases += 1
    return {"passed": True, "seed": seed, "numeric_cases": cases}
