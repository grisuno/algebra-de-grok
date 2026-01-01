# Structural Weight Transfer for Grokked Networks

**Zero-shot transfer of learned algorithms via weight expansion**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18072859.svg)](https://doi.org/10.5281/zenodo.18072859)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)


---

## What This Does

Train a small neural network on binary parity (64 bits) until it "groks" the algorithm. Then expand the model to 2048 bits by copying weights into a larger matrix and padding with zeros. The expanded model achieves 100% accuracy without any additional training.

**Key result:** Perfect generalization at 128, 256, 512, 1024, and 2048 bits with zero gradient updates. Total time: 99 seconds.

---

## Results

| Bits | Hidden Dim | Test Accuracy | Time (s) |
|-----:|-----------:|--------------:|---------:|
| 128  | 2,048      | 100%          | 0.14     |
| 256  | 4,096      | 100%          | 0.42     |
| 512  | 8,192      | 100%          | 1.34     |
| 1024 | 16,384     | 100%          | 8.25     |
| 2048 | 32,768     | 100%          | 44.14    |

Control models with random weights: ~50% (chance).

<img width="1268" height="623" alt="image" src="https://github.com/user-attachments/assets/828fb191-a859-4154-9f2c-19cf03f308c1" />

<img width="417" height="305" alt="image" src="https://github.com/user-attachments/assets/17f9e8a0-cde3-4835-931c-9ffab9730dcb" />


Target:

<img width="789" height="600" alt="newplot" src="https://github.com/user-attachments/assets/f4f5e04d-e2e2-47c5-a537-711d369f93fe" />

Observed:

<img width="1279" height="700" alt="1" src="https://github.com/user-attachments/assets/2b458676-9c11-4329-a3bc-529f9c7110bb" />


Target:

<img width="789" height="600" alt="newplot (1)" src="https://github.com/user-attachments/assets/fe8b6c93-650b-4351-b0a5-88b2c8b5ae1a" />

Observed:

<img width="1279" height="700" alt="2" src="https://github.com/user-attachments/assets/5737fad7-ff59-442f-b072-57140cb54640" />

Target:

<img width="789" height="600" alt="newplot (2)" src="https://github.com/user-attachments/assets/29e7b4d9-47f1-40e5-9493-fb328f060471" />

Observed:

<img width="1279" height="700" alt="3" src="https://github.com/user-attachments/assets/db5f0f2d-8651-4dd4-95d9-cb32875e1886" />

## Ablation

<img width="1239" height="440" alt="image" src="https://github.com/user-attachments/assets/44f514e7-f9ec-41be-8910-c821212131d5" />

<img width="1301" height="411" alt="image" src="https://github.com/user-attachments/assets/02d612c1-4bdf-429f-8fc3-aa48f0141a3c" />

<img width="1298" height="413" alt="image" src="https://github.com/user-attachments/assets/b0272921-4196-4123-81b0-4288fe9fedb5" />

<img width="425" height="205" alt="image" src="https://github.com/user-attachments/assets/bc724ed3-7734-48ad-8d02-e430a4304572" />

---

## Method

1. **Train base model:** Standard MLP (2 hidden layers, ReLU) on 64-bit parity with strong regularization until test accuracy reaches 100% (grokking).

2. **Weight expansion:** For a weight matrix W ∈ ℝ^(d×n), create W' ∈ ℝ^(2d×2n):
   - Copy W into upper-left block
   - Pad remaining entries with zeros
   - Repeat for each layer

3. **Evaluate:** Test expanded model immediately (no training).

---

## Code

```bash
# Train base 64-bit model (requires grokking)
python app.py

# Expand to 2048 bits
python 2048bits.py

# Visualize weight geometry
streamlit run view_streamlit.py
```

---

## Task Definition

We solve **k-bit subset parity** embedded in n-bit inputs:

```
f(x) = (sum of k specific bits) mod 2
```

where k is fixed (e.g., k=3) and learned during training. The remaining n-k bits are noise.

**Not solved:** Full n-bit parity where all bits matter. This is subset preservation, not length generalization.

---

## Why It Works

Grokking discovers a geometric representation of the algorithm (observable via PCA: neurons cluster at cardinal points). This geometry is dimension-invariant—it depends on angular relationships, not absolute coordinates. Weight expansion preserves these relationships.

---

## Limitations

- Requires initial grokking (can take thousands of epochs)
- Works for tasks with compact algorithmic structure
- Preserves fixed k-bit subcircuits, not arbitrary n-bit functions
- Numerical precision limits extreme scales

---

## Related Work

- **[SWAN-Phoenix-Rising](https://github.com/grisuno/SWAN-Phoenix-Rising):** Applied same method to different task (AUPRC > 0.99). Shows technique generalizes beyond AUPRC.
- **[Kepler Orbit Grokker](https://github.com/grisuno/kepler_orbit_grokker/):** Applied same method to different task . Shows technique generalizes beyond Kepler Orbit.
- **[Structural Transfer for Physical Laws: Zero-Shot Algorithmic Expansion in Hamiltonian Systems](https://github.com/grisuno/chaotic_pendulum_grokked):** Applied same method to different task . Shows technique generalizes beyond Chaotic Pendulum.
- **[Structural Transfer for Wave Dynamics](https://github.com/grisuno/1d_wave_equation_grokker): Zero-Shot Algorithmic Expansion in 1D Wave Propagation:** Applied same method to different task . Shows technique generalizes beyond 1D Wave Equation.
- **[Agentic Grokked Integrated is a Unified Framework for Zero-Shot Structural Transfer of Grokked Algorithmic Cassettes](https://github.com/grisuno/agi):** Modular framework for composing and deploying neural networks that have grokked compact algorithmic or physical laws.
---
## Demo

[https://huggingface.co/spaces/grisun0/algebra-de-grok](https://huggingface.co/spaces/grisun0/algebra-de-grok)

## References

1. Citation for Grokking and Local Complexity (LC): Title: Deep Networks Always Grok and Here is Why

Authors: Ahmed Imtiaz Humayun, Randall Balestriero, Richard Baraniuk

2. Citation for Superposition and Sparse Autoencoders (SAE): Title: Superposition as Lossy Compression: Measure with Sparse Autoencoders and Connect to Adversarial Vulnerability

Authors: Leonard Bereska, Zoe Tzifa-Kratira, Reza Samavi, Efstratios Gavves


---

## Citation

```bibtex
@software{grisuno2025_structural_weight_transfer,
  author = {grisun0},
  title = {Structural Weight Transfer for Grokked Networks},
  year = {2025},
  doi = {10.5281/zenodo.18072859},
  url = {https://github.com/grisuno/algebra-de-grok}
}
```

---

## License

GPL v3

---

**Note:** This demonstrates that learned algorithmic representations can be transferred to larger models without retraining. It does not solve the general problem of length extrapolation or full n-bit parity.

**Critique**: "You are merely evaluating the same 64-bit sub-circuit within a larger space."

**Response**: "Exactly. That is defined as Structural Transfer. I have demonstrated that once the model 'groks' the algorithm, that algorithm crystallizes into a modular primitive. This primitive can then be injected into massive models (1.1B parameters) without any loss in efficiency or the need for further training."

## [PAPER.md](https://github.com/grisuno/agi/blob/main/PAPER.md)
## [Medium Article](https://medium.com/@lazyown.redteam/the-algorithmic-heist-how-i-built-non-hallucinating-ai-on-hardware-your-grandma-throws-away-6bc5146608f1?postPublishedType=initial)

- [https://doi.org/10.5281/zenodo.18072859](https://doi.org/10.5281/zenodo.18072859)
- [https://www.youtube.com](https://www.youtube.com/watch?v=o43jstmm160&list=PLW9Qe5HJK5CFXyIsF9b0NB6n9EY8Am3YZ&index=1)
- [https://deepwiki.com/grisuno/algebra-de-grok](https://deepwiki.com/grisuno/algebra-de-grok)
- [https://medium.com/@lazyown.redteam/the-grokking-heist-how-i-stole-perfect-generalization](https://medium.com/@lazyown.redteam/the-grokking-heist-how-i-stole-perfect-generalization-from-%C2%B2%E2%81%B6%E2%81%B4-possible-inputs-using-only-1-800-c3c415133218)
- [https://huggingface.co/spaces/grisun0/algebra-de-grok](https://huggingface.co/spaces/grisun0/algebra-de-grok)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18072859.svg)](https://doi.org/10.5281/zenodo.18072859)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)
