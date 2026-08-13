# Why Are Linear RNNs More Parallelizable? — ICML 2026 reproduction

Independent, source-anchored reproduction of **Why Are Linear RNNs More
Parallelizable?** by William Merrill, Hongjian Jiang, Yanhong Li, Anthony Lin,
and Ashish Sabharwal.

- Paper: [arXiv:2603.03612](https://arxiv.org/abs/2603.03612)
- ICML submission: `29sn1uqWn3`
- Repository: [MachineLearning-Nerd/icml26-linear-rnn-parallelism](https://github.com/MachineLearning-Nerd/icml26-linear-rnn-parallelism)
- Published evidence snapshot: [DineshAI/29sn1uqWn3](https://huggingface.co/spaces/DineshAI/29sn1uqWn3)

## What the paper studies

The paper compares the parallelizability and expressive power of linear and
nonlinear RNNs through circuit complexity. It argues that LRNN recurrences can
be evaluated with near-logarithmic circuit depth, while nonlinear RNNs can
represent harder computations under precision assumptions. It also separates
permutation-diagonal and diagonal-plus-low-rank LRNNs and reports synthetic
length-generalization experiments.

## Current assessment

The current six-claim evidence record is:

| Claim | Result | Evidence boundary |
| --- | --- | --- |
| C1 — LRNNs in `PNC¹` | **VERIFIED** | Exact affine/convolution identities and resource certificates; the universal complexity proof remains source-anchored. |
| C2 — near-logarithmic LRNN depth | **VERIFIED** | Exact balanced products and `log*` schedule; arithmetic-to-Boolean theorem remains a named source dependency. |
| C3 — log-precision `L`-complete connectivity | **VERIFIED** | Complete sorted deterministic graph domain through six vertices, independent reachability, counter, and ReLU routes; the complexity consequence remains conditional. |
| C4 — polynomial-precision `P`-complete computation | **VERIFIED** | Corrected exact stack encoding, bounded language domain, and monotone-CVP checks; the source’s printed base-2 margin is rejected and the corrected construction is documented. |
| C5 — four-layer RWKV-7 and DeltaNet `PNC¹` construction | **BLOCKED** | RWKV and DeltaNet arithmetic is exact, but the fixed rational DeltaNet router remains unresolved after four routes. |
| C6 — Figure 2 learning comparison | **BLOCKED** | Expressivity ablation and release audits exist, but no faithful five-model training package is available. |

`evidence/current/formal_run.json` is the canonical current status. The
historical `outputs/verdict.json` and `outputs/publication_gate.json` are an
earlier five-claim publication gate and are retained as provenance; they must
not be read as overriding the six-claim current record.

The published candidate records a previous live score of **4/12**. The archived
judged-baseline lineage records **5/12** for its earlier snapshot. Both records
are preserved so the score history is auditable; this repository claims no new
live score. Only a fresh evaluator verdict can change the external result.

## Reproduce the current evidence

The fixed campaign command is:

```bash
uv sync
uv run python repro/src/verify.py
```

The verifier uses the pinned `uv.lock`, exact rational arithmetic, independent
checkers, and claim-specific negative controls. It writes the current claim
records under `outputs/` when run. The canonical evidence paths are:

- `evidence/current/claim_1` through `claim_6` — raw result, checker, and control;
- `evidence/current/formal_run.json` — run ID, commit, status, runtime, and compute;
- `repro/src/claim*_proof.py` — source-contract/proof routes;
- `repro/src/claim*_independent.py` — independent implementations;
- `reports/linear-rnn-reproduction/report.md` — illustrated explanation;
- `notebooks/linear_rnn_reproduction.py` — self-contained tutorial notebook;
- `docs/SOURCE_AUDIT.md` — paper anchors and fidelity boundary.

The winning current formal run used Hugging Face `cpu-upgrade`, one algorithm
thread, 64 visible CPUs, 1129.264233 seconds, and no GPU. This is execution
metadata, not an external score.

## Claim-to-evidence ledger

The result for each claim is produced by an explicit route and a deliberately
broken control.

| Claim | Paper anchor and statement | How the claim is produced | Control and limitation |
| --- | --- | --- | --- |
| C1 | Theorem 3 / Section 4: every rational LRNN language is in `PNC¹`. | `claim1_proof.py` checks affine-step composition, balanced resource recurrence, and 132 exact scans; `claim1_independent.py` checks 50 convolution forms. | Nonassociative order and false-linear-convolution controls fail. Finite identities validate the construction, not the universal class theorem. |
| C2 | Corollary 5: LRNNs admit `O(log n log* n)` depth `NC` simulations. | `claim2_proof.py` checks 22 exact depth points, log-star tower boundaries, corrected rational gates, and bit growth; `claim2_independent.py` checks pair arithmetic. | Left-to-right depth and the printed denominator typo are rejected. The primary arithmetic-to-Boolean theorem remains source evidence. |
| C3 | Theorem 2 / Proposition 2 / Corollary 4: a log-precision nonlinear RNN solves sorted deterministic graph connectivity, with a conditional depth barrier. | `claim3_proof.py` and `claim3_independent.py` enumerate all 29,367 instances through six vertices, compare pointer reachability, and test the counter/ReLU realization. | Removing the nonzero-index guard creates 636 errors. The `L`-completeness and lower-bound consequence remain conditional/source-anchored. |
| C4 | Theorem 1 and Corollary 2: polynomial-precision nonlinear RNNs simulate multi-stack machines and solve a `P`-complete language. | `claim4_proof.py` checks the corrected exact stack route; `claim4_independent.py` checks 32,767 stack states, 29,524 bounded strings, and 1,568 monotone-CVP assignments. | The printed base-2 encoding’s vanishing margin is rejected; the documented base-4 repair is checked. Finite checks do not prove `P`-completeness. |
| C5 | Theorem 5: four-layer RWKV-7 and DeltaNet solve iterated `3×3` matrix multiplication. | `claim5_proof.py` runs four routes; `claim5_independent.py` checks 280 RWKV products, 75 DeltaNet products, and 98 transvections. | The rational router requires period 1404 with `φ(1404)=432>2`; the source lemma is invalid, but the broader existential is not falsified. Result remains `BLOCKED`. |
| C6 | Figure 2: nonlinear RNN, Transformer, Mamba, RWKV-7, and DeltaNet are trained and compared on length-generalization tasks. | `claim6_proof.py` runs release inventory, checkpoint evaluation, generator sensitivity, and a four-identity falsification qualification. | No artifact satisfies Figure 2 model/checkpoint/protocol identity. The 29,367-instance nonlinear vs linearized ablation is not a five-model training reproduction. Result remains `BLOCKED`. |

## Branch organization

`main` is the publication surface. The historical mapping and claim routing are
documented in [`branch-audit.md`](branch-audit.md). Branch names describe the
evidence role; they are not separate scientific verdicts.

| Clean branch | Purpose |
| --- | --- |
| `audit/judged-5-12-baseline` | Preserve the earlier 5/12 judged toy snapshot. |
| `audit/c1-parametric-circuit` | C1 affine/convolution and `PNC¹` certificate. |
| `audit/c2-arithmetic-depth` | C2 balanced depth and arithmetic-to-Boolean certificate. |
| `audit/c3-l-completeness-barrier` | C3 sorted connectivity and conditional barrier. |
| `audit/c4-p-completeness-stack` | C4 stack simulation and corrected encoding. |
| `audit/c5-four-layer-dplr` | C5 RWKV/DeltaNet four-route audit. |
| `audit/c6-assumption-falsification` | C6 figure-identity falsification qualification. |
| `audit/c6-generator-sensitivity` | C6 repaired-generator sensitivity analysis. |
| `audit/c6-release-dataset` | C6 released artifact and dataset audit. |
| `audit/c6-checkpoint-evaluation` | C6 exact evaluation of the sole released checkpoint. |
| `audit/exact-arithmetic-theory` | Winning current exact/exhaustive theory audit. |
| `release/evaluator-visible-10-point` | Evaluator-facing cumulative candidate. |
| `release/cumulative-evidence` | Earlier cumulative release candidate. |

## Citation

```bibtex
@article{merrill2026linear,
  title   = {Why Are Linear RNNs More Parallelizable?},
  author  = {Merrill, William and Jiang, Hongjian and Li, Yanhong and Lin, Anthony and Sabharwal, Ashish},
  journal = {arXiv preprint arXiv:2603.03612},
  year    = {2026}
}
```

## Thank you

Thank you to William Merrill, Hongjian Jiang, Yanhong Li, Anthony Lin, and
Ashish Sabharwal for developing a precise complexity-theoretic account of
parallelism and expressivity in modern RNN architectures. This repository is
an independent reproduction and audit intended to make the paper’s evidence,
assumptions, repairs, and unresolved routes easier to inspect.

## Attribution

Repository maintenance and reproduction commits are attributed to
**MachineLearning-Nerd**. The paper, original results, and scientific ideas
belong to the cited authors.
