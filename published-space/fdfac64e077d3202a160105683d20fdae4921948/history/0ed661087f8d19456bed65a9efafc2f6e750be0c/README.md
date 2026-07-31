---
title: "Repro - Why Are Linear RNNs More Parallelizable?"
emoji: 🎯
colorFrom: yellow
colorTo: red
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

# Repro - Why Are Linear RNNs More Parallelizable?

Current evidence is additive to judged revision
`7060a61044f1907faf21d782d76e232ed7cae692`. The four historical pages and
their files remain unchanged and reachable.

Start with the [release overview](pages/release-overview/page.md), then inspect
the canonical claim pages:

- [Claim 1 — VERIFIED](pages/current-claim-1/page.md)
- [Claim 2 — VERIFIED](pages/current-claim-2/page.md)
- [Claim 3 — VERIFIED](pages/current-claim-3/page.md)
- [Claim 4 — VERIFIED](pages/current-claim-4/page.md)
- [Claim 5 — BLOCKED](pages/current-claim-5/page.md)
- [Claim 6 — BLOCKED](pages/current-claim-6/page.md)

Fixed command:

```bash
uv run python repro/src/verify.py
```

Previous live judged score: **5/12**. Conservative forecast: **5–9/12**.
Best-supported possible score: **9/12**, as a forecast only. This revision has
not yet been evaluated by the live judge.

Open the [interactive logbook](index.html) for the navigation-first view.
