# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 22 | **Total Symbols Extracted:** 282 | **Total Imports:** 177

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    realtime_train_py["realtime_train.py (py)"]
    class realtime_train_py mod;
    realtime_train_py_ExperimentConfig["ExperimentConfig"]
    class realtime_train_py_ExperimentConfig cls;
    realtime_train_py --> realtime_train_py_ExperimentConfig
    realtime_train_py_IMetricCalculator["IMetricCalculator"]
    class realtime_train_py_IMetricCalculator cls;
    realtime_train_py --> realtime_train_py_IMetricCalculator
    realtime_train_py_IModelArchitecture["IModelArchitecture"]
    class realtime_train_py_IModelArchitecture cls;
    realtime_train_py --> realtime_train_py_IModelArchitecture
    realtime_train_py_ICheckpointManager["ICheckpointManager"]
    class realtime_train_py_ICheckpointManager cls;
    realtime_train_py --> realtime_train_py_ICheckpointManager
    realtime_train_py_GrokkingTransformer["GrokkingTransformer"]
    class realtime_train_py_GrokkingTransformer cls;
    realtime_train_py --> realtime_train_py_GrokkingTransformer
    new_experiment_streamlit_app_py["streamlit_app.py (py)"]
    class new_experiment_streamlit_app_py mod;
    new_experiment_streamlit_app_py_ThermodynamicAnalyzer["ThermodynamicAnalyzer"]
    class new_experiment_streamlit_app_py_ThermodynamicAnalyzer cls;
    new_experiment_streamlit_app_py --> new_experiment_streamlit_app_py_ThermodynamicAnalyzer
    new_experiment_streamlit_app_py_StreamlitTrainer["StreamlitTrainer"]
    class new_experiment_streamlit_app_py_StreamlitTrainer cls;
    new_experiment_streamlit_app_py --> new_experiment_streamlit_app_py_StreamlitTrainer
    new_experiment_streamlit_app_py_main["main"]
    class new_experiment_streamlit_app_py_main fn;
    new_experiment_streamlit_app_py --> new_experiment_streamlit_app_py_main
    new_experiment_streamlit_app_py_compute_metrics["compute_metrics"]
    class new_experiment_streamlit_app_py_compute_metrics fn;
    new_experiment_streamlit_app_py --> new_experiment_streamlit_app_py_compute_metrics
    new_experiment_streamlit_app_py___init__["__init__"]
    class new_experiment_streamlit_app_py___init__ fn;
    new_experiment_streamlit_app_py --> new_experiment_streamlit_app_py___init__
    view_streamlit_py["view_streamlit.py (py)"]
    class view_streamlit_py mod;
    view_streamlit_py_ThermodynamicAnalyzer["ThermodynamicAnalyzer"]
    class view_streamlit_py_ThermodynamicAnalyzer cls;
    view_streamlit_py --> view_streamlit_py_ThermodynamicAnalyzer
    view_streamlit_py_visualize_3d_geometry["visualize_3d_geometry"]
    class view_streamlit_py_visualize_3d_geometry fn;
    view_streamlit_py --> view_streamlit_py_visualize_3d_geometry
    view_streamlit_py_visualize_2d_texture["visualize_2d_texture"]
    class view_streamlit_py_visualize_2d_texture fn;
    view_streamlit_py --> view_streamlit_py_visualize_2d_texture
    view_streamlit_py_CompleteCurriculumWrapper["CompleteCurriculumWrapper"]
    class view_streamlit_py_CompleteCurriculumWrapper cls;
    view_streamlit_py --> view_streamlit_py_CompleteCurriculumWrapper
    view_streamlit_py_main["main"]
    class view_streamlit_py_main fn;
    view_streamlit_py --> view_streamlit_py_main
    purity_analysis_py["purity_analysis.py (py)"]
    class purity_analysis_py mod;
    purity_analysis_py_PurityConfig["PurityConfig"]
    class purity_analysis_py_PurityConfig cls;
    purity_analysis_py --> purity_analysis_py_PurityConfig
    purity_analysis_py_IModel["IModel"]
    class purity_analysis_py_IModel cls;
    purity_analysis_py --> purity_analysis_py_IModel
    purity_analysis_py_IPurityIndexCalculator["IPurityIndexCalculator"]
    class purity_analysis_py_IPurityIndexCalculator cls;
    purity_analysis_py --> purity_analysis_py_IPurityIndexCalculator
    purity_analysis_py_IEffectiveTemperatureCalculator["IEffectiveTemperatureCalculator"]
    class purity_analysis_py_IEffectiveTemperatureCalculator cls;
    purity_analysis_py --> purity_analysis_py_IEffectiveTemperatureCalculator
    purity_analysis_py_IPhaseClassifier["IPhaseClassifier"]
    class purity_analysis_py_IPhaseClassifier cls;
    purity_analysis_py --> purity_analysis_py_IPhaseClassifier
    new_experiment_training_py["training.py (py)"]
    class new_experiment_training_py mod;
    new_experiment_training_py_CurriculumStageTrainer["CurriculumStageTrainer"]
    class new_experiment_training_py_CurriculumStageTrainer cls;
    new_experiment_training_py --> new_experiment_training_py_CurriculumStageTrainer
    new_experiment_training_py___init__["__init__"]
    class new_experiment_training_py___init__ fn;
    new_experiment_training_py --> new_experiment_training_py___init__
    new_experiment_training_py_train_stage["train_stage"]
    class new_experiment_training_py_train_stage fn;
    new_experiment_training_py --> new_experiment_training_py_train_stage
    new_experiment_training_py__create_checkpoint_state["_create_checkpoint_state"]
    class new_experiment_training_py__create_checkpoint_state fn;
    new_experiment_training_py --> new_experiment_training_py__create_checkpoint_state
    visualizador_py["visualizador.py (py)"]
    class visualizador_py mod;
    visualizador_py_load_full_system["load_full_system"]
    class visualizador_py_load_full_system fn;
    visualizador_py --> visualizador_py_load_full_system
    visualizador_py_calculate_model_accuracy["calculate_model_accuracy"]
    class visualizador_py_calculate_model_accuracy fn;
    visualizador_py --> visualizador_py_calculate_model_accuracy
    visualizador_py_get_real_activations["get_real_activations"]
    class visualizador_py_get_real_activations fn;
    visualizador_py --> visualizador_py_get_real_activations
    visualizador_py_extract_sae_metrics["extract_sae_metrics"]
    class visualizador_py_extract_sae_metrics fn;
    visualizador_py --> visualizador_py_extract_sae_metrics
    visualizador_py_plot_sae_autopsy["plot_sae_autopsy"]
    class visualizador_py_plot_sae_autopsy fn;
    visualizador_py --> visualizador_py_plot_sae_autopsy
    app_wandb_py["app_wandb.py (py)"]
    class app_wandb_py mod;
    app_wandb_py_init_wandb["init_wandb"]
    class app_wandb_py_init_wandb fn;
    app_wandb_py --> app_wandb_py_init_wandb
    app_wandb_py_log_training_step["log_training_step"]
    class app_wandb_py_log_training_step fn;
    app_wandb_py --> app_wandb_py_log_training_step
    app_wandb_py_finish_wandb["finish_wandb"]
    class app_wandb_py_finish_wandb fn;
    app_wandb_py --> app_wandb_py_finish_wandb
    app_wandb_py_SuperpositionSAE["SuperpositionSAE"]
    class app_wandb_py_SuperpositionSAE cls;
    app_wandb_py --> app_wandb_py_SuperpositionSAE
    app_wandb_py_ComplexityAnalyzer["ComplexityAnalyzer"]
    class app_wandb_py_ComplexityAnalyzer cls;
    app_wandb_py --> app_wandb_py_ComplexityAnalyzer
    new_experiment_metrics_py["metrics.py (py)"]
    class new_experiment_metrics_py mod;
    new_experiment_metrics_py_IMetricCalculator["IMetricCalculator"]
    class new_experiment_metrics_py_IMetricCalculator cls;
    new_experiment_metrics_py --> new_experiment_metrics_py_IMetricCalculator
    new_experiment_metrics_py_LocalComplexityCalculator["LocalComplexityCalculator"]
    class new_experiment_metrics_py_LocalComplexityCalculator cls;
    new_experiment_metrics_py --> new_experiment_metrics_py_LocalComplexityCalculator
    new_experiment_metrics_py_GradientCovarianceCalculator["GradientCovarianceCalculator"]
    class new_experiment_metrics_py_GradientCovarianceCalculator cls;
    new_experiment_metrics_py --> new_experiment_metrics_py_GradientCovarianceCalculator
    new_experiment_metrics_py_ThermodynamicMetricsCalculator["ThermodynamicMetricsCalculator"]
    class new_experiment_metrics_py_ThermodynamicMetricsCalculator cls;
    new_experiment_metrics_py --> new_experiment_metrics_py_ThermodynamicMetricsCalculator
    new_experiment_metrics_py_DeltaCalculator["DeltaCalculator"]
    class new_experiment_metrics_py_DeltaCalculator cls;
    new_experiment_metrics_py --> new_experiment_metrics_py_DeltaCalculator
    new_experiment_test_framework_py["test_framework.py (py)"]
    class new_experiment_test_framework_py mod;
    new_experiment_test_framework_py_test_configuration["test_configuration"]
    class new_experiment_test_framework_py_test_configuration fn;
    new_experiment_test_framework_py --> new_experiment_test_framework_py_test_configuration
    new_experiment_test_framework_py_test_data_generation["test_data_generation"]
    class new_experiment_test_framework_py_test_data_generation fn;
    new_experiment_test_framework_py --> new_experiment_test_framework_py_test_data_generation
    new_experiment_test_framework_py_test_models["test_models"]
    class new_experiment_test_framework_py_test_models fn;
    new_experiment_test_framework_py --> new_experiment_test_framework_py_test_models
    new_experiment_test_framework_py_test_metrics["test_metrics"]
    class new_experiment_test_framework_py_test_metrics fn;
    new_experiment_test_framework_py --> new_experiment_test_framework_py_test_metrics
    new_experiment_test_framework_py_test_checkpointing["test_checkpointing"]
    class new_experiment_test_framework_py_test_checkpointing fn;
    new_experiment_test_framework_py --> new_experiment_test_framework_py_test_checkpointing
    app_py["app.py (py)"]
    class app_py mod;
    app_py_SuperpositionSAE["SuperpositionSAE"]
    class app_py_SuperpositionSAE cls;
    app_py --> app_py_SuperpositionSAE
    app_py_ComplexityAnalyzer["ComplexityAnalyzer"]
    class app_py_ComplexityAnalyzer cls;
    app_py --> app_py_ComplexityAnalyzer
    app_py_GrokkingTransformer["GrokkingTransformer"]
    class app_py_GrokkingTransformer cls;
    app_py --> app_py_GrokkingTransformer
    app_py_get_parity_dataset["get_parity_dataset"]
    class app_py_get_parity_dataset fn;
    app_py --> app_py_get_parity_dataset
    app_py_AdaptiveCurriculumTrainer["AdaptiveCurriculumTrainer"]
    class app_py_AdaptiveCurriculumTrainer cls;
    app_py --> app_py_AdaptiveCurriculumTrainer
    new_experiment_checkpointing_py["checkpointing.py (py)"]
    class new_experiment_checkpointing_py mod;
    new_experiment_checkpointing_py_ICheckpointManager["ICheckpointManager"]
    class new_experiment_checkpointing_py_ICheckpointManager cls;
    new_experiment_checkpointing_py --> new_experiment_checkpointing_py_ICheckpointManager
    new_experiment_checkpointing_py_CheckpointManager["CheckpointManager"]
    class new_experiment_checkpointing_py_CheckpointManager cls;
    new_experiment_checkpointing_py --> new_experiment_checkpointing_py_CheckpointManager
    new_experiment_checkpointing_py_save["save"]
    class new_experiment_checkpointing_py_save fn;
    new_experiment_checkpointing_py --> new_experiment_checkpointing_py_save
    new_experiment_checkpointing_py_load["load"]
    class new_experiment_checkpointing_py_load fn;
    new_experiment_checkpointing_py --> new_experiment_checkpointing_py_load
    new_experiment_checkpointing_py_should_checkpoint["should_checkpoint"]
    class new_experiment_checkpointing_py_should_checkpoint fn;
    new_experiment_checkpointing_py --> new_experiment_checkpointing_py_should_checkpoint
    new_experiment_models_py["models.py (py)"]
    class new_experiment_models_py mod;
    new_experiment_models_py_IModelArchitecture["IModelArchitecture"]
    class new_experiment_models_py_IModelArchitecture cls;
    new_experiment_models_py --> new_experiment_models_py_IModelArchitecture
    new_experiment_models_py_GrokkingTransformer["GrokkingTransformer"]
    class new_experiment_models_py_GrokkingTransformer cls;
    new_experiment_models_py --> new_experiment_models_py_GrokkingTransformer
    new_experiment_models_py_SuperpositionSAE["SuperpositionSAE"]
    class new_experiment_models_py_SuperpositionSAE cls;
    new_experiment_models_py --> new_experiment_models_py_SuperpositionSAE
    new_experiment_models_py_forward["forward"]
    class new_experiment_models_py_forward fn;
    new_experiment_models_py --> new_experiment_models_py_forward
    new_experiment_models_py_get_pre_activations["get_pre_activations"]
    class new_experiment_models_py_get_pre_activations fn;
    new_experiment_models_py --> new_experiment_models_py_get_pre_activations
    new_experiment_main_py["main.py (py)"]
    class new_experiment_main_py mod;
    new_experiment_main_py_MultiSeedCurriculumRunner["MultiSeedCurriculumRunner"]
    class new_experiment_main_py_MultiSeedCurriculumRunner cls;
    new_experiment_main_py --> new_experiment_main_py_MultiSeedCurriculumRunner
    new_experiment_main_py_main["main"]
    class new_experiment_main_py_main fn;
    new_experiment_main_py --> new_experiment_main_py_main
    new_experiment_main_py___init__["__init__"]
    class new_experiment_main_py___init__ fn;
    new_experiment_main_py --> new_experiment_main_py___init__
    new_experiment_main_py__set_seed["_set_seed"]
    class new_experiment_main_py__set_seed fn;
    new_experiment_main_py --> new_experiment_main_py__set_seed
    new_experiment_main_py_run_single_seed["run_single_seed"]
    class new_experiment_main_py_run_single_seed fn;
    new_experiment_main_py --> new_experiment_main_py_run_single_seed
    new_experiment_config_py["config.py (py)"]
    class new_experiment_config_py mod;
    new_experiment_config_py_ExperimentConfig["ExperimentConfig"]
    class new_experiment_config_py_ExperimentConfig cls;
    new_experiment_config_py --> new_experiment_config_py_ExperimentConfig
    new_experiment_config_py_get_adaptive_train_size["get_adaptive_train_size"]
    class new_experiment_config_py_get_adaptive_train_size fn;
    new_experiment_config_py --> new_experiment_config_py_get_adaptive_train_size
    new_experiment_config_py_get_adaptive_weight_decay["get_adaptive_weight_decay"]
    class new_experiment_config_py_get_adaptive_weight_decay fn;
    new_experiment_config_py --> new_experiment_config_py_get_adaptive_weight_decay
    new_experiment_config_py_get_adaptive_max_steps["get_adaptive_max_steps"]
    class new_experiment_config_py_get_adaptive_max_steps fn;
    new_experiment_config_py --> new_experiment_config_py_get_adaptive_max_steps
    test_wandb_ablation_py["test_wandb_ablation.py (py)"]
    class test_wandb_ablation_py mod;
    test_wandb_ablation_py_init_ablation_wandb["init_ablation_wandb"]
    class test_wandb_ablation_py_init_ablation_wandb fn;
    test_wandb_ablation_py --> test_wandb_ablation_py_init_ablation_wandb
    test_wandb_ablation_py_log_scale_results["log_scale_results"]
    class test_wandb_ablation_py_log_scale_results fn;
    test_wandb_ablation_py --> test_wandb_ablation_py_log_scale_results
    test_wandb_ablation_py_finish_ablation_wandb["finish_ablation_wandb"]
    class test_wandb_ablation_py_finish_ablation_wandb fn;
    test_wandb_ablation_py --> test_wandb_ablation_py_finish_ablation_wandb
    test_wandb_ablation_py_accuracy["accuracy"]
    class test_wandb_ablation_py_accuracy fn;
    test_wandb_ablation_py --> test_wandb_ablation_py_accuracy
    test_wandb_ablation_py_load_base["load_base"]
    class test_wandb_ablation_py_load_base fn;
    test_wandb_ablation_py --> test_wandb_ablation_py_load_base
    new_experiment_training_dynamics_py["training_dynamics.py (py)"]
    class new_experiment_training_dynamics_py mod;
    new_experiment_training_dynamics_py_SmartWeightTransfer["SmartWeightTransfer"]
    class new_experiment_training_dynamics_py_SmartWeightTransfer cls;
    new_experiment_training_dynamics_py --> new_experiment_training_dynamics_py_SmartWeightTransfer
    new_experiment_training_dynamics_py_StagnationDetector["StagnationDetector"]
    class new_experiment_training_dynamics_py_StagnationDetector cls;
    new_experiment_training_dynamics_py --> new_experiment_training_dynamics_py_StagnationDetector
    new_experiment_training_dynamics_py_transfer["transfer"]
    class new_experiment_training_dynamics_py_transfer fn;
    new_experiment_training_dynamics_py --> new_experiment_training_dynamics_py_transfer
    new_experiment_training_dynamics_py___init__["__init__"]
    class new_experiment_training_dynamics_py___init__ fn;
    new_experiment_training_dynamics_py --> new_experiment_training_dynamics_py___init__
    new_experiment_training_dynamics_py_is_stagnant["is_stagnant"]
    class new_experiment_training_dynamics_py_is_stagnant fn;
    new_experiment_training_dynamics_py --> new_experiment_training_dynamics_py_is_stagnant
    n_128bits_py["128bits.py (py)"]
    class n_128bits_py mod;
    n_128bits_py_evaluate["evaluate"]
    class n_128bits_py_evaluate fn;
    n_128bits_py --> n_128bits_py_evaluate
    n_128bits_py_load_64bit_model["load_64bit_model"]
    class n_128bits_py_load_64bit_model fn;
    n_128bits_py --> n_128bits_py_load_64bit_model
    n_128bits_py_run_experiment["run_experiment"]
    class n_128bits_py_run_experiment fn;
    n_128bits_py --> n_128bits_py_run_experiment
    new_experiment_wandb_integration_py["wandb_integration.py (py)"]
    class new_experiment_wandb_integration_py mod;
    new_experiment_wandb_integration_py_WandBLogger["WandBLogger"]
    class new_experiment_wandb_integration_py_WandBLogger cls;
    new_experiment_wandb_integration_py --> new_experiment_wandb_integration_py_WandBLogger
    new_experiment_wandb_integration_py___init__["__init__"]
    class new_experiment_wandb_integration_py___init__ fn;
    new_experiment_wandb_integration_py --> new_experiment_wandb_integration_py___init__
    new_experiment_wandb_integration_py_initialize["initialize"]
    class new_experiment_wandb_integration_py_initialize fn;
    new_experiment_wandb_integration_py --> new_experiment_wandb_integration_py_initialize
    new_experiment_wandb_integration_py_log_metrics["log_metrics"]
    class new_experiment_wandb_integration_py_log_metrics fn;
    new_experiment_wandb_integration_py --> new_experiment_wandb_integration_py_log_metrics
    new_experiment_wandb_integration_py_finish["finish"]
    class new_experiment_wandb_integration_py_finish fn;
    new_experiment_wandb_integration_py --> new_experiment_wandb_integration_py_finish
    n_2048bits_py["2048bits.py (py)"]
    class n_2048bits_py mod;
    n_2048bits_py_evaluate["evaluate"]
    class n_2048bits_py_evaluate fn;
    n_2048bits_py --> n_2048bits_py_evaluate
    n_2048bits_py_load_base_model["load_base_model"]
    class n_2048bits_py_load_base_model fn;
    n_2048bits_py --> n_2048bits_py_load_base_model
    n_2048bits_py_zero_shot_test["zero_shot_test"]
    class n_2048bits_py_zero_shot_test fn;
    n_2048bits_py --> n_2048bits_py_zero_shot_test
    new_experiment_data_generation_py["data_generation.py (py)"]
    class new_experiment_data_generation_py mod;
    new_experiment_data_generation_py_ParityDatasetGenerator["ParityDatasetGenerator"]
    class new_experiment_data_generation_py_ParityDatasetGenerator cls;
    new_experiment_data_generation_py --> new_experiment_data_generation_py_ParityDatasetGenerator
    new_experiment_data_generation_py___init__["__init__"]
    class new_experiment_data_generation_py___init__ fn;
    new_experiment_data_generation_py --> new_experiment_data_generation_py___init__
    new_experiment_data_generation_py_generate["generate"]
    class new_experiment_data_generation_py_generate fn;
    new_experiment_data_generation_py --> new_experiment_data_generation_py_generate
    test_py["test.py (py)"]
    class test_py mod;
    test_py_accuracy["accuracy"]
    class test_py_accuracy fn;
    test_py --> test_py_accuracy
    test_py_load_base["load_base"]
    class test_py_load_base fn;
    test_py --> test_py_load_base
    test_py_zero_shot_test["zero_shot_test"]
    class test_py_zero_shot_test fn;
    test_py --> test_py_zero_shot_test
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_time["time"]
    class ext_time ext;
    n_128bits_py -.->|imports| ext_time
    ext_torch["torch"]
    class ext_torch ext;
    n_128bits_py -.->|imports| ext_torch
    ext_copy["copy"]
    class ext_copy ext;
    n_128bits_py -.->|imports| ext_copy
    ext_app["app"]
    class ext_app ext;
    n_128bits_py -.->|imports| ext_app
    n_2048bits_py -.->|imports| ext_time
    n_2048bits_py -.->|imports| ext_torch
    n_2048bits_py -.->|imports| ext_app
    app_py -.->|imports| ext_torch
    ext_torch_nn["torch.nn"]
    class ext_torch_nn ext;
    app_py -.->|imports| ext_torch_nn
    ext_torch_nn_functional["torch.nn.functional"]
    class ext_torch_nn_functional ext;
    app_py -.->|imports| ext_torch_nn_functional
    ext_math["math"]
    class ext_math ext;
    app_py -.->|imports| ext_math
    ext_os["os"]
    class ext_os ext;
    app_py -.->|imports| ext_os
    ext_numpy["numpy"]
    class ext_numpy ext;
    app_py -.->|imports| ext_numpy
    app_py -.->|imports| ext_copy
    app_wandb_py -.->|imports| ext_torch
    app_wandb_py -.->|imports| ext_torch_nn
    app_wandb_py -.->|imports| ext_torch_nn_functional
    app_wandb_py -.->|imports| ext_math
    app_wandb_py -.->|imports| ext_os
    app_wandb_py -.->|imports| ext_numpy
    app_wandb_py -.->|imports| ext_copy
    ext_wandb["wandb"]
    class ext_wandb ext;
    app_wandb_py -.->|imports| ext_wandb
    new_experiment_checkpointing_py -.->|imports| ext_torch
    new_experiment_checkpointing_py -.->|imports| ext_time
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    new_experiment_checkpointing_py -.->|imports| ext_pathlib
    ext_typing["typing"]
    class ext_typing ext;
    new_experiment_checkpointing_py -.->|imports| ext_typing
    ext_abc["abc"]
    class ext_abc ext;
    new_experiment_checkpointing_py -.->|imports| ext_abc
    ext_datetime["datetime"]
    class ext_datetime ext;
    new_experiment_checkpointing_py -.->|imports| ext_datetime
    ext_config["config"]
    class ext_config ext;
    new_experiment_checkpointing_py -.->|imports| ext_config
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    new_experiment_config_py -.->|imports| ext_dataclasses
    new_experiment_config_py -.->|imports| ext_typing
    new_experiment_config_py -.->|imports| ext_torch
    new_experiment_config_py -.->|imports| ext_math
    new_experiment_config_py -.->|imports| ext_math
    new_experiment_config_py -.->|imports| ext_math
    new_experiment_data_generation_py -.->|imports| ext_torch
    new_experiment_data_generation_py -.->|imports| ext_typing
    new_experiment_data_generation_py -.->|imports| ext_config
    ext_argparse["argparse"]
    class ext_argparse ext;
    new_experiment_main_py -.->|imports| ext_argparse
    new_experiment_main_py -.->|imports| ext_torch
    new_experiment_main_py -.->|imports| ext_numpy
    new_experiment_main_py -.->|imports| ext_pathlib
    new_experiment_main_py -.->|imports| ext_config
    ext_training["training"]
    class ext_training ext;
    new_experiment_main_py -.->|imports| ext_training
    new_experiment_metrics_py -.->|imports| ext_torch
    new_experiment_metrics_py -.->|imports| ext_torch_nn
    new_experiment_metrics_py -.->|imports| ext_numpy
    new_experiment_metrics_py -.->|imports| ext_typing
    ext_collections["collections"]
    class ext_collections ext;
    new_experiment_metrics_py -.->|imports| ext_collections
    new_experiment_metrics_py -.->|imports| ext_abc
    new_experiment_metrics_py -.->|imports| ext_config
    ext_models["models"]
    class ext_models ext;
    new_experiment_metrics_py -.->|imports| ext_models
    new_experiment_models_py -.->|imports| ext_torch
    new_experiment_models_py -.->|imports| ext_torch_nn
    new_experiment_models_py -.->|imports| ext_torch_nn_functional
    new_experiment_models_py -.->|imports| ext_math
    new_experiment_models_py -.->|imports| ext_typing
    new_experiment_models_py -.->|imports| ext_abc
    ext_streamlit["streamlit"]
    class ext_streamlit ext;
    new_experiment_streamlit_app_py -.->|imports| ext_streamlit
    new_experiment_streamlit_app_py -.->|imports| ext_torch
    new_experiment_streamlit_app_py -.->|imports| ext_torch_nn_functional
    ext_plotly_graph_objects["plotly.graph_objects"]
    class ext_plotly_graph_objects ext;
    new_experiment_streamlit_app_py -.->|imports| ext_plotly_graph_objects
    ext_plotly_subplots["plotly.subplots"]
    class ext_plotly_subplots ext;
    new_experiment_streamlit_app_py -.->|imports| ext_plotly_subplots
    new_experiment_streamlit_app_py -.->|imports| ext_numpy
    ext_sklearn_decomposition["sklearn.decomposition"]
    class ext_sklearn_decomposition ext;
    new_experiment_streamlit_app_py -.->|imports| ext_sklearn_decomposition
    ext_sklearn_cluster["sklearn.cluster"]
    class ext_sklearn_cluster ext;
    new_experiment_streamlit_app_py -.->|imports| ext_sklearn_cluster
    ext_scipy_spatial_distance["scipy.spatial.distance"]
    class ext_scipy_spatial_distance ext;
    new_experiment_streamlit_app_py -.->|imports| ext_scipy_spatial_distance
    ext_scipy["scipy"]
    class ext_scipy ext;
    new_experiment_streamlit_app_py -.->|imports| ext_scipy
    new_experiment_streamlit_app_py -.->|imports| ext_time
    new_experiment_streamlit_app_py -.->|imports| ext_pathlib
    new_experiment_streamlit_app_py -.->|imports| ext_typing
    new_experiment_streamlit_app_py -.->|imports| ext_copy
    new_experiment_streamlit_app_py -.->|imports| ext_config
    new_experiment_streamlit_app_py -.->|imports| ext_models
    ext_data_generation["data_generation"]
    class ext_data_generation ext;
    new_experiment_streamlit_app_py -.->|imports| ext_data_generation
    ext_metrics["metrics"]
    class ext_metrics ext;
    new_experiment_streamlit_app_py -.->|imports| ext_metrics
    ext_training_dynamics["training_dynamics"]
    class ext_training_dynamics ext;
    new_experiment_streamlit_app_py -.->|imports| ext_training_dynamics
    ext_wandb_integration["wandb_integration"]
    class ext_wandb_integration ext;
    new_experiment_streamlit_app_py -.->|imports| ext_wandb_integration
    new_experiment_test_framework_py -.->|imports| ext_torch
    new_experiment_test_framework_py -.->|imports| ext_numpy
    new_experiment_test_framework_py -.->|imports| ext_config
    new_experiment_test_framework_py -.->|imports| ext_models
    new_experiment_test_framework_py -.->|imports| ext_data_generation
    new_experiment_test_framework_py -.->|imports| ext_metrics
    ext_checkpointing["checkpointing"]
    class ext_checkpointing ext;
    new_experiment_test_framework_py -.->|imports| ext_checkpointing
    new_experiment_test_framework_py -.->|imports| ext_training_dynamics
    new_experiment_training_py -.->|imports| ext_torch
    new_experiment_training_py -.->|imports| ext_torch_nn_functional
    ext_torch_optim["torch.optim"]
    class ext_torch_optim ext;
    new_experiment_training_py -.->|imports| ext_torch_optim
    new_experiment_training_py -.->|imports| ext_typing
    new_experiment_training_py -.->|imports| ext_copy
    new_experiment_training_py -.->|imports| ext_config
    new_experiment_training_py -.->|imports| ext_models
    new_experiment_training_py -.->|imports| ext_data_generation
    new_experiment_training_py -.->|imports| ext_metrics
    new_experiment_training_py -.->|imports| ext_checkpointing
    new_experiment_training_py -.->|imports| ext_training_dynamics
    new_experiment_training_py -.->|imports| ext_wandb_integration
    new_experiment_training_py -.->|imports| ext_datetime
    new_experiment_training_dynamics_py -.->|imports| ext_torch
    new_experiment_training_dynamics_py -.->|imports| ext_torch_nn
    new_experiment_training_dynamics_py -.->|imports| ext_typing
    new_experiment_training_dynamics_py -.->|imports| ext_config
    new_experiment_wandb_integration_py -.->|imports| ext_typing
    new_experiment_wandb_integration_py -.->|imports| ext_wandb
    new_experiment_wandb_integration_py -.->|imports| ext_config
    purity_analysis_py -.->|imports| ext_torch
    purity_analysis_py -.->|imports| ext_torch_nn
    purity_analysis_py -.->|imports| ext_numpy
    ext_json["json"]
    class ext_json ext;
    purity_analysis_py -.->|imports| ext_json
    purity_analysis_py -.->|imports| ext_os
    purity_analysis_py -.->|imports| ext_argparse
    purity_analysis_py -.->|imports| ext_datetime
    purity_analysis_py -.->|imports| ext_typing
    purity_analysis_py -.->|imports| ext_pathlib
    ext_glob["glob"]
    class ext_glob ext;
    purity_analysis_py -.->|imports| ext_glob
    purity_analysis_py -.->|imports| ext_dataclasses
    ext_scipy_stats["scipy.stats"]
    class ext_scipy_stats ext;
    purity_analysis_py -.->|imports| ext_scipy_stats
    ext_new_experiment_config["new_experiment.config"]
    class ext_new_experiment_config ext;
    purity_analysis_py -.->|imports| ext_new_experiment_config
    ext_new_experiment_models["new_experiment.models"]
    class ext_new_experiment_models ext;
    purity_analysis_py -.->|imports| ext_new_experiment_models
    ext_traceback["traceback"]
    class ext_traceback ext;
    purity_analysis_py -.->|imports| ext_traceback
    realtime_train_py -.->|imports| ext_torch
    realtime_train_py -.->|imports| ext_torch_nn
    realtime_train_py -.->|imports| ext_torch_nn_functional
    realtime_train_py -.->|imports| ext_torch_optim
    realtime_train_py -.->|imports| ext_numpy
    realtime_train_py -.->|imports| ext_math
    realtime_train_py -.->|imports| ext_json
    realtime_train_py -.->|imports| ext_time
    ext_signal["signal"]
    class ext_signal ext;
    realtime_train_py -.->|imports| ext_signal
    ext_sys["sys"]
    class ext_sys ext;
    realtime_train_py -.->|imports| ext_sys
    realtime_train_py -.->|imports| ext_pathlib
    realtime_train_py -.->|imports| ext_dataclasses
    realtime_train_py -.->|imports| ext_typing
    realtime_train_py -.->|imports| ext_collections
    realtime_train_py -.->|imports| ext_datetime
    realtime_train_py -.->|imports| ext_copy
    realtime_train_py -.->|imports| ext_abc
    ext_warnings["warnings"]
    class ext_warnings ext;
    realtime_train_py -.->|imports| ext_warnings
    ext_matplotlib["matplotlib"]
    class ext_matplotlib ext;
    realtime_train_py -.->|imports| ext_matplotlib
    ext_matplotlib_pyplot["matplotlib.pyplot"]
    class ext_matplotlib_pyplot ext;
    realtime_train_py -.->|imports| ext_matplotlib_pyplot
    ext_matplotlib_gridspec["matplotlib.gridspec"]
    class ext_matplotlib_gridspec ext;
    realtime_train_py -.->|imports| ext_matplotlib_gridspec
    realtime_train_py -.->|imports| ext_argparse
    test_py -.->|imports| ext_time
    test_py -.->|imports| ext_torch
    test_py -.->|imports| ext_app
    test_wandb_ablation_py -.->|imports| ext_time
    test_wandb_ablation_py -.->|imports| ext_torch
    test_wandb_ablation_py -.->|imports| ext_wandb
    test_wandb_ablation_py -.->|imports| ext_app
    view_streamlit_py -.->|imports| ext_streamlit
    view_streamlit_py -.->|imports| ext_numpy
    view_streamlit_py -.->|imports| ext_plotly_graph_objects
    view_streamlit_py -.->|imports| ext_plotly_subplots
    view_streamlit_py -.->|imports| ext_sklearn_decomposition
    view_streamlit_py -.->|imports| ext_sklearn_cluster
    view_streamlit_py -.->|imports| ext_scipy_spatial_distance
    view_streamlit_py -.->|imports| ext_scipy
    view_streamlit_py -.->|imports| ext_torch
    view_streamlit_py -.->|imports| ext_torch_nn
    view_streamlit_py -.->|imports| ext_torch_nn_functional
    view_streamlit_py -.->|imports| ext_math
    view_streamlit_py -.->|imports| ext_sys
    view_streamlit_py -.->|imports| ext_os
    view_streamlit_py -.->|imports| ext_copy
    view_streamlit_py -.->|imports| ext_datetime
    view_streamlit_py -.->|imports| ext_app
    visualizador_py -.->|imports| ext_os
    visualizador_py -.->|imports| ext_torch
    visualizador_py -.->|imports| ext_numpy
    visualizador_py -.->|imports| ext_matplotlib_pyplot
    ext_mpl_toolkits_mplot3d["mpl_toolkits.mplot3d"]
    class ext_mpl_toolkits_mplot3d ext;
    visualizador_py -.->|imports| ext_mpl_toolkits_mplot3d
    visualizador_py -.->|imports| ext_sklearn_decomposition
    ext_sklearn_manifold["sklearn.manifold"]
    class ext_sklearn_manifold ext;
    visualizador_py -.->|imports| ext_sklearn_manifold
    visualizador_py -.->|imports| ext_warnings
    visualizador_py -.->|imports| ext_app
    visualizador_py -.->|imports| ext_traceback
