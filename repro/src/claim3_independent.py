"""Independent exhaustive checker for the Claim 3 layered reduction."""
from __future__ import annotations

import itertools


def reachable(successor, source, target):
    seen = set()
    current = source
    while current is not None and current not in seen:
        if current == target:
            return True
        seen.add(current)
        current = successor[current]
    return False


def layered_instance(successor, source, target):
    size = len(successor)
    final = (size + 1) * size
    target_sink = list(successor)
    target_sink[target] = None
    edges = []
    for layer in range(size):
        for vertex, next_vertex in enumerate(target_sink):
            start = layer * size + vertex
            if vertex == target:
                edges.append((start, final))
            elif next_vertex is not None:
                edges.append((start, (layer + 1) * size + next_vertex))
    edges.append((size * size + target, final))
    return sorted(edges), source, final


def sorted_scan(edges, source):
    current = source
    for left, right in edges:
        if current == left:
            current = right
    return current


def check():
    instances = 0
    for size in range(2, 6):
        choices = [None, *range(size)]
        for successor in itertools.product(choices, repeat=size):
            for source in range(size):
                for target in range(size):
                    edges, reduced_source, reduced_target = layered_instance(
                        successor, source, target
                    )
                    starts = [left for left, _ in edges]
                    if starts != sorted(starts) or len(starts) != len(set(starts)):
                        raise AssertionError("layered output is not sorted/deterministic")
                    if any(right <= left for left, right in edges):
                        raise AssertionError("layered output is not topologically ordered")
                    reduced = sorted_scan(edges, reduced_source) == reduced_target
                    if reduced != reachable(successor, source, target):
                        raise AssertionError("layered reduction changed reachability")
                    instances += 1
    return {"passed": True, "complete_finite_domain_instances": instances}
