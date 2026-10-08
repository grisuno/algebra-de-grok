# API

## 128bits.py
Depends on: `app.py`
- `evaluate` (function) `128bits.py:34` `def evaluate(model, x, y)`
- `load_64bit_model` (function) `128bits.py:39` `def load_64bit_model()`
- `run_experiment` (function) `128bits.py:49` `def run_experiment(use_padding)`

## 2048bits.py
Depends on: `app.py`
- `evaluate` (function) `2048bits.py:44` `def evaluate(model, x, y)`
- `load_base_model` (function) `2048bits.py:49` `def load_base_model()`
- `zero_shot_test` (function) `2048bits.py:59` `def zero_shot_test(prev_model, n_bits, d_h, use_padding)`

## app.py
Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`
- `SuperpositionSAE.__init__` (method) `app.py:33` `def __init__(self, d_model, d_sae)`
- `SuperpositionSAE.forward` (method) `app.py:40` `def forward(self, x)`
- `SuperpositionSAE.get_metrics` (method) `app.py:45` `def get_metrics(self, z)`
- `ComplexityAnalyzer.measure_lc` (method) `app.py:57` `def measure_lc(model, x, epsilon)`
- `GrokkingTransformer.__init__` (method) `app.py:68` `def __init__(self, d_in, d_h)`
- `GrokkingTransformer.get_pre_acts` (method) `app.py:74` `def get_pre_acts(self, x)`
- `GrokkingTransformer.forward` (method) `app.py:80` `def forward(self, x)`
- `GrokkingTransformer.get_parity_dataset` (method) `app.py:87` `def get_parity_dataset(n_bits, k, size)`
- `AdaptiveCurriculumTrainer.__init__` (method) `app.py:93` `def __init__(self)`
- `AdaptiveCurriculumTrainer.calculate_adaptive_params` (method) `app.py:109` `def calculate_adaptive_params(self, n_bits, d_h, stage)` -- Calcula parámetros adaptativos según la complejidad de la etapa
- `AdaptiveCurriculumTrainer.smart_weight_transfer` (method) `app.py:126` `def smart_weight_transfer(self, prev_model, new_model, stage)` -- Transferencia inteligente de pesos con padding/interpolación
- `AdaptiveCurriculumTrainer.detect_stagnation` (method) `app.py:166` `def detect_stagnation(self, history, current_lc, d_h, step)` -- Detecta si el modelo está estancado y necesita reinicio
- `AdaptiveCurriculumTrainer.train_stage` (method) `app.py:184` `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` -- Entrena una etapa individual con parámetros adaptativos
- `AdaptiveCurriculumTrainer.run_curriculum` (method) `app.py:316` `def run_curriculum(self)` -- Ejecuta el curriculum completo con adaptación automática

## app_wandb.py
- `init_wandb` (function) `app_wandb.py:35` `def init_wandb(project_name, config)` -- Initialize wandb tracking
- `log_training_step` (function) `app_wandb.py:43` `def log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)` -- Log metrics to wandb
- `finish_wandb` (function) `app_wandb.py:59` `def finish_wandb()` -- Finish wandb run
- `SuperpositionSAE.__init__` (method) `app_wandb.py:64` `def __init__(self, d_model, d_sae)`
- `SuperpositionSAE.forward` (method) `app_wandb.py:71` `def forward(self, x)`
- `SuperpositionSAE.get_metrics` (method) `app_wandb.py:76` `def get_metrics(self, z)`
- `ComplexityAnalyzer.measure_lc` (method) `app_wandb.py:88` `def measure_lc(model, x, epsilon)`
- `GrokkingTransformer.__init__` (method) `app_wandb.py:99` `def __init__(self, d_in, d_h)`
- `GrokkingTransformer.get_pre_acts` (method) `app_wandb.py:105` `def get_pre_acts(self, x)`
- `GrokkingTransformer.forward` (method) `app_wandb.py:111` `def forward(self, x)`
- `GrokkingTransformer.get_parity_dataset` (method) `app_wandb.py:118` `def get_parity_dataset(n_bits, k, size)`
- `AdaptiveCurriculumTrainer.__init__` (method) `app_wandb.py:124` `def __init__(self)`
- `AdaptiveCurriculumTrainer.calculate_adaptive_params` (method) `app_wandb.py:140` `def calculate_adaptive_params(self, n_bits, d_h, stage)` -- Calculate adaptive parameters according to stage complexity
- `AdaptiveCurriculumTrainer.smart_weight_transfer` (method) `app_wandb.py:157` `def smart_weight_transfer(self, prev_model, new_model, stage)` -- Intelligent weight transfer with padding/interpolation
- `AdaptiveCurriculumTrainer.detect_stagnation` (method) `app_wandb.py:196` `def detect_stagnation(self, history, current_lc, d_h, step)` -- Detect if model is stagnant and needs restart
- `AdaptiveCurriculumTrainer.train_stage` (method) `app_wandb.py:212` `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` -- Train individual stage with adaptive parameters
- `AdaptiveCurriculumTrainer.run_curriculum` (method) `app_wandb.py:345` `def run_curriculum(self)` -- Execute complete curriculum with automatic adaptation

## new_experiment/checkpointing.py
Depends on: `new_experiment/config.py`
Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`
- `ICheckpointManager.save` (method) `new_experiment/checkpointing.py:20` `def save(self, state, path)` -- Save checkpoint and return path.
- `ICheckpointManager.load` (method) `new_experiment/checkpointing.py:25` `def load(self, path)` -- Load checkpoint from path.
- `ICheckpointManager.should_checkpoint` (method) `new_experiment/checkpointing.py:30` `def should_checkpoint(self)` -- Determine if checkpoint should be saved.
- `CheckpointManager.__init__` (method) `new_experiment/checkpointing.py:43` `def __init__(self, config)` -- Initialize checkpoint manager.
- `CheckpointManager.save` (method) `new_experiment/checkpointing.py:55` `def save(self, state, path)` -- Save checkpoint to disk.
- `CheckpointManager.load` (method) `new_experiment/checkpointing.py:85` `def load(self, path)` -- Load checkpoint from disk.
- `CheckpointManager.should_checkpoint` (method) `new_experiment/checkpointing.py:101` `def should_checkpoint(self)` -- Check if checkpoint interval has elapsed.
- `CheckpointManager.get_latest_checkpoint_path` (method) `new_experiment/checkpointing.py:111` `def get_latest_checkpoint_path(self)` -- Get path to latest checkpoint if exists.

