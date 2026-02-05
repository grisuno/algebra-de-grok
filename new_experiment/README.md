---
title: "Thermodynamic Grokking in Binary Parity: A First Look at 100 Seeds"
author: grisun0
date: February 2026
---

## What I Did

I trained 100 neural networks on binary parity prediction (k=3 bits) using a curriculum learning protocol. The architecture is a simple two-layer MLP: input dimension scales from 10 to 64 bits across four curriculum stages, hidden dimensions from 128 to 1024. I used AdamW with weight decay, tracked gradient covariance (κ), discretization margin (δ), effective temperature (T_eff), local complexity (LC), and superposition coefficient (ψ) throughout training.

The training stops when test accuracy hits 98%—what I call "grokking"—or when stagnation is detected. I then analyze the final checkpoints with a crystallography protocol that tests stability under pruning and measures how close weights are to discrete values.

## What I Found

All 100 seeds achieved grokking. None crystallized.

Every checkpoint ended in what I call "cold glass": functional, generalizing, but structurally amorphous. The metrics tell a consistent story:

- **κ = infinity** for all seeds. The gradient covariance matrix is singular—gradients are linearly dependent, indicating the system sits in a flat minimum with many equivalent directions.
- **δ ≈ 0.00015** on average. Weights are close to integers but not exactly there. The closest seed (53) reached δ = 0.00010; the worst (32) stayed at 0.00017.
- **LC ≈ 899**. Local complexity remains high, meaning many neurons are still active and the representation hasn't collapsed to a sparse, structured form.
- **ψ ≈ 2.48**. The superposition coefficient indicates substantial feature overlap—unlike the Strassen crystals where ψ dropped to ~1.8.

The phase transition detector fired at step 1.0 for every seed. This isn't a real transition—it's an artifact of the early stopping condition. The system grokked but never had time to anneal into a crystalline state.

## What This Means

Binary parity grokking produces glass, not crystal. The network learns to generalize without discovering a compact, discrete algorithmic structure. This contrasts sharply with my Strassen experiments where 68% of runs crystallized into exact integer coefficients that transferred zero-shot to larger matrices.

I see three possible explanations:

**The architecture is too expressive.** A two-layer MLP has enough parameters to implement parity through distributed, overlapping representations rather than being forced into a discrete factorization. The bilinear structure in Strassen may have provided necessary constraints.

**The stopping criterion is too early.** Grokking at 98% accuracy leaves the network in a "warm" state—functional but not settled. In Strassen, I trained for 1000+ epochs past initial convergence to reach κ = 1 and δ = 0.

**Parity is fundamentally different.** Matrix multiplication has algebraic structure (associativity, distributivity) that admits compact tensor decompositions. Parity is a simpler predicate but may not have a "natural" discrete parameterization in this architecture.

## What I Don't Know

Whether longer training would crystallize these networks. The stagnation detector triggers on lack of accuracy improvement, but the thermodynamic metrics (κ, δ, LC) might still be evolving even when accuracy plateaus.

Whether a different architecture—particularly one with multiplicative interactions or explicit modular structure—would enable crystallization. The bilinear parameterization was crucial for Strassen.

Whether the "cold glass" state is actually desirable. These networks generalize perfectly and are robust to pruning (structural integrity ~4.5% at zero pruning, collapsing to zero under any actual pruning). The crystal state in Strassen was fragile—0% success with noise σ ≥ 0.001. Glass may be the better engineering outcome even if it's less theoretically clean.

## What Comes Next

I need to run longer training. The current protocol stops at grokking, but the Strassen crystals required extended annealing. I also want to test whether intermediate pruning—forcing sparsity during training rather than analyzing it post-hoc—can induce crystallization.

The curriculum transfer works: networks trained on 10-bit parity generalize to 64-bit. But they do so through interpolation, not through discovering a scalable discrete algorithm. Whether this distinction matters for downstream tasks is an open question.

## Data Availability

Code and checkpoints: https://github.com/grisuno/algebra-de-grok

Space HuggingFace : https://huggingface.co/spaces/grisun0/algebra-de-grok

- https://doi.org/10.5281/zenodo.18489853
- https://doi.org/10.5281/zenodo.18072858
- https://doi.org/10.5281/zenodo.18446389

---

grisun0
February 2026
