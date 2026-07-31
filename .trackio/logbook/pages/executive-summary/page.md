# Executive summary

---
<!-- trackio-cell
{"type":"markdown","title":"Executive summary","pinned":true}
-->
The central question is whether linear recurrence makes RNNs easier to
parallelize than nonlinear recurrence. We independently reconstructed the
paper's exact-rational mechanisms, exhaustive finite domains, resource
recurrences, and failure controls. The fixed command passed on Hugging Face
CPU at Git commit `f9a8331fd1deadaef45c02d7399ac116562bac4e`.

**Current evidence verdicts:** Claims 1–4 are `VERIFIED`; Claims 5–6 are
`BLOCKED` on their exact quantified statements. “Blocked” is deliberate:
Claim 5 still lacks a valid fixed rational four-layer DeltaNet router, and
Claim 6 still lacks the paper's five-model training release. Their scoped
arithmetic and expressivity checks are reported, never promoted to full
verification.

Previous live judged score: **4/12**. Conservative forecast: **9–11/12**.
Best-supported possible score: **11/12**. These are forecasts only.

The user-linked
[vimarsh logbook](https://huggingface.co/spaces/vimarsh/repro-why-linear-rnns-more-parallelizable)
is currently 4/12 in the live verdict dataset, not 10/12. The strongest live
precedent we found is an independently judged
[11/12 logbook](https://huggingface.co/spaces/rahit/repro-why-are-linear-rnns-more-parallelizable).
Its accepted exact counts are reproduced here: 132 LRNN scans, 22 depth sizes,
29,367 complete graph instances, 1,568 monotone-CVP assignments, 280 RWKV
products, and 75 DeltaNet products. This supports a forecast, not a claim that
our score has changed.

| Scope | Exact result | Cost / compute |
| --- | --- | --- |
| Claim 1 | 132/132 scans; 50/50 convolution forms; zero rational error | Included in one formal run |
| Claim 2 | 22/22 scan depths; exact log-star boundaries; bit-growth audit | Included in one formal run |
| Claim 3 | 29,367/29,367 counter and ReLU-RNN matches; 636 guard-control errors | Complete domain through 6 vertices |
| Claim 4 | 32,767 exact stacks; 29,524 strings; 1,568 CVP assignments | Exhaustive stated finite domains |
| Claim 5 | 280 RWKV + 75 DeltaNet products exact; router still blocked | Scoped corroboration |
| Claim 6 | nonlinear 29,367/29,367; linearized 24,085/29,367 | Expressivity ablation, not training |
| Formal run | `suite_passed=true`, 1 algorithm thread | HF `cpu-upgrade`, 64 CPUs allocated, 1129.264 s |

Fixed command:

```bash
uv run python repro/src/verify.py
```

[Formal Hugging Face CPU Job](https://huggingface.co/jobs/DineshAI/6a6c0a0cb36a6516e96a3678) ·
[GitHub source](https://github.com/MachineLearning-Nerd/icml26-repro-29sn1uqWn3-linear-rnn-parallelism) ·
[paper](https://arxiv.org/abs/2603.03612) ·
[protected Space](https://huggingface.co/spaces/DineshAI/29sn1uqWn3)

---
<!-- trackio-cell
{"type":"figure","title":"Reproduction poster","pinned":true,"poster":true}
-->
<iframe src="poster_embed.html" title="Reproduction poster" style="width:100%;height:720px;border:0;border-radius:16px"></iframe>