## new_experiment/config.py
Imported by: `new_experiment/checkpointing.py`, `new_experiment/data_generation.py`, `new_experiment/main.py`, `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`, `purity_analysis.py`
- `ExperimentConfig.get_adaptive_train_size` (method) `new_experiment/config.py:111` `def get_adaptive_train_size(self, n_bits)` -- Calculate adaptive training size based on input dimensionality.
- `ExperimentConfig.get_adaptive_weight_decay` (method) `new_experiment/config.py:117` `def get_adaptive_weight_decay(self, n_bits, hidden_dim)` -- Calculate adaptive weight decay based on problem complexity.
- `ExperimentConfig.get_adaptive_max_steps` (method) `new_experiment/config.py:126` `def get_adaptive_max_steps(self, n_bits, hidden_dim)` -- Calculate adaptive maximum steps based on problem complexity.

## new_experiment/data_generation.py
Depends on: `new_experiment/config.py`
Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`
- `ParityDatasetGenerator.__init__` (method) `new_experiment/data_generation.py:19` `def __init__(self, config)` -- Initialize dataset generator.
- `ParityDatasetGenerator.generate` (method) `new_experiment/data_generation.py:28` `def generate(self, n_bits, k_bits, dataset_size)` -- Generate random binary vectors with k-bit parity labels.

## new_experiment/main.py
Depends on: `new_experiment/config.py`, `new_experiment/training.py`
- `MultiSeedCurriculumRunner.__init__` (method) `new_experiment/main.py:24` `def __init__(self, config)` -- Initialize runner.
- `MultiSeedCurriculumRunner.run_single_seed` (method) `new_experiment/main.py:48` `def run_single_seed(self, seed)` -- Run curriculum for a single seed.
- `MultiSeedCurriculumRunner.run_experiment` (method) `new_experiment/main.py:90` `def run_experiment(self, start_seed, end_seed)` -- Run experiment across multiple seeds.
- `MultiSeedCurriculumRunner.main` (method) `new_experiment/main.py:130` `def main()` -- Main entry point for command-line execution.

## new_experiment/metrics.py
Depends on: `new_experiment/config.py`, `new_experiment/models.py`
Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`
- `IMetricCalculator.calculate` (method) `new_experiment/metrics.py:21` `def calculate(self)` -- Calculate metrics and return dictionary of results.
- `LocalComplexityCalculator.__init__` (method) `new_experiment/metrics.py:34` `def __init__(self, config)` -- Initialize calculator.
- `LocalComplexityCalculator.calculate` (method) `new_experiment/metrics.py:44` `def calculate(self, model, x_batch)` -- Measure LC as count of near-zero pre-activations.
- `GradientCovarianceCalculator.__init__` (method) `new_experiment/metrics.py:90` `def __init__(self, config)` -- Initialize calculator.
- `GradientCovarianceCalculator.accumulate_gradient` (method) `new_experiment/metrics.py:102` `def accumulate_gradient(self, model)` -- Store current gradient vector.
- `GradientCovarianceCalculator.calculate_kappa` (method) `new_experiment/metrics.py:121` `def calculate_kappa(self)` -- Calculate condition number of gradient covariance matrix.
- `GradientCovarianceCalculator.reset` (method) `new_experiment/metrics.py:161` `def reset(self)` -- Clear gradient buffer.
- `ThermodynamicMetricsCalculator.__init__` (method) `new_experiment/metrics.py:174` `def __init__(self, config)` -- Initialize calculator.
- `ThermodynamicMetricsCalculator.calculate` (method) `new_experiment/metrics.py:183` `def calculate(self, gradient_covariance)` -- Calculate effective temperature and Planck constant.
- `DeltaCalculator.calculate` (method) `new_experiment/metrics.py:261` `def calculate(self, model)` -- Calculate mean squared distance to nearest integer.
- `ComprehensiveMetricsAggregator.__init__` (method) `new_experiment/metrics.py:289` `def __init__(self, config)` -- Initialize aggregator.
- `ComprehensiveMetricsAggregator.compute_all_metrics` (method) `new_experiment/metrics.py:302` `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae...` -- Compute comprehensive metric suite.
- `ComprehensiveMetricsAggregator.accumulate_gradient` (method) `new_experiment/metrics.py:374` `def accumulate_gradient(self, model)` -- Accumulate gradient for kappa calculation.
- `ComprehensiveMetricsAggregator.reset` (method) `new_experiment/metrics.py:383` `def reset(self)` -- Reset all stateful calculators.

