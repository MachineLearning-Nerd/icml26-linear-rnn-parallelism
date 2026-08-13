# Results

Run the current CPU campaign with:

```bash
uv sync
uv run python repro/src/verify.py
```

| Claim | Current result | Primary route | Control / limitation |
| --- | --- | --- | --- |
| C1 | VERIFIED | 132 exact affine scans and 50 convolution identities | Nonassociative/false-convolution controls; universal `PNC¹` theorem remains source-anchored |
| C2 | VERIFIED | 22 depth points, log-star boundaries, corrected rational gates | Left-to-right depth and printed denominator controls |
| C3 | VERIFIED | 29,367 complete graph instances through six vertices | Guard removal yields 636 errors; complexity barrier is conditional |
| C4 | VERIFIED | 32,767 stacks, 29,524 bounded strings, 1,568 CVP assignments | Printed base-2 margin rejected; corrected base-4 route checked |
| C5 | BLOCKED | 280 RWKV and 75 DeltaNet exact products; 98 transvections | Four-route audit leaves the fixed rational DeltaNet router unresolved |
| C6 | BLOCKED | 29,367-instance expressivity ablation and four release routes | No faithful five-model Figure 2 training package |

The current run used one algorithm thread on HF `cpu-upgrade`, with 64 visible
CPUs, 1129.264233 seconds, and no GPU. These are local reproduction results,
not an external evaluator score.

The published candidate records 4/12; the archived judged-baseline lineage
records 5/12. Both are retained as historical snapshots, and no new score is
claimed here.
