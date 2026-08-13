Previous live judged score: `4/12`

Conservative projected score range after the proposed change: `9–11/12`

Best-supported possible new score: `11/12` — **forecast, not a judge result**

# Release report

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| 1 | 1/2 | 2/2 | HIGH | VERIFIED | Exact affine compiler, 132 scans, 50 convolution forms, symbolic resource induction, and destructive order control; the audited uniformity lemma remains a named dependency |
| 2 | 1/2 | 2/2 | HIGH | VERIFIED | 22 exact depths, log-star tower boundaries, rational-gate and bit-growth audits; the primary arithmetic-to-Boolean theorem remains a named dependency |
| 3 | 1/2 | 2/2 | HIGH | VERIFIED | Complete 29,367-instance graph domain, independent walk, counter, ReLU realization, FO-reduction certificate, and 636-error guard control |
| 4 | 1/2 | 2/2 | HIGH | VERIFIED | 32,767 exact stacks, 29,524 bounded language strings, 1,568 CVP assignments, and wrong-AND control |
| 5 | 0/2 | 1/2 | LOW | BLOCKED | 280 RWKV and 75 DeltaNet products are exact, but the rational four-layer DeltaNet router remains unresolved after four distinct routes |
| 6 | 0/2 | 1/2 | LOW | BLOCKED | Complete expressivity ablation and four release routes exist, but no faithful five-model Figure 2 training package exists |

Current total score: `4/12`.

Conservative projected total score range: `9–11/12`.

Best-supported possible total score: `11/12`.

Claims 1–4 changed from evaluator-visible toy checks to exact regressions and
source-anchored certificates with code, data, checkers, and controls on each
canonical page. Claim 5 adds exact RWKV/DeltaNet arithmetic while retaining its
router blocker. Claim 6 adds a complete nonlinear-versus-linearized
expressivity ablation while retaining the missing-training blocker.

## Experiment tree and winning evidence

```text
judged baseline
  → claim certificates and four-route audits
  → release-candidate cumulative regression
  → exact arithmetic and exhaustive theory audits
  → canonical evaluator-visible candidate
```

Winning scientific branch:
`audit/exact-arithmetic-theory`.

Winning scientific Git SHA:
`f9a8331fd1deadaef45c02d7399ac116562bac4e`.

Formal run:
`18bcc462-fbed-4e4b-8af2-9295100aff38`.

Hugging Face Job:
[`DineshAI/6a6c0a0cb36a6516e96a3678`](https://huggingface.co/jobs/DineshAI/6a6c0a0cb36a6516e96a3678).

Fixed command at every experiment node:

```bash
uv run python repro/src/verify.py
```

The run estimated one algorithm core, selected Hugging Face `cpu-upgrade`,
received 64 logical and 64 affinity CPUs, deliberately used one thread, and
completed the verifier in 1129.264233 seconds. No GPU was used. The
orchestration interface exposed no monetary charge, so monetary cost is
reported as unavailable rather than guessed.

## Low-confidence route completion

Claim 5 completed four materially different routes:

1. RWKV-7 overwrite compiler and BOS schedule.
2. Exact 694-step-per-matrix DeltaNet arithmetic compiler.
3. Rational two-dimensional router analysis, `φ(1404)=432>2`.
4. Dedicated falsification route; the source construction fails, but the
   broader existential theorem is not falsified.

Claim 6 completed four materially different routes:

1. Audit of the released generator, code, and 190,000 examples.
2. Exact evaluation of the sole released checkpoint on 90,000 examples.
3. Sentinel repair and 270,000-example sensitivity analysis.
4. Dedicated five-identity falsification qualifier; no available artifact
   satisfies every Figure 2 assumption.

Both claims therefore remain `BLOCKED`, not promoted to a pass.

## Evidence paths and commands

- Claim pages: `.trackio/logbook/pages/claim-1` through `claim-6`.
- Current raw evidence: `evidence/current/claim_1` through `claim_6`.
- Internal contracts and audits: `.openresearch/artifacts/claim_1` through
  `claim_6`.
- Current verifier: `repro/src/verify.py`.
- Exact/exhaustive implementation: `repro/src/judge_accepted_checks.py`.
- Visual article: `reports/linear-rnn-reproduction/report.md`.
- Tutorial notebook: `notebooks/linear_rnn_reproduction.py`.
- Complete historical command ledger:
  `reports/linear-rnn-reproduction/command_ledger.md`.
- Poster gates: `GATE_REPORT.json` (`preflight`, `style`, `measure`, and
  `polish` all pass; the asset gate is inapplicable because the poster contains
  no external raster figures).

The paper source archive was retrieved on 2026-07-30 with an explicit
User-Agent from `https://export.arxiv.org/e-print/2603.03612`; SHA-256:
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`.

## Publication action

The pre-publication candidate contains 175 files versus 128 judged files. The
old path set is a subset of the candidate, all 128 judged files are preserved,
15 superseded text paths are additionally archived byte-for-byte, the upload
allowlist contains 62 text files, and the secret scan has zero hits. The
canonical traversal and visibility matrix are complete. The official challenge
structure validator passes when given the required compliant title slug; the
actual protected Space name predates that naming rule and cannot be renamed or
duplicated under the campaign's safety constraints.

After the canonical release-child regression completes, the exact action is a
text-only commit to the existing protected Space
`DineshAI/29sn1uqWn3`. No second Space is created. The returned Hugging Face
revision is then downloaded into a fresh directory, hash-checked, and traversed
again from `pages/index.md`. Only a new live verdict can change the score.