## new_experiment/models.py
Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`
- `IModelArchitecture.forward` (method) `new_experiment/models.py:18` `def forward(self, x)` -- Forward pass returning logits and latent representation.
- `IModelArchitecture.get_pre_activations` (method) `new_experiment/models.py:23` `def get_pre_activations(self, x)` -- Get pre-activation tensors for complexity analysis.
- `IModelArchitecture.get_flat_parameters` (method) `new_experiment/models.py:28` `def get_flat_parameters(self)` -- Get flattened parameter vector.
- `GrokkingTransformer.__init__` (method) `new_experiment/models.py:41` `def __init__(self, input_dim, hidden_dim, output_dim)` -- Initialize network.
- `GrokkingTransformer.get_pre_activations` (method) `new_experiment/models.py:59` `def get_pre_activations(self, x)` -- Get pre-activation tensors for local complexity calculation.
- `GrokkingTransformer.forward` (method) `new_experiment/models.py:74` `def forward(self, x)` -- Forward pass through network.
- `GrokkingTransformer.get_flat_parameters` (method) `new_experiment/models.py:91` `def get_flat_parameters(self)` -- Get flattened parameter vector.
- `SuperpositionSAE.__init__` (method) `new_experiment/models.py:109` `def __init__(self, model_dim, sae_dim)` -- Initialize SAE.
- `SuperpositionSAE.forward` (method) `new_experiment/models.py:126` `def forward(self, x)` -- Encode and decode with ReLU activation.
- `SuperpositionSAE.compute_superposition_metrics` (method) `new_experiment/models.py:140` `def compute_superposition_metrics(self, z_encoded)` -- Calculate superposition coefficient and effective features.

## new_experiment/streamlit_app.py
Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`
- `ThermodynamicAnalyzer.compute_metrics` (method) `new_experiment/streamlit_app.py:79` `def compute_metrics(weights_list, phase, epoch)` -- Calculate complete thermodynamic state.
- `StreamlitTrainer.__init__` (method) `new_experiment/streamlit_app.py:146` `def __init__(self, config)` -- Initialize trainer.
- `StreamlitTrainer.train_stage_with_visualization` (method) `new_experiment/streamlit_app.py:163` `def train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` -- Train stage with real-time Streamlit visualization.
- `StreamlitTrainer.run_curriculum` (method) `new_experiment/streamlit_app.py:570` `def run_curriculum(self)` -- Execute complete curriculum.
- `StreamlitTrainer.main` (method) `new_experiment/streamlit_app.py:596` `def main()` -- Main Streamlit application.

