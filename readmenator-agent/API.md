# API

## 128bits.py

### evaluate `def evaluate(model, x, y)`
- Defined: `128bits.py:34`
- Depends on: `app.py`

### load_64bit_model `def load_64bit_model()`
- Defined: `128bits.py:39`
- Depends on: `app.py`

### run_experiment `def run_experiment(use_padding)`
- Defined: `128bits.py:49`
- Depends on: `app.py`

## 2048bits.py

### evaluate `def evaluate(model, x, y)`
- Defined: `2048bits.py:44`
- Depends on: `app.py`

### load_base_model `def load_base_model()`
- Defined: `2048bits.py:49`
- Depends on: `app.py`

### zero_shot_test `def zero_shot_test(prev_model, n_bits, d_h, use_padding)`
- Defined: `2048bits.py:59`
- Depends on: `app.py`

## app.py

### get_parity_dataset `def get_parity_dataset(n_bits, k, size)`
- Defined: `app.py:87`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### __init__ `def __init__(self, d_model, d_sae)`
- Defined: `app.py:33`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### forward `def forward(self, x)`
- Defined: `app.py:40`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### get_metrics `def get_metrics(self, z)`
- Defined: `app.py:45`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### measure_lc `def measure_lc(model, x, epsilon)`
- Defined: `app.py:57`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### __init__ `def __init__(self, d_in, d_h)`
- Defined: `app.py:68`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### get_pre_acts `def get_pre_acts(self, x)`
- Defined: `app.py:74`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### forward `def forward(self, x)`
- Defined: `app.py:80`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### __init__ `def __init__(self)`
- Defined: `app.py:93`
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### calculate_adaptive_params `def calculate_adaptive_params(self, n_bits, d_h, stage)`
- Defined: `app.py:109`
- Doc: Calcula parámetros adaptativos según la complejidad de la etapa
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### smart_weight_transfer `def smart_weight_transfer(self, prev_model, new_model, stage)`
- Defined: `app.py:126`
- Doc: Transferencia inteligente de pesos con padding/interpolación
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### detect_stagnation `def detect_stagnation(self, history, current_lc, d_h, step)`
- Defined: `app.py:166`
- Doc: Detecta si el modelo está estancado y necesita reinicio
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### train_stage `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)`
- Defined: `app.py:184`
- Doc: Entrena una etapa individual con parámetros adaptativos
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

### run_curriculum `def run_curriculum(self)`
- Defined: `app.py:316`
- Doc: Ejecuta el curriculum completo con adaptación automática
- Imported by: `128bits.py`, `2048bits.py`, `test.py`, `test_wandb_ablation.py`, `view_streamlit.py`, `visualizador.py`

## app_wandb.py

### init_wandb `def init_wandb(project_name, config)`
- Defined: `app_wandb.py:35`
- Doc: Initialize wandb tracking

### log_training_step `def log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)`
- Defined: `app_wandb.py:43`
- Doc: Log metrics to wandb

### finish_wandb `def finish_wandb()`
- Defined: `app_wandb.py:59`
- Doc: Finish wandb run

### get_parity_dataset `def get_parity_dataset(n_bits, k, size)`
- Defined: `app_wandb.py:118`

### __init__ `def __init__(self, d_model, d_sae)`
- Defined: `app_wandb.py:64`

### forward `def forward(self, x)`
- Defined: `app_wandb.py:71`

### get_metrics `def get_metrics(self, z)`
- Defined: `app_wandb.py:76`

### measure_lc `def measure_lc(model, x, epsilon)`
- Defined: `app_wandb.py:88`

### __init__ `def __init__(self, d_in, d_h)`
- Defined: `app_wandb.py:99`

### get_pre_acts `def get_pre_acts(self, x)`
- Defined: `app_wandb.py:105`

### forward `def forward(self, x)`
- Defined: `app_wandb.py:111`

### __init__ `def __init__(self)`
- Defined: `app_wandb.py:124`

### calculate_adaptive_params `def calculate_adaptive_params(self, n_bits, d_h, stage)`
- Defined: `app_wandb.py:140`
- Doc: Calculate adaptive parameters according to stage complexity

