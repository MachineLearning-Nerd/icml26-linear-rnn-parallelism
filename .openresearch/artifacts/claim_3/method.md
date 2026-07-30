# Claim 3 method

The proof certificate has three independently checked layers:

1. A parametric `|V|`-layer FO reduction from functional reachability to a
   sorted deterministic DAG, with an induction on path length.
2. A one-pass counter invariant and an explicit integer-exact ReLU zero mask.
   Counter magnitudes are bounded by unary input length, giving logarithmic
   precision.
3. The conditional circuit-depth contrapositive, with the open assumption
   retained verbatim.

An independent implementation exhausts every partial successor function,
source, and target for 2 through 5 vertices. Removing all but one copied layer
is a negative control that must miss the path `0 -> 1 -> 2`.
