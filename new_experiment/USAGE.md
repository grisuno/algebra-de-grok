# Thermodynamic Grokking - Complete Usage Guide

## Installation

1. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Option 1: Command Line Training

Single seed with default parameters:
```bash
python main.py --seed 42
```

Multiple seeds:
```bash
python main.py --seed-start 1 --seed-end 10
```

Custom hyperparameters:
```bash
python main.py --seed 42 \
    --base-lr 0.001 \
    --base-wd 1.0 \
    --checkpoint-interval 300
```

Disable WandB:
```bash
python main.py --seed 42 --no-wandb
```

Force CPU:
```bash
python main.py --seed 42 --device cpu
```

### Option 2: Streamlit Real-Time Visualization

Launch web interface:
```bash
streamlit run streamlit_app.py
```

Then in browser:
1. Set random seed (textbox in sidebar)
2. Toggle WandB logging
3. Click "Start Training"
4. Watch real-time:
   - Core metrics (train/test accuracy, psi, LC)
   - Thermodynamic state (temperature, entropy, order, energy, coherence)
   - 3D neural geometry (PCA projection with cluster density)
   - 2D weight texture (heatmap, distribution, FFT, histogram)
   - Training dynamics charts

## Configuration

All parameters are in `config.py` as the `ExperimentConfig` dataclass.

### Key Configurable Parameters

```python
from config import ExperimentConfig

config = ExperimentConfig(
    # Seed
    seed=42,
    
    # Curriculum stages: (n_bits, hidden_dim)
    curriculum_stages=(
        (10, 128),
        (24, 256),
        (32, 512),
        (64, 1024)
    ),
    
    # Base training parameters
    base_learning_rate=1e-3,
    base_weight_decay=1.0,
    base_train_size=300,
    base_max_steps=600000,
    
    # SAE configuration
    sae_expansion_factor=4,
    sae_l1_coefficient=0.01,
    
    # Convergence thresholds
    grokking_threshold=0.98,
    partial_success_threshold=0.70,
    
    # Stagnation detection
    min_test_accuracy_improvement=0.01,
    max_steps_without_improvement=50000,
    lc_stagnation_threshold_factor=0.95,
    
    # Logging and checkpointing
    metrics_log_interval=500,
    checkpoint_interval_seconds=300.0,
    visualization_update_interval=2000,
    
    # WandB
    use_wandb=True,
    wandb_project="thermodynamic_grokking",
    
    # Device
    device="cuda"  # or "cpu"
)
```

### Adaptive Parameter Calculation

The framework automatically adjusts per stage:

**Training Size**: `train_size = base_train_size * log2(n_bits + 1)`
- Scales with input complexity
- Capped at `max_train_size_limit=2000`

**Weight Decay**: `wd = base_weight_decay / sqrt(complexity_factor)`
- Decreases for larger models
- Floored at `min_weight_decay_limit=0.01`

**Max Steps**: `steps = base_max_steps * log2(complexity_factor + 1)`
- Increases with complexity
- Capped at `max_steps_limit=2000000`

Where `complexity_factor = (n_bits * hidden_dim) / (10 * 128)`

## Metrics Explained

### Learning Metrics

**Train Accuracy**: Classification accuracy on training set
- Range: [0, 1]
- Target: High but can overfit

**Test Accuracy**: Classification accuracy on test set
- Range: [0, 1]
- Target: >0.98 for grokking

**Loss**: Cross-entropy loss
- Range: [0, ∞)
- Lower is better

### Superposition Metrics

**Psi (ψ)**: Superposition coefficient
- Range: [0, 1]
- Measures: Information packing efficiency
- Formula: `psi = exp(H[p]) / model_dim`
- Where `H[p]` is Shannon entropy of feature usage

**Effective Features**: Number of active SAE features
- Range: [0, sae_dim]
- Indicates representational capacity

### Complexity Metrics

**Local Complexity (LC)**: Count of near-zero pre-activations
- Range: [0, hidden_dim]
- High LC = sparse, structured representation
- Low LC = dense, unstructured representation