### smart_weight_transfer `def smart_weight_transfer(self, prev_model, new_model, stage)`
- Defined: `app_wandb.py:157`
- Doc: Intelligent weight transfer with padding/interpolation

### detect_stagnation `def detect_stagnation(self, history, current_lc, d_h, step)`
- Defined: `app_wandb.py:196`
- Doc: Detect if model is stagnant and needs restart

### train_stage `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)`
- Defined: `app_wandb.py:212`
- Doc: Train individual stage with adaptive parameters

### run_curriculum `def run_curriculum(self)`
- Defined: `app_wandb.py:345`
- Doc: Execute complete curriculum with automatic adaptation

## new_experiment/checkpointing.py

### save `def save(self, state, path)`
- Defined: `new_experiment/checkpointing.py:20`
- Doc: Save checkpoint and return path.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

### load `def load(self, path)`
- Defined: `new_experiment/checkpointing.py:25`
- Doc: Load checkpoint from path.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

### should_checkpoint `def should_checkpoint(self)`
- Defined: `new_experiment/checkpointing.py:30`
- Doc: Determine if checkpoint should be saved.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/checkpointing.py:43`
- Doc: Initialize checkpoint manager.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

### save `def save(self, state, path)`
- Defined: `new_experiment/checkpointing.py:55`
- Doc: Save checkpoint to disk.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

### load `def load(self, path)`
- Defined: `new_experiment/checkpointing.py:85`
- Doc: Load checkpoint from disk.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

### should_checkpoint `def should_checkpoint(self)`
- Defined: `new_experiment/checkpointing.py:101`
- Doc: Check if checkpoint interval has elapsed.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

### get_latest_checkpoint_path `def get_latest_checkpoint_path(self)`
- Defined: `new_experiment/checkpointing.py:111`
- Doc: Get path to latest checkpoint if exists.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/config.py

### get_adaptive_train_size `def get_adaptive_train_size(self, n_bits)`
- Defined: `new_experiment/config.py:111`
- Doc: Calculate adaptive training size based on input dimensionality.
- Imported by: `new_experiment/checkpointing.py`, `new_experiment/data_generation.py`, `new_experiment/main.py`, `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`, `purity_analysis.py`

### get_adaptive_weight_decay `def get_adaptive_weight_decay(self, n_bits, hidden_dim)`
- Defined: `new_experiment/config.py:117`
- Doc: Calculate adaptive weight decay based on problem complexity.
- Imported by: `new_experiment/checkpointing.py`, `new_experiment/data_generation.py`, `new_experiment/main.py`, `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`, `purity_analysis.py`

### get_adaptive_max_steps `def get_adaptive_max_steps(self, n_bits, hidden_dim)`
- Defined: `new_experiment/config.py:126`
- Doc: Calculate adaptive maximum steps based on problem complexity.
- Imported by: `new_experiment/checkpointing.py`, `new_experiment/data_generation.py`, `new_experiment/main.py`, `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`, `purity_analysis.py`

## new_experiment/data_generation.py

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/data_generation.py:19`
- Doc: Initialize dataset generator.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### generate `def generate(self, n_bits, k_bits, dataset_size)`
- Defined: `new_experiment/data_generation.py:28`
- Doc: Generate random binary vectors with k-bit parity labels.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/main.py

### main `def main()`
- Defined: `new_experiment/main.py:130`
- Doc: Main entry point for command-line execution.
- Depends on: `new_experiment/config.py`, `new_experiment/training.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/main.py:24`
- Doc: Initialize runner.
- Depends on: `new_experiment/config.py`, `new_experiment/training.py`

### _set_seed `def _set_seed(self, seed)`
- Defined: `new_experiment/main.py:35`
- Doc: Set random seed for reproducibility.
- Depends on: `new_experiment/config.py`, `new_experiment/training.py`

### run_single_seed `def run_single_seed(self, seed)`
- Defined: `new_experiment/main.py:48`
- Doc: Run curriculum for a single seed.
- Depends on: `new_experiment/config.py`, `new_experiment/training.py`