## new_experiment/training.py
Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`
Imported by: `new_experiment/main.py`
- `CurriculumStageTrainer.__init__` (method) `new_experiment/training.py:29` `def __init__(self, config, seed)` -- Initialize stage trainer.
- `CurriculumStageTrainer.train_stage` (method) `new_experiment/training.py:48` `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` -- Train a single curriculum stage.

## new_experiment/training_dynamics.py
Depends on: `new_experiment/config.py`
Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`
- `SmartWeightTransfer.transfer` (method) `new_experiment/training_dynamics.py:21` `def transfer(self, previous_model, new_model, stage)` -- Transfer weights with padding or cropping as needed.
- `StagnationDetector.__init__` (method) `new_experiment/training_dynamics.py:91` `def __init__(self, config)` -- Initialize detector.
- `StagnationDetector.is_stagnant` (method) `new_experiment/training_dynamics.py:101` `def is_stagnant(self, metrics_history, current_step, hidden_dim)` -- Determine if training is stagnant.

## new_experiment/wandb_integration.py
Depends on: `new_experiment/config.py`
Imported by: `new_experiment/streamlit_app.py`, `new_experiment/training.py`
- `WandBLogger.__init__` (method) `new_experiment/wandb_integration.py:19` `def __init__(self, config)` -- Initialize WandB logger.
- `WandBLogger.initialize` (method) `new_experiment/wandb_integration.py:30` `def initialize(self, run_name, run_config)` -- Initialize WandB run.
- `WandBLogger.log_metrics` (method) `new_experiment/wandb_integration.py:58` `def log_metrics(self, metrics, step)` -- Log metrics to WandB.
- `WandBLogger.finish` (method) `new_experiment/wandb_integration.py:77` `def finish(self)` -- Finish WandB run.

