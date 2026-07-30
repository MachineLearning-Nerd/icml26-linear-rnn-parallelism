"""Sensitivity audit for the released DGC generator's zero-sentinel defect."""
from __future__ import annotations

import math
import random

P_VALUES = (0.1, 0.5, 0.9)
SEEDS = (0, 1, 260303612)
SPLITS = {
    "id_1_100": (2, 100),
    "ood_101_200": (101, 200),
    "ood_201_300": (201, 300),
}
EXAMPLES_PER_SPLIT = 10_000


def build_edges(bucket):
    edges = []
    for bucket_id in (0, 1):
        nodes = [index for index, value in enumerate(bucket) if value == bucket_id]
        edges.extend(zip(nodes, nodes[1:]))
    return sorted(edges)


def generate(rng, node_count, probability, label, released_bug=False):
    empty = 0 if released_bug else None
    bucket = [empty] * (node_count + 1)
    source_bucket = rng.randint(0, 1)
    if label:
        bucket[0] = source_bucket
        bucket[node_count] = source_bucket
        bucket[rng.randint(1, node_count - 1)] = source_bucket
    else:
        bucket[0] = source_bucket
        bucket[node_count] = 1 - source_bucket
    for index in range(1, node_count):
        if bucket[index] not in (0, 1):
            bucket[index] = 0 if rng.random() < probability else 1
    return build_edges(bucket)


def reachable(edges, target):
    successor = dict(edges)
    current = 0
    seen = set()
    while current in successor and current not in seen:
        seen.add(current)
        current = successor[current]
    return current == target


def endpoint_signature(edges, target):
    return any(left == 0 for left, _ in edges) and any(
        right == target for _, right in edges
    )


def wilson(correct, total, z=1.959963984540054):
    p = correct / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    radius = (
        z
        * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total))
        / denominator
    )
    return [center - radius, center + radius]


def audit_configuration(probability, seed, released_bug=False):
    rng = random.Random(seed)
    rows = {}
    for split_name, (low, high) in SPLITS.items():
        correct_reachability = 0
        correct_endpoint = 0
        for index in range(EXAMPLES_PER_SPLIT):
            label = index % 2
            node_count = rng.randint(low, high)
            edges = generate(
                rng,
                node_count,
                probability,
                label,
                released_bug=released_bug,
            )
            correct_reachability += int(reachable(edges, node_count) == bool(label))
            correct_endpoint += int(
                endpoint_signature(edges, node_count) == bool(label)
            )
        if correct_reachability != EXAMPLES_PER_SPLIT:
            raise AssertionError("repaired generator does not preserve labels")
        rows[split_name] = {
            "examples": EXAMPLES_PER_SPLIT,
            "reachability_accuracy": 1.0,
            "endpoint_signature_accuracy": correct_endpoint / EXAMPLES_PER_SPLIT,
            "endpoint_signature_wilson_95": wilson(
                correct_endpoint,
                EXAMPLES_PER_SPLIT,
            ),
        }
    return rows


def check():
    repaired = []
    for probability in P_VALUES:
        for seed in SEEDS:
            repaired.append(
                {
                    "p": probability,
                    "seed": seed,
                    "splits": audit_configuration(probability, seed),
                }
            )

    released_control = audit_configuration(0.5, 0, released_bug=True)
    if any(
        row["endpoint_signature_accuracy"] != 1.0
        for row in released_control.values()
    ):
        raise AssertionError("released zero-initialization control did not restore shortcut")

    endpoint_values = [
        row["endpoint_signature_accuracy"]
        for configuration in repaired
        for row in configuration["splits"].values()
    ]
    if max(endpoint_values) >= 0.55:
        raise AssertionError("endpoint shortcut survived corrected generator")

    # Assumption-breaking negative control: label a graph positive while forcing
    # source and target into different buckets. The reachability checker rejects it.
    rng = random.Random(7)
    corrupted_edges = generate(rng, 100, 0.5, label=0)
    if reachable(corrupted_edges, 100):
        raise AssertionError("corrupted positive-label control unexpectedly reachable")

    return {
        "passed": True,
        "examples_per_split_per_configuration": EXAMPLES_PER_SPLIT,
        "p_values": list(P_VALUES),
        "seeds": list(SEEDS),
        "configurations": repaired,
        "endpoint_accuracy_range": [min(endpoint_values), max(endpoint_values)],
        "released_bug_control": released_control,
        "negative_control": {
            "name": "positive label with source and target forced apart",
            "expected": "reachability checker rejects",
            "observed": "rejected",
        },
    }
