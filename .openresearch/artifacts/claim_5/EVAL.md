# Claim 5 evaluator entry

Run:

```bash
uv run python repro/src/verify.py
```

`proof_claims.claim_5` must report `BLOCKED` and four completed routes. A
scientifically valid evidence suite exits zero because the blocker itself is
reproduced. Any missing route, arithmetic mismatch, or altered conclusion exits
nonzero. `all_exact_claims_resolved` must remain false.
