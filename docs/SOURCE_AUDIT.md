# Primary-source and scope audit

Paper: **Why Are Linear RNNs More Parallelizable?** by William Merrill,
Hongjian Jiang, Yanhong Li, Anthony Lin, and Ashish Sabharwal.

- Primary source: [arXiv:2603.03612](https://arxiv.org/abs/2603.03612), version 3
- ICML submission: `29sn1uqWn3`
- Source archive SHA-256 retained by the release: `f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`
- Relevant sections: 3–6 and Appendices A–F

The paper’s theory claims are universal or conditional complexity statements;
finite executable checks validate their constructions and assumptions but do
not independently prove a complexity-class theorem.

| ID | Primary-source anchor | Evidence produced | Current status |
| --- | --- | --- | --- |
| C1 | Theorem 3, LRNN upper bound; Section 4 convolutional form | Exact affine composition, balanced products, and independent convolution checks | VERIFIED |
| C2 | Corollary 5, `O(log n log* n)` `NC` depth | Exact balanced-depth schedule, rational gate correction, and bit-growth audit | VERIFIED |
| C3 | Theorem 2, Proposition 2, and Corollary 4; Section 3.2 | Sorted deterministic connectivity enumeration, pointer reachability, counter machine, and ReLU realization | VERIFIED |
| C4 | Theorem 1 and Corollary 2; Appendix A | Exact stack operations, bounded language checks, and monotone-CVP evaluator | VERIFIED |
| C5 | Theorem 5; Section 5.1 and Appendices B.3/B.5 | RWKV/DeltaNet product arithmetic, transvection checks, and four-route router audit | BLOCKED |
| C6 | Figure 2 and Section 6; Appendix F | Released-artifact inventory, checkpoint evaluation, generator sensitivity, and falsification qualification | BLOCKED |

## Fidelity boundary

Claims 1–4 use exact rational/integer constructions and independent controls,
but their universal complexity consequences remain tied to the source proofs
and stated reductions. Claim 3’s depth consequence is conditional on the
paper’s circuit-complexity assumption. Claim 4 documents a corrected stack
encoding because the printed base-2 route has no stable classification margin.
Claim 5’s arithmetic core is exact, but a necessary fixed rational router lemma
is unresolved. Claim 6 cannot reproduce Figure 2 faithfully without the full
five-model training artifacts, checkpoints, and protocol identity.

The current evidence therefore reports blocked claims honestly rather than
substituting proxy experiments for the paper’s exact statements.
