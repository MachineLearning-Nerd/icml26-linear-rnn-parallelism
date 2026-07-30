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

This route leaves Claim 6 `BLOCKED`; it supplies no five-model training result.