### Gradient Metrics

**Kappa (κ)**: Condition number of gradient covariance
- Range: [1, ∞)
- Formula: `kappa = λ_max / λ_min`
- Low = well-conditioned optimization
- High = ill-conditioned, slow convergence

### Thermodynamic Metrics

**Effective Temperature (T_eff)**: Average gradient variance
- Formula: `T_eff = trace(Σ) / dim`
- High = exploration phase
- Low = exploitation phase

**Effective Planck Constant (ħ_eff)**: Position uncertainty
- Formula: `h_bar_eff = sqrt(mean(eigenvalues)) * regularization`
- Quantum-inspired metric

**Thermodynamic Entropy**: Boltzmann-like entropy
- Measures disorder in gradient distribution

### Discretization Metrics

**Delta (δ)**: Mean squared distance to integers
- Range: [0, ∞)
- Formula: `delta = mean((W - round(W))^2)`
- Low = crystallized weights
- High = continuous weights

## Phase Transitions

### Gas Phase (Stage 1: 10 bits, 128 hidden)
- **Characteristics**: Random exploration, high entropy
- **Temperature**: High
- **Order**: Low
- **Kappa**: High (ill-conditioned)
- **LC**: Low (dense activations)

### Liquid Phase (Stage 2: 24 bits, 256 hidden)
- **Characteristics**: Cluster formation, medium entropy
- **Temperature**: Medium
- **Order**: Medium
- **Kappa**: Decreasing
- **LC**: Increasing

### Transition Phase (Stage 3: 32 bits, 512 hidden)
- **Characteristics**: Crystallization begins
- **Temperature**: Decreasing
- **Order**: Increasing
- **Kappa**: Low
- **LC**: High

### Crystalline Phase (Stage 4: 64 bits, 1024 hidden)
- **Characteristics**: Compact crystal, algorithmic weights
- **Temperature**: Minimum
- **Order**: Maximum
- **Kappa**: Minimum
- **LC**: Maximum
- **Delta**: Minimum (integer-like weights)

## Checkpointing

Checkpoints saved automatically:
- Every 5 minutes (configurable)
- When grokking threshold reached
- Latest checkpoint always available

Location: `checkpoints/latest_checkpoint.pt`

Checkpoint contains:
```python
{
    'seed': int,
    'stage': int,
    'n_bits': int,
    'hidden_dim': int,
    'step': int,
    'model_state_dict': dict,
    'sae_state_dict': dict,
    'optimizer_state_dict': dict,
    'metrics_history': list,
    'config': ExperimentConfig,
    'timestamp': str
}
```

Resume from checkpoint:
```python
from checkpointing import CheckpointManager
from config import ExperimentConfig

config = ExperimentConfig()
manager = CheckpointManager(config)
state = manager.load("checkpoints/latest_checkpoint.pt")

# Restore training state
model.load_state_dict(state['model_state_dict'])
optimizer.load_state_dict(state['optimizer_state_dict'])
```

## WandB Integration

### Setup

1. Install WandB:
```bash
pip install wandb
```

2. Login:
```bash
wandb login
```

3. Configure (optional):
```python
config = ExperimentConfig(
    use_wandb=True,
    wandb_project="my_project",
    wandb_entity="my_entity"
)
```

### Metrics Logged

All metrics are logged in real-time:
- step, loss, train_accuracy, test_accuracy
- psi, effective_features
- local_complexity
- kappa, delta
- T_eff, h_bar_eff, thermodynamic_entropy
- trace_gradient_covariance
- loss_sae

### Viewing Results

Go to https://wandb.ai and view:
- Metric plots over time
- Hyperparameter comparison
- Run comparisons
- System metrics

## Programmatic Usage

### Basic Training

```python
from config import ExperimentConfig
from training import CurriculumStageTrainer

config = ExperimentConfig(seed=42)
trainer = CurriculumStageTrainer(config, seed=42)

# Train single stage
model, sae, success, history = trainer.train_stage(
    stage=0,
    n_bits=10,
    hidden_dim=128,
    previous_model=None,
    previous_sae=None
)

if success:
    print(f"Final test accuracy: {history[-1]['test_accuracy']}")
```

