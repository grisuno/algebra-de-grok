# Subsystem: new_experiment

## new_experiment/checkpointing.py
- Layer: utility
- Language: py
- Symbols:
  - `ICheckpointManager` (class, line 16) `class ICheckpointManager(ABC)`
  - `CheckpointManager` (class, line 35) `class CheckpointManager(ICheckpointManager)`
  - `save` (method, line 20) `def save(self, state, path)`
  - `load` (method, line 25) `def load(self, path)`
  - `should_checkpoint` (method, line 30) `def should_checkpoint(self)`
  - `__init__` (method, line 43) `def __init__(self, config)`
  - `save` (method, line 55) `def save(self, state, path)`
  - `load` (method, line 85) `def load(self, path)`
  - `should_checkpoint` (method, line 101) `def should_checkpoint(self)`
  - `get_latest_checkpoint_path` (method, line 111) `def get_latest_checkpoint_path(self)`
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/config.py
- Layer: infrastructure
- Language: py
- Symbols:
  - `ExperimentConfig` (class, line 13) `class ExperimentConfig`
  - `get_adaptive_train_size` (method, line 111) `def get_adaptive_train_size(self, n_bits)`
  - `get_adaptive_weight_decay` (method, line 117) `def get_adaptive_weight_decay(self, n_bits, hidden_dim)`
  - `get_adaptive_max_steps` (method, line 126) `def get_adaptive_max_steps(self, n_bits, hidden_dim)`
- Imported by: `new_experiment/checkpointing.py`, `new_experiment/data_generation.py`, `new_experiment/main.py`, `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`, `purity_analysis.py`

## new_experiment/data_generation.py
- Layer: data_access
- Language: py
- Symbols:
  - `ParityDatasetGenerator` (class, line 11) `class ParityDatasetGenerator`
  - `__init__` (method, line 19) `def __init__(self, config)`
  - `generate` (method, line 28) `def generate(self, n_bits, k_bits, dataset_size)`
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/main.py
- Layer: utility
- Language: py
- Symbols:
  - `MultiSeedCurriculumRunner` (class, line 16) `class MultiSeedCurriculumRunner`
  - `main` (method, line 130) `def main()`
  - `__init__` (method, line 24) `def __init__(self, config)`
  - `_set_seed` (method, line 35) `def _set_seed(self, seed)`
  - `run_single_seed` (method, line 48) `def run_single_seed(self, seed)`
  - `run_experiment` (method, line 90) `def run_experiment(self, start_seed, end_seed)`
- Depends on: `new_experiment/config.py`, `new_experiment/training.py`

## new_experiment/metrics.py
- Layer: utility
- Language: py
- Symbols:
  - `IMetricCalculator` (class, line 17) `class IMetricCalculator(ABC)`
  - `LocalComplexityCalculator` (class, line 26) `class LocalComplexityCalculator(IMetricCalculator)`
  - `GradientCovarianceCalculator` (class, line 81) `class GradientCovarianceCalculator`
  - `ThermodynamicMetricsCalculator` (class, line 166) `class ThermodynamicMetricsCalculator(IMetricCalculator)`
  - `DeltaCalculator` (class, line 253) `class DeltaCalculator(IMetricCalculator)`
  - `ComprehensiveMetricsAggregator` (class, line 282) `class ComprehensiveMetricsAggregator`
  - `calculate` (method, line 21) `def calculate(self)`
  - `__init__` (method, line 34) `def __init__(self, config)`
  - `calculate` (method, line 44) `def calculate(self, model, x_batch)`
  - `__init__` (method, line 90) `def __init__(self, config)`
  - `accumulate_gradient` (method, line 102) `def accumulate_gradient(self, model)`
  - `calculate_kappa` (method, line 121) `def calculate_kappa(self)`
  - `reset` (method, line 161) `def reset(self)`
  - `__init__` (method, line 174) `def __init__(self, config)`
  - `calculate` (method, line 183) `def calculate(self, gradient_covariance)`
  - `calculate` (method, line 261) `def calculate(self, model)`
  - `__init__` (method, line 289) `def __init__(self, config)`
  - `compute_all_metrics` (method, line 302) `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, step)`
  - `accumulate_gradient` (method, line 374) `def accumulate_gradient(self, model)`
  - `reset` (method, line 383) `def reset(self)`
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/models.py
- Layer: business_logic
- Language: py
- Symbols:
  - `IModelArchitecture` (class, line 14) `class IModelArchitecture(ABC)`
  - `GrokkingTransformer` (class, line 33) `class GrokkingTransformer(Module, IModelArchitecture)`
  - `SuperpositionSAE` (class, line 101) `class SuperpositionSAE(Module)`
  - `forward` (method, line 18) `def forward(self, x)`
  - `get_pre_activations` (method, line 23) `def get_pre_activations(self, x)`
  - `get_flat_parameters` (method, line 28) `def get_flat_parameters(self)`
  - `__init__` (method, line 41) `def __init__(self, input_dim, hidden_dim, output_dim)`
  - `get_pre_activations` (method, line 59) `def get_pre_activations(self, x)`
  - `forward` (method, line 74) `def forward(self, x)`
  - `get_flat_parameters` (method, line 91) `def get_flat_parameters(self)`
  - `__init__` (method, line 109) `def __init__(self, model_dim, sae_dim)`
  - `forward` (method, line 126) `def forward(self, x)`
  - `compute_superposition_metrics` (method, line 140) `def compute_superposition_metrics(self, z_encoded)`
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

