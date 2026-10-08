# root

*Community 1 | 7 files | cohesion 1.00*

## Definition

This community groups 7 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `AdaptiveCurriculumTrainer`, `CompleteCurriculumWrapper`, `ComplexityAnalyzer`, `GrokkingTransformer`, `SuperpositionSAE`, `ThermodynamicAnalyzer`, `__init__`, `accuracy`. Core file: `app.py` (18 symbols). Documented purpose: PoC ABLACIÓN — TRANSFERENCIA ALGORÍTMICA Paridad Binaria Escala: 128 bits | 2048 hidden ZERO-SHOT (sin entrenamiento).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `128bits.py` | py | utility | 3 | yes |
| `2048bits.py` | py | utility | 3 | yes |
| `app.py` | py | utility | 18 | yes |
| `test.py` | py | testing | 3 | yes |
| `test_wandb_ablation.py` | py | testing | 6 | yes |
| `view_streamlit.py` | py | presentation | 13 | yes |
| `visualizador.py` | py | utility | 5 | yes |

## Key Symbols

- `evaluate` (function, `128bits.py:34`) `def evaluate(model, x, y)`
- `load_64bit_model` (function, `128bits.py:39`) `def load_64bit_model()`
- `run_experiment` (function, `128bits.py:49`) `def run_experiment(use_padding)`
- `evaluate` (function, `2048bits.py:44`) `def evaluate(model, x, y)`
- `load_base_model` (function, `2048bits.py:49`) `def load_base_model()`
- `zero_shot_test` (function, `2048bits.py:59`) `def zero_shot_test(prev_model, n_bits, d_h, use_padding)`
- `SuperpositionSAE` (class, `app.py:32`) `class SuperpositionSAE(Module)`
- `__init__` (method, `app.py:33`) `def __init__(self, d_model, d_sae)`
- `forward` (method, `app.py:40`) `def forward(self, x)`
- `get_metrics` (method, `app.py:45`) `def get_metrics(self, z)`
- `ComplexityAnalyzer` (class, `app.py:55`) `class ComplexityAnalyzer`
- `measure_lc` (method, `app.py:57`) `def measure_lc(model, x, epsilon)`
- `GrokkingTransformer` (class, `app.py:67`) `class GrokkingTransformer(Module)`
- `__init__` (method, `app.py:68`) `def __init__(self, d_in, d_h)`
- `get_pre_acts` (method, `app.py:74`) `def get_pre_acts(self, x)`
- `forward` (method, `app.py:80`) `def forward(self, x)`
- `get_parity_dataset` (method, `app.py:87`) `def get_parity_dataset(n_bits, k, size)`
- `AdaptiveCurriculumTrainer` (class, `app.py:92`) `class AdaptiveCurriculumTrainer`
- `__init__` (method, `app.py:93`) `def __init__(self)`
- `calculate_adaptive_params` (method, `app.py:109`) `def calculate_adaptive_params(self, n_bits, d_h, stage)` - Calcula parámetros adaptativos según la complejidad de la etapa
- `smart_weight_transfer` (method, `app.py:126`) `def smart_weight_transfer(self, prev_model, new_model, stage)` - Transferencia inteligente de pesos con padding/interpolación
- `detect_stagnation` (method, `app.py:166`) `def detect_stagnation(self, history, current_lc, d_h, step)` - Detecta si el modelo está estancado y necesita reinicio
- `train_stage` (method, `app.py:184`) `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` - Entrena una etapa individual con parámetros adaptativos
- `run_curriculum` (method, `app.py:316`) `def run_curriculum(self)` - Ejecuta el curriculum completo con adaptación automática
- `accuracy` (function, `test.py:31`) `def accuracy(model, x, y)`
- `load_base` (function, `test.py:36`) `def load_base()`
- `zero_shot_test` (function, `test.py:43`) `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)`
- `init_ablation_wandb` (function, `test_wandb_ablation.py:24`) `def init_ablation_wandb(project_name)` - Initialize wandb for ablation experiment
- `log_scale_results` (function, `test_wandb_ablation.py:37`) `def log_scale_results(n_bits, d_h, train_acc_transfer, test_acc_transfer, train_` - Log results for each scale to wandb
- `finish_ablation_wandb` (function, `test_wandb_ablation.py:54`) `def finish_ablation_wandb()` - Finish wandb run

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 6
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (new_experiment: checkpointing) and community 1 (root).
- [INFERRED] shares_context community 1 <-> 2 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (root) and community 2 (new_experiment: purity_analysis).
- [INFERRED] shares_context community 1 <-> 3 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (root) and community 3 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `128bits.py`
- `2048bits.py`
- `app.py`
- `test.py`
- `test_wandb_ablation.py`
- `view_streamlit.py`
- `visualizador.py`
