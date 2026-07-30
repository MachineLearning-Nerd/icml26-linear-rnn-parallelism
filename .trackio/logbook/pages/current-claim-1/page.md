# Current verification - Claim 1

**Verdict: VERIFIED by a parametric proof certificate.**

This page supersedes the finite Claim 1 check in the historical verification
page. The historical files remain unchanged and reachable, but they are not the
current verifier.

## Exact claim contract

For every fixed finite-depth LRNN \(M\) over exact rational arithmetic whose
fixed-width parameter maps have arithmetic closed forms independent of sequence
position, the language accepted by the sign of \(M\)'s final rational readout
has an FO-uniform, polynomial-size, bounded-fan-in arithmetic circuit family of
\(O(\log n)\) depth; equivalently, it is in PNC¹.

The quantifiers are universal over every fixed LRNN satisfying those
assumptions, every input length \(n \ge 1\), and every string of that length.
The obligation is an exact, not approximate, simulation.

Source: arXiv 2603.03612 source archive, retrieved 2026-07-30, SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`;
`2-prelim.tex` lines 45-54, 124-131, 206-237 and `4-linear.tex`
lines 19-64.

## Assumptions and source audit

- Alphabet, layer count, head count, and hidden dimensions are constants fixed
  by \(M\).
- Arithmetic is exact over Q, with polynomial-size rational representations.
- Parameter maps, queries, feed-forward maps, normalization, and readout are
  arithmetic closed forms independent of position.
- The audited closed-form-to-FO-uniform-TC⁰ lemma and standard finite circuit
  composition are explicit trusted library lemmas.
- The paper's LRNN display types the state as a matrix but its bias as a vector,
  and the convolutional display has an index typo. The certificate uses the
  dimensionally valid affine recurrence \(h_t=h_{t-1}A_t+b_t\), which is the
  recurrence used by the proof.

## Machine-checkable certificate

Each recurrent step is lifted to an affine pair:

```text
(A, b) ∘ (C, d) = (AC, bC + d)
```

The verifier normalizes both parenthesizations as noncommutative polynomials,
then checks the balanced composition recurrence:

```text
width' = ceil(width / 2)
D(1) = 0
D(n) = 1 + D(ceil(n / 2)) = ceil(log2 n)
S(n) = n - 1 product nodes
```

Because width and architecture depth are fixed by \(M\), each affine product
has constant circuit depth. The resulting family has \(O(\log n)\) depth and
polynomial size. The fixed final positivity gate is the PNC¹ predicate.

An independent implementation checks exact integer recurrence equivalence and
associativity on 256 seeded cases across dimensions 1, 2, 3, and 5. This is a
bug detector, not the universal proof. The universal evidence is the symbolic
identity and resource induction.

The negative control deliberately reverses the bias action. Its two
parenthesizations differ as formal noncommutative polynomials, so the verifier
must reject it.

## Reproduction

Fixed command for every experiment node:

```bash
uv run python repro/src/verify.py
```

Environment: Python 3.12, dependencies pinned by `uv.lock`, official CPU-only
PyTorch 2.8.0 index. Seed: `260303612`. Requested compute: Hugging Face
`cpu-upgrade`; estimated requirement: one CPU core.

Evaluator-visible current source:

- [fail-closed symbolic/resource checker](../../repro/src/claim1_proof.py)
- [independent exact-integer checker](../../repro/src/claim1_independent.py)
- [full claim contract](../../evidence/claim_1/claim_contract.json)
- [proof certificate](../../evidence/claim_1/certificate.json)

The command exits nonzero on a source-hash mismatch, missing lemma, symbolic
identity failure, resource mismatch, independent-checker mismatch, or a
negative control that unexpectedly passes.

## Raw result

Run `0010393c-cfa3-406f-b00a-62f3530b7bd8` reached `done` at Git SHA
`3a1fd68ababec3354765ad243b041e95b5873b8d`.

```json
{
  "status": "VERIFIED",
  "formal_associativity": true,
  "resource_boundary_cases": 59,
  "largest_checked_boundary": 1048577,
  "independent_checker": {
    "passed": true,
    "seed": 260303612,
    "numeric_cases": 256
  },
  "negative_control": "rejected as non-associative",
  "estimated_cores": 1,
  "selected_flavor": "cpu-upgrade",
  "logical_cpus": 64,
  "affinity_cpus": 64,
  "verifier_runtime_seconds": 0.2163839580007334,
  "job_runtime_seconds": 26
}
```

Downloadable records:

- [raw run](../../evidence/claim_1/raw_run.json)
- [checker output](../../evidence/claim_1/checker_output.json)
- [negative-control output](../../evidence/claim_1/negative_control_output.json)

## Limitations

The certificate reconstructs the LRNN-to-affine-circuit compiler and checks its
universal algebraic and resource invariants. It treats the cited
closed-form-to-FO-uniform-TC⁰ result and standard circuit closure facts as
trusted library lemmas rather than re-proving those foundations.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | This page | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Current Claim 2 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Current Claim 3 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Current Claim 4 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | Current Claim 5 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | Current Claim 6 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