```

---

## Architecture Reference

### PY (21 files)

#### `128bits.py`
**Path:** `128bits.py`

**Functions:**
- `evaluate` (line 34) `def evaluate(model, x, y)`
- `load_64bit_model` (line 39) `def load_64bit_model()`
- `run_experiment` (line 49) `def run_experiment(use_padding)`

#### `2048bits.py`
**Path:** `2048bits.py`

**Functions:**
- `evaluate` (line 44) `def evaluate(model, x, y)`
- `load_base_model` (line 49) `def load_base_model()`
- `zero_shot_test` (line 59) `def zero_shot_test(prev_model, n_bits, d_h, use_padding)`

#### `app.py`
**Path:** `app.py`

**Classes:**
- `SuperpositionSAE` (line 32) `class SuperpositionSAE`
- `ComplexityAnalyzer` (line 55) `class ComplexityAnalyzer`
- `GrokkingTransformer` (line 67) `class GrokkingTransformer`
- `AdaptiveCurriculumTrainer` (line 92) `class AdaptiveCurriculumTrainer`

**Functions:**
- `get_parity_dataset` (line 87) `def get_parity_dataset(n_bits, k, size)`
- `__init__` (line 33) `def __init__(self, d_model, d_sae)`
- `forward` (line 40) `def forward(self, x)`
- `get_metrics` (line 45) `def get_metrics(self, z)`
- `measure_lc` (line 57) `def measure_lc(model, x, epsilon)`
- `__init__` (line 68) `def __init__(self, d_in, d_h)`
- `get_pre_acts` (line 74) `def get_pre_acts(self, x)`
- `forward` (line 80) `def forward(self, x)`
- `__init__` (line 93) `def __init__(self)`
- `calculate_adaptive_params` (line 109) `def calculate_adaptive_params(self, n_bits, d_h, stage)` - *Calcula parámetros adaptativos según la complejidad de la etapa*
- `smart_weight_transfer` (line 126) `def smart_weight_transfer(self, prev_model, new_model, stage)` - *Transferencia inteligente de pesos con padding/interpolación*
- `detect_stagnation` (line 166) `def detect_stagnation(self, history, current_lc, d_h, step)` - *Detecta si el modelo está estancado y necesita reinicio*
- `train_stage` (line 184) `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` - *Entrena una etapa individual con parámetros adaptativos*
- `run_curriculum` (line 316) `def run_curriculum(self)` - *Ejecuta el curriculum completo con adaptación automática*

#### `app_wandb.py`
**Path:** `app_wandb.py`

**Classes:**
- `SuperpositionSAE` (line 63) `class SuperpositionSAE`
- `ComplexityAnalyzer` (line 86) `class ComplexityAnalyzer`
- `GrokkingTransformer` (line 98) `class GrokkingTransformer`
- `AdaptiveCurriculumTrainer` (line 123) `class AdaptiveCurriculumTrainer`

**Functions:**
- `init_wandb` (line 35) `def init_wandb(project_name, config)` - *Initialize wandb tracking*
- `log_training_step` (line 43) `def log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)` - *Log metrics to wandb*
- `finish_wandb` (line 59) `def finish_wandb()` - *Finish wandb run*
- `get_parity_dataset` (line 118) `def get_parity_dataset(n_bits, k, size)`
- `__init__` (line 64) `def __init__(self, d_model, d_sae)`
- `forward` (line 71) `def forward(self, x)`
- `get_metrics` (line 76) `def get_metrics(self, z)`
- `measure_lc` (line 88) `def measure_lc(model, x, epsilon)`
- `__init__` (line 99) `def __init__(self, d_in, d_h)`
- `get_pre_acts` (line 105) `def get_pre_acts(self, x)`
- `forward` (line 111) `def forward(self, x)`
- `__init__` (line 124) `def __init__(self)`
- `calculate_adaptive_params` (line 140) `def calculate_adaptive_params(self, n_bits, d_h, stage)` - *Calculate adaptive parameters according to stage complexity*
- `smart_weight_transfer` (line 157) `def smart_weight_transfer(self, prev_model, new_model, stage)` - *Intelligent weight transfer with padding/interpolation*
- `detect_stagnation` (line 196) `def detect_stagnation(self, history, current_lc, d_h, step)` - *Detect if model is stagnant and needs restart*
- `train_stage` (line 212) `def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)` - *Train individual stage with adaptive parameters*
- `run_curriculum` (line 345) `def run_curriculum(self)` - *Execute complete curriculum with automatic adaptation*

#### `checkpointing.py`
**Path:** `new_experiment/checkpointing.py`

**Classes:**
- `ICheckpointManager` (line 16) `class ICheckpointManager(ABC)` - *Interface for checkpoint management.*
- `CheckpointManager` (line 35) `class CheckpointManager(ICheckpointManager)` - *Manage experiment checkpoints with automatic interval-based saving.

Saves both timestamped checkpoints and a latest checkpoint that
can be used for resuming training.*

**Functions:**
- `save` (line 20) `def save(self, state, path)` - *Save checkpoint and return path.*
- `load` (line 25) `def load(self, path)` - *Load checkpoint from path.*
- `should_checkpoint` (line 30) `def should_checkpoint(self)` - *Determine if checkpoint should be saved.*
- `__init__` (line 43) `def __init__(self, config)` - *Initialize checkpoint manager.

Args:
    config: Experiment configuration*
- `save` (line 55) `def save(self, state, path)` - *Save checkpoint to disk.

Args:
    state: State dictionary to save
    path: Optional specific path for checkpoint
    
Returns:
    Path where checkpoint was saved*
- `load` (line 85) `def load(self, path)` - *Load checkpoint from disk.

Args:
    path: Path to checkpoint file
    
Returns:
    Loaded state dictionary or None if load fails*
- `should_checkpoint` (line 101) `def should_checkpoint(self)` - *Check if checkpoint interval has elapsed.

Returns:
    True if time to save checkpoint*
- `get_latest_checkpoint_path` (line 111) `def get_latest_checkpoint_path(self)` - *Get path to latest checkpoint if exists.

Returns:
    Path to latest checkpoint or None*

#### `config.py`
**Path:** `new_experiment/config.py`

**Classes:**
- `ExperimentConfig` (line 13) `class ExperimentConfig` - *Centralized configuration for all experimental parameters.
All magic numbers are eliminated and made explicit.*

**Functions:**
- `get_adaptive_train_size` (line 111) `def get_adaptive_train_size(self, n_bits)` - *Calculate adaptive training size based on input dimensionality.*
- `get_adaptive_weight_decay` (line 117) `def get_adaptive_weight_decay(self, n_bits, hidden_dim)` - *Calculate adaptive weight decay based on problem complexity.*
- `get_adaptive_max_steps` (line 126) `def get_adaptive_max_steps(self, n_bits, hidden_dim)` - *Calculate adaptive maximum steps based on problem complexity.*

#### `data_generation.py`
**Path:** `new_experiment/data_generation.py`

**Classes:**
- `ParityDatasetGenerator` (line 11) `class ParityDatasetGenerator` - *Generates binary parity learning datasets.

The parity function computes whether the sum of the first k bits
of an n-bit input vector is odd (1) or even (0).*

**Functions:**
- `__init__` (line 19) `def __init__(self, config)` - *Initialize dataset generator.

Args:
    config: Experiment configuration*
- `generate` (line 28) `def generate(self, n_bits, k_bits, dataset_size)` - *Generate random binary vectors with k-bit parity labels.

Args:
    n_bits: Total number of input bits
    k_bits: Number of bits used for parity calculation
    dataset_size: Number of samples to generate
    
Returns:
    Tuple of (inputs, labels) where inputs are binary vectors
    and labels are parity values*

#### `main.py`
**Path:** `new_experiment/main.py`

**Classes:**
- `MultiSeedCurriculumRunner` (line 16) `class MultiSeedCurriculumRunner` - *Run curriculum training across multiple random seeds.

Executes the full curriculum for each seed, collecting
comprehensive results and metrics.*

**Functions:**
- `main` (line 130) `def main()` - *Main entry point for command-line execution.*
- `__init__` (line 24) `def __init__(self, config)` - *Initialize runner.

Args:
    config: Experiment configuration*
- `_set_seed` (line 35) `def _set_seed(self, seed)` - *Set random seed for reproducibility.

Args:
    seed: Random seed value*
- `run_single_seed` (line 48) `def run_single_seed(self, seed)` - *Run curriculum for a single seed.

Args:
    seed: Random seed value
    
Returns:
    True if curriculum completed successfully*
- `run_experiment` (line 90) `def run_experiment(self, start_seed, end_seed)` - *Run experiment across multiple seeds.

Args:
    start_seed: Starting seed number
    end_seed: Ending seed number*

#### `metrics.py`
**Path:** `new_experiment/metrics.py`

**Classes:**
- `IMetricCalculator` (line 17) `class IMetricCalculator(ABC)` - *Interface for metric calculation strategies.*
- `LocalComplexityCalculator` (line 26) `class LocalComplexityCalculator(IMetricCalculator)` - *Calculate local complexity as effective local dimensionality.

Local complexity measures the number of near-zero pre-activations,
indicating representational sparsity.*
- `GradientCovarianceCalculator` (line 81) `class GradientCovarianceCalculator` - *Calculate gradient covariance matrix and condition number.

The condition number kappa measures the ratio of largest to smallest
eigenvalues of the gradient covariance matrix, indicating optimization
landscape geometry.*
- `ThermodynamicMetricsCalculator` (line 166) `class ThermodynamicMetricsCalculator(IMetricCalculator)` - *Calculate thermodynamic metrics: effective temperature and Planck constant.

These metrics characterize the energy landscape and quantum-like properties
of the learning dynamics.*
- `DeltaCalculator` (line 253) `class DeltaCalculator(IMetricCalculator)` - *Calculate discretization margin delta.

Delta measures how close parameter values are to integers,
indicating algorithmic crystallization.*
- `ComprehensiveMetricsAggregator` (line 282) `class ComprehensiveMetricsAggregator` - *Aggregate all thermodynamic and learning metrics.

Centralizes metric calculation and provides unified interface.*

**Functions:**
- `calculate` (line 21) `def calculate(self)` - *Calculate metrics and return dictionary of results.*
- `__init__` (line 34) `def __init__(self, config)` - *Initialize calculator.

Args:
    config: Experiment configuration*
- `calculate` (line 44) `def calculate(self, model, x_batch)` - *Measure LC as count of near-zero pre-activations.

Args:
    model: Neural network model
    x_batch: Input batch
    
Returns:
    Dictionary containing local complexity value*
- `__init__` (line 90) `def __init__(self, config)` - *Initialize calculator.

Args:
    config: Experiment configuration*
- `accumulate_gradient` (line 102) `def accumulate_gradient(self, model)` - *Store current gradient vector.

Args:
    model: Neural network model*
- `calculate_kappa` (line 121) `def calculate_kappa(self)` - *Calculate condition number of gradient covariance matrix.

Returns:
    Tuple of (kappa, covariance_matrix)*
- `reset` (line 161) `def reset(self)` - *Clear gradient buffer.*
- `__init__` (line 174) `def __init__(self, config)` - *Initialize calculator.

Args:
    config: Experiment configuration*
- `calculate` (line 183) `def calculate(self, gradient_covariance)` - *Calculate effective temperature and Planck constant.

Args:
    gradient_covariance: Gradient covariance matrix
    
Returns:
    Dictionary containing thermodynamic metrics*
- `calculate` (line 261) `def calculate(self, model)` - *Calculate mean squared distance to nearest integer.

Args:
    model: Neural network model
    
Returns:
    Dictionary containing delta value*
- `__init__` (line 289) `def __init__(self, config)` - *Initialize aggregator.

Args:
    config: Experiment configuration*
- `compute_all_metrics` (line 302) `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, step)` - *Compute comprehensive metric suite.

Args:
    model: Neural network model
    sae: Sparse autoencoder
    train_loader: Training data
    train_labels: Training labels
    test_loader: Test data
    test_labels: Test labels
    current_loss: Current loss value
    z_sae: SAE encoded features
    step: Current training step
    
Returns:
    Dictionary containing all computed metrics*
- `accumulate_gradient` (line 374) `def accumulate_gradient(self, model)` - *Accumulate gradient for kappa calculation.

Args:
    model: Neural network model*
- `reset` (line 383) `def reset(self)` - *Reset all stateful calculators.*

#### `models.py`
**Path:** `new_experiment/models.py`

**Classes:**
- `IModelArchitecture` (line 14) `class IModelArchitecture(ABC)` - *Interface for neural network architectures.*
- `GrokkingTransformer` (line 33) `class GrokkingTransformer(IModelArchitecture)` - *Two-layer MLP for parity learning experiments.

Architecture:
    input -> fc1 -> ReLU -> fc2 -> ReLU -> output*
- `SuperpositionSAE` (line 101) `class SuperpositionSAE` - *Sparse Autoencoder for superposition analysis.

Used to measure effective feature dimensionality and
superposition coefficient in learned representations.*

**Functions:**
- `forward` (line 18) `def forward(self, x)` - *Forward pass returning logits and latent representation.*
- `get_pre_activations` (line 23) `def get_pre_activations(self, x)` - *Get pre-activation tensors for complexity analysis.*
- `get_flat_parameters` (line 28) `def get_flat_parameters(self)` - *Get flattened parameter vector.*
- `__init__` (line 41) `def __init__(self, input_dim, hidden_dim, output_dim)` - *Initialize network.

Args:
    input_dim: Number of input features
    hidden_dim: Hidden layer dimensionality
    output_dim: Number of output classes*
- `get_pre_activations` (line 59) `def get_pre_activations(self, x)` - *Get pre-activation tensors for local complexity calculation.

Args:
    x: Input tensor
    
Returns:
    List of pre-activation tensors*
- `forward` (line 74) `def forward(self, x)` - *Forward pass through network.

Args:
    x: Input tensor
    
Returns:
    Tuple of (logits, latent_representation)*
- `get_flat_parameters` (line 91) `def get_flat_parameters(self)` - *Get flattened parameter vector.

Returns:
    1D tensor containing all model parameters*
- `__init__` (line 109) `def __init__(self, model_dim, sae_dim)` - *Initialize SAE.

Args:
    model_dim: Dimensionality of model representations
    sae_dim: Expanded SAE feature dimensionality*
- `forward` (line 126) `def forward(self, x)` - *Encode and decode with ReLU activation.

Args:
    x: Input representations
    
Returns:
    Tuple of (reconstructed, encoded_features)*
- `compute_superposition_metrics` (line 140) `def compute_superposition_metrics(self, z_encoded)` - *Calculate superposition coefficient and effective features.

The superposition coefficient measures how efficiently the model
packs information into its representation space.

Args:
    z_encoded: Encoded feature activations
    
Returns:
    Tuple of (psi_coefficient, effective_features)*

#### `streamlit_app.py`
**Path:** `new_experiment/streamlit_app.py`

**Classes:**
- `ThermodynamicAnalyzer` (line 75) `class ThermodynamicAnalyzer` - *Complete thermodynamic analysis of phase transitions.*
- `StreamlitTrainer` (line 143) `class StreamlitTrainer` - *Real-time training with Streamlit visualization.*

**Functions:**
- `main` (line 596) `def main()` - *Main Streamlit application.*
- `compute_metrics` (line 79) `def compute_metrics(weights_list, phase, epoch)` - *Calculate complete thermodynamic state.*
- `__init__` (line 146) `def __init__(self, config)` - *Initialize trainer.*
- `train_stage_with_visualization` (line 163) `def train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` - *Train stage with real-time Streamlit visualization.*
- `_create_3d_visualization` (line 424) `def _create_3d_visualization(self, weights_list, phase_name, thermo_metrics)` - *Create 3D PCA visualization.*
- `_create_2d_visualization` (line 478) `def _create_2d_visualization(self, weights_list, phase_name, thermo_metrics)` - *Create 2D texture visualization.*
- `_create_metrics_plot` (line 526) `def _create_metrics_plot(self, history, phase_name)` - *Create comprehensive metrics plot.*
- `run_curriculum` (line 570) `def run_curriculum(self)` - *Execute complete curriculum.*

#### `test_framework.py`
**Path:** `new_experiment/test_framework.py`

**Functions:**
- `test_configuration` (line 17) `def test_configuration()` - *Test configuration creation and parameter calculation.*
- `test_data_generation` (line 38) `def test_data_generation()` - *Test dataset generation.*
- `test_models` (line 53) `def test_models()` - *Test model architectures.*
- `test_metrics` (line 80) `def test_metrics()` - *Test metric calculation.*
- `test_checkpointing` (line 119) `def test_checkpointing()` - *Test checkpoint management.*
- `test_weight_transfer` (line 142) `def test_weight_transfer()` - *Test smart weight transfer.*
- `test_stagnation_detection` (line 158) `def test_stagnation_detection()` - *Test stagnation detector.*
- `run_all_tests` (line 178) `def run_all_tests()` - *Run all tests.*

#### `training.py`
**Path:** `new_experiment/training.py`

**Classes:**
- `CurriculumStageTrainer` (line 21) `class CurriculumStageTrainer` - *Train a single curriculum stage with full metric tracking.

Handles training loop, metric computation, checkpoint management,
and stagnation detection for one stage of the curriculum.*

**Functions:**
- `__init__` (line 29) `def __init__(self, config, seed)` - *Initialize stage trainer.

Args:
    config: Experiment configuration
    seed: Random seed for reproducibility*
- `train_stage` (line 48) `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` - *Train a single curriculum stage.

Args:
    stage: Stage number
    n_bits: Number of input bits
    hidden_dim: Hidden layer dimensionality
    previous_model: Model from previous stage
    previous_sae: SAE from previous stage
    
Returns:
    Tuple of (model, sae, success, metrics_history)*
- `_create_checkpoint_state` (line 289) `def _create_checkpoint_state(self, model, sae, optimizer, stage, n_bits, hidden_dim, step, metrics_history)` - *Create checkpoint state dictionary.

Args:
    model: Neural network model
    sae: Sparse autoencoder
    optimizer: Optimizer
    stage: Current stage
    n_bits: Number of bits
    hidden_dim: Hidden dimensionality
    step: Current step
    metrics_history: Training metrics
    
Returns:
    State dictionary for checkpointing*

#### `training_dynamics.py`
**Path:** `new_experiment/training_dynamics.py`

**Classes:**
- `SmartWeightTransfer` (line 13) `class SmartWeightTransfer` - *Transfer weights intelligently between curriculum stages.

Handles dimension mismatches through padding and cropping
while preserving learned algorithmic structure.*
- `StagnationDetector` (line 83) `class StagnationDetector` - *Detect training stagnation and trigger optimizer resets.

Monitors test accuracy improvement and local complexity to
identify when training is stuck in poor local minima.*

**Functions:**
- `transfer` (line 21) `def transfer(self, previous_model, new_model, stage)` - *Transfer weights with padding or cropping as needed.

Args:
    previous_model: Model from previous curriculum stage
    new_model: New model for current stage
    stage: Current stage number
    
Returns:
    New model with transferred weights*
- `__init__` (line 91) `def __init__(self, config)` - *Initialize detector.

Args:
    config: Experiment configuration*
- `is_stagnant` (line 101) `def is_stagnant(self, metrics_history, current_step, hidden_dim)` - *Determine if training is stagnant.

Args:
    metrics_history: List of historical metrics
    current_step: Current training step
    hidden_dim: Hidden layer dimensionality
    
Returns:
    Tuple of (is_stagnant, reason)*

#### `wandb_integration.py`
**Path:** `new_experiment/wandb_integration.py`

**Classes:**
- `WandBLogger` (line 12) `class WandBLogger` - *Wrapper for Weights and Biases logging functionality.

Handles initialization, metric logging, and cleanup.*

**Functions:**
- `__init__` (line 19) `def __init__(self, config)` - *Initialize WandB logger.

Args:
    config: Experiment configuration*
- `initialize` (line 30) `def initialize(self, run_name, run_config)` - *Initialize WandB run.

Args:
    run_name: Name for this run
    run_config: Configuration dictionary to log*
- `log_metrics` (line 58) `def log_metrics(self, metrics, step)` - *Log metrics to WandB.

Args:
    metrics: Dictionary of metric names to values
    step: Optional step number*
- `finish` (line 77) `def finish(self)` - *Finish WandB run.*

#### `purity_analysis.py`
**Path:** `purity_analysis.py`

**Classes:**
- `PurityConfig` (line 25) `class PurityConfig` - *Configuration for purity index analysis.*
- `IModel` (line 49) `class IModel(Protocol)` - *Protocol for models supporting purity analysis.*
- `IPurityIndexCalculator` (line 56) `class IPurityIndexCalculator(Protocol)` - *Protocol for purity index calculation.*
- `IEffectiveTemperatureCalculator` (line 63) `class IEffectiveTemperatureCalculator(Protocol)` - *Protocol for effective temperature calculation.*
- `IPhaseClassifier` (line 70) `class IPhaseClassifier(Protocol)` - *Protocol for phase classification.*
- `IPolycrystalAnalyzer` (line 77) `class IPolycrystalAnalyzer(Protocol)` - *Protocol for polycrystal analysis.*
- `IPurityComparator` (line 88) `class IPurityComparator(Protocol)` - *Protocol for purity comparison.*
- `PurityIndexCalculator` (line 98) `class PurityIndexCalculator` - *Calculate purity index for neural network models.

Measures how close weights are to integer values (crystallization).*
- `EffectiveTemperatureCalculator` (line 235) `class EffectiveTemperatureCalculator` - *Calculate effective temperature from loss dynamics.

Temperature measures training volatility and convergence.*
- `PhaseClassifier` (line 314) `class PhaseClassifier` - *Classify crystallization phase based on purity and temperature.

Identifies gas, liquid, transition, and crystalline phases.*
- `PolycrystalAnalyzer` (line 393) `class PolycrystalAnalyzer` - *Analyze polycrystalline structure through weight pruning.

Tests structural robustness and phase stability.*
- `PurityComparator` (line 501) `class PurityComparator` - *Compare purity metrics between original and perturbed states.

Quantifies structural memory and thermal damage.*
- `CheckpointLoader` (line 576) `class CheckpointLoader` - *Load and validate checkpoints for purity analysis.

Handles different checkpoint formats and model configurations.*
- `PurityAnalyzer` (line 643) `class PurityAnalyzer` - *Main purity analysis orchestrator.

Coordinates all analysis components and generates comprehensive reports.*
- `PurityPipeline` (line 818) `class PurityPipeline` - *Pipeline for batch processing checkpoints.

Handles multiple checkpoints and generates aggregate statistics.*

**Functions:**
- `main` (line 1049) `def main()` - *Main entry point for purity analysis.*
- `get_flat_parameters` (line 52) `def get_flat_parameters(self)`
- `calculate` (line 59) `def calculate(self, model)`
- `calculate` (line 66) `def calculate(self, loss_history)`
- `classify` (line 73) `def classify(self, alpha, temperature)`
- `analyze_polycrystal` (line 80) `def analyze_polycrystal(self, model, pruning_level)`
- `compare` (line 91) `def compare(self, original, polycrystal)`
- `__init__` (line 105) `def __init__(self, config)` - *Initialize calculator.

Args:
    config: Purity analysis configuration*
- `calculate` (line 114) `def calculate(self, model)` - *Calculate comprehensive purity metrics.

Args:
    model: Neural network model
    
Returns:
    Dictionary containing purity metrics*
- `_compute_layer_purity` (line 159) `def _compute_layer_purity(self, weights)` - *Compute purity metrics for a single layer.

Args:
    weights: Layer weight tensor
    
Returns:
    Tuple of (alpha, delta)*
- `_delta_to_alpha` (line 177) `def _delta_to_alpha(self, delta)` - *Convert discretization margin to purity index.

Args:
    delta: Discretization margin
    
Returns:
    Purity index alpha*
- `_assess_purity_quality` (line 191) `def _assess_purity_quality(self, alpha, variance)` - *Assess overall purity quality.

Args:
    alpha: Global purity index
    variance: Alpha variance across layers
    
Returns:
    Quality assessment string*
- `_compute_crystallization_score` (line 215) `def _compute_crystallization_score(self, alpha, variance)` - *Compute overall crystallization quality score.

Args:
    alpha: Global purity index
    variance: Alpha variance
    
Returns:
    Crystallization score [0, 1]*
- `__init__` (line 242) `def __init__(self, config)` - *Initialize calculator.

Args:
    config: Purity analysis configuration*
- `calculate` (line 251) `def calculate(self, loss_history)` - *Calculate thermodynamic metrics from loss history.

Args:
    loss_history: List of loss values over training
    
Returns:
    Dictionary containing temperature metrics*
- `__init__` (line 321) `def __init__(self, config)` - *Initialize classifier.

Args:
    config: Purity analysis configuration*
- `classify` (line 330) `def classify(self, alpha, temperature)` - *Classify current phase state.

Args:
    alpha: Purity index
    temperature: Effective temperature
    
Returns:
    Phase classification string*
- `classify_polycrystal_state` (line 359) `def classify_polycrystal_state(self, original_alpha, original_temp, poly_alpha, poly_temp)` - *Classify polycrystal state after perturbation.

Args:
    original_alpha: Original purity index
    original_temp: Original temperature
    poly_alpha: Polycrystal purity index
    poly_temp: Polycrystal temperature
    
Returns:
    Polycrystal state classification*
- `__init__` (line 400) `def __init__(self, config)` - *Initialize analyzer.

Args:
    config: Purity analysis configuration*
- `analyze_polycrystal` (line 412) `def analyze_polycrystal(self, model, pruning_level, loss_history)` - *Analyze model after weight pruning.

Args:
    model: Neural network model
    pruning_level: Fraction of weights to prune [0, 1]
    loss_history: Training loss history
    
Returns:
    Dictionary containing polycrystal analysis*
- `_prune_model` (line 461) `def _prune_model(self, model, sparsity)` - *Prune smallest magnitude weights.

Args:
    model: Neural network model
    sparsity: Fraction of weights to zero out*
- `_assess_structural_integrity` (line 480) `def _assess_structural_integrity(self, alpha, pruning_level)` - *Assess how well structure survives pruning.

Args:
    alpha: Purity index after pruning
    pruning_level: Fraction of weights pruned
    
Returns:
    Structural integrity score [0, 1]*
- `__init__` (line 508) `def __init__(self, config)` - *Initialize comparator.

Args:
    config: Purity analysis configuration*
- `compare` (line 518) `def compare(self, original, polycrystal)` - *Compare original and polycrystal states.

Args:
    original: Original state metrics
    polycrystal: Polycrystal state metrics
    
Returns:
    Dictionary containing comparison metrics*
- `__init__` (line 583) `def __init__(self, config)` - *Initialize loader.

Args:
    config: Experiment configuration*
- `load` (line 592) `def load(self, checkpoint_path)` - *Load checkpoint and extract model.

Args:
    checkpoint_path: Path to checkpoint file
    
Returns:
    Tuple of (model, sae, checkpoint_data)*
- `__init__` (line 650) `def __init__(self, checkpoint_path, experiment_config, purity_config)` - *Initialize analyzer.

Args:
    checkpoint_path: Path to checkpoint file
    experiment_config: Experiment configuration
    purity_config: Purity analysis configuration*
- `_load_checkpoint` (line 677) `def _load_checkpoint(self)` - *Load checkpoint and extract components.*
- `analyze` (line 694) `def analyze(self)` - *Perform comprehensive purity analysis.

Returns:
    Dictionary containing complete analysis results*
- `_print_report` (line 759) `def _print_report(self, results)` - *Print analysis report to console.

Args:
    results: Analysis results dictionary*
- `__init__` (line 825) `def __init__(self, experiment_config, purity_config)` - *Initialize pipeline.

Args:
    experiment_config: Experiment configuration
    purity_config: Purity analysis configuration*
- `process_checkpoint` (line 840) `def process_checkpoint(self, checkpoint_path, output_dir)` - *Process single checkpoint.

Args:
    checkpoint_path: Path to checkpoint file
    output_dir: Directory for output files
    
Returns:
    Analysis results dictionary*
- `process_directory` (line 874) `def process_directory(self, checkpoint_dir, n_latest, output_dir)` - *Process all checkpoints in directory.

Args:
    checkpoint_dir: Directory containing checkpoints
    n_latest: Number of latest checkpoints to process
    output_dir: Directory for output files
    
Returns:
    List of analysis results*
- `generate_summary` (line 917) `def generate_summary(self, all_results, output_dir)` - *Generate summary statistics across all checkpoints.

Args:
    all_results: List of analysis results
    output_dir: Directory for output files*
- `_generate_text_report` (line 996) `def _generate_text_report(self, summary, output_dir)` - *Generate human-readable text report.

Args:
    summary: Summary statistics dictionary
    output_dir: Directory for output files*

#### `realtime_train.py`
**Path:** `realtime_train.py`

**Classes:**
- `ExperimentConfig` (line 63) `class ExperimentConfig` - *Immutable configuration for thermodynamic grokking experiments.*
- `IMetricCalculator` (line 130) `class IMetricCalculator(ABC)` - *Interface for metric calculation strategies.*
- `IModelArchitecture` (line 139) `class IModelArchitecture(ABC)` - *Interface for neural network architectures.*
- `ICheckpointManager` (line 158) `class ICheckpointManager(ABC)` - *Interface for checkpoint management.*
- `GrokkingTransformer` (line 177) `class GrokkingTransformer(IModelArchitecture)` - *Two-layer MLP for parity learning experiments.*
- `SuperpositionSAE` (line 211) `class SuperpositionSAE` - *Sparse autoencoder for superposition analysis.*
- `ParityDatasetGenerator` (line 245) `class ParityDatasetGenerator` - *Generate parity learning datasets.*
- `LocalComplexityCalculator` (line 259) `class LocalComplexityCalculator(IMetricCalculator)` - *Calculate local complexity as effective local dimensionality.*
- `GradientCovarianceCalculator` (line 288) `class GradientCovarianceCalculator` - *Calculate gradient covariance matrix and kappa.*
- `ThermodynamicMetricsCalculator` (line 349) `class ThermodynamicMetricsCalculator(IMetricCalculator)` - *Calculate thermodynamic metrics: T_eff and h_bar_eff.*
- `DeltaCalculator` (line 412) `class DeltaCalculator(IMetricCalculator)` - *Calculate discretization margin delta.*
- `ComprehensiveMetricsAggregator` (line 424) `class ComprehensiveMetricsAggregator` - *Aggregate all thermodynamic and learning metrics.*
- `CheckpointManager` (line 497) `class CheckpointManager(ICheckpointManager)` - *Manage experiment checkpoints.*
- `StagnationDetector` (line 543) `class StagnationDetector` - *Detect training stagnation and trigger resets.*
- `SmartWeightTransfer` (line 579) `class SmartWeightTransfer` - *Transfer weights intelligently between curriculum stages.*
- `AdaptiveParameterCalculator` (line 630) `class AdaptiveParameterCalculator` - *Calculate adaptive training parameters based on problem complexity.*
- `CurriculumStageTrainer` (line 665) `class CurriculumStageTrainer` - *Train a single curriculum stage with full metric tracking.*
- `ResultsAnalyzer` (line 898) `class ResultsAnalyzer` - *Analyze experimental results and generate comprehensive statistics.*
- `ResultsVisualizer` (line 1157) `class ResultsVisualizer` - *Generate comprehensive visualizations of experimental results.*
- `MultiSeedCurriculumRunner` (line 1367) `class MultiSeedCurriculumRunner` - *Run curriculum training across multiple random seeds.*

**Functions:**
- `main` (line 1527) `def main()` - *Main entry point.*
- `calculate` (line 134) `def calculate(self)` - *Calculate metrics and return dictionary of results.*
- `forward` (line 143) `def forward(self, x)` - *Forward pass returning logits and latent representation.*
- `get_pre_activations` (line 148) `def get_pre_activations(self, x)` - *Get pre-activation tensors for complexity analysis.*
- `get_flat_parameters` (line 153) `def get_flat_parameters(self)` - *Get flattened parameter vector.*
- `save` (line 162) `def save(self, state, path)` - *Save checkpoint and return path.*
- `load` (line 167) `def load(self, path)` - *Load checkpoint from path.*
- `should_checkpoint` (line 172) `def should_checkpoint(self)` - *Determine if checkpoint should be saved.*
- `__init__` (line 180) `def __init__(self, input_dim, hidden_dim, output_dim)`
- `get_pre_activations` (line 190) `def get_pre_activations(self, x)` - *Get pre-activation tensors for LC calculation.*
- `forward` (line 197) `def forward(self, x)` - *Forward pass returning logits and latent representation.*
- `get_flat_parameters` (line 206) `def get_flat_parameters(self)` - *Get flattened parameter vector.*
- `__init__` (line 214) `def __init__(self, model_dim, sae_dim)`
- `forward` (line 224) `def forward(self, x)` - *Encode and decode with ReLU activation.*
- `compute_superposition_metrics` (line 230) `def compute_superposition_metrics(self, z_encoded)` - *Calculate psi (superposition coefficient) and effective features.*
- `__init__` (line 248) `def __init__(self, config)`
- `generate` (line 251) `def generate(self, n_bits, k_bits, dataset_size)` - *Generate random binary vectors with k-bit parity labels.*
- `__init__` (line 262) `def __init__(self, config)`
- `calculate` (line 266) `def calculate(self, model, x_batch)` - *Measure LC as count of near-zero pre-activations.*
- `__init__` (line 291) `def __init__(self, config)`
- `accumulate_gradient` (line 297) `def accumulate_gradient(self, model)` - *Store current gradient vector.*
- `calculate_kappa` (line 311) `def calculate_kappa(self)` - *Calculate condition number of gradient covariance matrix.*
- `reset` (line 344) `def reset(self)` - *Clear gradient buffer.*
- `__init__` (line 352) `def __init__(self, config)`
- `calculate` (line 355) `def calculate(self, gradient_covariance)` - *Calculate effective temperature and Planck constant.*
- `calculate` (line 415) `def calculate(self, model)` - *Calculate mean squared distance to nearest integer.*
- `__init__` (line 427) `def __init__(self, config)`
- `compute_all_metrics` (line 434) `def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, step)` - *Compute comprehensive metric suite.*
- `accumulate_gradient` (line 488) `def accumulate_gradient(self, model)` - *Accumulate gradient for kappa calculation.*
- `reset` (line 492) `def reset(self)` - *Reset all stateful calculators.*
- `__init__` (line 500) `def __init__(self, config)`
- `save` (line 506) `def save(self, state, path)` - *Save checkpoint to disk.*
- `load` (line 524) `def load(self, path)` - *Load checkpoint from disk.*
- `should_checkpoint` (line 532) `def should_checkpoint(self)` - *Check if checkpoint interval has elapsed.*
- `get_latest_checkpoint_path` (line 537) `def get_latest_checkpoint_path(self)` - *Get path to latest checkpoint if exists.*
- `__init__` (line 546) `def __init__(self, config)`
- `is_stagnant` (line 550) `def is_stagnant(self, metrics_history, current_step, hidden_dim)` - *Determine if training is stagnant.*
- `transfer` (line 582) `def transfer(self, previous_model, new_model, stage)` - *Transfer weights with padding/cropping as needed.*
- `__init__` (line 633) `def __init__(self, config)`
- `calculate` (line 636) `def calculate(self, n_bits, hidden_dim, stage)` - *Calculate training parameters for current stage.*
- `__init__` (line 668) `def __init__(self, config, seed)`
- `train_stage` (line 680) `def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)` - *Train a single curriculum stage.*
- `__init__` (line 901) `def __init__(self, config)`
- `analyze_seed_results` (line 905) `def analyze_seed_results(self, all_results)` - *Generate comprehensive analysis of all seed results.*
- `print_analysis_report` (line 1067) `def print_analysis_report(self, analysis)` - *Print comprehensive analysis report to console.*
- `__init__` (line 1160) `def __init__(self, config)`
- `create_seed_training_dynamics` (line 1166) `def create_seed_training_dynamics(self, seed_result)` - *Create training dynamics visualization for a single seed.*
- `create_aggregate_visualizations` (line 1269) `def create_aggregate_visualizations(self, all_results)` - *Create aggregate visualizations across all seeds.*
- `__init__` (line 1370) `def __init__(self, config)`
- `_signal_handler` (line 1381) `def _signal_handler(self, signum, frame)` - *Handle interrupt signal.*
- `_set_seed` (line 1386) `def _set_seed(self, seed)` - *Set random seed for reproducibility.*
- `run_experiment` (line 1394) `def run_experiment(self)` - *Run multi-seed curriculum experiment.*

#### `test.py`
**Path:** `test.py`

**Functions:**
- `accuracy` (line 31) `def accuracy(model, x, y)`
- `load_base` (line 36) `def load_base()`
- `zero_shot_test` (line 43) `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)`

#### `test_wandb_ablation.py`
**Path:** `test_wandb_ablation.py`

**Functions:**
- `init_ablation_wandb` (line 24) `def init_ablation_wandb(project_name)` - *Initialize wandb for ablation experiment*
- `log_scale_results` (line 37) `def log_scale_results(n_bits, d_h, train_acc_transfer, test_acc_transfer, train_acc_control, test_acc_control, time_elapsed, generalization_success)` - *Log results for each scale to wandb*
- `finish_ablation_wandb` (line 54) `def finish_ablation_wandb()` - *Finish wandb run*
- `accuracy` (line 59) `def accuracy(model, x, y)`
- `load_base` (line 63) `def load_base()`
- `zero_shot_test` (line 69) `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)`

#### `view_streamlit.py`
**Path:** `view_streamlit.py`

**Classes:**
- `ThermodynamicAnalyzer` (line 82) `class ThermodynamicAnalyzer` - *Complete thermodynamic analysis of phase transitions*
- `CompleteCurriculumWrapper` (line 426) `class CompleteCurriculumWrapper` - *Wraps app.py training with complete real-time visualization*

**Functions:**
- `visualize_3d_geometry` (line 256) `def visualize_3d_geometry(weights_list, phase_name, thermo_metrics)` - *Complete 3D visualization with clustering and geometry*
- `visualize_2d_texture` (line 346) `def visualize_2d_texture(weights_list, phase_name, thermo_metrics)` - *Complete 2D texture: heatmap, distribution, FFT, histogram*
- `main` (line 863) `def main()`
- `compute_metrics` (line 86) `def compute_metrics(weights_list, phase, epoch)` - *Calculate complete thermodynamic state*
- `visualize_thermal_engine` (line 149) `def visualize_thermal_engine(thermo_history)` - *Complete thermal engine visualization*
- `__init__` (line 429) `def __init__(self)`
- `calculate_adaptive_params` (line 454) `def calculate_adaptive_params(self, n_bits, d_h, stage)` - *EXACTO app.py: Calcula parámetros adaptativos*
- `capture_snapshot` (line 473) `def capture_snapshot(self, model, sae, stage, n_bits, d_h, step, metrics)` - *Capture complete snapshot*
- `smart_weight_transfer` (line 502) `def smart_weight_transfer(self, prev_model, new_model, stage)` - *EXACTO app.py: Transferencia inteligente de pesos*
- `train_stage_complete` (line 527) `def train_stage_complete(self, stage, n_bits, d_h, prev_model)` - *Train stage with REAL-TIME 3D/2D visualization every 500 steps*
- `run_full_curriculum` (line 821) `def run_full_curriculum(self)` - *Execute complete curriculum - EXACTO app.py*

#### `visualizador.py`
**Path:** `visualizador.py`

**Functions:**
- `load_full_system` (line 24) `def load_full_system(n_bits, d_h, stage)` - *Carga el MODELO entrenado y el SAE*
- `calculate_model_accuracy` (line 50) `def calculate_model_accuracy(model, x, y)` - *Calcula la precisión real del modelo cargado*
- `get_real_activations` (line 58) `def get_real_activations(model, x)` - *Obtiene las activaciones latentes REALES del modelo*
- `extract_sae_metrics` (line 64) `def extract_sae_metrics(sae, h2)` - *Extrae métricas del SAE sobre las activaciones reales*
- `plot_sae_autopsy` (line 80) `def plot_sae_autopsy(data, accuracy, n_bits, d_h, sae)` - *Visualización centrada en la verdad del Modelo*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
