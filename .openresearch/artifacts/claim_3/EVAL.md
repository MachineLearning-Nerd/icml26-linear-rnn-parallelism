# Claim 3 evaluator entry

Run:

```bash
uv run python repro/src/verify.py
```

Inspect `proof_claims.claim_3`. It must report `VERIFIED`, retain the explicit
conditional assumption, pass the complete bounded-domain independent checker,
validate the integer ReLU zero mask, and reject the one-layer reduction
control. Any failed obligation exits nonzero.