### run_experiment `def run_experiment(self, start_seed, end_seed)`
- Defined: `new_experiment/main.py:90`
- Doc: Run experiment across multiple seeds.
- Depends on: `new_experiment/config.py`, `new_experiment/training.py`

## new_experiment/metrics.py

### calculate `def calculate(self)`
- Defined: `new_experiment/metrics.py:21`
- Doc: Calculate metrics and return dictionary of results.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/metrics.py:34`
- Doc: Initialize calculator.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### calculate `def calculate(self, model, x_batch)`
- Defined: `new_experiment/metrics.py:44`
- Doc: Measure LC as count of near-zero pre-activations.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/metrics.py:90`
- Doc: Initialize calculator.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### accumulate_gradient `def accumulate_gradient(self, model)`
- Defined: `new_experiment/metrics.py:102`
- Doc: Store current gradient vector.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### calculate_kappa `def calculate_kappa(self)`
- Defined: `new_experiment/metrics.py:121`
- Doc: Calculate condition number of gradient covariance matrix.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### reset `def reset(self)`
- Defined: `new_experiment/metrics.py:161`
- Doc: Clear gradient buffer.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/metrics.py:174`
- Doc: Initialize calculator.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### calculate `def calculate(self, gradient_covariance)`
- Defined: `new_experiment/metrics.py:183`
- Doc: Calculate effective temperature and Planck constant.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### calculate `def calculate(self, model)`
- Defined: `new_experiment/metrics.py:261`
- Doc: Calculate mean squared distance to nearest integer.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/metrics.py:289`
- Doc: Initialize aggregator.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### compute_all_metrics `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, step)`
- Defined: `new_experiment/metrics.py:302`
- Doc: Compute comprehensive metric suite.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### accumulate_gradient `def accumulate_gradient(self, model)`
- Defined: `new_experiment/metrics.py:374`
- Doc: Accumulate gradient for kappa calculation.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### reset `def reset(self)`
- Defined: `new_experiment/metrics.py:383`
- Doc: Reset all stateful calculators.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/models.py

### forward `def forward(self, x)`
- Defined: `new_experiment/models.py:18`
- Doc: Forward pass returning logits and latent representation.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### get_pre_activations `def get_pre_activations(self, x)`
- Defined: `new_experiment/models.py:23`
- Doc: Get pre-activation tensors for complexity analysis.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### get_flat_parameters `def get_flat_parameters(self)`
- Defined: `new_experiment/models.py:28`
- Doc: Get flattened parameter vector.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### __init__ `def __init__(self, input_dim, hidden_dim, output_dim)`
- Defined: `new_experiment/models.py:41`
- Doc: Initialize network.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### get_pre_activations `def get_pre_activations(self, x)`
- Defined: `new_experiment/models.py:59`
- Doc: Get pre-activation tensors for local complexity calculation.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### forward `def forward(self, x)`
- Defined: `new_experiment/models.py:74`
- Doc: Forward pass through network.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### get_flat_parameters `def get_flat_parameters(self)`
- Defined: `new_experiment/models.py:91`
- Doc: Get flattened parameter vector.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### __init__ `def __init__(self, model_dim, sae_dim)`
- Defined: `new_experiment/models.py:109`
- Doc: Initialize SAE.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### forward `def forward(self, x)`
- Defined: `new_experiment/models.py:126`
- Doc: Encode and decode with ReLU activation.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

### compute_superposition_metrics `def compute_superposition_metrics(self, z_encoded)`
- Defined: `new_experiment/models.py:140`
- Doc: Calculate superposition coefficient and effective features.
- Imported by: `new_experiment/metrics.py`, `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`, `purity_analysis.py`

## new_experiment/streamlit_app.py

### main `def main()`
- Defined: `new_experiment/streamlit_app.py:596`
- Doc: Main Streamlit application.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