## new_experiment/streamlit_app.py
- Layer: utility
- Language: py
- Symbols:
  - `ThermodynamicAnalyzer` (class, line 75) `class ThermodynamicAnalyzer`
  - `StreamlitTrainer` (class, line 143) `class StreamlitTrainer`
  - `main` (method, line 596) `def main()`
  - `compute_metrics` (method, line 79) `def compute_metrics(weights_list, phase, epoch)`
  - `__init__` (method, line 146) `def __init__(self, config)`
  - `train_stage_with_visualization` (method, line 163) `def train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)`
  - `_create_3d_visualization` (method, line 424) `def _create_3d_visualization(self, weights_list, phase_name, thermo_metrics)`
  - `_create_2d_visualization` (method, line 478) `def _create_2d_visualization(self, weights_list, phase_name, thermo_metrics)`
  - `_create_metrics_plot` (method, line 526) `def _create_metrics_plot(self, history, phase_name)`
  - `run_curriculum` (method, line 570) `def run_curriculum(self)`
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

## new_experiment/test_framework.py
- Layer: testing
- Language: py
- Symbols:
  - `test_configuration` (function, line 17) `def test_configuration()`
  - `test_data_generation` (function, line 38) `def test_data_generation()`
  - `test_models` (function, line 53) `def test_models()`
  - `test_metrics` (function, line 80) `def test_metrics()`
  - `test_checkpointing` (function, line 119) `def test_checkpointing()`
  - `test_weight_transfer` (function, line 142) `def test_weight_transfer()`
  - `test_stagnation_detection` (function, line 158) `def test_stagnation_detection()`
  - `run_all_tests` (function, line 178) `def run_all_tests()`
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

## new_experiment/training.py
- Layer: utility
- Language: py
- Symbols:
  - `CurriculumStageTrainer` (class, line 21) `class CurriculumStageTrainer`
  - `__init__` (method, line 29) `def __init__(self, config, seed)`
  - `train_stage` (method, line 48) `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)`
  - `_create_checkpoint_state` (method, line 289) `def _create_checkpoint_state(self, model, sae, optimizer, stage, n_bits, hidden_dim, step, metrics_history)`
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`
- Imported by: `new_experiment/main.py`

## new_experiment/training_dynamics.py
- Layer: utility
- Language: py
- Symbols:
  - `SmartWeightTransfer` (class, line 13) `class SmartWeightTransfer`
  - `StagnationDetector` (class, line 83) `class StagnationDetector`
  - `transfer` (method, line 21) `def transfer(self, previous_model, new_model, stage)`
  - `__init__` (method, line 91) `def __init__(self, config)`
  - `is_stagnant` (method, line 101) `def is_stagnant(self, metrics_history, current_step, hidden_dim)`
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/wandb_integration.py
- Layer: utility
- Language: py
- Symbols:
  - `WandBLogger` (class, line 12) `class WandBLogger`
  - `__init__` (method, line 19) `def __init__(self, config)`
  - `initialize` (method, line 30) `def initialize(self, run_name, run_config)`
  - `log_metrics` (method, line 58) `def log_metrics(self, metrics, step)`
  - `finish` (method, line 77) `def finish(self)`
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/training.py`
