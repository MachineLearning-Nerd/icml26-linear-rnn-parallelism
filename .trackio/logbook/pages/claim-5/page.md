# Claim 5 — Four-layer DPLR matrix products

## Current formal regression

**Verdict: BLOCKED on the exact conjunctive architecture claim.** The scoped
arithmetic is exact: 280 RWKV products over lengths 1–21, 75 DeltaNet products
over lengths 1–8 (694 compiled H-steps per matrix), and 98 transvections pass.
A wrong coefficient produces nonzero error. But the rational 2×2 router would
need period 1,404, with `φ(1404)=432`; no valid fixed rational four-layer
replacement was established.

[Current verifier](../../repro/src/verify.py) ·
[implementation](../../repro/src/judge_accepted_checks.py) ·
[raw](../../evidence/current/claim_5/raw.json) ·
[checker](../../evidence/current/claim_5/checker_output.json) ·
[control](../../evidence/current/claim_5/negative_control_output.json)

**Verdict: BLOCKED after four distinct routes.**

The historical 18-state arithmetic trace is not the current verifier. The exact
claim requires both a four-layer RWKV-7 and a four-layer DeltaNet, for every
input length. RWKV is repairable and DeltaNet arithmetic is valid, but the
published exact rational DeltaNet router is not.

## Exact claim contract

There exist a four-layer RWKV-7 and a four-layer DeltaNet, over the paper’s
exact rational definitions, that on every stream of \(3\times3\) matrices over
`{-1,0,1}` output all nine entries of their iterated product at the final
position. Positivity of entry `(0,0)` is then PNC¹-complete under FO
reductions.

Source: arXiv 2603.03612 archive, retrieved 2026-07-30, SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`;
`5-fine-grained.tex` lines 20-71 and `appendix-dplr.tex`.
Primary completeness source: Caussinus, McKenzie, Thérien, and Vollmer (1998),
DOI `10.1006/jcss.1998.1588`.

## Route 1 — RWKV-7 architecture

For destination coordinate \(j\) and coefficients \(c_j=0\), the overwrite

```text
U = I - e_j e_j^T + c e_j^T
```

is exactly the RWKV-7 transition obtained from `w=1`, `a=e_j`,
`kappa=e_j-c`, and `lambda=1`. Nine overwrites write
`vec(PA)` into an inactive nine-coordinate buffer without interference.

The paper initializes at the first data token while also counting that token as
overwrite 1. With zero initial state those operations cannot both occur. The
global architecture definition already prepends BOS, so initializing on BOS
repairs the schedule. The independent compiler audits 144 parameterized
overwrites and matrix streams through 257 matrices.

**Route conclusion: verified with explicit BOS repair.**

## Route 2 — DeltaNet arithmetic

The checker reconstructs:

- `H(beta,k)=I-beta kk^T`;
- the three-step rational unit transvection;
- the eight-step scaled add using one temporary coordinate;
- the 694-step program applying an arbitrary \(9\times9\) matrix;
- the 702-token budget for 78 input matrices.

It checks general exact rational \(9\times9\) programs against direct products.
This route assumes the paper’s unrestricted rational `beta`; common
sigmoid-restricted DeltaNet does not contain required values such as `beta=2`
or arbitrary `1-lambda`.

**Route conclusion: arithmetic compiler verified, router not established.**

## Route 3 — DeltaNet router audit

The source claims two Householder reflections in a two-dimensional rational
state produce the position cycle used by layers 1–2. The matrix-multiplication
construction requires period 1,404.

A rational \(2\times2\) matrix cannot have a primitive 1,404th-root
eigenvalue: the cyclotomic degree is

```text
phi(1404) = 432 > 2
```

Thus the stated two-reflection cycle cannot exist over Q. The source supplies
no alternative exact four-layer rational router.

**Route conclusion: a necessary published lemma is invalid.**

## Route 4 — dedicated falsification attempt

The exact existential statement, assumptions, domain, and universal input
quantifier were restated before testing. At \(N=1\), the published zero-state
RWKV schedule leaves the first destination coordinate at 0 instead of the
identity value 1. This is an assumption-satisfying counterexample to that
schedule. However, the explicit BOS repair from Route 1 works, so it is not a
counterexample to every possible four-layer RWKV-7.

The rational-cycle obstruction invalidates the published DeltaNet proof but
does not establish that no other four-layer DeltaNet construction exists.

**Route conclusion: falsification did not succeed.**

## Reproduction

```bash
uv run python repro/src/verify.py
```

Evaluator-visible current code and records:

- [proof checker](../../repro/src/claim5_proof.py)
- [independent checker](../../repro/src/claim5_independent.py)
- [claim contract](../../evidence/claim_5/claim_contract.json)
- [four-route record](../../evidence/claim_5/routes.json)
- [raw result](../../evidence/claim_5/raw_run.json)
- [negative-control output](../../evidence/claim_5/negative_control_output.json)

The evidence suite exits nonzero on any missing route or altered arithmetic
result. A valid `BLOCKED` evidence result exits zero while
`all_exact_claims_resolved` remains false.

## Raw result

Terminal run `b147fc79-8d1f-4ddf-811b-254196e18d9e` completed at Git commit
`b3f9564a106a1b367c9e2590ec65ea16035ec3f9`:

```json
{
  "status": "BLOCKED",
  "routes_completed": 4,
  "rwkv_largest_stream_matrices": 257,
  "deltanet_steps_per_matrix": 694,
  "required_router_period": 1404,
  "euler_phi": 432,
  "all_exact_claims_resolved": false
}
```

The verifier estimated one logical core, ran on Hugging Face `cpu-upgrade`
with 64 logical and affinity CPUs available, and took 7.142337281 seconds
(26-second job duration).

## What would unblock the claim

Either an exact four-layer DeltaNet over Q with a valid unbounded-position
router, or a machine-checkable impossibility proof covering every four-layer
DeltaNet. The current evidence establishes neither.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Current Claim 2 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Current Claim 3 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Current Claim 4 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | This page | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | Current Claim 6 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