### compute_metrics `def compute_metrics(weights_list, phase, epoch)`
- Defined: `new_experiment/streamlit_app.py:79`
- Doc: Calculate complete thermodynamic state.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/streamlit_app.py:146`
- Doc: Initialize trainer.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

### train_stage_with_visualization `def train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)`
- Defined: `new_experiment/streamlit_app.py:163`
- Doc: Train stage with real-time Streamlit visualization.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

### _create_3d_visualization `def _create_3d_visualization(self, weights_list, phase_name, thermo_metrics)`
- Defined: `new_experiment/streamlit_app.py:424`
- Doc: Create 3D PCA visualization.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

### _create_2d_visualization `def _create_2d_visualization(self, weights_list, phase_name, thermo_metrics)`
- Defined: `new_experiment/streamlit_app.py:478`
- Doc: Create 2D texture visualization.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

### _create_metrics_plot `def _create_metrics_plot(self, history, phase_name)`
- Defined: `new_experiment/streamlit_app.py:526`
- Doc: Create comprehensive metrics plot.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

### run_curriculum `def run_curriculum(self)`
- Defined: `new_experiment/streamlit_app.py:570`
- Doc: Execute complete curriculum.
- Depends on: `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`

## new_experiment/test_framework.py

### test_configuration `def test_configuration()`
- Defined: `new_experiment/test_framework.py:17`
- Doc: Test configuration creation and parameter calculation.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

### test_data_generation `def test_data_generation()`
- Defined: `new_experiment/test_framework.py:38`
- Doc: Test dataset generation.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

### test_models `def test_models()`
- Defined: `new_experiment/test_framework.py:53`
- Doc: Test model architectures.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

### test_metrics `def test_metrics()`
- Defined: `new_experiment/test_framework.py:80`
- Doc: Test metric calculation.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

### test_checkpointing `def test_checkpointing()`
- Defined: `new_experiment/test_framework.py:119`
- Doc: Test checkpoint management.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

### test_weight_transfer `def test_weight_transfer()`
- Defined: `new_experiment/test_framework.py:142`
- Doc: Test smart weight transfer.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

### test_stagnation_detection `def test_stagnation_detection()`
- Defined: `new_experiment/test_framework.py:158`
- Doc: Test stagnation detector.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

### run_all_tests `def run_all_tests()`
- Defined: `new_experiment/test_framework.py:178`
- Doc: Run all tests.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`

## new_experiment/training.py

### __init__ `def __init__(self, config, seed)`
- Defined: `new_experiment/training.py:29`
- Doc: Initialize stage trainer.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`
- Imported by: `new_experiment/main.py`

### train_stage `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)`
- Defined: `new_experiment/training.py:48`
- Doc: Train a single curriculum stage.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`
- Imported by: `new_experiment/main.py`

### _create_checkpoint_state `def _create_checkpoint_state(self, model, sae, optimizer, stage, n_bits, hidden_dim, step, metrics_history)`
- Defined: `new_experiment/training.py:289`
- Doc: Create checkpoint state dictionary.
- Depends on: `new_experiment/checkpointing.py`, `new_experiment/config.py`, `new_experiment/data_generation.py`, `new_experiment/metrics.py`, `new_experiment/models.py`, `new_experiment/training_dynamics.py`, `new_experiment/wandb_integration.py`
- Imported by: `new_experiment/main.py`

## new_experiment/training_dynamics.py

### transfer `def transfer(self, previous_model, new_model, stage)`
- Defined: `new_experiment/training_dynamics.py:21`
- Doc: Transfer weights with padding or cropping as needed.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/training_dynamics.py:91`
- Doc: Initialize detector.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

### is_stagnant `def is_stagnant(self, metrics_history, current_step, hidden_dim)`
- Defined: `new_experiment/training_dynamics.py:101`
- Doc: Determine if training is stagnant.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/test_framework.py`, `new_experiment/training.py`

## new_experiment/wandb_integration.py

### __init__ `def __init__(self, config)`
- Defined: `new_experiment/wandb_integration.py:19`
- Doc: Initialize WandB logger.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/training.py`

### initialize `def initialize(self, run_name, run_config)`
- Defined: `new_experiment/wandb_integration.py:30`
- Doc: Initialize WandB run.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/training.py`

