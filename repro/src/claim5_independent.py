"""Independent architecture-level routes for Claim 5."""
from __future__ import annotations

import random
from fractions import Fraction


def matmul(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def vecmat(vector, matrix):
    return [
        sum(vector[i] * matrix[i][j] for i in range(len(vector)))
        for j in range(len(matrix[0]))
    ]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def flatten(matrix):
    return [value for row in matrix for value in row]


def rwkv_overwrite_matrix(destination, coefficients):
    size = len(coefficients)
    matrix = identity(size)
    for row in range(size):
        matrix[row][destination] = coefficients[row]
    return matrix


def rwkv_parameter_matrix(destination, coefficients):
    size = len(coefficients)
    kappa = [-value for value in coefficients]
    kappa[destination] += 1
    matrix = identity(size)
    for row in range(size):
        matrix[row][destination] -= kappa[row]
    return matrix


def overwrite(vector, destination, coefficients):
    updated = vector[:]
    updated[destination] = sum(x * c for x, c in zip(vector, coefficients))
    return updated


def rwkv_product(matrices):
    row = flatten(identity(3)) + flatten(identity(3))
    active = 0
    previous = identity(3)
    for matrix in matrices:
        for output in range(9):
            i, j = divmod(output, 3)
            destination = 9 * (1 - active) + output
            coefficients = [0] * 18
            for k in range(3):
                coefficients[9 * active + 3 * i + k] = previous[k][j]
            row = overwrite(row, destination, coefficients)
        active = 1 - active
        previous = matrix
    completed = matmul(
        [row[9 * active + 3 * i:9 * active + 3 * i + 3] for i in range(3)],
        matrices[-1],
    )
    return completed


def h_step(vector, beta, key):
    inner = sum(x * y for x, y in zip(vector, key))
    return [x - beta * inner * y for x, y in zip(vector, key)]


def basis(size, index):
    return [Fraction(int(i == index)) for i in range(size)]


def transvection(vector, source, destination):
    size = len(vector)
    source_basis = basis(size, source)
    u = source_basis[:]
    u[destination] += 1
    w = source_basis[:]
    w[destination] += 2
    vector = h_step(vector, Fraction(2), u)
    vector = h_step(vector, Fraction(1, 2), source_basis)
    vector = h_step(vector, Fraction(1, 3), w)
    return vector, 3


def deltanet_apply_matrix(vector, matrix):
    size = len(matrix)
    row = [*map(Fraction, vector), *([Fraction(0)] * size), Fraction(0)]
    steps = 0
    for index in range(size, 2 * size + 1):
        row = h_step(row, Fraction(1), basis(2 * size + 1, index))
        steps += 1
    temporary = 2 * size
    for destination in range(size):
        for source in range(size):
            row, used = transvection(row, source, temporary)
            steps += used
            row = h_step(
                row,
                1 - Fraction(matrix[source][destination]),
                basis(2 * size + 1, temporary),
            )
            steps += 1
            row, used = transvection(row, temporary, size + destination)
            steps += used
            row = h_step(row, Fraction(1), basis(2 * size + 1, temporary))
            steps += 1
    for index in range(size):
        row = h_step(row, Fraction(1), basis(2 * size + 1, index))
        steps += 1
    for index in range(size):
        row, used = transvection(row, size + index, index)
        steps += used
    return row, steps


def euler_phi(value):
    result = value
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            while remaining % divisor == 0:
                remaining //= divisor
            result -= result // divisor
        divisor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def check():
    rng = random.Random(260303612)

    overwrite_cases = 0
    for destination in range(18):
        for _ in range(8):
            coefficients = [rng.randrange(-2, 3) for _ in range(18)]
            coefficients[destination] = 0
            if rwkv_overwrite_matrix(destination, coefficients) != rwkv_parameter_matrix(
                destination, coefficients
            ):
                raise AssertionError("RWKV parameterization does not realize overwrite")
            overwrite_cases += 1

    rwkv_streams = 0
    for length in (1, 2, 3, 9, 64, 257):
        matrices = [
            [[rng.randrange(-1, 2) for _ in range(3)] for _ in range(3)]
            for _ in range(length)
        ]
        direct = identity(3)
        for matrix in matrices:
            direct = matmul(direct, matrix)
        if rwkv_product(matrices) != direct:
            raise AssertionError("BOS-repaired RWKV compiled stream failed")
        rwkv_streams += 1

    deltanet_cases = 0
    for _ in range(5):
        matrix = [[rng.randrange(-2, 3) for _ in range(9)] for _ in range(9)]
        vector = [rng.randrange(-2, 3) for _ in range(9)]
        compiled, steps = deltanet_apply_matrix(vector, matrix)
        expected = [*map(Fraction, vecmat(vector, matrix))]
        if compiled[:9] != expected or compiled[9:18] != expected or compiled[18] != 0:
            raise AssertionError("DeltaNet 694-step arithmetic program failed")
        if steps != 694:
            raise AssertionError("DeltaNet arithmetic step count changed")
        deltanet_cases += 1

    modulus = 1404
    phi = euler_phi(modulus)
    if phi <= 2:
        raise AssertionError("rational finite-order router obstruction vanished")

    # Published RWKV timing: initialize at data token 1, then only offsets 2..9
    # of the first identity block are applied. Destination coordinate 0 is zero.
    published_destination = [Fraction(0)] * 9
    for output in range(1, 9):
        published_destination[output] = Fraction(flatten(identity(3))[output])
    if published_destination[0] == 1:
        raise AssertionError("published first-token timing control unexpectedly passed")

    return {
        "passed": True,
        "route_1_rwkv": {
            "status": "verified_with_bos_repair",
            "overwrite_parameter_cases": overwrite_cases,
            "matrix_streams": rwkv_streams,
            "largest_stream_matrices": 257,
        },
        "route_2_deltanet_arithmetic": {
            "status": "verified",
            "general_9x9_cases": deltanet_cases,
            "steps_per_matrix": 694,
            "available_tokens_per_superblock": 702,
        },
        "route_3_deltanet_router": {
            "status": "invalid_source_lemma",
            "required_period": modulus,
            "euler_phi": phi,
            "reason": "a rational 2x2 matrix cannot have a primitive 1404th-root eigenvalue",
        },
        "route_4_falsification": {
            "status": "did_not_falsify_existential_claim",
            "published_n1_first_destination": str(published_destination[0]),
            "expected_identity_destination": "1",
            "conclusion": "the published schedule fails, but an explicit BOS repair remains possible",
        },
    }
