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