## purity_analysis.py
Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- `IModel.get_flat_parameters` (method) `purity_analysis.py:52` `def get_flat_parameters(self)`
- `IPurityIndexCalculator.calculate` (method) `purity_analysis.py:59` `def calculate(self, model)`
- `IEffectiveTemperatureCalculator.calculate` (method) `purity_analysis.py:66` `def calculate(self, loss_history)`
- `IPhaseClassifier.classify` (method) `purity_analysis.py:73` `def classify(self, alpha, temperature)`
- `IPolycrystalAnalyzer.analyze_polycrystal` (method) `purity_analysis.py:80` `def analyze_polycrystal(self, model, pruning_level)`
- `IPurityComparator.compare` (method) `purity_analysis.py:91` `def compare(self, original, polycrystal)`
- `PurityIndexCalculator.__init__` (method) `purity_analysis.py:105` `def __init__(self, config)` -- Initialize calculator.
- `PurityIndexCalculator.calculate` (method) `purity_analysis.py:114` `def calculate(self, model)` -- Calculate comprehensive purity metrics.
- `EffectiveTemperatureCalculator.__init__` (method) `purity_analysis.py:242` `def __init__(self, config)` -- Initialize calculator.
- `EffectiveTemperatureCalculator.calculate` (method) `purity_analysis.py:251` `def calculate(self, loss_history)` -- Calculate thermodynamic metrics from loss history.
- `PhaseClassifier.__init__` (method) `purity_analysis.py:321` `def __init__(self, config)` -- Initialize classifier.
- `PhaseClassifier.classify` (method) `purity_analysis.py:330` `def classify(self, alpha, temperature)` -- Classify current phase state.
- `PhaseClassifier.classify_polycrystal_state` (method) `purity_analysis.py:359` `def classify_polycrystal_state(self, original_alpha, original_temp, poly_alpha, poly_temp)` -- Classify polycrystal state after perturbation.
- `PolycrystalAnalyzer.__init__` (method) `purity_analysis.py:400` `def __init__(self, config)` -- Initialize analyzer.
- `PolycrystalAnalyzer.analyze_polycrystal` (method) `purity_analysis.py:412` `def analyze_polycrystal(self, model, pruning_level, loss_history)` -- Analyze model after weight pruning.
- `PurityComparator.__init__` (method) `purity_analysis.py:508` `def __init__(self, config)` -- Initialize comparator.
- `PurityComparator.compare` (method) `purity_analysis.py:518` `def compare(self, original, polycrystal)` -- Compare original and polycrystal states.
- `CheckpointLoader.__init__` (method) `purity_analysis.py:583` `def __init__(self, config)` -- Initialize loader.
- `CheckpointLoader.load` (method) `purity_analysis.py:592` `def load(self, checkpoint_path)` -- Load checkpoint and extract model.
- `PurityAnalyzer.__init__` (method) `purity_analysis.py:650` `def __init__(self, checkpoint_path, experiment_config, purity_config)` -- Initialize analyzer.
- `PurityAnalyzer.analyze` (method) `purity_analysis.py:694` `def analyze(self)` -- Perform comprehensive purity analysis.
- `PurityPipeline.__init__` (method) `purity_analysis.py:825` `def __init__(self, experiment_config, purity_config)` -- Initialize pipeline.
- `PurityPipeline.process_checkpoint` (method) `purity_analysis.py:840` `def process_checkpoint(self, checkpoint_path, output_dir)` -- Process single checkpoint.
- `PurityPipeline.process_directory` (method) `purity_analysis.py:874` `def process_directory(self, checkpoint_dir, n_latest, output_dir)` -- Process all checkpoints in directory.
- `PurityPipeline.generate_summary` (method) `purity_analysis.py:917` `def generate_summary(self, all_results, output_dir)` -- Generate summary statistics across all checkpoints.
- `PurityPipeline.main` (method) `purity_analysis.py:1049` `def main()` -- Main entry point for purity analysis.

