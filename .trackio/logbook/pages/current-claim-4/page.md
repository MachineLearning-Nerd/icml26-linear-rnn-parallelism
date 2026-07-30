# Current verification - Claim 4

**Candidate verdict: VERIFIED by a corrected exact construction.**

The paper’s base-2 toy mechanism is not accepted as the universal proof. This
page documents its vanishing-margin defect and independently proves the exact
existential P-completeness claim with a gapped base-4 stack encoding.

## Exact claim contract

There exists a fixed one-layer polynomial-precision nonlinear MLP RNN whose
language is P-complete under FO reductions. Consequently, if `NC != P`, there
is a nonlinear RNN that cannot, for any fixed \(k\), be simulated by
polynomial-size bounded-fan-in circuits of depth \(O(\log^k n)\).

The RNN language is explicitly padded with enough clock symbols for one
recurrent transition per simulated polynomial-time machine step. The circuit
statement is conditional on `NC != P`.

Source: arXiv 2603.03612 archive, retrieved 2026-07-30, SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`;
`3-nonlinear.tex` lines 61-96 and `appendix-rnn.tex` lines 14-64.
Primary reference: Siegelmann and Sontag (1995),
DOI `10.1006/jcss.1995.1013`.

## Why the displayed base-2 proof is rejected

The appendix starts at scalar 1 and uses:

```text
push_v(s) = v + s/2
head(s) = 1[s >= 1]
```

At increasing depth, reachable top-0 states approach 1 from below and top-1
states approach 1 from above. Their separation therefore tends to zero. A
fixed continuous ReLU network using the claimed threshold tolerance
`epsilon=1/3` cannot implement this discontinuous head test exactly for
unbounded depth.

The verifier measures this shrinking margin through depth 64 and requires the
base-2 fixed-margin construction to be rejected.

## Corrected gapped stack certificate

For a binary stack \(bw\), use:

```text
E(empty) = 0
E(bw) = (2b + 1 + E(w)) / 4
```

Reachable values have fixed separated intervals:

```text
empty:  0
top 0:  [1/4, 1/2)
top 1:  [3/4, 1)
```

The fixed ReLU observers and affine updates are:

```text
head(s)     = 4 ReLU(s - 1/2) - 4 ReLU(s - 3/4)
nonempty(s) = 4s - ReLU(4s - 1)
push_b(s)   = (2b + 1 + s) / 4
pop(s)      = 4s - (2 head(s) + 1)
```

They are exact on every reachable rational encoding. For bounded
\(x\in[0,1]\) and one-hot bit \(u\), `ReLU(x+u-1)` selects \(x\) exactly, so a
fixed ReLU MLP can select among the finite state and stack updates.

After \(T\) operations, numerator and denominator are bounded by \(4^T\), hence
each stack needs \(O(T)\) bits. Polynomial padding makes \(T\) polynomial in
input length.

For a fixed P-complete \(L\) decidable in \(C n^c\) steps, the FO-definable
language `L_pad = {w #^(C|w|^c) : w in L}` is in P and P-hard. The fixed RNN
stores \(w\), then uses one padding symbol per stack-machine transition. A
polylog-depth circuit for this P-complete language would put P in NC.

## Independent checker

An independent exact-fraction implementation exhausts every binary stack from
depth 0 through 14—32,767 stacks—and verifies head, empty, push-0, push-1, and
pop. This finite sweep is a bug detector; the interval and algebraic
certificate is parametric.

## Reproduction

```bash
uv run python repro/src/verify.py
```

Environment: Python 3.12 with `uv.lock`; requested compute will be Hugging Face
`cpu-upgrade`. Current code:

- `repro/src/claim4_proof.py`
- `repro/src/claim4_independent.py`
- `.openresearch/artifacts/claim_4/claim_contract.json`
- `.openresearch/artifacts/claim_4/certificate.json`

Any lost gap, algebra error, precision mismatch, missing padding/condition, or
negative-control pass exits nonzero.

## Raw result

Pending this cumulative branch’s terminal run. Exact output, Git SHA,
allocation, and runtime will be embedded by the next node.

## Limitations

This repairs rather than validates the paper’s displayed base-2 proof. It does
not claim an unpadded RNN can perform arbitrarily many internal transitions per
input token. The circuit consequence remains conditional on `NC != P`.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Current Claim 2 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Current Claim 3 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | This page | Yes | Pending terminal run | Pending terminal run | Yes | Yes | Yes | Pending |
| 5 | Historical only | No | No | No | No | Toy only | No | BLOCKED |
| 6 | None | No | No | No | No | No | No | BLOCKED |
