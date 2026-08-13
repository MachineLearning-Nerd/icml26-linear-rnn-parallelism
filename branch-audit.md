# Branch audit

The historical branches used the `orx/` prefix. The clean names below are the
publication names after the repository cleanup. Branch history records
provenance and experiment purpose; it is not an additional verdict system.

| Historical branch | Clean branch | Role and canonical evidence |
| --- | --- | --- |
| `main` | `main` | Publication surface and six-claim status. |
| `orx/judged-5-12-toy-baseline` | `audit/judged-5-12-baseline` | Earlier judged toy snapshot; preserves the historical 5/12 record. |
| `orx/c1-parametric-circuit-certificate` | `audit/c1-parametric-circuit` | C1 LRNN affine/convolution and resource certificate. |
| `orx/c2-arithmetic-to-boolean-depth-certificate` | `audit/c2-arithmetic-depth` | C2 balanced arithmetic depth, `log*` schedule, and gate correction. |
| `orx/c3-l-completeness-and-conditional-barrier-certif` | `audit/c3-l-completeness-barrier` | C3 sorted connectivity, counter/ReLU construction, and conditional lower-bound audit. |
| `orx/c4-p-completeness-stack-simulation-certificate` | `audit/c4-p-completeness-stack` | C4 multi-stack simulation and corrected exact stack encoding. |
| `orx/c5-four-layer-dplr-architecture-certificate` | `audit/c5-four-layer-dplr` | C5 RWKV/DeltaNet arithmetic and four-route router audit. |
| `orx/c6-exact-assumption-falsification-qualification` | `audit/c6-assumption-falsification` | C6 route testing whether available evidence can falsify the Figure 2 claim. |
| `orx/c6-generator-repair-sensitivity-audit` | `audit/c6-generator-sensitivity` | C6 repaired-generator and sensitivity analysis. |
| `orx/c6-released-artifact-and-dataset-audit` | `audit/c6-release-dataset` | C6 released source, dataset, and checkpoint inventory. |
| `orx/c6-released-checkpoint-exact-evaluation` | `audit/c6-checkpoint-evaluation` | C6 exact evaluation of the sole released checkpoint. |
| `orx/exact-arithmetic-and-exhaustive-theory-audits` | `audit/exact-arithmetic-theory` | Current winning exact/exhaustive audit; canonical C1–C6 evidence lineage. |
| `orx/canonical-evaluator-visible-10-point-candidate` | `release/evaluator-visible-10-point` | Evaluator-facing candidate and published evidence surface. |
| `orx/release-candidate-cumulative-evidence` | `release/cumulative-evidence` | Earlier cumulative release candidate. |

## Canonical claim routing

- **C1:** `repro/src/claim1_proof.py`, `claim1_independent.py`, and
  `evidence/current/claim_1`.
- **C2:** `repro/src/claim2_proof.py`, `claim2_independent.py`, and
  `evidence/current/claim_2`.
- **C3:** `repro/src/claim3_proof.py`, `claim3_independent.py`, and
  `evidence/current/claim_3`.
- **C4:** `repro/src/claim4_proof.py`, `claim4_independent.py`, and
  `evidence/current/claim_4`.
- **C5:** `repro/src/claim5_proof.py`, `claim5_independent.py`, and
  `evidence/current/claim_5`.
- **C6:** `repro/src/claim6_proof.py`, the release/checkpoint/sensitivity
  modules, and `evidence/current/claim_6`.

The current status is C1–C4 `VERIFIED`, C5–C6 `BLOCKED`. The published
candidate’s 4/12 score and the earlier baseline’s 5/12 score are historical
provenance snapshots, not competing current verdicts.