### log_metrics `def log_metrics(self, metrics, step)`
- Defined: `new_experiment/wandb_integration.py:58`
- Doc: Log metrics to WandB.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/training.py`

### finish `def finish(self)`
- Defined: `new_experiment/wandb_integration.py:77`
- Doc: Finish WandB run.
- Depends on: `new_experiment/config.py`
- Imported by: `new_experiment/streamlit_app.py`, `new_experiment/training.py`

## purity_analysis.py

### main `def main()`
- Defined: `purity_analysis.py:1049`
- Doc: Main entry point for purity analysis.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### get_flat_parameters `def get_flat_parameters(self)`
- Defined: `purity_analysis.py:52`
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### calculate `def calculate(self, model)`
- Defined: `purity_analysis.py:59`
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### calculate `def calculate(self, loss_history)`
- Defined: `purity_analysis.py:66`
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### classify `def classify(self, alpha, temperature)`
- Defined: `purity_analysis.py:73`
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### analyze_polycrystal `def analyze_polycrystal(self, model, pruning_level)`
- Defined: `purity_analysis.py:80`
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### compare `def compare(self, original, polycrystal)`
- Defined: `purity_analysis.py:91`
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, config)`
- Defined: `purity_analysis.py:105`
- Doc: Initialize calculator.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### calculate `def calculate(self, model)`
- Defined: `purity_analysis.py:114`
- Doc: Calculate comprehensive purity metrics.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _compute_layer_purity `def _compute_layer_purity(self, weights)`
- Defined: `purity_analysis.py:159`
- Doc: Compute purity metrics for a single layer.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _delta_to_alpha `def _delta_to_alpha(self, delta)`
- Defined: `purity_analysis.py:177`
- Doc: Convert discretization margin to purity index.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _assess_purity_quality `def _assess_purity_quality(self, alpha, variance)`
- Defined: `purity_analysis.py:191`
- Doc: Assess overall purity quality.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _compute_crystallization_score `def _compute_crystallization_score(self, alpha, variance)`
- Defined: `purity_analysis.py:215`
- Doc: Compute overall crystallization quality score.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, config)`
- Defined: `purity_analysis.py:242`
- Doc: Initialize calculator.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### calculate `def calculate(self, loss_history)`
- Defined: `purity_analysis.py:251`
- Doc: Calculate thermodynamic metrics from loss history.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, config)`
- Defined: `purity_analysis.py:321`
- Doc: Initialize classifier.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### classify `def classify(self, alpha, temperature)`
- Defined: `purity_analysis.py:330`
- Doc: Classify current phase state.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### classify_polycrystal_state `def classify_polycrystal_state(self, original_alpha, original_temp, poly_alpha, poly_temp)`
- Defined: `purity_analysis.py:359`
- Doc: Classify polycrystal state after perturbation.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, config)`
- Defined: `purity_analysis.py:400`
- Doc: Initialize analyzer.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### analyze_polycrystal `def analyze_polycrystal(self, model, pruning_level, loss_history)`
- Defined: `purity_analysis.py:412`
- Doc: Analyze model after weight pruning.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _prune_model `def _prune_model(self, model, sparsity)`
- Defined: `purity_analysis.py:461`
- Doc: Prune smallest magnitude weights.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _assess_structural_integrity `def _assess_structural_integrity(self, alpha, pruning_level)`
- Defined: `purity_analysis.py:480`
- Doc: Assess how well structure survives pruning.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, config)`
- Defined: `purity_analysis.py:508`
- Doc: Initialize comparator.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### compare `def compare(self, original, polycrystal)`
- Defined: `purity_analysis.py:518`
- Doc: Compare original and polycrystal states.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, config)`
- Defined: `purity_analysis.py:583`
- Doc: Initialize loader.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### load `def load(self, checkpoint_path)`
- Defined: `purity_analysis.py:592`
- Doc: Load checkpoint and extract model.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, checkpoint_path, experiment_config, purity_config)`
- Defined: `purity_analysis.py:650`
- Doc: Initialize analyzer.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _load_checkpoint `def _load_checkpoint(self)`
- Defined: `purity_analysis.py:677`
- Doc: Load checkpoint and extract components.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### analyze `def analyze(self)`
- Defined: `purity_analysis.py:694`
- Doc: Perform comprehensive purity analysis.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _print_report `def _print_report(self, results)`
- Defined: `purity_analysis.py:759`
- Doc: Print analysis report to console.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### __init__ `def __init__(self, experiment_config, purity_config)`
- Defined: `purity_analysis.py:825`
- Doc: Initialize pipeline.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### process_checkpoint `def process_checkpoint(self, checkpoint_path, output_dir)`
- Defined: `purity_analysis.py:840`
- Doc: Process single checkpoint.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### process_directory `def process_directory(self, checkpoint_dir, n_latest, output_dir)`
- Defined: `purity_analysis.py:874`
- Doc: Process all checkpoints in directory.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### generate_summary `def generate_summary(self, all_results, output_dir)`
- Defined: `purity_analysis.py:917`
- Doc: Generate summary statistics across all checkpoints.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

