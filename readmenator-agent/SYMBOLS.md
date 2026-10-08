# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `evaluate` | function | `128bits.py:34` | `def evaluate(model, x, y)` |
| `load_64bit_model` | function | `128bits.py:39` | `def load_64bit_model()` |
| `run_experiment` | function | `128bits.py:49` | `def run_experiment(use_padding)` |
| `evaluate` | function | `2048bits.py:44` | `def evaluate(model, x, y)` |
| `load_base_model` | function | `2048bits.py:49` | `def load_base_model()` |
| `zero_shot_test` | function | `2048bits.py:59` | `def zero_shot_test(prev_model, n_bits, d_h, use_padding)` |
| `AdaptiveCurriculumTrainer` | class | `app.py:92` | `class AdaptiveCurriculumTrainer` |
| `ComplexityAnalyzer` | class | `app.py:55` | `class ComplexityAnalyzer` |
| `GrokkingTransformer` | class | `app.py:67` | `class GrokkingTransformer(Module)` |
| `SuperpositionSAE` | class | `app.py:32` | `class SuperpositionSAE(Module)` |
| `__init__` | method | `app.py:33` | `def __init__(self, d_model, d_sae)` |
| `__init__` | method | `app.py:68` | `def __init__(self, d_in, d_h)` |
| `__init__` | method | `app.py:93` | `def __init__(self)` |
| `calculate_adaptive_params` | method | `app.py:109` | `def calculate_adaptive_params(self, n_bits, d_h, stage)` |
| `detect_stagnation` | method | `app.py:166` | `def detect_stagnation(self, history, current_lc, d_h, step)` |
| `forward` | method | `app.py:40` | `def forward(self, x)` |
| `forward` | method | `app.py:80` | `def forward(self, x)` |
| `get_metrics` | method | `app.py:45` | `def get_metrics(self, z)` |
| `get_parity_dataset` | method | `app.py:87` | `def get_parity_dataset(n_bits, k, size)` |
| `get_pre_acts` | method | `app.py:74` | `def get_pre_acts(self, x)` |
| `measure_lc` | method | `app.py:57` | `def measure_lc(model, x, epsilon)` |
| `run_curriculum` | method | `app.py:316` | `def run_curriculum(self)` |
| `smart_weight_transfer` | method | `app.py:126` | `def smart_weight_transfer(self, prev_model, new_model, stage)` |
| `train_stage` | method | `app.py:184` | `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` |
| `AdaptiveCurriculumTrainer` | class | `app_wandb.py:123` | `class AdaptiveCurriculumTrainer` |
| `ComplexityAnalyzer` | class | `app_wandb.py:86` | `class ComplexityAnalyzer` |
| `GrokkingTransformer` | class | `app_wandb.py:98` | `class GrokkingTransformer(Module)` |
| `SuperpositionSAE` | class | `app_wandb.py:63` | `class SuperpositionSAE(Module)` |
| `__init__` | method | `app_wandb.py:64` | `def __init__(self, d_model, d_sae)` |
| `__init__` | method | `app_wandb.py:99` | `def __init__(self, d_in, d_h)` |
| `__init__` | method | `app_wandb.py:124` | `def __init__(self)` |
| `calculate_adaptive_params` | method | `app_wandb.py:140` | `def calculate_adaptive_params(self, n_bits, d_h, stage)` |
| `detect_stagnation` | method | `app_wandb.py:196` | `def detect_stagnation(self, history, current_lc, d_h, step)` |
| `finish_wandb` | function | `app_wandb.py:59` | `def finish_wandb()` |
| `forward` | method | `app_wandb.py:71` | `def forward(self, x)` |
| `forward` | method | `app_wandb.py:111` | `def forward(self, x)` |
| `get_metrics` | method | `app_wandb.py:76` | `def get_metrics(self, z)` |
| `get_parity_dataset` | method | `app_wandb.py:118` | `def get_parity_dataset(n_bits, k, size)` |
| `get_pre_acts` | method | `app_wandb.py:105` | `def get_pre_acts(self, x)` |
| `init_wandb` | function | `app_wandb.py:35` | `def init_wandb(project_name, config)` |
| `log_training_step` | function | `app_wandb.py:43` | `def log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)` |
| `measure_lc` | method | `app_wandb.py:88` | `def measure_lc(model, x, epsilon)` |
| `run_curriculum` | method | `app_wandb.py:345` | `def run_curriculum(self)` |
| `smart_weight_transfer` | method | `app_wandb.py:157` | `def smart_weight_transfer(self, prev_model, new_model, stage)` |
| `train_stage` | method | `app_wandb.py:212` | `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` |
| `CheckpointManager` | class | `new_experiment/checkpointing.py:35` | `class CheckpointManager(ICheckpointManager)` |
| `ICheckpointManager` | class | `new_experiment/checkpointing.py:16` | `class ICheckpointManager(ABC)` |
| `__init__` | method | `new_experiment/checkpointing.py:43` | `def __init__(self, config)` |
| `get_latest_checkpoint_path` | method | `new_experiment/checkpointing.py:111` | `def get_latest_checkpoint_path(self)` |
| `load` | method | `new_experiment/checkpointing.py:25` | `def load(self, path)` |
| `load` | method | `new_experiment/checkpointing.py:85` | `def load(self, path)` |
| `save` | method | `new_experiment/checkpointing.py:20` | `def save(self, state, path)` |
| `save` | method | `new_experiment/checkpointing.py:55` | `def save(self, state, path)` |
| `should_checkpoint` | method | `new_experiment/checkpointing.py:30` | `def should_checkpoint(self)` |
| `should_checkpoint` | method | `new_experiment/checkpointing.py:101` | `def should_checkpoint(self)` |
| `ExperimentConfig` | class | `new_experiment/config.py:13` | `class ExperimentConfig` |
| `get_adaptive_max_steps` | method | `new_experiment/config.py:126` | `def get_adaptive_max_steps(self, n_bits, hidden_dim)` |
| `get_adaptive_train_size` | method | `new_experiment/config.py:111` | `def get_adaptive_train_size(self, n_bits)` |
| `get_adaptive_weight_decay` | method | `new_experiment/config.py:117` | `def get_adaptive_weight_decay(self, n_bits, hidden_dim)` |
| `ParityDatasetGenerator` | class | `new_experiment/data_generation.py:11` | `class ParityDatasetGenerator` |
| `__init__` | method | `new_experiment/data_generation.py:19` | `def __init__(self, config)` |
| `generate` | method | `new_experiment/data_generation.py:28` | `def generate(self, n_bits, k_bits, dataset_size)` |
| `MultiSeedCurriculumRunner` | class | `new_experiment/main.py:16` | `class MultiSeedCurriculumRunner` |
| `__init__` | method | `new_experiment/main.py:24` | `def __init__(self, config)` |
| `_set_seed` | method | `new_experiment/main.py:35` | `def _set_seed(self, seed)` |
| `main` | method | `new_experiment/main.py:130` | `def main()` |
| `run_experiment` | method | `new_experiment/main.py:90` | `def run_experiment(self, start_seed, end_seed)` |
| `run_single_seed` | method | `new_experiment/main.py:48` | `def run_single_seed(self, seed)` |
| `ComprehensiveMetricsAggregator` | class | `new_experiment/metrics.py:282` | `class ComprehensiveMetricsAggregator` |
| `DeltaCalculator` | class | `new_experiment/metrics.py:253` | `class DeltaCalculator(IMetricCalculator)` |
| `GradientCovarianceCalculator` | class | `new_experiment/metrics.py:81` | `class GradientCovarianceCalculator` |
| `IMetricCalculator` | class | `new_experiment/metrics.py:17` | `class IMetricCalculator(ABC)` |
| `LocalComplexityCalculator` | class | `new_experiment/metrics.py:26` | `class LocalComplexityCalculator(IMetricCalculator)` |
| `ThermodynamicMetricsCalculator` | class | `new_experiment/metrics.py:166` | `class ThermodynamicMetricsCalculator(IMetricCalculator)` |
| `__init__` | method | `new_experiment/metrics.py:34` | `def __init__(self, config)` |
| `__init__` | method | `new_experiment/metrics.py:90` | `def __init__(self, config)` |
| `__init__` | method | `new_experiment/metrics.py:174` | `def __init__(self, config)` |
| `__init__` | method | `new_experiment/metrics.py:289` | `def __init__(self, config)` |
| `accumulate_gradient` | method | `new_experiment/metrics.py:102` | `def accumulate_gradient(self, model)` |
| `accumulate_gradient` | method | `new_experiment/metrics.py:374` | `def accumulate_gradient(self, model)` |
| `calculate` | method | `new_experiment/metrics.py:21` | `def calculate(self)` |
| `calculate` | method | `new_experiment/metrics.py:44` | `def calculate(self, model, x_batch)` |
| `calculate` | method | `new_experiment/metrics.py:183` | `def calculate(self, gradient_covariance)` |
| `calculate` | method | `new_experiment/metrics.py:261` | `def calculate(self, model)` |
| `calculate_kappa` | method | `new_experiment/metrics.py:121` | `def calculate_kappa(self)` |
| `compute_all_metrics` | method | `new_experiment/metrics.py:302` | `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, ste` |
| `reset` | method | `new_experiment/metrics.py:161` | `def reset(self)` |
| `reset` | method | `new_experiment/metrics.py:383` | `def reset(self)` |
| `GrokkingTransformer` | class | `new_experiment/models.py:33` | `class GrokkingTransformer(Module, IModelArchitecture)` |
| `IModelArchitecture` | class | `new_experiment/models.py:14` | `class IModelArchitecture(ABC)` |
| `SuperpositionSAE` | class | `new_experiment/models.py:101` | `class SuperpositionSAE(Module)` |
| `__init__` | method | `new_experiment/models.py:41` | `def __init__(self, input_dim, hidden_dim, output_dim)` |
| `__init__` | method | `new_experiment/models.py:109` | `def __init__(self, model_dim, sae_dim)` |
| `compute_superposition_metrics` | method | `new_experiment/models.py:140` | `def compute_superposition_metrics(self, z_encoded)` |
| `forward` | method | `new_experiment/models.py:18` | `def forward(self, x)` |
| `forward` | method | `new_experiment/models.py:74` | `def forward(self, x)` |
| `forward` | method | `new_experiment/models.py:126` | `def forward(self, x)` |
| `get_flat_parameters` | method | `new_experiment/models.py:28` | `def get_flat_parameters(self)` |
| `get_flat_parameters` | method | `new_experiment/models.py:91` | `def get_flat_parameters(self)` |
| `get_pre_activations` | method | `new_experiment/models.py:23` | `def get_pre_activations(self, x)` |
| `get_pre_activations` | method | `new_experiment/models.py:59` | `def get_pre_activations(self, x)` |
| `StreamlitTrainer` | class | `new_experiment/streamlit_app.py:143` | `class StreamlitTrainer` |
| `ThermodynamicAnalyzer` | class | `new_experiment/streamlit_app.py:75` | `class ThermodynamicAnalyzer` |
| `__init__` | method | `new_experiment/streamlit_app.py:146` | `def __init__(self, config)` |
| `_create_2d_visualization` | method | `new_experiment/streamlit_app.py:478` | `def _create_2d_visualization(self, weights_list, phase_name, thermo_metrics)` |
| `_create_3d_visualization` | method | `new_experiment/streamlit_app.py:424` | `def _create_3d_visualization(self, weights_list, phase_name, thermo_metrics)` |
| `_create_metrics_plot` | method | `new_experiment/streamlit_app.py:526` | `def _create_metrics_plot(self, history, phase_name)` |
| `compute_metrics` | method | `new_experiment/streamlit_app.py:79` | `def compute_metrics(weights_list, phase, epoch)` |
| `main` | method | `new_experiment/streamlit_app.py:596` | `def main()` |
| `run_curriculum` | method | `new_experiment/streamlit_app.py:570` | `def run_curriculum(self)` |
| `train_stage_with_visualization` | method | `new_experiment/streamlit_app.py:163` | `def train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` |
| `run_all_tests` | function | `new_experiment/test_framework.py:178` | `def run_all_tests()` |
| `test_checkpointing` | function | `new_experiment/test_framework.py:119` | `def test_checkpointing()` |
| `test_configuration` | function | `new_experiment/test_framework.py:17` | `def test_configuration()` |
| `test_data_generation` | function | `new_experiment/test_framework.py:38` | `def test_data_generation()` |
| `test_metrics` | function | `new_experiment/test_framework.py:80` | `def test_metrics()` |
| `test_models` | function | `new_experiment/test_framework.py:53` | `def test_models()` |
| `test_stagnation_detection` | function | `new_experiment/test_framework.py:158` | `def test_stagnation_detection()` |
| `test_weight_transfer` | function | `new_experiment/test_framework.py:142` | `def test_weight_transfer()` |
| `CurriculumStageTrainer` | class | `new_experiment/training.py:21` | `class CurriculumStageTrainer` |
| `__init__` | method | `new_experiment/training.py:29` | `def __init__(self, config, seed)` |
| `_create_checkpoint_state` | method | `new_experiment/training.py:289` | `def _create_checkpoint_state(self, model, sae, optimizer, stage, n_bits, hidden_dim, step, metrics_history)` |
| `train_stage` | method | `new_experiment/training.py:48` | `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` |
| `SmartWeightTransfer` | class | `new_experiment/training_dynamics.py:13` | `class SmartWeightTransfer` |
| `StagnationDetector` | class | `new_experiment/training_dynamics.py:83` | `class StagnationDetector` |
| `__init__` | method | `new_experiment/training_dynamics.py:91` | `def __init__(self, config)` |
| `is_stagnant` | method | `new_experiment/training_dynamics.py:101` | `def is_stagnant(self, metrics_history, current_step, hidden_dim)` |
| `transfer` | method | `new_experiment/training_dynamics.py:21` | `def transfer(self, previous_model, new_model, stage)` |
| `WandBLogger` | class | `new_experiment/wandb_integration.py:12` | `class WandBLogger` |
| `__init__` | method | `new_experiment/wandb_integration.py:19` | `def __init__(self, config)` |
| `finish` | method | `new_experiment/wandb_integration.py:77` | `def finish(self)` |
| `initialize` | method | `new_experiment/wandb_integration.py:30` | `def initialize(self, run_name, run_config)` |
| `log_metrics` | method | `new_experiment/wandb_integration.py:58` | `def log_metrics(self, metrics, step)` |
| `CheckpointLoader` | class | `purity_analysis.py:576` | `class CheckpointLoader` |
| `EffectiveTemperatureCalculator` | class | `purity_analysis.py:235` | `class EffectiveTemperatureCalculator` |
| `IEffectiveTemperatureCalculator` | class | `purity_analysis.py:63` | `class IEffectiveTemperatureCalculator(Protocol)` |
| `IModel` | class | `purity_analysis.py:49` | `class IModel(Protocol)` |
| `IPhaseClassifier` | class | `purity_analysis.py:70` | `class IPhaseClassifier(Protocol)` |
| `IPolycrystalAnalyzer` | class | `purity_analysis.py:77` | `class IPolycrystalAnalyzer(Protocol)` |
| `IPurityComparator` | class | `purity_analysis.py:88` | `class IPurityComparator(Protocol)` |
| `IPurityIndexCalculator` | class | `purity_analysis.py:56` | `class IPurityIndexCalculator(Protocol)` |
| `PhaseClassifier` | class | `purity_analysis.py:314` | `class PhaseClassifier` |
| `PolycrystalAnalyzer` | class | `purity_analysis.py:393` | `class PolycrystalAnalyzer` |
| `PurityAnalyzer` | class | `purity_analysis.py:643` | `class PurityAnalyzer` |
| `PurityComparator` | class | `purity_analysis.py:501` | `class PurityComparator` |
| `PurityConfig` | class | `purity_analysis.py:25` | `class PurityConfig` |
| `PurityIndexCalculator` | class | `purity_analysis.py:98` | `class PurityIndexCalculator` |
| `PurityPipeline` | class | `purity_analysis.py:818` | `class PurityPipeline` |
| `__init__` | method | `purity_analysis.py:105` | `def __init__(self, config)` |
| `__init__` | method | `purity_analysis.py:242` | `def __init__(self, config)` |
| `__init__` | method | `purity_analysis.py:321` | `def __init__(self, config)` |
| `__init__` | method | `purity_analysis.py:400` | `def __init__(self, config)` |
| `__init__` | method | `purity_analysis.py:508` | `def __init__(self, config)` |
| `__init__` | method | `purity_analysis.py:583` | `def __init__(self, config)` |
| `__init__` | method | `purity_analysis.py:650` | `def __init__(self, checkpoint_path, experiment_config, purity_config)` |
| `__init__` | method | `purity_analysis.py:825` | `def __init__(self, experiment_config, purity_config)` |
| `_assess_purity_quality` | method | `purity_analysis.py:191` | `def _assess_purity_quality(self, alpha, variance)` |
| `_assess_structural_integrity` | method | `purity_analysis.py:480` | `def _assess_structural_integrity(self, alpha, pruning_level)` |
| `_compute_crystallization_score` | method | `purity_analysis.py:215` | `def _compute_crystallization_score(self, alpha, variance)` |
| `_compute_layer_purity` | method | `purity_analysis.py:159` | `def _compute_layer_purity(self, weights)` |
| `_delta_to_alpha` | method | `purity_analysis.py:177` | `def _delta_to_alpha(self, delta)` |
| `_generate_text_report` | method | `purity_analysis.py:996` | `def _generate_text_report(self, summary, output_dir)` |
| `_load_checkpoint` | method | `purity_analysis.py:677` | `def _load_checkpoint(self)` |
| `_print_report` | method | `purity_analysis.py:759` | `def _print_report(self, results)` |
| `_prune_model` | method | `purity_analysis.py:461` | `def _prune_model(self, model, sparsity)` |
| `analyze` | method | `purity_analysis.py:694` | `def analyze(self)` |
| `analyze_polycrystal` | method | `purity_analysis.py:80` | `def analyze_polycrystal(self, model, pruning_level)` |
| `analyze_polycrystal` | method | `purity_analysis.py:412` | `def analyze_polycrystal(self, model, pruning_level, loss_history)` |
| `calculate` | method | `purity_analysis.py:59` | `def calculate(self, model)` |
| `calculate` | method | `purity_analysis.py:66` | `def calculate(self, loss_history)` |
| `calculate` | method | `purity_analysis.py:114` | `def calculate(self, model)` |
| `calculate` | method | `purity_analysis.py:251` | `def calculate(self, loss_history)` |
| `classify` | method | `purity_analysis.py:73` | `def classify(self, alpha, temperature)` |
| `classify` | method | `purity_analysis.py:330` | `def classify(self, alpha, temperature)` |
| `classify_polycrystal_state` | method | `purity_analysis.py:359` | `def classify_polycrystal_state(self, original_alpha, original_temp, poly_alpha, poly_temp)` |
| `compare` | method | `purity_analysis.py:91` | `def compare(self, original, polycrystal)` |
| `compare` | method | `purity_analysis.py:518` | `def compare(self, original, polycrystal)` |
| `generate_summary` | method | `purity_analysis.py:917` | `def generate_summary(self, all_results, output_dir)` |
| `get_flat_parameters` | method | `purity_analysis.py:52` | `def get_flat_parameters(self)` |
| `load` | method | `purity_analysis.py:592` | `def load(self, checkpoint_path)` |
| `main` | method | `purity_analysis.py:1049` | `def main()` |
| `process_checkpoint` | method | `purity_analysis.py:840` | `def process_checkpoint(self, checkpoint_path, output_dir)` |
| `process_directory` | method | `purity_analysis.py:874` | `def process_directory(self, checkpoint_dir, n_latest, output_dir)` |
| `AdaptiveParameterCalculator` | class | `realtime_train.py:630` | `class AdaptiveParameterCalculator` |
| `CheckpointManager` | class | `realtime_train.py:497` | `class CheckpointManager(ICheckpointManager)` |
| `ComprehensiveMetricsAggregator` | class | `realtime_train.py:424` | `class ComprehensiveMetricsAggregator` |
| `CurriculumStageTrainer` | class | `realtime_train.py:665` | `class CurriculumStageTrainer` |
| `DeltaCalculator` | class | `realtime_train.py:412` | `class DeltaCalculator(IMetricCalculator)` |
| `ExperimentConfig` | class | `realtime_train.py:63` | `class ExperimentConfig` |
| `GradientCovarianceCalculator` | class | `realtime_train.py:288` | `class GradientCovarianceCalculator` |
| `GrokkingTransformer` | class | `realtime_train.py:177` | `class GrokkingTransformer(Module, IModelArchitecture)` |
| `ICheckpointManager` | class | `realtime_train.py:158` | `class ICheckpointManager(ABC)` |
| `IMetricCalculator` | class | `realtime_train.py:130` | `class IMetricCalculator(ABC)` |
| `IModelArchitecture` | class | `realtime_train.py:139` | `class IModelArchitecture(ABC)` |
| `LocalComplexityCalculator` | class | `realtime_train.py:259` | `class LocalComplexityCalculator(IMetricCalculator)` |
| `MultiSeedCurriculumRunner` | class | `realtime_train.py:1367` | `class MultiSeedCurriculumRunner` |
| `ParityDatasetGenerator` | class | `realtime_train.py:245` | `class ParityDatasetGenerator` |
| `ResultsAnalyzer` | class | `realtime_train.py:898` | `class ResultsAnalyzer` |
| `ResultsVisualizer` | class | `realtime_train.py:1157` | `class ResultsVisualizer` |
| `SmartWeightTransfer` | class | `realtime_train.py:579` | `class SmartWeightTransfer` |
| `StagnationDetector` | class | `realtime_train.py:543` | `class StagnationDetector` |
| `SuperpositionSAE` | class | `realtime_train.py:211` | `class SuperpositionSAE(Module)` |
| `ThermodynamicMetricsCalculator` | class | `realtime_train.py:349` | `class ThermodynamicMetricsCalculator(IMetricCalculator)` |
| `__init__` | method | `realtime_train.py:180` | `def __init__(self, input_dim, hidden_dim, output_dim)` |
| `__init__` | method | `realtime_train.py:214` | `def __init__(self, model_dim, sae_dim)` |
| `__init__` | method | `realtime_train.py:248` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:262` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:291` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:352` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:427` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:500` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:546` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:633` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:668` | `def __init__(self, config, seed)` |
| `__init__` | method | `realtime_train.py:901` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:1160` | `def __init__(self, config)` |
| `__init__` | method | `realtime_train.py:1370` | `def __init__(self, config)` |
| `_set_seed` | method | `realtime_train.py:1386` | `def _set_seed(self, seed)` |
| `_signal_handler` | method | `realtime_train.py:1381` | `def _signal_handler(self, signum, frame)` |
| `accumulate_gradient` | method | `realtime_train.py:297` | `def accumulate_gradient(self, model)` |
| `accumulate_gradient` | method | `realtime_train.py:488` | `def accumulate_gradient(self, model)` |
| `analyze_seed_results` | method | `realtime_train.py:905` | `def analyze_seed_results(self, all_results)` |
| `calculate` | method | `realtime_train.py:134` | `def calculate(self)` |
| `calculate` | method | `realtime_train.py:266` | `def calculate(self, model, x_batch)` |
| `calculate` | method | `realtime_train.py:355` | `def calculate(self, gradient_covariance)` |
| `calculate` | method | `realtime_train.py:415` | `def calculate(self, model)` |
| `calculate` | method | `realtime_train.py:636` | `def calculate(self, n_bits, hidden_dim, stage)` |
| `calculate_kappa` | method | `realtime_train.py:311` | `def calculate_kappa(self)` |
| `compute_all_metrics` | method | `realtime_train.py:434` | `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, ste` |
| `compute_superposition_metrics` | method | `realtime_train.py:230` | `def compute_superposition_metrics(self, z_encoded)` |
| `create_aggregate_visualizations` | method | `realtime_train.py:1269` | `def create_aggregate_visualizations(self, all_results)` |
| `create_seed_training_dynamics` | method | `realtime_train.py:1166` | `def create_seed_training_dynamics(self, seed_result)` |
| `forward` | method | `realtime_train.py:143` | `def forward(self, x)` |
| `forward` | method | `realtime_train.py:197` | `def forward(self, x)` |
| `forward` | method | `realtime_train.py:224` | `def forward(self, x)` |
| `generate` | method | `realtime_train.py:251` | `def generate(self, n_bits, k_bits, dataset_size)` |
| `get_flat_parameters` | method | `realtime_train.py:153` | `def get_flat_parameters(self)` |
| `get_flat_parameters` | method | `realtime_train.py:206` | `def get_flat_parameters(self)` |
| `get_latest_checkpoint_path` | method | `realtime_train.py:537` | `def get_latest_checkpoint_path(self)` |
| `get_pre_activations` | method | `realtime_train.py:148` | `def get_pre_activations(self, x)` |
| `get_pre_activations` | method | `realtime_train.py:190` | `def get_pre_activations(self, x)` |
| `is_stagnant` | method | `realtime_train.py:550` | `def is_stagnant(self, metrics_history, current_step, hidden_dim)` |
| `load` | method | `realtime_train.py:167` | `def load(self, path)` |
| `load` | method | `realtime_train.py:524` | `def load(self, path)` |
| `main` | method | `realtime_train.py:1527` | `def main()` |
| `print_analysis_report` | method | `realtime_train.py:1067` | `def print_analysis_report(self, analysis)` |
| `reset` | method | `realtime_train.py:344` | `def reset(self)` |
| `reset` | method | `realtime_train.py:492` | `def reset(self)` |
| `run_experiment` | method | `realtime_train.py:1394` | `def run_experiment(self)` |
| `save` | method | `realtime_train.py:162` | `def save(self, state, path)` |
| `save` | method | `realtime_train.py:506` | `def save(self, state, path)` |
| `should_checkpoint` | method | `realtime_train.py:172` | `def should_checkpoint(self)` |
| `should_checkpoint` | method | `realtime_train.py:532` | `def should_checkpoint(self)` |
| `train_stage` | method | `realtime_train.py:680` | `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` |
| `transfer` | method | `realtime_train.py:582` | `def transfer(self, previous_model, new_model, stage)` |
| `accuracy` | function | `test.py:31` | `def accuracy(model, x, y)` |
| `load_base` | function | `test.py:36` | `def load_base()` |
| `zero_shot_test` | function | `test.py:43` | `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)` |
| `accuracy` | function | `test_wandb_ablation.py:59` | `def accuracy(model, x, y)` |
| `finish_ablation_wandb` | function | `test_wandb_ablation.py:54` | `def finish_ablation_wandb()` |
| `init_ablation_wandb` | function | `test_wandb_ablation.py:24` | `def init_ablation_wandb(project_name)` |
| `load_base` | function | `test_wandb_ablation.py:63` | `def load_base()` |
| `log_scale_results` | function | `test_wandb_ablation.py:37` | `def log_scale_results(n_bits, d_h, train_acc_transfer, test_acc_transfer, train_acc_control, test_acc_control, time_elap` |
| `zero_shot_test` | function | `test_wandb_ablation.py:69` | `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)` |
| `CompleteCurriculumWrapper` | class | `view_streamlit.py:426` | `class CompleteCurriculumWrapper` |
| `ThermodynamicAnalyzer` | class | `view_streamlit.py:82` | `class ThermodynamicAnalyzer` |
| `__init__` | method | `view_streamlit.py:429` | `def __init__(self)` |
| `calculate_adaptive_params` | method | `view_streamlit.py:454` | `def calculate_adaptive_params(self, n_bits, d_h, stage)` |
| `capture_snapshot` | method | `view_streamlit.py:473` | `def capture_snapshot(self, model, sae, stage, n_bits, d_h, step, metrics)` |
| `compute_metrics` | method | `view_streamlit.py:86` | `def compute_metrics(weights_list, phase, epoch)` |
| `main` | method | `view_streamlit.py:863` | `def main()` |
| `run_full_curriculum` | method | `view_streamlit.py:821` | `def run_full_curriculum(self)` |
| `smart_weight_transfer` | method | `view_streamlit.py:502` | `def smart_weight_transfer(self, prev_model, new_model, stage)` |
| `train_stage_complete` | method | `view_streamlit.py:527` | `def train_stage_complete(self, stage, n_bits, d_h, prev_model)` |
| `visualize_2d_texture` | method | `view_streamlit.py:346` | `def visualize_2d_texture(weights_list, phase_name, thermo_metrics)` |
| `visualize_3d_geometry` | method | `view_streamlit.py:256` | `def visualize_3d_geometry(weights_list, phase_name, thermo_metrics)` |
| `visualize_thermal_engine` | method | `view_streamlit.py:149` | `def visualize_thermal_engine(thermo_history)` |
| `calculate_model_accuracy` | function | `visualizador.py:50` | `def calculate_model_accuracy(model, x, y)` |
| `extract_sae_metrics` | function | `visualizador.py:64` | `def extract_sae_metrics(sae, h2)` |
| `get_real_activations` | function | `visualizador.py:58` | `def get_real_activations(model, x)` |
| `load_full_system` | function | `visualizador.py:24` | `def load_full_system(n_bits, d_h, stage)` |
| `plot_sae_autopsy` | function | `visualizador.py:80` | `def plot_sae_autopsy(data, accuracy, n_bits, d_h, sae)` |
