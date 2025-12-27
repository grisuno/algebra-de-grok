---
title: "Algorithmic Conservation in Neural Networks: A Unified Framework for Zero-Shot Transfer and Temporal Stability"
author: |
  **grisun0**  
  Independent Research  
  *Correspondence: grisun0[AT]proton[DOT]me*
date: "2025-12-28"
---

# Abstract

We identify a unifying principle underlying several recent phenomena in neural network research, which we term **algorithmic conservation**. The principle states that once a neural network discovers a compact algorithmic *subspace*, that representation can be preserved under structural transformations and embedded into larger parameter spaces without further gradient-based learning.

We show that three seemingly independent systems—RESMA 4.3.6 (physical-analogue neural architectures), SWAN (adaptive sparse graph learning under temporal drift), and zero-shot parity transfer via structural weight homomorphisms—can all be understood as instantiations of this single conservation principle.

Across these systems, generalization scalability is determined primarily by **training curriculum and representation preservation**, rather than by raw compute or dataset size. In the parity case, we demonstrate that a parity subcircuit learned at small scale can be deterministically embedded into networks of up to 2048 input dimensions with perfect zero-shot accuracy, with all observed limits arising from hardware constraints (memory and numerical precision), not from statistical generalization failure.

This reframes grokking not as delayed memorization, but as a one-time **conservation event** in which the network transitions from interpolative dynamics to stable algorithmic computation.

---

## 1. Introduction

Neural networks are commonly described as universal function approximators whose generalization is fundamentally local. Under this view, tasks requiring global coordination across inputs—such as parity, modular arithmetic, or long-horizon temporal reasoning—are expected to scale poorly with input dimension.

However, several recent empirical findings challenge this assumption:

1. **Grokking**: networks abruptly transition from memorization to perfect generalization after extended training.
2. **Zero-shot structural transfer**: learned solutions can be embedded into larger models without retraining.
3. **Adaptive regularization and sparsity control**: representations can remain stable across temporal distribution shifts.

These results are typically studied in isolation. In this work, we argue they share a common causal mechanism: **the conservation of an algorithmic subspace once discovered**.

The central claim is not that neural networks automatically learn scalable algorithms, but that *when* such an algorithmic representation is found, generalization across scale or time depends on preserving that structure rather than rediscovering it through further optimization.

---

## 2. The Algorithmic Conservation Principle

### 2.1 Formal Definition

Let \( f_\theta : \mathcal{X} \to \mathcal{Y} \) be a neural network implementing a learned representation, and let \( \mathcal{L} \) denote the task loss. We say that an algorithmic subspace is **conserved** if there exists an operator \( \mathcal{T} \) such that:

\[
\mathcal{T}[f_\theta] = f_{\theta'} \quad \text{with} \quad \mathcal{L}(f_{\theta'}) = \mathcal{L}(f_\theta)
\]