### _generate_text_report `def _generate_text_report(self, summary, output_dir)`
- Defined: `purity_analysis.py:996`
- Doc: Generate human-readable text report.
- Depends on: `new_experiment/config.py`, `new_experiment/models.py`

## realtime_train.py

### main `def main()`
- Defined: `realtime_train.py:1527`
- Doc: Main entry point.

### calculate `def calculate(self)`
- Defined: `realtime_train.py:134`
- Doc: Calculate metrics and return dictionary of results.

### forward `def forward(self, x)`
- Defined: `realtime_train.py:143`
- Doc: Forward pass returning logits and latent representation.

### get_pre_activations `def get_pre_activations(self, x)`
- Defined: `realtime_train.py:148`
- Doc: Get pre-activation tensors for complexity analysis.

### get_flat_parameters `def get_flat_parameters(self)`
- Defined: `realtime_train.py:153`
- Doc: Get flattened parameter vector.

### save `def save(self, state, path)`
- Defined: `realtime_train.py:162`
- Doc: Save checkpoint and return path.

### load `def load(self, path)`
- Defined: `realtime_train.py:167`
- Doc: Load checkpoint from path.

### should_checkpoint `def should_checkpoint(self)`
- Defined: `realtime_train.py:172`
- Doc: Determine if checkpoint should be saved.

### __init__ `def __init__(self, input_dim, hidden_dim, output_dim)`
- Defined: `realtime_train.py:180`

### get_pre_activations `def get_pre_activations(self, x)`
- Defined: `realtime_train.py:190`
- Doc: Get pre-activation tensors for LC calculation.

### forward `def forward(self, x)`
- Defined: `realtime_train.py:197`
- Doc: Forward pass returning logits and latent representation.

### get_flat_parameters `def get_flat_parameters(self)`
- Defined: `realtime_train.py:206`
- Doc: Get flattened parameter vector.

### __init__ `def __init__(self, model_dim, sae_dim)`
- Defined: `realtime_train.py:214`

### forward `def forward(self, x)`
- Defined: `realtime_train.py:224`
- Doc: Encode and decode with ReLU activation.

### compute_superposition_metrics `def compute_superposition_metrics(self, z_encoded)`
- Defined: `realtime_train.py:230`
- Doc: Calculate psi (superposition coefficient) and effective features.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:248`

### generate `def generate(self, n_bits, k_bits, dataset_size)`
- Defined: `realtime_train.py:251`
- Doc: Generate random binary vectors with k-bit parity labels.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:262`

### calculate `def calculate(self, model, x_batch)`
- Defined: `realtime_train.py:266`
- Doc: Measure LC as count of near-zero pre-activations.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:291`

### accumulate_gradient `def accumulate_gradient(self, model)`
- Defined: `realtime_train.py:297`
- Doc: Store current gradient vector.

### calculate_kappa `def calculate_kappa(self)`
- Defined: `realtime_train.py:311`
- Doc: Calculate condition number of gradient covariance matrix.

### reset `def reset(self)`
- Defined: `realtime_train.py:344`
- Doc: Clear gradient buffer.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:352`

