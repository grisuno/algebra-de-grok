# new_experiment: purity_analysis

*Community 2 | 4 files | cohesion 0.29*

## Definition

This community groups 4 file(s) rooted at `new_experiment` with dominant language py (cohesion 0.29). Central symbols: `CheckpointLoader`, `ComprehensiveMetricsAggregator`, `DeltaCalculator`, `EffectiveTemperatureCalculator`, `GradientCovarianceCalculator`, `GrokkingTransformer`, `IEffectiveTemperatureCalculator`, `IMetricCalculator`. Core file: `purity_analysis.py` (50 symbols). Documented purpose: Metrics calculation module for thermodynamic and learning analysis..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `new_experiment/metrics.py` | py | utility | 20 | yes |
| `new_experiment/models.py` | py | business_logic | 13 | yes |
| `new_experiment/streamlit_app.py` | py | utility | 10 | yes |
| `purity_analysis.py` | py | utility | 50 | yes |

## Key Symbols

- `IMetricCalculator` (class, `new_experiment/metrics.py:17`) `class IMetricCalculator(ABC)` - Interface for metric calculation strategies.
- `calculate` (method, `new_experiment/metrics.py:21`) `def calculate(self)` - Calculate metrics and return dictionary of results.
- `LocalComplexityCalculator` (class, `new_experiment/metrics.py:26`) `class LocalComplexityCalculator(IMetricCalculator)` - Calculate local complexity as effective local dimensionality.
- `__init__` (method, `new_experiment/metrics.py:34`) `def __init__(self, config)` - Initialize calculator.
- `calculate` (method, `new_experiment/metrics.py:44`) `def calculate(self, model, x_batch)` - Measure LC as count of near-zero pre-activations.
- `GradientCovarianceCalculator` (class, `new_experiment/metrics.py:81`) `class GradientCovarianceCalculator` - Calculate gradient covariance matrix and condition number.
- `__init__` (method, `new_experiment/metrics.py:90`) `def __init__(self, config)` - Initialize calculator.
- `accumulate_gradient` (method, `new_experiment/metrics.py:102`) `def accumulate_gradient(self, model)` - Store current gradient vector.
- `calculate_kappa` (method, `new_experiment/metrics.py:121`) `def calculate_kappa(self)` - Calculate condition number of gradient covariance matrix.
- `reset` (method, `new_experiment/metrics.py:161`) `def reset(self)` - Clear gradient buffer.
- `ThermodynamicMetricsCalculator` (class, `new_experiment/metrics.py:166`) `class ThermodynamicMetricsCalculator(IMetricCalculator)` - Calculate thermodynamic metrics: effective temperature and Planck constant.
- `__init__` (method, `new_experiment/metrics.py:174`) `def __init__(self, config)` - Initialize calculator.
- `calculate` (method, `new_experiment/metrics.py:183`) `def calculate(self, gradient_covariance)` - Calculate effective temperature and Planck constant.
- `DeltaCalculator` (class, `new_experiment/metrics.py:253`) `class DeltaCalculator(IMetricCalculator)` - Calculate discretization margin delta.
- `calculate` (method, `new_experiment/metrics.py:261`) `def calculate(self, model)` - Calculate mean squared distance to nearest integer.
- `ComprehensiveMetricsAggregator` (class, `new_experiment/metrics.py:282`) `class ComprehensiveMetricsAggregator` - Aggregate all thermodynamic and learning metrics.
- `__init__` (method, `new_experiment/metrics.py:289`) `def __init__(self, config)` - Initialize aggregator.
- `compute_all_metrics` (method, `new_experiment/metrics.py:302`) `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loade` - Compute comprehensive metric suite.
- `accumulate_gradient` (method, `new_experiment/metrics.py:374`) `def accumulate_gradient(self, model)` - Accumulate gradient for kappa calculation.
- `reset` (method, `new_experiment/metrics.py:383`) `def reset(self)` - Reset all stateful calculators.
- `IModelArchitecture` (class, `new_experiment/models.py:14`) `class IModelArchitecture(ABC)` - Interface for neural network architectures.
- `forward` (method, `new_experiment/models.py:18`) `def forward(self, x)` - Forward pass returning logits and latent representation.
- `get_pre_activations` (method, `new_experiment/models.py:23`) `def get_pre_activations(self, x)` - Get pre-activation tensors for complexity analysis.
- `get_flat_parameters` (method, `new_experiment/models.py:28`) `def get_flat_parameters(self)` - Get flattened parameter vector.
- `GrokkingTransformer` (class, `new_experiment/models.py:33`) `class GrokkingTransformer(Module, IModelArchitecture)` - Two-layer MLP for parity learning experiments.
- `__init__` (method, `new_experiment/models.py:41`) `def __init__(self, input_dim, hidden_dim, output_dim)` - Initialize network.
- `get_pre_activations` (method, `new_experiment/models.py:59`) `def get_pre_activations(self, x)` - Get pre-activation tensors for local complexity calculation.
- `forward` (method, `new_experiment/models.py:74`) `def forward(self, x)` - Forward pass through network.
- `get_flat_parameters` (method, `new_experiment/models.py:91`) `def get_flat_parameters(self)` - Get flattened parameter vector.
- `SuperpositionSAE` (class, `new_experiment/models.py:101`) `class SuperpositionSAE(Module)` - Sparse Autoencoder for superposition analysis.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 4
- Cross-boundary resolved imports (EXTRACTED): 10

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: new_experiment/metrics.py imports new_experiment/config.py.
- [INFERRED] shares_context community 1 <-> 2 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (root) and community 2 (new_experiment: purity_analysis).
- [INFERRED] shares_context community 2 <-> 3 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (new_experiment: purity_analysis) and community 3 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in new_experiment: purity_analysis changed?
- Should new_experiment: purity_analysis be split, given cohesion 0.29?

## Sources

- `new_experiment/metrics.py`
- `new_experiment/models.py`
- `new_experiment/streamlit_app.py`
- `purity_analysis.py`
