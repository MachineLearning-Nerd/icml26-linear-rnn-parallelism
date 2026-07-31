---
title: "Reproduction: Why Are Linear RNNs More Parallelizable?"
emoji: 🔬
colorFrom: blue
colorTo: yellow
sdk: static
pinned: false
tags:
 - trackio
 - trackio-logbook
 - open-experiment
 - icml2026-repro
 - paper-29sn1uqWn3
 - theory
 - rnn
---

# Reproduction: Why Are Linear RNNs More Parallelizable?

Start with the [canonical index](pages/index.md) or open the
[interactive logbook](index.html). The current claim pages expose the exact
statement, source quantifiers, executable verifier, fixed command, raw JSON,
checker, negative control, limitations, commit, and CPU runtime.

- [Executive summary](pages/executive-summary/page.md)
- [Claim 1 — VERIFIED](pages/claim-1/page.md)
- [Claim 2 — VERIFIED](pages/claim-2/page.md)
- [Claim 3 — VERIFIED](pages/claim-3/page.md)
- [Claim 4 — VERIFIED](pages/claim-4/page.md)
- [Claim 5 — BLOCKED](pages/claim-5/page.md)
- [Claim 6 — BLOCKED](pages/claim-6/page.md)
- [Conclusion and visibility matrix](pages/conclusion/page.md)

The current verifier supersedes the
[Historical rejected baseline](pages/verification-run/page.md). Every file
from judged revision `0ed661087f8d19456bed65a9efafc2f6e750be0c` remains
preserved.

Fixed command:

```bash
uv run python repro/src/verify.py
```

Previous live judged score: **4/12**. Conservative forecast:
**9–11/12**. Best-supported possible score: **11/12**, as a forecast only.
Only a new live verdict can change the score.
