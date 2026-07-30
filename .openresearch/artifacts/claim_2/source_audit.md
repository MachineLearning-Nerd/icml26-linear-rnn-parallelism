# Claim 2 source audit

The audited arXiv source archive was retrieved on 2026-07-30 from
`https://export.arxiv.org/e-print/2603.03612` and has SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`.

Corollary 5 in `4-linear.tex:93-102` universally quantifies over languages
recognized by LRNNs over Q and asserts an NC family of depth
`O(log n log* n)`. The nearby transformer comparison is an asymptotic
upper-bound comparison, not an exact schedule or measured latency.

The simulation source is Hermann Jung, *Depth efficient transformations of
arithmetic into boolean circuits*, FCT 1985,
DOI `10.1007/BFb0028801`. Its stated result converts integer arithmetic depth
`d(n)` to bounded Boolean depth `O(d(n) log* n)`.

Appendix A contains a typographical error:
`a/b+c/d=(ad+bc)/(bc)`. The denominator must be `bd`. The new verifier checks
the correct identity independently and rejects the printed formula on `1/2+1/3`.
This repairs the gate-level derivation; it does not contradict the corollary.
