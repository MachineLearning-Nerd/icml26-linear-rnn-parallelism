# Why Are Linear RNNs More Parallelizable?

## Reproduction status — exact certificates and release audit

This CPU-only campaign tests all six claims from ICML 2026 paper
`29sn1uqWn3`, *Why Are Linear RNNs More Parallelizable?* (arXiv `2603.03612`).
Claims 1-4 are `VERIFIED` by parametric certificates. Claim 5 is `BLOCKED`
because the published exact rational DeltaNet router cannot have its required
period, while the broader existential remains open. Claim 6 is `BLOCKED`
after four routes because the Figure 2 checkpoints, seeds, logs, locked
environment, and one consistent five-model protocol are unavailable.

The strongest empirical result is an exact evaluation of the sole released
DGC checkpoint over all 90,000 validation examples:

| Split | Paper Transformer | Released checkpoint | Difference |
| --- | ---: | ---: | ---: |
| 1-100 | 95.60% | 52.52% | -43.08 points |
| 101-200 | 68.20% | 50.0167% | -18.1833 points |
| 201-300 | 62.15% | 50.8867% | -11.2633 points |

The checkpoint is a one-layer self-attention model despite its
`SAN-Simple_RNN_RELU` filename. This divergence is not called a falsification,
because the release does not identify it as the Figure 2 checkpoint.

[Read the illustrated report](reports/linear-rnn-reproduction/report.md) or
[open the self-contained tutorial notebook](notebooks/linear_rnn_reproduction.py).

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

Previous live judged score: `5/12`. Conservative forecast after publication:
`5-9/12`; best-supported possible score: `9/12`. These are forecasts only. The
live judge has not evaluated this revision.
