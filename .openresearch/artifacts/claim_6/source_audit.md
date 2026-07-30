# Claim 6 source audit

Paper archive: `https://export.arxiv.org/e-print/2603.03612`, retrieved
2026-07-30, SHA-256
`f1078eb9464172f9a941c1dd95354116ae749d64b91ec29947b47a588d2a1f9f`.

The paper links the author repository at
`https://arg-git.informatik.uni-kl.de/pub/LinearRNN`. The audited head is
`e6d2832c0be35b93630a094124ae8dbabcbfb18d`.

The source and release conflict:

- the main text says batch 64, learning rate `1e-4`, two layers, and eight
  Transformer heads;
- the appendix says batch 128, learning rate `3e-4`, two layers, and four
  Transformer heads;
- released launchers use other per-model settings, generally one layer and
  30,000 rather than 60,000 steps;
- no Figure 2 seeds, uncertainty intervals, logs, environment, or five matching
  checkpoints are released.

The released generator initializes every bucket entry to zero and only samples
when an entry is neither zero nor one. Consequently, the documented Bernoulli
`p` is unreachable.