where \( \theta' \) may correspond to a different parameterization (e.g., higher dimensionality or later training time).

Conservation is:

- **Strong** if \( \mathcal{T}^2 = \mathcal{T} \) (idempotent, exact preservation),
- **Weak** if \( \| \mathcal{T}^2 - \mathcal{T} \| < \varepsilon \) (approximate, regulated preservation).

---

### 2.2 Conserved Quantities

Across the systems studied, conservation applies to the following quantities:

| Quantity | RESMA | SWAN | Parity Transfer |
|--------|-------|------|-----------------|
| Effective feature count | \( F_{\text{eff}} = e^{H(p)} \) | \( \Psi = F_{\text{eff}} / d \) | Subspace dimension (64) |
| Structural invariant | PT-symmetric topology | Graph connectivity | Weight subspace rank |
| Information flow | \( \Delta S < \epsilon_c \) | Phoenix threshold \( \Psi_0 \) | Frozen gradients |

---

## 3. Three Instantiations of Conservation

### 3.1 RESMA: Hard Conservation via Physical Analogy

RESMA enforces conservation through architectural constraints inspired by PT-symmetric physical systems. A monitoring module measures an entropy gap:

\[
\Delta S = S_{\text{vN}}(\rho_{\text{red}}) - S_{\text{top}}(b_1)
\]

When \( \Delta S < \epsilon_c \), the system enters *silencio* mode, suppressing further parameter updates:

\[
\frac{\partial \theta}{\partial t} \approx 0
\]

This creates a hard conservation regime in which the learned representation becomes invariant under continued training and scaling.

---

### 3.2 SWAN: Soft Conservation via Adaptive Control

SWAN implements conservation through closed-loop sparsity control. The Phoenix Mechanism adjusts regularization strength based on the superposition ratio \( \Psi \):

\[
\lambda_{\ell_1}(t) = \lambda_{\ell_1}(0) \cdot \left(1 + \tanh\left(\frac{\Psi_0 - \Psi(t)}{\tau}\right)\right)
\]

When representational collapse is detected, sparsity pressure is relaxed, allowing dormant features to re-emerge. This preserves the learned algorithmic structure across temporal distribution shifts without freezing parameters entirely.

---

### 3.3 Parity Transfer: Discrete Conservation via Structural Freezing

Parity transfer provides the clearest illustration of algorithmic conservation.

A base model is trained until grokking occurs on a small parity task, learning a compact XOR subcircuit over a fixed number of input dimensions. Once learned, parameters are frozen.

To embed this subcircuit into a larger model, a structural expansion operator \( \Phi \) is applied:

\[
W' =
\begin{pmatrix}
W & 0 \\
0 & 0
\end{pmatrix}
\quad \text{with} \quad
\text{rank}(W') = \text{rank}(W)
\]

This transformation preserves the learned algorithmic subspace exactly, while rendering newly introduced dimensions mathematically irrelevant to the output.

Importantly, this does **not** constitute learning parity over all input bits; it preserves a fixed parity subcircuit embedded within a higher-dimensional input space.

---

## 4. Unified Conservation Dynamics

All three systems can be described by the following approximate conservation equation:

\[
\frac{d \mathcal{I}(\theta; \mathcal{D})}{dt}
=
\nabla_\theta \mathcal{L} \cdot \frac{d\theta}{dt}
+
\mathcal{C}(\theta, \mathcal{M})
\;\;\approx\;\; 0
\]

where \( \mathcal{C} \) is a conservation functional governed by a monitoring metric \( \mathcal{M} \).

Exact equality holds only in discrete freezing regimes; in adaptive systems, conservation is asymptotic rather than exact.

---

## 5. Experimental Evidence

### 5.1 Parity Subspace Scaling

A parity subcircuit learned at small scale was embedded into networks with increasing input dimensionality:

| Input Dim | Hidden Dim | Test Accuracy | Time (s) |
|---------:|-----------:|--------------:|---------:|
| 128 | 2048 | 1.000 | 0.14 |
| 256 | 4096 | 1.000 | 0.42 |
| 512 | 8192 | 1.000 | 1.34 |
| 1024 | 16384 | 1.000 | 8.25 |
| 2048 | 32768 | 1.000 | 44.14 |

Control models with random initialization remain at chance accuracy. Accuracy remains constant for all scales in which the conserved subspace fully determines the task output.

---

## 6. Discussion

### 6.1 Implications

1. **Curriculum over Compute**: Discovering compact algorithmic subspaces is more critical than scaling optimization.
2. **Preservation Enables Extrapolation**: Once conserved, representations scale deterministically.
3. **Grokking Reinterpreted**: Grokking marks the transition into a conserved algorithmic regime.

### 6.2 Limitations

- Conservation applies only when a compact algorithmic solution exists.
- Identification of conservation metrics currently requires manual design.
- Extreme scaling remains bounded by memory and numerical precision.

---

## 7. Conclusion

We have shown that several modern approaches to stable generalization—physical constraints, adaptive sparsity, and structural freezing—are unified by a single principle: **algorithmic conservation**.

Neural networks fail to generalize at scale not because they cannot represent algorithms, but because training procedures often destroy discovered structure. When that structure is preserved, extrapolation becomes a matter of engineering rather than learning.

---

## References

1. Power, A. et al. (2022). *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets*.  
2. Liu, Z. et al. (2023). *Understanding Grokking via Sparse Autoencoders*.  
3. grisun0 (2025). *Structural Weight Transfer for Parity Subspaces*.  
4. grisun0 (2025). *SWAN: Adaptive Sparse Learning under Temporal Drift*.  
5. grisun0 (2024). *RESMA 4.3.6: Production System Documentation*.

---

## License

GPL v3
