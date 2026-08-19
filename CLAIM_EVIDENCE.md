# Claim-to-evidence ledger

This is the current six-claim audit of *Why Are Linear RNNs More
Parallelizable?*. The current record is deliberately separate from the older
five-claim `outputs/` gate. C1–C4 pass scoped construction contracts; C5–C6
remain blocked where the exact source claim cannot be completed from the
available evidence.

| Claim | Paper anchor | How the result is produced | Control and limitation | Status |
| --- | --- | --- | --- | --- |
| C1 — LRNNs in `PNC¹` | Theorem 3; Section 4 convolutional form | `repro/src/claim1_proof.py` checks affine composition, balanced resource recurrence, and 132 exact scans; `claim1_independent.py` checks 50 convolution forms. | Reversing noncommuting transitions produces exact error. Finite identities do not prove the universal complexity-class theorem. | **VERIFIED_SCOPED** |
| C2 — near-logarithmic LRNN depth | Corollary 5; Section 4 | `claim2_proof.py` checks 22 exact depth points, log-star tower boundaries, corrected rational gates, and bit growth; the independent route checks pair arithmetic. | The left-to-right scan and the printed rational-addition denominator are rejected. The arithmetic-to-Boolean theorem remains source-anchored. | **VERIFIED_SCOPED** |
| C3 — log-precision `L`-complete connectivity | Theorem 2; Proposition 2; Corollary 4; Section 3.2 | `claim3_proof.py` and `claim3_independent.py` enumerate all 29,367 sorted deterministic graph instances through six vertices and compare pointer, counter, and ReLU routes. | Removing the nonzero-index guard creates 636 errors. The `L`-completeness and depth-barrier consequence remain conditional/source-anchored. | **VERIFIED_SCOPED** |
| C4 — polynomial-precision `P`-complete computation | Theorem 1; Corollary 2; Appendix A | `claim4_proof.py` checks the corrected exact base-4 stack route; independent checks cover 32,767 stack states, 29,524 bounded strings, and 1,568 monotone-CVP assignments. | The printed base-2 encoding’s margin is rejected; the documented base-4 repair is checked. Finite checks do not prove `P`-completeness. | **VERIFIED_SCOPED** |
| C5 — four-layer RWKV-7 and DeltaNet construction | Theorem 5; Section 5.1; Appendices B.3/B.5 | `claim5_proof.py` and `claim5_independent.py` verify 280 RWKV products, 75 DeltaNet products, and 98 transvections across four routes. | The fixed rational router requires period 1404 with `phi(1404)=432>2`; the necessary source lemma is unresolved. The broader existential claim is not falsified. | **BLOCKED** |
| C6 — Figure 2 learning comparison | Figure 2; Section 6; Appendix F | `claim6_proof.py` audits the released generator, sole checkpoint, generator repair/sensitivity, and a four-identity falsification route; the current ablation is not treated as a five-model reproduction. | No faithful five-model training package, checkpoints, logs, seeds, and protocol identity are available. The endpoint shortcut and checkpoint divergence do not by themselves falsify Figure 2. | **BLOCKED** |

## Reading the evidence

- [`evidence/current/formal_run.json`](evidence/current/formal_run.json) is the
  canonical current status record.
- `evidence/current/claim_1` through `claim_6` contain the current raw result,
  checker output, and negative control for each claim.
- `repro/src/claim*_proof.py` and `claim*_independent.py` are the production
  paths; `.openresearch/artifacts/claim_*` preserves contracts, source audits,
  limitations, and route-specific records.
- The historical five-claim `outputs/` record is retained for provenance and
  must not override the current C1–C6 statuses.

## Overall result

`PARTIAL_C1_C4_VERIFIED_SCOPED_C5_C6_BLOCKED_HISTORICAL_SCORE_4_OF_12_ARCHIVED_BASELINE_5_OF_12_NO_CURRENT_SCORE`

The current evidence is ready for review, but no score increase or author
endorsement is claimed.
