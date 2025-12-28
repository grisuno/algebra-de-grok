# Algorithmic Conservation in Neural Networks

**grisun0**  
Independent Research  
2025-12-28

---

## Abstract

We observe that three independent neural network systems preserve learned algorithmic structure under different conditions: RESMA (via architectural constraints), SWAN (via adaptive regularization), and structural weight transfer (via parameter freezing). We propose that these share a common mechanism: once a network discovers a compact algorithmic representation, that structure can be preserved without further gradient updates.

In the clearest case (parity transfer), a learned 64-bit subcircuit scales to 2048 bits with 100% accuracy and zero training. Control models remain at chance.

This suggests grokking marks a transition to a stable algorithmic regime that can be preserved rather than requiring rediscovery.

---

## 1. Observation

Three systems maintain learned structure under transformation:

1. **RESMA**: Freezes parameters when entropy gap crosses threshold
2. **SWAN**: Adjusts sparsity to prevent feature collapse during distribution shift  
3. **Parity transfer**: Embeds learned subcircuit into larger networks via weight expansion

Common pattern: All preserve a learned algorithmic subspace once discovered.

---

## 2. Formal Statement

Let f_θ be a network solving task L. A subspace is **conserved** if operator T exists such that:

```
T[f_θ] = f_θ' with L(f_θ') = L(f_θ)
```

where θ' has different dimensionality or exists at later time.

**Strong conservation:** T² = T (exact, RESMA and parity transfer)  
**Weak conservation:** ||T² - T|| < ε (approximate, SWAN)

---

## 3. Three Implementations

### 3.1 RESMA: Hard Parameter Freezing

Monitors entropy gap ΔS between quantum-inspired metrics. When ΔS < ε_c, sets ∂θ/∂t ≈ 0.

**Conservation:** Architectural constraint prevents parameter drift.

### 3.2 SWAN: Adaptive Regularization

Adjusts L1 penalty based on feature utilization Ψ:

```
λ_L1(t) = λ_0 · (1 + tanh((Ψ_0 - Ψ(t))/τ))
```

**Conservation:** Soft control maintains feature diversity under distribution shift.

### 3.3 Parity Transfer: Structural Expansion

Trains network on k-bit parity until grokking. Freezes weights. Embeds into larger matrix:

```
W' = [W  0]
     [0  0]
```

**Conservation:** Original subspace preserved exactly in block structure.

---

## 4. Experimental Evidence

Parity subcircuit (k=3 active bits) embedded in increasing input dimensions:

| Input Bits | Hidden Dim | Accuracy | Time (s) |
|-----------:|-----------:|---------:|---------:|
| 128        | 2,048      | 100%     | 0.14     |
| 256        | 4,096      | 100%     | 0.42     |
| 512        | 8,192      | 100%     | 1.34     |
| 1,024      | 16,384     | 100%     | 8.25     |
| 2,048      | 32,768     | 100%     | 44.14    |

Random-weight controls: ~50% (chance). No training performed after expansion.

**Note:** This preserves a fixed k-bit subcircuit, not full n-bit parity. Additional dimensions are noise.

---

## 5. Interpretation

All three systems follow approximate conservation:

```
d I(θ; D)/dt = ∇L · dθ/dt + C(θ, M) ≈ 0
```

where C is a conservation functional and M is a monitoring metric (entropy gap, feature utilization, or gradient norm).

Exact conservation (RESMA, parity) sets dθ/dt = 0 directly.  
Approximate conservation (SWAN) regulates but does not freeze parameters.

---

## 6. Implications

1. **Curriculum matters more than compute:** Finding the algorithmic subspace is the bottleneck, not scaling it.

2. **Preservation enables transfer:** Once found, structure scales without retraining.

3. **Grokking = discovery of conservable structure:** Sharp transition occurs when network enters regime where learned representation stabilizes.

---

## 7. Limitations

- Applies only to tasks with compact algorithmic solutions
- Conservation metrics currently require manual design per domain
- Parity results demonstrate subcircuit preservation, not length generalization
- Extreme scales limited by memory and numerical precision

---

## 8. Conclusion

When neural networks discover compact algorithmic representations, those structures can be preserved under expansion (parity), time (SWAN), or architectural constraint (RESMA). Failure to generalize often stems from destroying learned structure during continued training, not from inability to learn.

Preservation, not rediscovery, may be the key to scalable algorithmic learning.

---

## References

1. Power et al. (2022). Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets
2. Liu et al. (2023). Understanding Grokking via Sparse Autoencoders  
3. grisun0 (2025). Structural Weight Transfer (DOI: 10.5281/zenodo.18072859)
4. grisun0 (2025). SWAN: Adaptive Sparse Learning under Temporal Drift
5. grisun0 (2024). RESMA 4.3.6 Documentation

---

**License:** GPL v3
