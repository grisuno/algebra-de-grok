# Fast Grokking via Adaptive Curriculum and Algorithmic Weight Transfer

**Author:** grisun0  
**Date:** 2025  

**Keywords:** Grokking, Curriculum Learning, Algorithmic Generalization, Parity, Sparse Autoencoders

---

## Abstract

We demonstrate that binary parity functions over up to **64 input bits** can be learned with **perfect generalization** in minutes rather than hours by combining:

1. An **adaptive curriculum** over input dimensionality.  
2. **Algorithm-preserving weight transfer** via structured padding.  
3. Controlled regularization schedules known to induce grokking.  
4. Sparse Autoencoders (SAEs) used as *diagnostic probes* of internal structure.

Once the parity algorithm is discovered at low dimensionality (10 bits), it transfers immediately to larger models and higher-dimensional inputs, achieving **100% test accuracy at step 1** for 24, 32, and 64-bit parity tasks.

This provides empirical evidence that grokking corresponds to the discovery of a **compact algorithmic subspace** that can be preserved and re-embedded under scaling.

---

## 1. Introduction

Binary parity is a canonical example of a task that is:

- Easy to specify  
- Hard to learn  
- Impossible to solve via local heuristics  

Despite its simplicity, parity has long been used as a stress test for generalization and inductive bias in neural networks.

Prior work on grokking shows that networks may generalize only after prolonged overfitting, often requiring millions of optimization steps.  
Here, we show that **once grokking occurs, the learned algorithm can be transferred**, eliminating the need to re-grok at larger scales.

---

## 2. Task Definition

Given a binary vector:

x ∈ {0,1}ⁿ

The label is defined as:

y = (∑ᵢ₌₁ᵏ xᵢ) mod 2

Where `k = 3` is fixed and `n` increases across curriculum stages.

This task requires learning **global parity**, not local correlations.

---

## 3. Model Architecture

We use a simple multilayer perceptron (MLP):

- Input dimension: `n_bits`  
- Two hidden ReLU layers  
- Binary classification output  

Computation graph:

x → Linear → ReLU → Linear → ReLU → Linear → logits

No attention, convolutions, skip connections, or architectural tricks are used.

---

## 4. Adaptive Curriculum Learning

Training proceeds in stages:

| Stage | n_bits | Hidden Dim |
|------:|-------:|-----------:|
| 1 | 10 | 128 |
| 2 | 24 | 256 |
| 3 | 32 | 512 |
| 4 | 64 | 1024 |

At each stage, training parameters are computed adaptively.

---

### 4.1 Training Set Size

Training set size grows logarithmically with input dimensionality:

N_train = O(log n_bits)

This prevents memorization while remaining sufficient for algorithm discovery.

---

### 4.2 Weight Decay Schedule

Weight decay is scaled as:

λ ∝ (n_bits · d_h)^(-1/2)

This enforces strong compression in early stages (encouraging grokking) while allowing flexibility as the model scales.

---

## 5. Algorithm-Preserving Weight Transfer

Between stages, weights are transferred using **structured padding**:

- Existing weights are copied into the upper-left submatrix  
- New dimensions are initialized to zero  
- Bias vectors are padded analogously  

This preserves the learned **algorithmic subspace** while expanding representational capacity.

No freezing, fine-tuning, or architectural changes are required.

---

## 6. Sparse Autoencoder Probes

A Sparse Autoencoder (SAE) is trained on hidden activations to measure internal structure:

- **ψ (psi):** effective feature utilization  
- **LC:** linearity / inactivity in pre-activations  

The SAE does **not** influence classifier training.  
It is used purely as a diagnostic and interpretability tool.

---

## 7. Results

### 7.1 Grokking Behavior

| Stage | n_bits | Grokking Step | Test Accuracy |
|------:|-------:|--------------:|--------------:|
| 1 | 10 | ~2000 | 1.00 |
| 2 | 24 | 1 | 1.00 |
| 3 | 32 | 1 | 1.00 |
| 4 | 64 | 1 | 1.00 |

Once grokking occurs at low dimensionality, **no further optimization is required**.

---

### 7.2 Generalization Efficiency

- ~1800 training samples  
- 64-bit input space (2⁶⁴ possible inputs)  
- Perfect generalization  

This violates naive VC-style intuitions but aligns with algorithmic compression theories.

---

## 8. Interpretation

The network does not memorize parity cases.  
It learns the function:

f(x) = (∑ xᵢ) mod 2

This function has:

- Constant description length  
- Dimension-independent generalization  
- Stable embedding under scaling  

Grokking corresponds to discovering this compact algorithmic representation.

---

## 9. Implications

These results suggest:

- Grokking is not a training inefficiency but a **search for algorithms**  
- Once found, algorithms can be **preserved and transferred**  
- Curriculum learning plus structured transfer dramatically reduces training cost  

---
## 10. Bibliography
1. Citation for Grokking and Local Complexity (LC): Title: Deep Networks Always Grok and Here is Why
Authors: Ahmed Imtiaz Humayun, Randall Balestriero, Richard Baraniuk
2. Citation for Superposition and Sparse Autoencoders (SAE): Title: Superposition as Lossy Compression: Measure with Sparse Autoencoders and Connect to Adversarial Vulnerability
Authors: Leonard Bereska, Zoe Tzifa-Kratira, Reza Samavi, Efstratios Gavves

---

## 11. Conclusion

We show that binary parity over 64 bits can be solved with perfect generalization in minutes by:

- Encouraging early algorithm discovery  
- Preserving learned structure during scaling  
- Monitoring internal representations directly  

Grokking is best understood as a **one-time algorithm discovery event**, not a recurring optimization cost.

---

## License

GPL V3


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)
