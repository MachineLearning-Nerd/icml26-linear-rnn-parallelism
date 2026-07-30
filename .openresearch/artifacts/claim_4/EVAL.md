# Claim 4 evaluator entry

Run:

```bash
uv run python repro/src/verify.py
```

`proof_claims.claim_4` must say `VERIFIED`, retain `NC != P`, pass every stack
through depth 14, report the fixed base-4 gap, and reject the paper's base-2
fixed-margin construction. Any failed obligation exits nonzero.
