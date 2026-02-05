# Thermodynamic Grokking Curriculum Framework

A comprehensive framework for studying phase transitions in neural network learning through curriculum-based training with full thermodynamic metric tracking and real-time visualization.

## Overview

This framework demonstrates that binary parity functions over up to 64 input bits can be learned with perfect generalization through:

1. Adaptive curriculum over input dimensionality
2. Algorithm-preserving weight transfer via structured padding
3. Controlled regularization schedules inducing grokking
4. Sparse Autoencoders (SAEs) as diagnostic probes of internal structure

## Features

- **Curriculum Learning**: Progressive scaling from 10 to 64 bits
- **Smart Weight Transfer**: Preserves learned algorithmic structure across stages
- **Comprehensive Metrics**: Tracks all thermodynamic and learning metrics
- **Real-time Visualization**: Streamlit interface with 3D/2D geometry visualization
- **WandB Integration**: Full experiment tracking and logging
- **Automatic Checkpointing**: Saves state every 5 minutes
- **Stagnation Detection**: Adaptive optimizer resets
- **SOLID Architecture**: Clean, maintainable, extensible code

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Command Line Training

Train with a single seed:
```bash
python main.py --seed 42
```

Train with multiple seeds:
```bash
python main.py --seed-start 1 --seed-end 10
```

With custom hyperparameters:
```bash
python main.py --seed 42 --base-lr 0.001 --base-wd 1.0
```

Disable WandB logging:
```bash
python main.py --seed 42 --no-wandb
```

### Streamlit Real-time Visualization

Launch the interactive visualization:
```bash
streamlit run streamlit_app.py
```

Then:
1. Configure seed in sidebar
2. Toggle WandB logging
3. Click "Start Training"
4. Watch real-time metrics, 3D geometry, and phase transitions

## Architecture

### Core Components

- **config.py**: Centralized configuration (no magic numbers)
- **models.py**: Neural network architectures
- **data_generation.py**: Parity dataset generation
- **metrics.py**: Comprehensive metric calculation
- **checkpointing.py**: Automatic checkpoint management
- **training_dynamics.py**: Weight transfer and stagnation detection
- **wandb_integration.py**: Experiment tracking
- **training.py**: Main training loop
- **main.py**: Command-line interface
- **streamlit_app.py**: Real-time visualization interface

### Metrics Tracked

#### Learning Metrics
- Train accuracy
- Test accuracy
- Classification loss
- SAE reconstruction loss

#### Superposition Metrics
- Psi coefficient
- Effective features
- Feature sparsity

#### Complexity Metrics
- Local complexity (LC)
- Pre-activation sparsity
- Representational dimensionality

#### Gradient Metrics
- Kappa (condition number)
- Gradient covariance eigenvalues
- Optimization landscape geometry

#### Thermodynamic Metrics
- Effective temperature (T_eff)
- Effective Planck constant (h_bar_eff)
- Thermodynamic entropy
- Trace of gradient covariance

#### Discretization Metrics
- Delta (distance to integers)
- Weight crystallization

### Curriculum Stages

1. **Gas Phase** (10 bits, 128 hidden)
   - High entropy, random exploration
   - Stochastic weight distribution

2. **Liquid Phase** (24 bits, 256 hidden)
   - Cluster formation
   - Medium entropy

3. **Transition Phase** (32 bits, 512 hidden)
   - Crystallization begins
   - Entropy decreasing

4. **Crystalline Phase** (64 bits, 1024 hidden)
   - Compact crystal structure
   - Minimum entropy, maximum order

## Configuration

All hyperparameters are centralized in `ExperimentConfig`:

```python
config = ExperimentConfig(
    seed=42,
    base_learning_rate=1e-3,
    base_weight_decay=1.0,
    sae_expansion_factor=4,
    grokking_threshold=0.98,
    checkpoint_interval_seconds=300.0,
    use_wandb=True
)
```

### Key Parameters

- `seed`: Random seed for reproducibility
- `curriculum_stages`: Tuple of (n_bits, hidden_dim) pairs
- `sae_expansion_factor`: SAE dimensionality multiplier
- `base_learning_rate`: Initial learning rate
- `base_weight_decay`: Base L2 regularization
- `grokking_threshold`: Test accuracy threshold for success
- `checkpoint_interval_seconds`: Auto-save interval
- `metrics_log_interval`: Steps between metric computation
- `visualization_update_interval`: Steps between viz updates

