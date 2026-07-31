Previous live judged score: `5/12`

Conservative projected score range after the proposed change: `5-9/12`

Best-supported possible new score: `9/12` — **forecast, not a judge result**

# Release report

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| 1 | 1/2 | 2/2 | MEDIUM | VERIFIED | Universal affine-circuit and resource certificate; evaluator may require deeper formalization of trusted circuit lemmas |
| 2 | 1/2 | 2/2 | MEDIUM | VERIFIED | Corrected rational lift and exact depth composition; Jung 1985 remains an explicit trusted theorem |
| 3 | 1/2 | 2/2 | MEDIUM | VERIFIED | Exact FO reduction/RNN certificate and complete qualifier; L-completeness reference remains trusted |
| 4 | 1/2 | 2/2 | MEDIUM | VERIFIED | Rejected defective base-2 proof and supplied gapped base-4 existential construction; P≠NC consequence remains conditional |
| 5 | 1/2 | 1/2 | LOW | BLOCKED | Four routes complete; source router is invalid, but neither another exact four-layer DeltaNet nor an impossibility proof is available |
| 6 | 0/2 | 0/2 | LOW | BLOCKED | Four routes complete; Figure checkpoints, seeds, logs, locked environment, and one consistent protocol are absent |

Current total score: `5/12`.

Conservative projected total score range: `5-9/12`.

Best-supported possible total score: `9/12`.

Claims 1-4 changed from finite toy evidence to current parametric or exact
certificates. Claim 5 changed from a toy arithmetic trace to a four-route
`BLOCKED` result exposing a rational-router obstruction. Claim 6 changed from
unaddressed to a four-route `BLOCKED` result with exact release, checkpoint,
generator, and falsification evidence.

## Experiment tree and winning revision

The tree is a single stacked lineage:

```text
judged baseline
  -> Claim 1
  -> Claim 2
  -> Claim 3
  -> Claim 4
  -> Claim 5
  -> Claim 6 release audit
  -> Claim 6 checkpoint evaluation
  -> Claim 6 generator sensitivity
  -> Claim 6 falsification qualification
  -> release candidate
```

Winning scientific branch:
`orx/c6-exact-assumption-falsification-qualification`.

Winning scientific Git SHA:
`59c144cdb1c9fe438d857e8e70d69c2aecce32de`.

Fixed command at every node:

```bash
uv run python repro/src/verify.py
```

The terminal scientific run was
`3722216e-11a8-4b94-8c21-80922a99e902`. It used Hugging Face
`cpu-upgrade`, estimated 64 useful cores, exposed 64 logical and 64 affinity
CPUs, spent 262.848332 seconds in the verifier, and completed in 291 seconds.
Successful formal jobs through that run used 982 seconds of aggregate job wall
time. The orchestration API exposed no monetary charge, so cost is
`not available` rather than estimated.

## Low-confidence route completion

Claim 5:

1. RWKV-7 overwrite compiler and BOS schedule repair.
2. Exact 694-step-per-matrix DeltaNet arithmetic compiler.
3. Rational two-dimensional router obstruction, `phi(1404)=432>2`.
4. Dedicated falsification route; source schedule counterexample does not
   contradict every possible four-layer architecture.

Claim 6:

1. Exact audit of 190,000 released examples, code, and sole checkpoint.
2. Exact evaluation of all 90,000 validation examples.
3. One-line generator repair over 270,000 deterministic examples.
4. Dedicated five-identity falsification qualifier and full immutable release
   inventory.

Both claims remain `BLOCKED` because their fourth routes did not establish a
valid assumption-satisfying falsification.

## Release gates and evidence paths

- Exact source archive:
  `https://export.arxiv.org/e-print/2603.03612`, retrieved 2026-07-30,
  SHA-256 `f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`.
- Protected judged Space:
  `DineshAI/29sn1uqWn3@7060a61044f1907faf21d782d76e232ed7cae692`.
- Protected external manifest:
  SHA-256 `f352e226df9f3241fd0aeaf644d68ad14428ede052f12612804aad4c323c142f`.
- Claim evidence: `.openresearch/artifacts/claim_1` through `claim_6`.
- Canonical pages: `.trackio/logbook/pages/release-overview` and
  `.trackio/logbook/pages/current-claim-{1..6}`.
- Visual report: `reports/linear-rnn-reproduction/report.md`.
- Tutorial notebook: `notebooks/linear_rnn_reproduction.py`.

Publication is allowed only after the candidate manifest, old/new subset test,
secret scan, logbook validation, link traversal, current-verifier audit, and
blind red-team record all pass. The exact publication action is a text-only
commit to the existing Space `DineshAI/29sn1uqWn3`, followed by downloading the
exact returned revision and repeating the manifest and canonical traversal.
No second Space will be created.
