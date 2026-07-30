# Claim 5 source audit

The exact theorem is conjunctive and universal over all matrix-stream lengths:
both a four-layer RWKV-7 and a four-layer DeltaNet must compute the exact
product. PNC1-hardness uses the fixed alphabet `{-1,0,1}` and Caussinus et al.
(1998), DOI `10.1006/jcss.1998.1588`.

The RWKV overwrite identity is correct, but the full proof initializes on the
first data token and simultaneously counts that token as overwrite 1. With
zero initial state, the multiplicative factor cannot act on the additive value
written at the same step. The global BOS convention repairs this indexing.

DeltaNet's 694-step arithmetic factorization is algebraically valid under
unrestricted rational beta. Its router is not: Lemma D.12 claims two rational
Householder reflections in 2D generate an arbitrary `2m`-state cycle. For the
IMM construction `2m=1404`. A rational 2x2 matrix cannot have a primitive
1404th-root eigenvalue because its cyclotomic degree is
`phi(1404)=432 > 2`.

No alternative exact four-layer rational DeltaNet router is supplied.
