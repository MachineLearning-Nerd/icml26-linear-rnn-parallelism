# Why Are Linear RNNs More Parallelizable?

## Reproduction status — exact arithmetic, exhaustive domains, visible evidence

This CPU-only campaign tests all six claims from ICML 2026 paper
`29sn1uqWn3`, *Why Are Linear RNNs More Parallelizable?* (arXiv `2603.03612`).
Claims 1–4 are `VERIFIED` by exact arithmetic, complete bounded domains, and
source-anchored certificates. Claim 5 is `BLOCKED` because the published exact
rational DeltaNet router cannot have its required period, while the broader
existential remains open. Claim 6 is `BLOCKED` because no faithful five-model
Figure 2 training release exists.

The strongest current result is the complete sorted deterministic graph domain
through six vertices:

| Evidence | Observed result | Assessment |
| --- | ---: | --- |
| Sorted-DGC counter and ReLU RNN | 29,367 / 29,367 | Exact complete domain through 6 vertices |
| Guard-removed control | 636 errors / 3,000 | Fails for the intended reason |
| LRNN scans / convolution forms | 132 / 132; 50 / 50 | Zero rational error |
| Monotone-CVP assignments | 1,568 / 1,568 | Exact bounded-domain check |
| RWKV / DeltaNet products | 280 / 280; 75 / 75 | Scoped evidence; Claim 5 remains BLOCKED |
| Nonlinear / linearized graph solver | 100%; 82.0138% | Expressivity ablation; not Figure 2 training |

The formal cumulative run passed on Hugging Face `cpu-upgrade` with one
algorithm thread in 1129.264 seconds. No GPU was used. The public logbook puts
the exact claim, code, raw JSON, independent checker, and negative control on
each canonical claim page.

[Read the illustrated report](reports/linear-rnn-reproduction/report.md) or
[open the self-contained tutorial notebook](notebooks/linear_rnn_reproduction.py).
The evaluator-facing artifact is published at
[Hugging Face revision `fdfac64e`](https://huggingface.co/spaces/DineshAI/29sn1uqWn3/tree/fdfac64e077d3202a160105683d20fdae4921948);
the [exact 62-file text snapshot](published-space/fdfac64e077d3202a160105683d20fdae4921948/README.md)
and its SHA-256 manifests are mirrored in this repository.

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/blob/main/notebooks/linear_rnn_reproduction.py)

Formal experiments used Hugging Face `cpu-upgrade` only. The fixed command was:

```bash
uv run python repro/src/verify.py
```

### Experiment log

`main` is the publication surface and was not run as an experiment. Every
formal node inherited the exact command shown below.

| Branch / experiment | Purpose | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| [`orx/judged-5-12-toy-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/judged-5-12-toy-baseline) | Freeze judged baseline and uv lock | `uv run python repro/src/verify.py` | Baseline reproduced | HF cpu-upgrade, 21s |
| [`orx/c1-parametric-circuit-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c1-parametric-circuit-certificate) | Claim 1 universal certificate | `uv run python repro/src/verify.py` | VERIFIED | HF cpu-upgrade, 26s |
| [`orx/c2-arithmetic-to-boolean-depth-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c2-arithmetic-to-boolean-depth-certificate) | Claim 2 depth conversion | `uv run python repro/src/verify.py` | VERIFIED | HF cpu-upgrade, 21s |
| [`orx/c3-l-completeness-and-conditional-barrier-certif`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c3-l-completeness-and-conditional-barrier-certif) | Claim 3 reduction and RNN | `uv run python repro/src/verify.py` | VERIFIED, conditional qualifier retained | HF cpu-upgrade, 21s |
| [`orx/c4-p-completeness-stack-simulation-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c4-p-completeness-stack-simulation-certificate) | Claim 4 corrected stack | `uv run python repro/src/verify.py` | VERIFIED after rejecting paper’s base-2 proof | HF cpu-upgrade, 26s |
| [`orx/c5-four-layer-dplr-architecture-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c5-four-layer-dplr-architecture-certificate) | Four Claim 5 routes | `uv run python repro/src/verify.py` | BLOCKED; exact router lemma invalid | HF cpu-upgrade, 26s |
| [`orx/c6-released-artifact-and-dataset-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c6-released-artifact-and-dataset-audit) | Audit 190k released examples | `uv run python repro/src/verify.py` | Exact endpoint shortcut found | HF cpu-upgrade, 63s |
| [`orx/c6-released-checkpoint-exact-evaluation`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c6-released-checkpoint-exact-evaluation) | Evaluate 90k examples | `uv run python repro/src/verify.py` | 11.26-43.08 point Figure gaps | HF cpu-upgrade, 238s |
| [`orx/c6-generator-repair-sensitivity-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c6-generator-repair-sensitivity-audit) | 270k repaired examples | `uv run python repro/src/verify.py` | Shortcut collapses to 50.00-54.83% | HF cpu-upgrade, 249s |
| [`orx/c6-exact-assumption-falsification-qualification`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/c6-exact-assumption-falsification-qualification) | Mandatory falsification route | `uv run python repro/src/verify.py` | No qualified counterexample; BLOCKED | HF cpu-upgrade, 291s |
| [`orx/exact-arithmetic-and-exhaustive-theory-audits`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/exact-arithmetic-and-exhaustive-theory-audits) | Match the strongest live judged exact checks and rerun every prior audit | `uv run python repro/src/verify.py` | C1–4 VERIFIED; C5–6 BLOCKED | HF cpu-upgrade, 1129.264s verifier |
| [`orx/canonical-evaluator-visible-10-point-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism/tree/orx/canonical-evaluator-visible-10-point-candidate) | Final cumulative regression of the published candidate | `uv run python repro/src/verify.py` | Suite passed at `467a72b`; C1–4 VERIFIED, C5–6 BLOCKED | HF cpu-upgrade, 599.512s verifier |

Previous live judged score: `4/12`. Conservative forecast after publication:
`9-11/12`; best-supported possible score: `11/12`. These are forecasts only. The
live judge has not evaluated this revision.
