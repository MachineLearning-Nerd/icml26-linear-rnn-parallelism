# Claim 6 route 1 evaluation

Run:

```bash
uv run python repro/src/verify.py
```

Pass requires immutable artifact hashes, correct labels under two independent
reachability algorithms, exact endpoint-signature statistics, reproduction of
the generator and launcher defects, and architecture identification of the
released checkpoint. Flipping one real label per split is the negative control
and must be rejected.

Route 2 additionally requires exact agreement between quadratic and
last-query-only self-attention evaluation, evaluates all 90,000 released
validation examples, and negates the decoder as a parameter-level control.

These routes leave Claim 6 `BLOCKED`; they supply no faithful five-model
training result.
