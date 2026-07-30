# Claim 2 evaluator entry

Run:

```bash
uv run python repro/src/verify.py
```

Inspect `proof_claims.claim_2` in `outputs/verdict.json`. A successful result
must say `VERIFIED`, report 3,025 independent exact-rational cases, show the
symbolic depth expansion, and report the printed-denominator control as
`rejected`. Any failed obligation exits nonzero.
