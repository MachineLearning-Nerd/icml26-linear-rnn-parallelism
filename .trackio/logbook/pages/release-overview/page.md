# Release overview - exact evidence first

**Previous live judged score: 5/12. Conservative forecast: 5-9/12.
Best-supported possible score: 9/12, as a forecast—not a judge result.**

The current cumulative verifier supersedes the historical toy verifier. It
reconstructs exact proof certificates for Claims 1-4, completes four distinct
routes for each low-confidence Claim 5 and Claim 6, and exits nonzero on an
evidence failure. It does not turn unresolved claims into passes.

## Claim results

| Claim | Previous | Current evidence | Confidence | Forecast | Core reason |
| --- | ---: | --- | --- | ---: | --- |
| 1 | 1/2 | VERIFIED | MEDIUM | 2/2 | Parametric affine-circuit identity and resource induction |
| 2 | 1/2 | VERIFIED | MEDIUM | 2/2 | Corrected rational lift and compositional depth certificate |
| 3 | 1/2 | VERIFIED | MEDIUM | 2/2 | FO reduction, exact RNN counter, conditional qualifier retained |
| 4 | 1/2 | VERIFIED | MEDIUM | 2/2 | Paper defect rejected; gapped base-4 stack proves the existential |
| 5 | 1/2 | BLOCKED | LOW | 1/2 | Published rational DeltaNet router is impossible; existential unresolved |
| 6 | 0/2 | BLOCKED | LOW | 0/2 | Figure protocol/checkpoints/seeds are not reproducibly identified |

Claims 5 and 6 each received exactly three distinct verification routes plus a
fourth route dedicated to falsification. Neither yielded an
assumption-satisfying counterexample to the exact existential or empirical
claim, so both remain `BLOCKED`.

## Strongest empirical evidence

The sole released DGC checkpoint is a one-layer self-attention model, not an
RNN. Exact evaluation over all 90,000 released validation examples produced
52.52%, 50.0167%, and 50.8867%, versus the Figure 2 Transformer row of 95.60%,
68.20%, and 62.15%. This is substantial divergence but not a falsification:
the release never identifies that checkpoint as the Figure 2 checkpoint.

The released 190,000-example dataset also has a perfect endpoint-only shortcut.
After repairing only its impossible zero sentinel, the shortcut falls to
50.00-54.83% over 270,000 deterministic examples while exact reachability
labels remain 100% correct.

## Fixed reproduction contract

```bash
uv run python repro/src/verify.py
```

Python is fixed to 3.12; dependencies are pinned by `uv.lock`; PyTorch 2.8.0
uses the official CPU-only index. All formal runs use Hugging Face
`cpu-upgrade`. The final scientific run at commit
`59c144cdb1c9fe438d857e8e70d69c2aecce32de` exposed 64 logical and 64 affinity
CPUs, ran the verifier for 262.848332 seconds, and completed in 291 seconds.

## Evaluator-visible evidence

- [Pinned environment](../../uv.lock)
- [Fixed verifier](../../repro/src/verify.py)
- [Claim 1 contract and raw result](../../evidence/claim_1/raw_run.json)
- [Claim 2 contract and raw result](../../evidence/claim_2/raw_run.json)
- [Claim 3 contract and raw result](../../evidence/claim_3/raw_run.json)
- [Claim 4 contract and raw result](../../evidence/claim_4/raw_run.json)
- [Claim 5 four-route result](../../evidence/claim_5/raw_run.json)
- [Claim 6 release audit](../../evidence/claim_6/raw_route_1.json)
- [Claim 6 checkpoint evaluation](../../evidence/claim_6/raw_route_2.json)
- [Claim 6 generator repair](../../evidence/claim_6/raw_route_3.json)
- [Claim 6 falsification route](../../evidence/claim_6/raw_route_4.json)

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current Claim 1 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 2 | Current Claim 2 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 3 | Current Claim 3 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 4 | Current Claim 4 | Yes | Yes | Yes | Yes | Yes | Yes | VERIFIED |
| 5 | Current Claim 5 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |
| 6 | Current Claim 6 | Yes | Yes | Yes | Yes | Yes | Yes | BLOCKED |

The `BLOCKED` rows are complete evidence rows: the evidence directly exposes
the attempted routes, controls, limitations, and concrete missing capability.
They are not positive claim verdicts.
