# Claim 1 method

Each token update is lifted to an affine transformation `(A,b)`. Composition
is `(A,b) o (C,d) = (AC,bC+d)`. The verifier represents every matrix/vector
symbol as a noncommutative formal monomial and normalizes distributive sums.
This checks associativity without choosing a numerical dimension or sample.

A balanced tree composes the `n` token transformations. At each level its
width changes from `m` to `ceil(m/2)`. Induction gives exactly
`ceil(log2 n)` levels, while a binary tree with `n` leaves has `n-1` product
nodes. Each matrix product has constant arithmetic depth because the model
dimension is fixed. Fixed heads/layers preserve O(log n) depth and polynomial
size. The final positivity gate is the PNC1 predicate.

An independent implementation uses exact integer arithmetic across 256
deterministic cases and compares recurrence execution with compiled affine
execution. This numeric route is corroboration, not the universal proof.

The negative control reverses the bias action. Its two parenthesizations
normalize differently, so the checker must reject it. A pass by this control
causes the whole verifier to exit nonzero.
