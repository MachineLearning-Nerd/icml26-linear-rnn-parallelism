# Current verification - Claim 3

**Candidate verdict: VERIFIED, including the exact conditional qualifier.**

This page supersedes the historical small-DAG scan. The current evidence is a
parametric reduction and RNN-simulation certificate; the bounded exhaustive
run is only its independent bug detector.

## Exact claim contract

There exists a fixed one-layer log-precision nonlinear MLP RNN that exactly
recognizes unary-encoded sorted deterministic graph connectivity, an L-complete
problem under FO reductions.

The associated depth statement is conditional:

> If not every language in L has polynomial-size bounded-fan-in Boolean
> circuits of depth \(o(\log^2 n)\), then some log-precision nonlinear RNN
> requires \(\Omega(\log^2 n)\) circuit depth to simulate.

The paper does not establish an unconditional circuit lower bound.

Source: arXiv 2603.03612 archive, retrieved 2026-07-30, SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`;
`3-nonlinear.tex` lines 99-184 and `appendix-rnn.tex` lines 70-117,
146-213. Primary L-completeness reference: Cook and McKenzie (1987),
DOI `10.1016/0196-6774(87)90018-6`.

## Layered FO reduction

For a functional graph on \(V\), first make the query target \(t\) a sink.
Create tuple vertices \((h,v)\) for \(0\le h\le |V|\):

```text
(h, v) -> (h + 1, f(v))
(h, t) -> F
```

The construction has \(O(|V|^2)\) size, at most one edge per source, and every
edge goes to a later lexicographic layer. A functional path reaches \(t\) iff
the layered graph reaches \(F\); a reachable target has a simple prefix of at
most \(|V|\) steps. The fixed-dimensional tuple interpretation and edge
relations are FO-definable.

## Counter and nonlinear RNN certificate

Scanning sources in topological order maintains one signed counter \(S\):
after every edge prefix, \(S\) is the unique vertex reached by following that
prefix. The unary edge routine subtracts the source label, branches on exact
zero, then either installs the target or restores the previous value.

The nonlinear MLP implements the integer zero bit exactly:

```text
zero(z) = ReLU(1 - (ReLU(z) + ReLU(-z)))
```

It is 1 exactly at integer zero and 0 at every other integer. Fixed finite
transition/update tables are piecewise-linear selectors. All counter
magnitudes are bounded by unary input length \(N\), so signed state needs at
most `ceil(log2(2N+1)) = O(log N)` bits.

The conditional lower bound is then a contrapositive: an
\(o(\log^2 n)\)-depth simulation for every such RNN would simulate this fixed
L-complete recognizer and, after FO composition, every language in L.

## Independent checker and control

The independent implementation exhausts every partial successor function,
source, and target for graph sizes 2 through 5, checking original
reachability against the sorted layered scan. It also checks determinism and
forward topological ordering. The ReLU mask is audited on every integer from
-4096 through 4096.

The negative control keeps too few copied layers. It must miss the valid
two-edge path `0 -> 1 -> 2`, while the full construction reaches the reduced
target.

## Reproduction

```bash
uv run python repro/src/verify.py
```

Environment: Python 3.12 with `uv.lock`; requested compute will be Hugging Face
`cpu-upgrade`. Current code:

- `repro/src/claim3_proof.py`
- `repro/src/claim3_independent.py`
- `.openresearch/artifacts/claim_3/claim_contract.json`
- `.openresearch/artifacts/claim_3/certificate.json`

Any dropped condition, reduction mismatch, zero-mask error, precision error,
or control pass exits nonzero.

## Raw result

Pending this cumulative branch’s terminal run. Exact output, Git SHA,
allocation, and runtime will be embedded by the next node.

## Limitations

The circuit lower bound remains conditional on an open conjecture. The
Cook-McKenzie L-completeness theorem is a trusted primary result. Exact integer
ReLU evaluation is the paper’s discrete model, not a floating-point robustness
claim.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Current Claim 2 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | This page | Yes | Pending terminal run | Pending terminal run | Yes | Yes | Yes | Pending |
| 4 | Historical only | No | No | No | No | Toy only | No | BLOCKED |
| 5 | Historical only | No | No | No | No | Toy only | No | BLOCKED |
| 6 | None | No | No | No | No | No | No | BLOCKED |