### calculate `def calculate(self, gradient_covariance)`
- Defined: `realtime_train.py:355`
- Doc: Calculate effective temperature and Planck constant.

### calculate `def calculate(self, model)`
- Defined: `realtime_train.py:415`
- Doc: Calculate mean squared distance to nearest integer.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:427`

### compute_all_metrics `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, step)`
- Defined: `realtime_train.py:434`
- Doc: Compute comprehensive metric suite.

### accumulate_gradient `def accumulate_gradient(self, model)`
- Defined: `realtime_train.py:488`
- Doc: Accumulate gradient for kappa calculation.

### reset `def reset(self)`
- Defined: `realtime_train.py:492`
- Doc: Reset all stateful calculators.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:500`

### save `def save(self, state, path)`
- Defined: `realtime_train.py:506`
- Doc: Save checkpoint to disk.

### load `def load(self, path)`
- Defined: `realtime_train.py:524`
- Doc: Load checkpoint from disk.

### should_checkpoint `def should_checkpoint(self)`
- Defined: `realtime_train.py:532`
- Doc: Check if checkpoint interval has elapsed.

### get_latest_checkpoint_path `def get_latest_checkpoint_path(self)`
- Defined: `realtime_train.py:537`
- Doc: Get path to latest checkpoint if exists.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:546`

### is_stagnant `def is_stagnant(self, metrics_history, current_step, hidden_dim)`
- Defined: `realtime_train.py:550`
- Doc: Determine if training is stagnant.

### transfer `def transfer(self, previous_model, new_model, stage)`
- Defined: `realtime_train.py:582`
- Doc: Transfer weights with padding/cropping as needed.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:633`

### calculate `def calculate(self, n_bits, hidden_dim, stage)`
- Defined: `realtime_train.py:636`
- Doc: Calculate training parameters for current stage.

### __init__ `def __init__(self, config, seed)`
- Defined: `realtime_train.py:668`

### train_stage `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)`
- Defined: `realtime_train.py:680`
- Doc: Train a single curriculum stage.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:901`

### analyze_seed_results `def analyze_seed_results(self, all_results)`
- Defined: `realtime_train.py:905`
- Doc: Generate comprehensive analysis of all seed results.

### print_analysis_report `def print_analysis_report(self, analysis)`
- Defined: `realtime_train.py:1067`
- Doc: Print comprehensive analysis report to console.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:1160`

### create_seed_training_dynamics `def create_seed_training_dynamics(self, seed_result)`
- Defined: `realtime_train.py:1166`
- Doc: Create training dynamics visualization for a single seed.

### create_aggregate_visualizations `def create_aggregate_visualizations(self, all_results)`
- Defined: `realtime_train.py:1269`
- Doc: Create aggregate visualizations across all seeds.

### __init__ `def __init__(self, config)`
- Defined: `realtime_train.py:1370`

### _signal_handler `def _signal_handler(self, signum, frame)`
- Defined: `realtime_train.py:1381`
- Doc: Handle interrupt signal.

### _set_seed `def _set_seed(self, seed)`
- Defined: `realtime_train.py:1386`
- Doc: Set random seed for reproducibility.

### run_experiment `def run_experiment(self)`
- Defined: `realtime_train.py:1394`
- Doc: Run multi-seed curriculum experiment.

## test.py

### accuracy `def accuracy(model, x, y)`
- Defined: `test.py:31`
- Depends on: `app.py`

### load_base `def load_base()`
- Defined: `test.py:36`
- Depends on: `app.py`

### zero_shot_test `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)`
- Defined: `test.py:43`
- Depends on: `app.py`

## test_wandb_ablation.py

### init_ablation_wandb `def init_ablation_wandb(project_name)`
- Defined: `test_wandb_ablation.py:24`
- Doc: Initialize wandb for ablation experiment
- Depends on: `app.py`

### log_scale_results `def log_scale_results(n_bits, d_h, train_acc_transfer, test_acc_transfer, train_acc_control, test_acc_control, time_elapsed, generalization_success)`
- Defined: `test_wandb_ablation.py:37`
- Doc: Log results for each scale to wandb
- Depends on: `app.py`

