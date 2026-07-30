# Claim 2 method

The verifier checks a five-step derivation:

1. Import the Claim 1 `O(log n)` arithmetic-depth certificate.
2. Lift each rational gate to a constant-depth integer numerator/denominator
   circuit using exact identities.
3. Apply Jung's primary arithmetic-to-Boolean simulation theorem.
4. Symbolically substitute the depth bounds and prove domination by
   `log n log* n` for `n >= 2`.
5. State the transformer comparison only as `TC0 subset NC1`.

An independent implementation exhaustively checks 3,025 pairs of small exact
rationals. Boundary cases exercise the integer log-star schedule, including an
input with 65,537 bits. The printed denominator typo is the negative control.
