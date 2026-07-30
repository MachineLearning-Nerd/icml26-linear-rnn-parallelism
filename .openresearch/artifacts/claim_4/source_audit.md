# Claim 4 source audit

The audited source archive has SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`.
The exact claim is existential: one fixed one-layer poly-precision nonlinear MLP
RNN recognizes a P-complete padded language. Its non-parallelizability statement
is conditional on `NC != P`.

The displayed Appendix E base-2 encoding has no fixed threshold margin. Reachable
top-0 values approach 1 from below and top-1 values approach 1 from above, so a
fixed continuous ReLU network with epsilon 1/3 cannot implement the displayed
head test for unbounded stack depth.

The certificate repairs the existential proof with the classical gapped base-4
Cantor encoding. It preserves exact rational arithmetic and requires O(T) bits
after T stack operations. This correction is explicit rather than silently
treating the base-2 toy check as proof.

Primary reference: Siegelmann and Sontag, *On the Computational Power of Neural
Nets*, 1995, DOI `10.1006/jcss.1995.1013`.
