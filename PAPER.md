# Algorithmic Weight Transfer Enables Zero-Shot Generalization of Parity to 128 Bits

**Author:** grisun0 (LazyOwn RedTeam)  
**Year:** 2025  

**Keywords:** Grokking, Algorithmic Generalization, Curriculum Learning, Parity, Sparse Autoencoders, Local Complexity

---

## Abstract

We study generalization in neural networks on the binary parity task under controlled scaling. We show that once a multilayer perceptron (MLP) discovers a parity-solving representation at low dimensionality, this representation can be preserved and re-embedded into higher-dimensional models via structured weight transfer. Using a curriculum over input dimensionality and an algorithm-preserving padding scheme, we demonstrate zero-shot generalization of parity to 128-bit inputs, achieving perfect test accuracy without any additional training. An explicit ablation study confirms that this behavior does not arise from chance initialization. These results support the interpretation of grokking as the discovery of a compact, dimension-independent algorithmic subspace that remains stable under architectural expansion.

---

## 1. Introduction

Binary parity is a canonical benchmark for studying generalization and inductive bias in neural networks. Although the target function has a simple algorithmic description, it is known to be difficult for gradient-based learners, especially under small data regimes.

Recent work has highlighted *grokking*, a phenomenon in which neural networks abruptly transition from memorization to generalization after extended training. Prior analyses have focused primarily on explaining why this transition occurs late. In contrast, we investigate what happens *after* grokking: specifically, whether the learned solution corresponds to a reusable algorithmic representation.

We show that once grokking occurs at small scale, the learned representation can be transferred to substantially larger models via structured weight expansion, enabling zero-shot generalization to input sizes far beyond the original training regime.

---

## 2. Task Definition

We consider the binary parity task. Given an input vector

\[
x \in \{0,1\}^n,
\]

the label is defined as

\[
y = \left(\sum_{i=1}^{n} x_i\right) \bmod 2.
\]

This task requires learning a global function over all input dimensions and cannot be solved via local heuristics or shallow correlations.

---

## 3. Model Architecture

All experiments use a standard multilayer perceptron with ReLU activations:

\[
h_1 = \mathrm{ReLU}(W_1 x + b_1),
\]
\[
h_2 = \mathrm{ReLU}(W_2 h_1 + b_2),
\]
\[
\hat{y} = W_3 h_2 + b_3.
\]

The output consists of two logits corresponding to binary classification. No architectural modifications (attention, normalization, skip connections) are used.

---

## 4. Curriculum Training at Low Dimensionality

Training proceeds via a curriculum over input dimensionality:

| Stage | Input Bits | Hidden Dimension |
|------:|-----------:|-----------------:|
| 1 | 10 | 128 |
| 2 | 24 | 256 |
| 3 | 32 | 512 |
| 4 | 64 | 1024 |

In Stage 1, the model is trained until grokking occurs, typically around 2000 optimization steps. Training set size scales logarithmically with input dimensionality, remaining below 2000 samples throughout.

Weight decay is scaled according to problem complexity:

\[
\lambda \propto (n_{\text{bits}} \cdot d_h)^{-1/2},
\]

encouraging early compression while allowing flexibility as the model scales.

---

## 5. Algorithm-Preserving Weight Transfer

To scale from stage \(s\) to stage \(s+1\), weights are transferred using structured padding:

- Learned weight matrices are copied into the upper-left submatrix of the expanded matrix.
- Newly introduced rows and columns are initialized to zero.
- Bias vectors are padded analogously.

This procedure preserves the learned computational subspace while embedding it into a higher-dimensional parameterization. No fine-tuning or retraining is performed after transfer.

---

## 6. Zero-Shot Transfer to 128 Bits

We evaluate whether the representation learned at 64 bits generalizes to 128-bit parity without training.

### Setup

- Input size: 128 bits  
- Hidden dimension: 2048  
- Training steps: 0 (zero-shot)  

The 128-bit model is initialized exclusively via structured weight transfer from the trained 64-bit model.

### Result

At initialization (step 0), the model achieves:

- Train accuracy: 1.00  
- Test accuracy: 1.00  

demonstrating perfect zero-shot generalization.

---

## 7. Ablation Study

To verify that zero-shot generalization is not due to chance initialization, we perform a controlled ablation.

### Conditions

1. **Algorithmic transfer:** structured padding from the trained 64-bit model.
2. **Control:** identical architecture with random initialization.

### Results

| Condition | Train Accuracy | Test Accuracy |
|----------:|---------------:|--------------:|
| With transfer | 1.00 | 1.00 |
| No transfer | ≈0.50 | ≈0.50 |

Both evaluations are performed at step 0, without training.

This confirms that generalization depends on preserving the learned weight structure.

---

## 8. Interpretation

The parity function admits a compact, dimension-independent algorithmic description. Our results indicate that grokking corresponds to discovering a representation that implements this algorithm.

Once discovered, this representation remains stable under expansion and can be reused without further optimization. In this sense, grokking is a one-time discovery event rather than a recurring training cost.

---

## 9. Limitations

- Experiments are limited to parity.
- Transfer assumes compatible architectures.
- Extension to other algorithmic or real-world tasks remains future work.

---

## 10. Bibliography

1. **Humayun, A. I., Balestriero, R., & Baraniuk, R.**  
   *Deep Networks Always Grok and Here is Why.*  
   arXiv:2402.15555  
   https://arxiv.org/html/2402.15555v2  

2. **Bereska, L., Tzifa-Kratira, Z., Samavi, R., & Gavves, E.**  
   *Superposition as Lossy Compression: Measure with Sparse Autoencoders and Connect to Adversarial Vulnerability.*  
   arXiv:2512.13568  
   https://arxiv.org/html/2512.13568v1  

---

## 11. Conclusion

We show that a neural network that has grokked parity at small scale can be expanded to 128-bit inputs and achieve perfect zero-shot generalization through structured weight transfer. An explicit ablation confirms that this effect does not arise from chance initialization. These findings support the view that grokking corresponds to the discovery of a reusable algorithmic subspace that remains stable under scaling.

---

## License

GPL v3
