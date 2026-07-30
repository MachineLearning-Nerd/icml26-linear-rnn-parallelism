# Claim 1 source audit

The audited source archive is `https://export.arxiv.org/e-print/2603.03612`,
retrieved with an explicit OpenResearch User-Agent on 2026-07-30. Its SHA-256
is `f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`.

Theorem 3 is in `4-linear.tex:19-25`: “The language recognized by any LRNN
over Q is in PNC1.” The operative domain and assumptions are supplied by
`2-prelim.tex`: exact rationals (`22-40`), arithmetic closed forms and their
FO-uniform TC0 compilation (`45-54`), the fixed-width LRNN recurrence
(`124-131`), fixed finite network composition (`206-231`), and final
positive readout (`233-237`).

The quantifier “any LRNN” ranges over a fixed model architecture. Width, layer
count, head count, alphabet, and parameter maps are fixed independently of
input length. The input length and string are universal. The proof obligation
is an FO-uniform polynomial-size O(log n)-depth arithmetic circuit family
whose sign agrees with the model for every string.

The paper's displayed convolution formula has inconsistent `i`/`t` indices
and its LRNN definition types `b_t` as a vector while describing a
matrix-valued state. The certificate therefore uses the dimensionally valid
affine recurrence `h_t = h_{t-1} A_t + b_t`, which is also the construction
implemented by the historical verifier. This deviation is explicit and does
not broaden the theorem.