### Full Curriculum

```python
from main import MultiSeedCurriculumRunner

config = ExperimentConfig(seed=42, use_wandb=False)
runner = MultiSeedCurriculumRunner(config)
runner.run_single_seed(42)
```

### Custom Curriculum

```python
config = ExperimentConfig(
    curriculum_stages=(
        (8, 64),
        (16, 128),
        (32, 256)
    )
)
```

## Troubleshooting

### CUDA Out of Memory
```python
config = ExperimentConfig(
    device="cpu",
    base_max_steps=100000  # Reduce steps
)
```

### Training Too Slow
```python
config = ExperimentConfig(
    metrics_log_interval=1000,  # Log less frequently
    checkpoint_interval_seconds=600,  # Checkpoint less often
    visualization_update_interval=5000  # Update viz less
)
```

### Grokking Not Achieved
```python
config = ExperimentConfig(
    base_max_steps=1000000,  # More steps
    base_weight_decay=2.0,  # Stronger regularization
    grokking_threshold=0.95  # Lower threshold
)
```

### WandB Issues
```bash
python main.py --seed 42 --no-wandb
```

## File Structure

```
project/
├── config.py                 # All configuration parameters
├── models.py                 # GrokkingTransformer, SuperpositionSAE
├── data_generation.py        # ParityDatasetGenerator
├── metrics.py                # All metric calculators
├── checkpointing.py          # CheckpointManager
├── training_dynamics.py      # SmartWeightTransfer, StagnationDetector
├── wandb_integration.py      # WandBLogger
├── training.py               # CurriculumStageTrainer
├── main.py                   # CLI interface
├── streamlit_app.py          # Web visualization interface
├── test_framework.py         # Unit tests
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
├── USAGE.md                  # This file
├── checkpoints/              # Saved checkpoints
│   └── latest_checkpoint.pt
└── results/                  # Training results
```

## Advanced Features

### Stagnation Detection

Automatically detects when training is stuck:
- Monitors test accuracy improvement
- Tracks local complexity
- Triggers optimizer restart with LR decay
- Preserves best model state

Disable:
```python
config = ExperimentConfig(
    max_steps_without_improvement=float('inf')
)
```

### Smart Weight Transfer

Preserves learned structure across stages:
- Direct copy for matching dimensions
- Padding for expansion
- Cropping for reduction

### Adaptive Parameters

Automatically scales:
- Training set size
- Weight decay
- Maximum steps

Based on problem complexity.

## Examples

### Example 1: Quick Test
```bash
python main.py --seed 42 --base-lr 0.01 --no-wandb
```

### Example 2: Production Run
```bash
python main.py --seed-start 1 --seed-end 100 \
    --base-lr 0.001 \
    --base-wd 1.0 \
    --checkpoint-interval 300
```

### Example 3: Custom Curriculum
```python
from config import ExperimentConfig
from main import MultiSeedCurriculumRunner

config = ExperimentConfig(
    curriculum_stages=(
        (6, 32),
        (12, 64),
        (24, 128),
        (48, 256)
    ),
    base_learning_rate=5e-4,
    use_wandb=True
)

runner = MultiSeedCurriculumRunner(config)
runner.run_experiment(1, 10)
```

## Performance Tips

1. **Use GPU**: Set `device="cuda"` in config
2. **Batch metrics**: Increase `metrics_log_interval`
3. **Reduce visualization**: Increase `visualization_update_interval`
4. **Disable WandB**: Use `--no-wandb` for local testing
5. **Reduce curriculum**: Test with fewer/smaller stages first

## Citation

```bibtex
@software{thermodynamic_grokking_2025,
  title={Thermodynamic Grokking Curriculum Framework},
  author={Gris Iscomeback},
  year={2025},
  url={https://github.com/grisuno/algebra-de-grok}
}
```