### finish_ablation_wandb `def finish_ablation_wandb()`
- Defined: `test_wandb_ablation.py:54`
- Doc: Finish wandb run
- Depends on: `app.py`

### accuracy `def accuracy(model, x, y)`
- Defined: `test_wandb_ablation.py:59`
- Depends on: `app.py`

### load_base `def load_base()`
- Defined: `test_wandb_ablation.py:63`
- Depends on: `app.py`

### zero_shot_test `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)`
- Defined: `test_wandb_ablation.py:69`
- Depends on: `app.py`

## view_streamlit.py

### visualize_3d_geometry `def visualize_3d_geometry(weights_list, phase_name, thermo_metrics)`
- Defined: `view_streamlit.py:256`
- Doc: Complete 3D visualization with clustering and geometry
- Depends on: `app.py`

### visualize_2d_texture `def visualize_2d_texture(weights_list, phase_name, thermo_metrics)`
- Defined: `view_streamlit.py:346`
- Doc: Complete 2D texture: heatmap, distribution, FFT, histogram
- Depends on: `app.py`

### main `def main()`
- Defined: `view_streamlit.py:863`
- Depends on: `app.py`

### compute_metrics `def compute_metrics(weights_list, phase, epoch)`
- Defined: `view_streamlit.py:86`
- Doc: Calculate complete thermodynamic state
- Depends on: `app.py`

### visualize_thermal_engine `def visualize_thermal_engine(thermo_history)`
- Defined: `view_streamlit.py:149`
- Doc: Complete thermal engine visualization
- Depends on: `app.py`

### __init__ `def __init__(self)`
- Defined: `view_streamlit.py:429`
- Depends on: `app.py`

### calculate_adaptive_params `def calculate_adaptive_params(self, n_bits, d_h, stage)`
- Defined: `view_streamlit.py:454`
- Doc: EXACTO app.py: Calcula parámetros adaptativos
- Depends on: `app.py`

### capture_snapshot `def capture_snapshot(self, model, sae, stage, n_bits, d_h, step, metrics)`
- Defined: `view_streamlit.py:473`
- Doc: Capture complete snapshot
- Depends on: `app.py`

### smart_weight_transfer `def smart_weight_transfer(self, prev_model, new_model, stage)`
- Defined: `view_streamlit.py:502`
- Doc: EXACTO app.py: Transferencia inteligente de pesos
- Depends on: `app.py`

### train_stage_complete `def train_stage_complete(self, stage, n_bits, d_h, prev_model)`
- Defined: `view_streamlit.py:527`
- Doc: Train stage with REAL-TIME 3D/2D visualization every 500 steps
- Depends on: `app.py`

### run_full_curriculum `def run_full_curriculum(self)`
- Defined: `view_streamlit.py:821`
- Doc: Execute complete curriculum - EXACTO app.py
- Depends on: `app.py`

## visualizador.py

### load_full_system `def load_full_system(n_bits, d_h, stage)`
- Defined: `visualizador.py:24`
- Doc: Carga el MODELO entrenado y el SAE
- Depends on: `app.py`

### calculate_model_accuracy `def calculate_model_accuracy(model, x, y)`
- Defined: `visualizador.py:50`
- Doc: Calcula la precisión real del modelo cargado
- Depends on: `app.py`

### get_real_activations `def get_real_activations(model, x)`
- Defined: `visualizador.py:58`
- Doc: Obtiene las activaciones latentes REALES del modelo
- Depends on: `app.py`

### extract_sae_metrics `def extract_sae_metrics(sae, h2)`
- Defined: `visualizador.py:64`
- Doc: Extrae métricas del SAE sobre las activaciones reales
- Depends on: `app.py`

### plot_sae_autopsy `def plot_sae_autopsy(data, accuracy, n_bits, d_h, sae)`
- Defined: `visualizador.py:80`
- Doc: Visualización centrada en la verdad del Modelo
- Depends on: `app.py`
