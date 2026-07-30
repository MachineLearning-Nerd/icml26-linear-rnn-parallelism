# Current verification - Claim 2

**Candidate verdict: VERIFIED by a compositional depth certificate.**

This is the current Claim 2 verifier. The historical page’s sampled equality
`ceil(log2 n) * log*(n)` is not the paper’s asymptotic theorem and is labeled
as a historical rejected baseline.

## Exact claim contract

For every language recognized by an LRNN over exact rational arithmetic under
Claim 1’s assumptions, there is a polynomial-size bounded-fan-in Boolean NC
circuit family of depth \(O(\log n\log^* n)\). Relative to the standard
TC⁰-to-NC¹ transformer upper bound of \(O(\log n)\), the asymptotic
multiplicative overhead is \(O(\log^* n)\).

This is universal over qualifying LRNN languages and every input length
\(n\ge2\). It is not an exact depth equality or a hardware latency claim.

Source: arXiv 2603.03612 source archive, retrieved 2026-07-30, SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`;
`2-prelim.tex` lines 282-323, `4-linear.tex` lines 93-102, and
`appendix-arithQ.tex` lines 12-35.

Primary simulation theorem: Hermann Jung, *Depth efficient transformations of
arithmetic into boolean circuits*, FCT 1985,
DOI `10.1007/BFb0028801`.

## Certificate

The fail-closed verifier checks this derivation:

```text
Claim 1:       d_A(n) <= a log n + b
Q-to-Z lift:   d_Z(n) <= r d_A(n) + s
Jung (1985):   d_B(n) <= j d_Z(n) log* n + k
Substitution:  d_B(n) = O(log n log* n)
```

It expands a symbolic positive-coefficient instance and checks every lower
term is dominated by `log n * log* n` for `n >= 2`. It independently verifies
the rational gate lift on 3,025 exact rational input pairs and audits log-star
boundaries through an integer with 65,537 bits.

## Source correction and negative control

Appendix A prints:

```text
a/b + c/d = (ad + bc) / (bc)
```

The denominator must be `bd`. On `1/2 + 1/3`, the printed expression produces
`5/2`, while exact addition produces `5/6`. The verifier uses the corrected
identity and must reject the printed formula. The typo affects the displayed
gate derivation, not the corollary after correction.

## Reproduction

Fixed command:

```bash
uv run python repro/src/verify.py
```

Environment: Python 3.12 with `uv.lock`; requested compute will be Hugging Face
`cpu-upgrade`. Evaluator-visible current source:

- [proof checker](../../repro/src/claim2_proof.py)
- [independent checker](../../repro/src/claim2_independent.py)
- [claim contract](../../evidence/claim_2/claim_contract.json)
- [certificate](../../evidence/claim_2/certificate.json)

The command exits nonzero on a source/DOI mismatch, missing derivation step,
symbolic-depth mismatch, exact-rational mismatch, or a control that passes.

## Raw result

Run `5b01911b-996a-48c2-bca1-015477c22888` reached `done` at Git SHA
`004afa281fd4118674b89314d8b11218d0255e62`.

```json
{
  "status": "VERIFIED",
  "derivation_steps": 5,
  "independent_exact_rational_cases": 3025,
  "resource_boundary_cases": 11,
  "largest_boundary_bit_length": 65537,
  "negative_control": {
    "printed_result": "5/2",
    "correct_result": "5/6",
    "observed": "rejected"
  },
  "estimated_cores": 1,
  "selected_flavor": "cpu-upgrade",
  "logical_cpus": 64,
  "affinity_cpus": 64,
  "verifier_runtime_seconds": 0.24239702100021532,
  "job_runtime_seconds": 21
}
```

Downloadable records:

- [raw run](../../evidence/claim_2/raw_run.json)
- [checker output](../../evidence/claim_2/checker_output.json)
- [negative-control output](../../evidence/claim_2/negative_control_output.json)

## Limitations

Jung’s 1985 arithmetic-to-Boolean simulation is an explicit trusted primary
theorem; its Chinese-remainder construction is not re-formalized. Big-O hides
constants and does not imply the historical exact sampled formula.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | This page | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Current Claim 3 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Current Claim 4 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | Current Claim 5 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | Current Claim 6 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