## realtime_train.py
- `IMetricCalculator.calculate` (method) `realtime_train.py:134` `def calculate(self)` -- Calculate metrics and return dictionary of results.
- `IModelArchitecture.forward` (method) `realtime_train.py:143` `def forward(self, x)` -- Forward pass returning logits and latent representation.
- `IModelArchitecture.get_pre_activations` (method) `realtime_train.py:148` `def get_pre_activations(self, x)` -- Get pre-activation tensors for complexity analysis.
- `IModelArchitecture.get_flat_parameters` (method) `realtime_train.py:153` `def get_flat_parameters(self)` -- Get flattened parameter vector.
- `ICheckpointManager.save` (method) `realtime_train.py:162` `def save(self, state, path)` -- Save checkpoint and return path.
- `ICheckpointManager.load` (method) `realtime_train.py:167` `def load(self, path)` -- Load checkpoint from path.
- `ICheckpointManager.should_checkpoint` (method) `realtime_train.py:172` `def should_checkpoint(self)` -- Determine if checkpoint should be saved.
- `GrokkingTransformer.__init__` (method) `realtime_train.py:180` `def __init__(self, input_dim, hidden_dim, output_dim)`
- `GrokkingTransformer.get_pre_activations` (method) `realtime_train.py:190` `def get_pre_activations(self, x)` -- Get pre-activation tensors for LC calculation.
- `GrokkingTransformer.forward` (method) `realtime_train.py:197` `def forward(self, x)` -- Forward pass returning logits and latent representation.
- `GrokkingTransformer.get_flat_parameters` (method) `realtime_train.py:206` `def get_flat_parameters(self)` -- Get flattened parameter vector.
- `SuperpositionSAE.__init__` (method) `realtime_train.py:214` `def __init__(self, model_dim, sae_dim)`
- `SuperpositionSAE.forward` (method) `realtime_train.py:224` `def forward(self, x)` -- Encode and decode with ReLU activation.
- `SuperpositionSAE.compute_superposition_metrics` (method) `realtime_train.py:230` `def compute_superposition_metrics(self, z_encoded)` -- Calculate psi (superposition coefficient) and effective features.
- `ParityDatasetGenerator.__init__` (method) `realtime_train.py:248` `def __init__(self, config)`
- `ParityDatasetGenerator.generate` (method) `realtime_train.py:251` `def generate(self, n_bits, k_bits, dataset_size)` -- Generate random binary vectors with k-bit parity labels.
- `LocalComplexityCalculator.__init__` (method) `realtime_train.py:262` `def __init__(self, config)`
- `LocalComplexityCalculator.calculate` (method) `realtime_train.py:266` `def calculate(self, model, x_batch)` -- Measure LC as count of near-zero pre-activations.
- `GradientCovarianceCalculator.__init__` (method) `realtime_train.py:291` `def __init__(self, config)`
- `GradientCovarianceCalculator.accumulate_gradient` (method) `realtime_train.py:297` `def accumulate_gradient(self, model)` -- Store current gradient vector.
- `GradientCovarianceCalculator.calculate_kappa` (method) `realtime_train.py:311` `def calculate_kappa(self)` -- Calculate condition number of gradient covariance matrix.
- `GradientCovarianceCalculator.reset` (method) `realtime_train.py:344` `def reset(self)` -- Clear gradient buffer.
- `ThermodynamicMetricsCalculator.__init__` (method) `realtime_train.py:352` `def __init__(self, config)`
- `ThermodynamicMetricsCalculator.calculate` (method) `realtime_train.py:355` `def calculate(self, gradient_covariance)` -- Calculate effective temperature and Planck constant.
- `DeltaCalculator.calculate` (method) `realtime_train.py:415` `def calculate(self, model)` -- Calculate mean squared distance to nearest integer.
- `ComprehensiveMetricsAggregator.__init__` (method) `realtime_train.py:427` `def __init__(self, config)`
- `ComprehensiveMetricsAggregator.compute_all_metrics` (method) `realtime_train.py:434` `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae...` -- Compute comprehensive metric suite.
- `ComprehensiveMetricsAggregator.accumulate_gradient` (method) `realtime_train.py:488` `def accumulate_gradient(self, model)` -- Accumulate gradient for kappa calculation.
- `ComprehensiveMetricsAggregator.reset` (method) `realtime_train.py:492` `def reset(self)` -- Reset all stateful calculators.
- `CheckpointManager.__init__` (method) `realtime_train.py:500` `def __init__(self, config)`
- `CheckpointManager.save` (method) `realtime_train.py:506` `def save(self, state, path)` -- Save checkpoint to disk.
- `CheckpointManager.load` (method) `realtime_train.py:524` `def load(self, path)` -- Load checkpoint from disk.
- `CheckpointManager.should_checkpoint` (method) `realtime_train.py:532` `def should_checkpoint(self)` -- Check if checkpoint interval has elapsed.
- `CheckpointManager.get_latest_checkpoint_path` (method) `realtime_train.py:537` `def get_latest_checkpoint_path(self)` -- Get path to latest checkpoint if exists.
- `StagnationDetector.__init__` (method) `realtime_train.py:546` `def __init__(self, config)`
- `StagnationDetector.is_stagnant` (method) `realtime_train.py:550` `def is_stagnant(self, metrics_history, current_step, hidden_dim)` -- Determine if training is stagnant.
- `SmartWeightTransfer.transfer` (method) `realtime_train.py:582` `def transfer(self, previous_model, new_model, stage)` -- Transfer weights with padding/cropping as needed.
- `AdaptiveParameterCalculator.__init__` (method) `realtime_train.py:633` `def __init__(self, config)`
- `AdaptiveParameterCalculator.calculate` (method) `realtime_train.py:636` `def calculate(self, n_bits, hidden_dim, stage)` -- Calculate training parameters for current stage.
- `CurriculumStageTrainer.__init__` (method) `realtime_train.py:668` `def __init__(self, config, seed)`
- `CurriculumStageTrainer.train_stage` (method) `realtime_train.py:680` `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` -- Train a single curriculum stage.
- `ResultsAnalyzer.__init__` (method) `realtime_train.py:901` `def __init__(self, config)`
- `ResultsAnalyzer.analyze_seed_results` (method) `realtime_train.py:905` `def analyze_seed_results(self, all_results)` -- Generate comprehensive analysis of all seed results.
- `ResultsAnalyzer.print_analysis_report` (method) `realtime_train.py:1067` `def print_analysis_report(self, analysis)` -- Print comprehensive analysis report to console.
- `ResultsVisualizer.__init__` (method) `realtime_train.py:1160` `def __init__(self, config)`
- `ResultsVisualizer.create_seed_training_dynamics` (method) `realtime_train.py:1166` `def create_seed_training_dynamics(self, seed_result)` -- Create training dynamics visualization for a single seed.
- `ResultsVisualizer.create_aggregate_visualizations` (method) `realtime_train.py:1269` `def create_aggregate_visualizations(self, all_results)` -- Create aggregate visualizations across all seeds.
- `MultiSeedCurriculumRunner.__init__` (method) `realtime_train.py:1370` `def __init__(self, config)`
- `MultiSeedCurriculumRunner.run_experiment` (method) `realtime_train.py:1394` `def run_experiment(self)` -- Run multi-seed curriculum experiment.
- `MultiSeedCurriculumRunner.main` (method) `realtime_train.py:1527` `def main()` -- Main entry point.

