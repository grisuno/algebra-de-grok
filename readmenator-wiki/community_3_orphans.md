# orphans

*Community 3 | 3 files | cohesion 0.00*

## Definition

This community groups 3 file(s) rooted at `root` with dominant language py (cohesion 0.00). Central symbols: `AdaptiveCurriculumTrainer`, `AdaptiveParameterCalculator`, `CheckpointManager`, `ComplexityAnalyzer`, `ComprehensiveMetricsAggregator`, `CurriculumStageTrainer`, `DeltaCalculator`, `ExperimentConfig`. Core file: `realtime_train.py` (72 symbols). Documented purpose: Author: Gris Iscomeback Email: grisiscomeback[at]gmail[dot]com Creation Date: 27/12/2025 License: GPL v3  Description:  Abstract  We demonstrate that binary par.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app_wandb.py` | py | utility | 21 | yes |
| `install.sh` | sh | utility | 0 | no |
| `realtime_train.py` | py | utility | 72 | yes |

## Key Symbols

- `init_wandb` (function, `app_wandb.py:35`) `def init_wandb(project_name, config)` - Initialize wandb tracking
- `log_training_step` (function, `app_wandb.py:43`) `def log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)` - Log metrics to wandb
- `finish_wandb` (function, `app_wandb.py:59`) `def finish_wandb()` - Finish wandb run
- `SuperpositionSAE` (class, `app_wandb.py:63`) `class SuperpositionSAE(Module)`
- `__init__` (method, `app_wandb.py:64`) `def __init__(self, d_model, d_sae)`
- `forward` (method, `app_wandb.py:71`) `def forward(self, x)`
- `get_metrics` (method, `app_wandb.py:76`) `def get_metrics(self, z)`
- `ComplexityAnalyzer` (class, `app_wandb.py:86`) `class ComplexityAnalyzer`
- `measure_lc` (method, `app_wandb.py:88`) `def measure_lc(model, x, epsilon)`
- `GrokkingTransformer` (class, `app_wandb.py:98`) `class GrokkingTransformer(Module)`
- `__init__` (method, `app_wandb.py:99`) `def __init__(self, d_in, d_h)`
- `get_pre_acts` (method, `app_wandb.py:105`) `def get_pre_acts(self, x)`
- `forward` (method, `app_wandb.py:111`) `def forward(self, x)`
- `get_parity_dataset` (method, `app_wandb.py:118`) `def get_parity_dataset(n_bits, k, size)`
- `AdaptiveCurriculumTrainer` (class, `app_wandb.py:123`) `class AdaptiveCurriculumTrainer`
- `__init__` (method, `app_wandb.py:124`) `def __init__(self)`
- `calculate_adaptive_params` (method, `app_wandb.py:140`) `def calculate_adaptive_params(self, n_bits, d_h, stage)` - Calculate adaptive parameters according to stage complexity
- `smart_weight_transfer` (method, `app_wandb.py:157`) `def smart_weight_transfer(self, prev_model, new_model, stage)` - Intelligent weight transfer with padding/interpolation
- `detect_stagnation` (method, `app_wandb.py:196`) `def detect_stagnation(self, history, current_lc, d_h, step)` - Detect if model is stagnant and needs restart
- `train_stage` (method, `app_wandb.py:212`) `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` - Train individual stage with adaptive parameters
- `run_curriculum` (method, `app_wandb.py:345`) `def run_curriculum(self)` - Execute complete curriculum with automatic adaptation
- `ExperimentConfig` (class, `realtime_train.py:63`) `class ExperimentConfig` - Immutable configuration for thermodynamic grokking experiments.
- `IMetricCalculator` (class, `realtime_train.py:130`) `class IMetricCalculator(ABC)` - Interface for metric calculation strategies.
- `calculate` (method, `realtime_train.py:134`) `def calculate(self)` - Calculate metrics and return dictionary of results.
- `IModelArchitecture` (class, `realtime_train.py:139`) `class IModelArchitecture(ABC)` - Interface for neural network architectures.
- `forward` (method, `realtime_train.py:143`) `def forward(self, x)` - Forward pass returning logits and latent representation.
- `get_pre_activations` (method, `realtime_train.py:148`) `def get_pre_activations(self, x)` - Get pre-activation tensors for complexity analysis.
- `get_flat_parameters` (method, `realtime_train.py:153`) `def get_flat_parameters(self)` - Get flattened parameter vector.
- `ICheckpointManager` (class, `realtime_train.py:158`) `class ICheckpointManager(ABC)` - Interface for checkpoint management.
- `save` (method, `realtime_train.py:162`) `def save(self, state, path)` - Save checkpoint and return path.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 3 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (new_experiment: checkpointing) and community 3 (orphans).
- [INFERRED] shares_context community 1 <-> 3 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (root) and community 3 (orphans).
- [INFERRED] shares_context community 2 <-> 3 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (new_experiment: purity_analysis) and community 3 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `app_wandb.py`
- `install.sh`
- `realtime_train.py`
