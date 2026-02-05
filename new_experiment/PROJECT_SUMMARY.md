# Thermodynamic Grokking Framework - Project Summary

## Overview

Complete, production-ready framework for studying phase transitions in neural network learning through curriculum-based training with comprehensive thermodynamic metric tracking and real-time visualization.

## Key Features

1. **Fully Parameterized Configuration**
   - Zero magic numbers
   - All hyperparameters in centralized config
   - Adaptive parameter calculation

2. **Comprehensive Metrics**
   - Learning: accuracy, loss
   - Superposition: psi, effective features
   - Complexity: local complexity
   - Gradient: kappa, covariance
   - Thermodynamic: T_eff, h_bar_eff, entropy
   - Discretization: delta

3. **Real-Time Visualization**
   - Streamlit web interface
   - 3D PCA neural geometry
   - 2D weight texture analysis
   - Live training metrics
   - Phase transition detection

4. **WandB Integration**
   - Full experiment tracking
   - Metric logging
   - Hyperparameter comparison

5. **Automatic Checkpointing**
   - Every 5 minutes (configurable)
   - On grokking achievement
   - Latest checkpoint always available

6. **Smart Weight Transfer**
   - Preserves algorithmic structure
   - Handles dimension changes
   - Padding/cropping strategies

7. **Stagnation Detection**
   - Monitors training progress
   - Automatic optimizer restart
   - Best model preservation

8. **SOLID Architecture**
   - Single Responsibility Principle
   - Open/Closed Principle
   - Liskov Substitution Principle
   - Interface Segregation Principle
   - Dependency Inversion Principle

## Architecture

### Core Components

```
config.py                  ExperimentConfig dataclass
                          All parameters centralized
                          Adaptive parameter methods

models.py                  IModelArchitecture interface
                          GrokkingTransformer (2-layer MLP)
                          SuperpositionSAE (sparse autoencoder)

data_generation.py         ParityDatasetGenerator
                          Binary parity task generation

metrics.py                 IMetricCalculator interface
                          LocalComplexityCalculator
                          GradientCovarianceCalculator
                          ThermodynamicMetricsCalculator
                          DeltaCalculator
                          ComprehensiveMetricsAggregator

checkpointing.py           ICheckpointManager interface
                          CheckpointManager
                          Automatic save/load
                          Interval-based checkpointing

training_dynamics.py       SmartWeightTransfer
                          StagnationDetector
                          Adaptive training management

wandb_integration.py       WandBLogger
                          Experiment tracking
                          Metric logging

training.py                CurriculumStageTrainer
                          Main training loop
                          Metric computation
                          Checkpoint management

main.py                    MultiSeedCurriculumRunner
                          CLI interface
                          Multi-seed experiments

streamlit_app.py           StreamlitTrainer
                          ThermodynamicAnalyzer
                          Real-time visualization
                          3D/2D geometry plots

test_framework.py          Unit tests
                          Component validation
```

### Design Patterns

1. **Strategy Pattern**: Metric calculators implement IMetricCalculator
2. **Factory Pattern**: Model and SAE creation
3. **Observer Pattern**: Metrics aggregation and logging
4. **Template Method**: Training loop structure
5. **Dependency Injection**: Config passed to all components

### SOLID Principles Applied

**Single Responsibility**:
- Each class has one clear purpose
- Metric calculators compute specific metrics
- Managers handle specific resources

**Open/Closed**:
- Interfaces define contracts
- New metric calculators can be added
- Extension without modification

**Liskov Substitution**:
- All metric calculators interchangeable
- Model architectures follow interface

**Interface Segregation**:
- Minimal, focused interfaces
- No forced dependencies

**Dependency Inversion**:
- Depend on abstractions (interfaces)
- Config dependency injection

## File Descriptions

### config.py (100 lines)
- `ExperimentConfig`: Dataclass with all hyperparameters
- Adaptive parameter methods
- No magic numbers
- Complete type hints

### models.py (150 lines)
- `IModelArchitecture`: Interface for neural networks
- `GrokkingTransformer`: 2-layer MLP for parity learning
- `SuperpositionSAE`: Sparse autoencoder for analysis
- Pre-activation access
- Superposition metrics

### data_generation.py (30 lines)
- `ParityDatasetGenerator`: Binary parity dataset creation
- Configurable k-bit parity
- Random binary vectors

### metrics.py (350 lines)
- `IMetricCalculator`: Metric calculator interface
- `LocalComplexityCalculator`: Sparsity analysis
- `GradientCovarianceCalculator`: Kappa computation
- `ThermodynamicMetricsCalculator`: T_eff, h_bar_eff
- `DeltaCalculator`: Weight discretization
- `ComprehensiveMetricsAggregator`: Unified metric collection

### checkpointing.py (100 lines)
- `ICheckpointManager`: Checkpoint interface
- `CheckpointManager`: Save/load implementation
- Automatic interval-based saving
- Latest checkpoint tracking

### training_dynamics.py (120 lines)
- `SmartWeightTransfer`: Algorithm-preserving transfer
- `StagnationDetector`: Training progress monitoring
- Padding/cropping strategies
- Optimizer restart logic