## view_streamlit.py
Depends on: `app.py`
- `ThermodynamicAnalyzer.compute_metrics` (method) `view_streamlit.py:86` `def compute_metrics(weights_list, phase, epoch)` -- Calculate complete thermodynamic state
- `ThermodynamicAnalyzer.visualize_thermal_engine` (method) `view_streamlit.py:149` `def visualize_thermal_engine(thermo_history)` -- Complete thermal engine visualization
- `ThermodynamicAnalyzer.visualize_3d_geometry` (method) `view_streamlit.py:256` `def visualize_3d_geometry(weights_list, phase_name, thermo_metrics)` -- Complete 3D visualization with clustering and geometry
- `ThermodynamicAnalyzer.visualize_2d_texture` (method) `view_streamlit.py:346` `def visualize_2d_texture(weights_list, phase_name, thermo_metrics)` -- Complete 2D texture: heatmap, distribution, FFT, histogram
- `CompleteCurriculumWrapper.__init__` (method) `view_streamlit.py:429` `def __init__(self)`
- `CompleteCurriculumWrapper.calculate_adaptive_params` (method) `view_streamlit.py:454` `def calculate_adaptive_params(self, n_bits, d_h, stage)` -- EXACTO app.py: Calcula parámetros adaptativos
- `CompleteCurriculumWrapper.capture_snapshot` (method) `view_streamlit.py:473` `def capture_snapshot(self, model, sae, stage, n_bits, d_h, step, metrics)` -- Capture complete snapshot
- `CompleteCurriculumWrapper.smart_weight_transfer` (method) `view_streamlit.py:502` `def smart_weight_transfer(self, prev_model, new_model, stage)` -- EXACTO app.py: Transferencia inteligente de pesos
- `CompleteCurriculumWrapper.train_stage_complete` (method) `view_streamlit.py:527` `def train_stage_complete(self, stage, n_bits, d_h, prev_model)` -- Train stage with REAL-TIME 3D/2D visualization every 500 steps
- `CompleteCurriculumWrapper.run_full_curriculum` (method) `view_streamlit.py:821` `def run_full_curriculum(self)` -- Execute complete curriculum - EXACTO app.py
- `CompleteCurriculumWrapper.main` (method) `view_streamlit.py:863` `def main()`

## visualizador.py
Depends on: `app.py`
- `load_full_system` (function) `visualizador.py:24` `def load_full_system(n_bits, d_h, stage)` -- Carga el MODELO entrenado y el SAE
- `calculate_model_accuracy` (function) `visualizador.py:50` `def calculate_model_accuracy(model, x, y)` -- Calcula la precisión real del modelo cargado
- `get_real_activations` (function) `visualizador.py:58` `def get_real_activations(model, x)` -- Obtiene las activaciones latentes REALES del modelo
- `extract_sae_metrics` (function) `visualizador.py:64` `def extract_sae_metrics(sae, h2)` -- Extrae métricas del SAE sobre las activaciones reales
- `plot_sae_autopsy` (function) `visualizador.py:80` `def plot_sae_autopsy(data, accuracy, n_bits, d_h, sae)` -- Visualización centrada en la verdad del Modelo
