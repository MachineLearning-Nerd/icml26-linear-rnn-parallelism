# Results

Run the complete CPU verification with:

```bash
python3 repro/src/verify.py
```

All five anchored theorem/construction claims pass. The machine-readable
evidence is in [`outputs/verdict.json`](outputs/verdict.json).

| Claim | Executable construction audit | Negative control |
|---|---|---|
| C1 | Exact LRNN recurrence equals the source convolutional matrix-product form across 288 instances | A nonlinear update cannot use the same distributive linear form |
| C2 | Balanced associative product trees and the `O(log n log* n)` schedule | A left-to-right scan has linear depth |
| C3 | Sorted deterministic graph connectivity counter scan against independent pointer reachability | An unsorted edge order defeats a one-pass scan |
| C4 | Literal scalar stack `head`/`push`/`pop` encoding used by the multi-stack proof | Fixed precision collapses distinct sufficiently deep stacks |
| C5 | Alternating-half 18-state RWKV arithmetic plus an independent WFA path-sum check | In-place coordinate writes corrupt the matrix product |

## Scope

This is a source-faithful theory reproduction. It checks the complete finite
constructions used in the authors’ proofs, not the un-released neural-training
experiment. No finite program is presented as a proof of a complexity-class
separation; those universal statements are anchored to the primary-source TeX
proofs.