### wandb_integration.py (70 lines)
- `WandBLogger`: WandB wrapper
- Initialization handling
- Metric logging
- Error resilience

### training.py (300 lines)
- `CurriculumStageTrainer`: Single-stage training
- Full metric tracking
- Checkpoint creation
- Stagnation handling
- WandB integration

### main.py (150 lines)
- `MultiSeedCurriculumRunner`: Multi-seed orchestration
- CLI argument parsing
- Seed management
- Result aggregation

### streamlit_app.py (500 lines)
- `ThermodynamicAnalyzer`: Phase transition analysis
- `StreamlitTrainer`: Real-time training with viz
- 3D PCA visualization
- 2D texture analysis
- Live metric dashboards

### test_framework.py (200 lines)
- Component unit tests
- Integration validation
- Syntax verification

## Usage Modes

### 1. Command Line
```bash
python main.py --seed 42
python main.py --seed-start 1 --seed-end 10
python main.py --seed 42 --base-lr 0.001 --no-wandb
```

### 2. Streamlit Web Interface
```bash
streamlit run streamlit_app.py
```
- Interactive configuration
- Real-time visualization
- Phase transition monitoring

### 3. Programmatic
```python
from config import ExperimentConfig
from training import CurriculumStageTrainer

config = ExperimentConfig(seed=42)
trainer = CurriculumStageTrainer(config, seed=42)
model, sae, success, history = trainer.train_stage(0, 10, 128)
```

## Metrics Tracked

### Learning
- Train/test accuracy
- Classification loss
- SAE reconstruction loss

### Superposition
- Psi coefficient (information packing)
- Effective features (active dimensions)

### Complexity
- Local complexity (sparsity measure)
- Pre-activation analysis

### Gradient
- Kappa (condition number)
- Eigenvalue spectrum
- Covariance matrix

### Thermodynamic
- Effective temperature
- Effective Planck constant
- Thermodynamic entropy
- Trace of gradient covariance

### Discretization
- Delta (distance to integers)
- Weight crystallization

## Curriculum Stages

1. **Gas** (10 bits, 128 hidden): Random exploration
2. **Liquid** (24 bits, 256 hidden): Cluster formation
3. **Transition** (32 bits, 512 hidden): Crystallization
4. **Crystalline** (64 bits, 1024 hidden): Algorithm discovery

## Key Innovations

1. **Parameter-free Configuration**: All magic numbers eliminated
2. **Adaptive Training**: Automatic parameter scaling
3. **Complete Metrics**: All paper metrics implemented
4. **Real-time Visualization**: 3D/2D geometry analysis
5. **Production Ready**: Checkpointing, logging, error handling
6. **Clean Architecture**: SOLID principles throughout

## Technical Specifications

- **Language**: Python 3.8+
- **Framework**: PyTorch
- **Visualization**: Streamlit, Plotly
- **Tracking**: Weights & Biases
- **Style**: Type hints, docstrings, PEP 8
- **Paradigm**: Object-oriented, functional
- **Patterns**: Strategy, Factory, Observer, Template Method
- **Principles**: SOLID, DRY, KISS

## Performance

- **GPU Support**: Full CUDA acceleration
- **Checkpointing**: Every 5 minutes
- **Metric Logging**: Configurable intervals
- **Memory Efficient**: Gradient windowing
- **Scalable**: Multi-seed parallelizable

## Quality Assurance

- Syntax validation: All files compile
- Type hints: Complete coverage
- Docstrings: All classes and methods
- Error handling: Try-catch blocks
- Unit tests: Core components validated

## Future Extensions

1. Additional curricula
2. Alternative architectures
3. More phase transition metrics
4. Distributed training
5. Hyperparameter optimization
6. Result analysis tools

## Files Provided

1. config.py - Configuration
2. models.py - Neural architectures
3. data_generation.py - Dataset generation
4. metrics.py - Metric calculation
5. checkpointing.py - Checkpoint management
6. training_dynamics.py - Training dynamics
7. wandb_integration.py - WandB logging
8. training.py - Training loop
9. main.py - CLI interface
10. streamlit_app.py - Web interface
11. test_framework.py - Unit tests
12. requirements.txt - Dependencies
13. README.md - Documentation
14. USAGE.md - Usage guide
15. PROJECT_SUMMARY.md - This file

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Quick test:
```bash
python main.py --seed 42 --no-wandb
```

3. Full visualization:
```bash
streamlit run streamlit_app.py
```

4. Production run:
```bash
python main.py --seed-start 1 --seed-end 100
```

## Support

- Documentation: README.md, USAGE.md
- Tests: test_framework.py
- Examples: In USAGE.md
- Issues: Check error messages, logs

## License

GPL v3

## Author

Gris Iscomeback
grisun0[at]proton[dot]me

## Citation

```bibtex
@software{thermodynamic_grokking_2025,
  title={Thermodynamic Grokking Curriculum Framework},
  author={Gris Iscomeback},
  year={2025}
}
```