## Adaptive Parameters

The framework automatically calculates stage-specific parameters:

- **Train Size**: Scales with log(n_bits)
- **Weight Decay**: Decreases with problem complexity
- **Max Steps**: Increases with complexity
- **Learning Rate**: Fixed base rate

## Checkpointing

Checkpoints are saved:
- Every 5 minutes (configurable)
- When grokking is achieved
- Latest checkpoint always available for resume

Checkpoint contains:
- Model state
- SAE state
- Optimizer state
- Metrics history
- Configuration
- Timestamp

## WandB Integration

When enabled, logs to Weights & Biases:
- All metrics in real-time
- Hyperparameters
- Stage information
- Run metadata

Configure with environment variables:
```bash
export WANDB_API_KEY=your_api_key
export WANDB_ENTITY=your_entity
```

## Visualization

### Streamlit Interface

Real-time visualization includes:

1. **Core Metrics Dashboard**
   - Train/test accuracy
   - Psi, LC, bits, hidden dim

2. **Thermodynamic State**
   - Temperature, entropy, order
   - Energy, coherence

3. **3D Neural Geometry**
   - PCA projection
   - Cluster visualization
   - Local density heatmap

4. **2D Weight Texture**
   - Heatmap visualization
   - Weight distribution
   - FFT spectrum
   - Histogram

5. **Training Metrics**
   - Accuracy evolution
   - Superposition coefficient
   - Local complexity
   - Kappa and delta

### Phase Transition Detection

Automatically detects transitions:
- Gas → Liquid: Cluster formation
- Liquid → Transition: Crystallization begins
- Transition → Crystalline: Grokking achieved

## Stagnation Detection

Monitors training progress:
- Test accuracy improvement
- Local complexity threshold
- Automatic optimizer restart with LR decay
- Best model state preservation

## Project Structure

```
.
├── config.py                 # Configuration
├── models.py                 # Neural architectures
├── data_generation.py        # Dataset generation
├── metrics.py                # Metric calculation
├── checkpointing.py          # Checkpoint management
├── training_dynamics.py      # Weight transfer & stagnation
├── wandb_integration.py      # WandB logging
├── training.py               # Training loop
├── main.py                   # CLI interface
├── streamlit_app.py          # Web interface
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

## Examples

### Basic Training
```python
from config import ExperimentConfig
from training import CurriculumStageTrainer

config = ExperimentConfig(seed=42)
trainer = CurriculumStageTrainer(config, seed=42)

# Train first stage
model, sae, success, history = trainer.train_stage(
    stage=0,
    n_bits=10,
    hidden_dim=128
)
```

### Custom Configuration
```python
config = ExperimentConfig(
    seed=42,
    base_learning_rate=5e-4,
    base_weight_decay=2.0,
    sae_expansion_factor=8,
    grokking_threshold=0.99,
    use_wandb=False
)
```

### Multi-Seed Experiment
```python
from main import MultiSeedCurriculumRunner

config = ExperimentConfig()
runner = MultiSeedCurriculumRunner(config)
runner.run_experiment(start_seed=1, end_seed=100)
```

## Results

Successful curriculum completion achieves:
- 100% test accuracy on 64-bit parity
- Phase transition from gas to crystalline
- Algorithmic weight structure
- Minimal entropy, maximal order

## Citation

If you use this framework, please cite:

```bibtex
@software{thermodynamic_grokking_2025,
  title={Thermodynamic Grokking Curriculum Framework},
  author={Gris Iscomeback},
  year={2025},
  url={https://github.com/grisuno/thermodynamic-grokking}
}
```

## License

GPL v3

## Author

Gris Iscomeback
Email: grisiscomeback[at]gmail[dot]com

## Contributing

Contributions welcome! Please:
1. Follow SOLID principles
2. Maintain clean architecture
3. Add comprehensive documentation
4. Include type hints
5. Test thoroughly

## Acknowledgments

Based on research in:
- Grokking and phase transitions in neural networks
- Curriculum learning
- Thermodynamic approaches to deep learning
- Superposition in neural networks
