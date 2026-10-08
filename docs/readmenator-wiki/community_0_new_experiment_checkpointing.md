# new_experiment: checkpointing

*Community 0 | 8 files | cohesion 0.60*

## Definition

This community groups 8 file(s) rooted at `new_experiment` with dominant language py (cohesion 0.60). Central symbols: `CheckpointManager`, `CurriculumStageTrainer`, `ExperimentConfig`, `ICheckpointManager`, `MultiSeedCurriculumRunner`, `ParityDatasetGenerator`, `SmartWeightTransfer`, `StagnationDetector`. Core file: `new_experiment/checkpointing.py` (10 symbols). Documented purpose: Checkpoint management for saving and loading training state..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `new_experiment/checkpointing.py` | py | utility | 10 | yes |
| `new_experiment/config.py` | py | infrastructure | 4 | yes |
| `new_experiment/data_generation.py` | py | data_access | 3 | yes |
| `new_experiment/main.py` | py | utility | 6 | yes |
| `new_experiment/test_framework.py` | py | testing | 8 | yes |
| `new_experiment/training.py` | py | utility | 4 | yes |
| `new_experiment/training_dynamics.py` | py | utility | 5 | yes |
| `new_experiment/wandb_integration.py` | py | utility | 5 | yes |

## Key Symbols

- `ICheckpointManager` (class, `new_experiment/checkpointing.py:16`) `class ICheckpointManager(ABC)` - Interface for checkpoint management.
- `save` (method, `new_experiment/checkpointing.py:20`) `def save(self, state, path)` - Save checkpoint and return path.
- `load` (method, `new_experiment/checkpointing.py:25`) `def load(self, path)` - Load checkpoint from path.
- `should_checkpoint` (method, `new_experiment/checkpointing.py:30`) `def should_checkpoint(self)` - Determine if checkpoint should be saved.
- `CheckpointManager` (class, `new_experiment/checkpointing.py:35`) `class CheckpointManager(ICheckpointManager)` - Manage experiment checkpoints with automatic interval-based saving.
- `__init__` (method, `new_experiment/checkpointing.py:43`) `def __init__(self, config)` - Initialize checkpoint manager.
- `save` (method, `new_experiment/checkpointing.py:55`) `def save(self, state, path)` - Save checkpoint to disk.
- `load` (method, `new_experiment/checkpointing.py:85`) `def load(self, path)` - Load checkpoint from disk.
- `should_checkpoint` (method, `new_experiment/checkpointing.py:101`) `def should_checkpoint(self)` - Check if checkpoint interval has elapsed.
- `get_latest_checkpoint_path` (method, `new_experiment/checkpointing.py:111`) `def get_latest_checkpoint_path(self)` - Get path to latest checkpoint if exists.
- `ExperimentConfig` (class, `new_experiment/config.py:13`) `class ExperimentConfig` - Centralized configuration for all experimental parameters.
- `get_adaptive_train_size` (method, `new_experiment/config.py:111`) `def get_adaptive_train_size(self, n_bits)` - Calculate adaptive training size based on input dimensionality.
- `get_adaptive_weight_decay` (method, `new_experiment/config.py:117`) `def get_adaptive_weight_decay(self, n_bits, hidden_dim)` - Calculate adaptive weight decay based on problem complexity.
- `get_adaptive_max_steps` (method, `new_experiment/config.py:126`) `def get_adaptive_max_steps(self, n_bits, hidden_dim)` - Calculate adaptive maximum steps based on problem complexity.
- `ParityDatasetGenerator` (class, `new_experiment/data_generation.py:11`) `class ParityDatasetGenerator` - Generates binary parity learning datasets.
- `__init__` (method, `new_experiment/data_generation.py:19`) `def __init__(self, config)` - Initialize dataset generator.
- `generate` (method, `new_experiment/data_generation.py:28`) `def generate(self, n_bits, k_bits, dataset_size)` - Generate random binary vectors with k-bit parity labels.
- `MultiSeedCurriculumRunner` (class, `new_experiment/main.py:16`) `class MultiSeedCurriculumRunner` - Run curriculum training across multiple random seeds.
- `__init__` (method, `new_experiment/main.py:24`) `def __init__(self, config)` - Initialize runner.
- `_set_seed` (method, `new_experiment/main.py:35`) `def _set_seed(self, seed)` - Set random seed for reproducibility.
- `run_single_seed` (method, `new_experiment/main.py:48`) `def run_single_seed(self, seed)` - Run curriculum for a single seed.
- `run_experiment` (method, `new_experiment/main.py:90`) `def run_experiment(self, start_seed, end_seed)` - Run experiment across multiple seeds.
- `main` (method, `new_experiment/main.py:130`) `def main()` - Main entry point for command-line execution.
- `test_configuration` (function, `new_experiment/test_framework.py:17`) `def test_configuration()` - Test configuration creation and parameter calculation.
- `test_data_generation` (function, `new_experiment/test_framework.py:38`) `def test_data_generation()` - Test dataset generation.
- `test_models` (function, `new_experiment/test_framework.py:53`) `def test_models()` - Test model architectures.
- `test_metrics` (function, `new_experiment/test_framework.py:80`) `def test_metrics()` - Test metric calculation.
- `test_checkpointing` (function, `new_experiment/test_framework.py:119`) `def test_checkpointing()` - Test checkpoint management.
- `test_weight_transfer` (function, `new_experiment/test_framework.py:142`) `def test_weight_transfer()` - Test smart weight transfer.
- `test_stagnation_detection` (function, `new_experiment/test_framework.py:158`) `def test_stagnation_detection()` - Test stagnation detector.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 15
- Cross-boundary resolved imports (EXTRACTED): 10

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: new_experiment/metrics.py imports new_experiment/config.py.
- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (new_experiment: checkpointing) and community 1 (root).
- [INFERRED] shares_context community 0 <-> 3 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (new_experiment: checkpointing) and community 3 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in new_experiment: checkpointing changed?
- Should new_experiment: checkpointing be split, given cohesion 0.60?

## Sources

- `new_experiment/checkpointing.py`
- `new_experiment/config.py`
- `new_experiment/data_generation.py`
- `new_experiment/main.py`
- `new_experiment/test_framework.py`
- `new_experiment/training.py`
- `new_experiment/training_dynamics.py`
- `new_experiment/wandb_integration.py`
