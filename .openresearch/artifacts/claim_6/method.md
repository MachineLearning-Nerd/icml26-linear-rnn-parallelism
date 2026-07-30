# Claim 6 route 1 method

The verifier downloads every released DGC split, all five training scripts, the
generator, the RNN launcher, and the sole checkpoint from the immutable author
commit. Each file is checked against its Git blob object ID and SHA-256.

Every released example is parsed independently. Pointer traversal and breadth
first search must agree, and the released label must equal reachability. A
constant endpoint signature is also evaluated: an example is positive exactly
when it contains both an edge out of the source and an edge into the target.

The source checker audits the unreachable sampling branch and incompatible RNN
launcher. The checkpoint is loaded with PyTorch's restricted `weights_only`
loader and classified from its tensor names.

Route 2 evaluates that checkpoint as the one-layer four-head `SAN-Simple`
architecture named by its tensor structure and released launcher. Because only
the final EOS output is scored and there is one attention layer, the evaluator
computes only the final query. A separate quadratic implementation of the
released source algebra must match its logits to `1e-6` before the optimized
evaluator is accepted.

Route 3 repairs only the generator's impossible sentinel condition: interior
vertices start as unassigned rather than bucket zero. It independently
regenerates the paper's 10,000-example test-bin scale for `p` in
`{0.1, 0.5, 0.9}` and three fixed seeds, verifies every label by graph
reachability, and measures the endpoint-only shortcut. Restoring the released
zero initialization is the matched control.

Route 4 is a dedicated falsification qualification audit. It retrieves the full
Git tree and history at the pinned author commit, verifies that the release has
only one DGC checkpoint and no dependency lock or DGC Mamba launcher, and
cross-checks the exact launcher arguments against the main-text and appendix
protocols. A candidate counterexample is accepted only if dataset, model,
Figure checkpoint, training protocol, and stochastic-run identity all hold.
The released checkpoint divergence, generator repair, and endpoint rule are
deliberate negative controls because each violates at least one identity.
