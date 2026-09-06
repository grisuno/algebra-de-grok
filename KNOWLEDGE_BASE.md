# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 22 | **Total Symbols Extracted:** 282 | **Total Imports:** 177
 | **Resolved Imports:** 35

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:4c8e0d2 | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Community Analysis](#community-analysis)
6. [Suggested Questions](#suggested-questions)
7. [Hotspot Analysis](#hotspot-analysis)
8. [Change Impact Analysis](#change-impact-analysis)
9. [Suggested Linting Rules](#suggested-linting-rules)
10. [Orphans](#orphans)
11. [Query Recipes](#query-recipes)
12. [Structural Knowledge Map](#structural-knowledge-map)
13. [UML Class Diagram](#uml-class-diagram)
14. [Code Property Graph](#code-property-graph)
15. [Architecture Reference](#architecture-reference)
    - [PY (21 files)](#py-21-files)
    - [SH (1 files)](#sh-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 22 |
| Total Symbols | 282 |
| Total Imports | 177 |
| Call Edges | 2535 |
| Inheritance Edges | 30 |
| Languages | 2 |
| Avg Symbols/File | 12.8 |
| Avg Imports/File | 8.0 |
| Resolved Imports | 35 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `realtime_train.py` | 22 | 72 | py |
| `streamlit_app.py` | 20 | 10 | py |
| `view_streamlit.py` | 17 | 13 | py |
| `purity_analysis.py` | 15 | 50 | py |
| `training.py` | 13 | 4 | py |
| `visualizador.py` | 10 | 5 | py |
| `app_wandb.py` | 8 | 21 | py |
| `metrics.py` | 8 | 20 | py |
| `test_framework.py` | 8 | 8 | py |
| `app.py` | 7 | 18 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 15 |
| testing | 3 |
| infrastructure | 1 |
| data_access | 1 |
| business_logic | 1 |
| presentation | 1 |

### utility

- `128bits.py` (py, 3 symbols)
- `2048bits.py` (py, 3 symbols)
- `app.py` (py, 18 symbols)
- `app_wandb.py` (py, 21 symbols)
- `install.sh` (sh, 0 symbols)
- `checkpointing.py` (py, 10 symbols)
- `main.py` (py, 6 symbols)
- `metrics.py` (py, 20 symbols)
- `streamlit_app.py` (py, 10 symbols)
- `training.py` (py, 4 symbols)
- `training_dynamics.py` (py, 5 symbols)
- `wandb_integration.py` (py, 5 symbols)
- `purity_analysis.py` (py, 50 symbols)
- `realtime_train.py` (py, 72 symbols)
- `visualizador.py` (py, 5 symbols)

### infrastructure

- `config.py` (py, 4 symbols)

### data_access

- `data_generation.py` (py, 3 symbols)

### business_logic

- `models.py` (py, 13 symbols)

### testing

- `test_framework.py` (py, 8 symbols)
- `test.py` (py, 3 symbols)
- `test_wandb_ablation.py` (py, 6 symbols)

### presentation

- `view_streamlit.py` (py, 13 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `models.py` | 0.5644 | 1.0000 | 0.0721 | 0.00 | 1.00 |
| 2 | `config.py` | 0.1441 | 0.0000 | 0.2203 | 0.00 | 1.00 |
| 3 | `visualizador.py` | 0.1258 | 0.0000 | 0.0289 | 0.00 | 1.20 |
| 4 | `data_generation.py` | 0.1084 | 0.0000 | 0.0420 | 0.00 | 1.00 |
| 5 | `metrics.py` | 0.1084 | 0.0000 | 0.0420 | 0.00 | 1.00 |
| 6 | `training_dynamics.py` | 0.1084 | 0.0000 | 0.0420 | 0.00 | 1.00 |
| 7 | `training.py` | 0.1082 | 0.0000 | 0.0411 | 0.00 | 1.00 |
| 8 | `checkpointing.py` | 0.1076 | 0.0000 | 0.0379 | 0.00 | 1.00 |
| 9 | `wandb_integration.py` | 0.1076 | 0.0000 | 0.0379 | 0.00 | 1.00 |
| 10 | `main.py` | 0.1058 | 0.0000 | 0.0289 | 0.00 | 1.00 |

**Query anchors:** new_experiment/models.py, realtime_train.py

**Top result justification paths:**

  `models.py`

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `config.py` | 20.4 | | 0.2203 |
| `training.py` | 16.4 | | 0.0411 |
| `app.py` | 13.8 | | 0.0000 |
| `streamlit_app.py` | 13.0 | | 0.0000 |
| `test_framework.py` | 12.8 | | 0.0000 |
| `metrics.py` | 12.0 | | 0.0420 |
| `models.py` | 11.3 | | 0.0721 |
| `purity_analysis.py` | 9.0 | | 0.0000 |
| `training_dynamics.py` | 8.5 | | 0.0420 |
| `data_generation.py` | 8.3 | | 0.0420 |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### root (Cohesion: 1.00)

**7 files** in this community:

- `128bits.py` (py, 3 symbols)
- `2048bits.py` (py, 3 symbols)
- `app.py` (py, 18 symbols)
- `test.py` (py, 3 symbols)
- `test_wandb_ablation.py` (py, 6 symbols)
- `view_streamlit.py` (py, 13 symbols)
- `visualizador.py` (py, 5 symbols)

### new_experiment (Cohesion: 1.00)

**12 files** in this community:

- `checkpointing.py` (py, 10 symbols)
- `config.py` (py, 4 symbols)
- `data_generation.py` (py, 3 symbols)
- `main.py` (py, 6 symbols)
- `metrics.py` (py, 20 symbols)
- `models.py` (py, 13 symbols)
- `streamlit_app.py` (py, 10 symbols)
- `test_framework.py` (py, 8 symbols)
- `training.py` (py, 4 symbols)
- `training_dynamics.py` (py, 5 symbols)
- `wandb_integration.py` (py, 5 symbols)
- `purity_analysis.py` (py, 50 symbols)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does config.py depend on, and what depends on it? (10 connections)
- What does training.py depend on, and what depends on it? (8 connections)
- What does app.py depend on, and what depends on it? (6 connections)
- How are the 7 files in 'root' related to each other?
- What is SuperpositionSAE in app.py and how is it used?

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `models.py` | 0.181 | 0.423 | 0.326 | 13 | 11 |
| `config.py` | 0.056 | 0.615 | 0.392 | 4 | 16 |
| `visualizador.py` | 0.069 | 0.423 | 0.282 | 5 | 11 |
| `data_generation.py` | 0.042 | 0.269 | 0.178 | 3 | 7 |
| `metrics.py` | 0.278 | 0.500 | 0.411 | 20 | 13 |
| `training_dynamics.py` | 0.069 | 0.308 | 0.212 | 5 | 8 |
| `training.py` | 0.056 | 0.808 | 0.507 | 4 | 21 |
| `checkpointing.py` | 0.139 | 0.385 | 0.286 | 10 | 10 |
| `wandb_integration.py` | 0.069 | 0.231 | 0.166 | 5 | 6 |
| `main.py` | 0.083 | 0.308 | 0.218 | 6 | 8 |
| `realtime_train.py` | 1.000 | 0.846 | 0.908 | 72 | 22 |
| `purity_analysis.py` | 0.694 | 0.654 | 0.670 | 50 | 17 |
| `streamlit_app.py` | 0.139 | 1.000 | 0.656 | 10 | 26 |
| `view_streamlit.py` | 0.181 | 0.692 | 0.488 | 13 | 18 |
| `app.py` | 0.250 | 0.500 | 0.400 | 18 | 13 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `config.py` | 10 | 0 | 10 |
| `app.py` | 6 | 0 | 6 |
| `models.py` | 5 | 1 | 6 |
| `data_generation.py` | 3 | 1 | 4 |
| `metrics.py` | 3 | 1 | 4 |
| `training_dynamics.py` | 3 | 1 | 4 |
| `checkpointing.py` | 2 | 1 | 3 |
| `wandb_integration.py` | 2 | 1 | 3 |
| `training.py` | 1 | 0 | 1 |
| `128bits.py` | 0 | 0 | 0 |
| `2048bits.py` | 0 | 0 | 0 |
| `app_wandb.py` | 0 | 0 | 0 |
| `install.sh` | 0 | 0 | 0 |
| `main.py` | 0 | 0 | 0 |
| `streamlit_app.py` | 0 | 0 | 0 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM002` | warning | Bare except clause catches all exceptions including SystemExit | python | 8 |
| `RM001` | info | Large number of functions in py: 217 total | py | 217 |
| `RM003` | info | Print statement found (consider logging instead) | python | 383 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `install.sh` (0 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    subgraph community_1 ["new_experiment"]
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
    realtime_train_py["realtime_train.py (py)"]
    class realtime_train_py mod;
    new_experiment_training_py["training.py (py)"]
    class new_experiment_training_py mod;
    end
    subgraph community_0 ["root"]
    view_streamlit_py["view_streamlit.py (py)"]
    class view_streamlit_py mod;
    purity_analysis_py["purity_analysis.py (py)"]
    class purity_analysis_py mod;
    new_experiment_test_framework_py["test_framework.py (py)"]
    class new_experiment_test_framework_py mod;
    visualizador_py["visualizador.py (py)"]
    class visualizador_py mod;
    new_experiment_metrics_py["metrics.py (py)"]
    class new_experiment_metrics_py mod;
    app_wandb_py["app_wandb.py (py)"]
    class app_wandb_py mod;
    new_experiment_checkpointing_py["checkpointing.py (py)"]
    class new_experiment_checkpointing_py mod;
    new_experiment_main_py["main.py (py)"]
    class new_experiment_main_py mod;
    app_py["app.py (py)"]
    class app_py mod;
    new_experiment_models_py["models.py (py)"]
    class new_experiment_models_py mod;
    new_experiment_config_py["config.py (py)"]
    class new_experiment_config_py mod;
    test_wandb_ablation_py["test_wandb_ablation.py (py)"]
    class test_wandb_ablation_py mod;
    new_experiment_training_dynamics_py["training_dynamics.py (py)"]
    class new_experiment_training_dynamics_py mod;
    n_128bits_py["128bits.py (py)"]
    class n_128bits_py mod;
    new_experiment_wandb_integration_py["wandb_integration.py (py)"]
    class new_experiment_wandb_integration_py mod;
    n_2048bits_py["2048bits.py (py)"]
    class n_2048bits_py mod;
    new_experiment_data_generation_py["data_generation.py (py)"]
    class new_experiment_data_generation_py mod;
    test_py["test.py (py)"]
    class test_py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    end
    n_128bits_py -- resolved_imports --> app_py
    n_2048bits_py -- resolved_imports --> app_py
    new_experiment_checkpointing_py -- resolved_imports --> new_experiment_config_py
    new_experiment_data_generation_py -- resolved_imports --> new_experiment_config_py
    new_experiment_main_py -- resolved_imports --> new_experiment_config_py
    new_experiment_main_py -- resolved_imports --> new_experiment_training_py
    new_experiment_metrics_py -- resolved_imports --> new_experiment_config_py
    new_experiment_metrics_py -- resolved_imports --> new_experiment_models_py
    new_experiment_streamlit_app_py -- resolved_imports --> new_experiment_config_py
    new_experiment_streamlit_app_py -- resolved_imports --> new_experiment_models_py
    new_experiment_streamlit_app_py -- resolved_imports --> new_experiment_data_generation_py
    new_experiment_streamlit_app_py -- resolved_imports --> new_experiment_metrics_py
    new_experiment_streamlit_app_py -- resolved_imports --> new_experiment_training_dynamics_py
    new_experiment_streamlit_app_py -- resolved_imports --> new_experiment_wandb_integration_py
    new_experiment_test_framework_py -- resolved_imports --> new_experiment_config_py
    new_experiment_test_framework_py -- resolved_imports --> new_experiment_models_py
    new_experiment_test_framework_py -- resolved_imports --> new_experiment_data_generation_py
    new_experiment_test_framework_py -- resolved_imports --> new_experiment_metrics_py
    new_experiment_test_framework_py -- resolved_imports --> new_experiment_checkpointing_py
    new_experiment_test_framework_py -- resolved_imports --> new_experiment_training_dynamics_py
    new_experiment_training_py -- resolved_imports --> new_experiment_config_py
    new_experiment_training_py -- resolved_imports --> new_experiment_models_py
    new_experiment_training_py -- resolved_imports --> new_experiment_data_generation_py
    new_experiment_training_py -- resolved_imports --> new_experiment_metrics_py
    new_experiment_training_py -- resolved_imports --> new_experiment_checkpointing_py
    new_experiment_training_py -- resolved_imports --> new_experiment_training_dynamics_py
    new_experiment_training_py -- resolved_imports --> new_experiment_wandb_integration_py
    new_experiment_training_dynamics_py -- resolved_imports --> new_experiment_config_py
    new_experiment_wandb_integration_py -- resolved_imports --> new_experiment_config_py
    purity_analysis_py -- resolved_imports --> new_experiment_config_py
    purity_analysis_py -- resolved_imports --> new_experiment_models_py
    test_py -- resolved_imports --> app_py
    test_wandb_ablation_py -- resolved_imports --> app_py
    view_streamlit_py -- resolved_imports --> app_py
    visualizador_py -- resolved_imports --> app_py
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

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class app_py_SuperpositionSAE {
    <<class>>
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
    +forward(self, x)
    +__init__(self)
    +calculate_adaptive_params(self, n_bits, d_h, stage)
  }
  class app_py_ComplexityAnalyzer {
    <<class>>
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
    +forward(self, x)
    +__init__(self)
    +calculate_adaptive_params(self, n_bits, d_h, stage)
  }
  class app_py_GrokkingTransformer {
    <<class>>
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
    +forward(self, x)
    +__init__(self)
    +calculate_adaptive_params(self, n_bits, d_h, stage)
  }
  class app_py_AdaptiveCurriculumTrainer {
    <<class>>
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
    +forward(self, x)
    +__init__(self)
    +calculate_adaptive_params(self, n_bits, d_h, stage)
  }
  class app_wandb_py_SuperpositionSAE {
    <<class>>
    +init_wandb(project_name, config)
    +log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)
    +finish_wandb()
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
  }
  class app_wandb_py_ComplexityAnalyzer {
    <<class>>
    +init_wandb(project_name, config)
    +log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)
    +finish_wandb()
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
  }
  class app_wandb_py_GrokkingTransformer {
    <<class>>
    +init_wandb(project_name, config)
    +log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)
    +finish_wandb()
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
  }
  class app_wandb_py_AdaptiveCurriculumTrainer {
    <<class>>
    +init_wandb(project_name, config)
    +log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)
    +finish_wandb()
    +get_parity_dataset(n_bits, k, size)
    +__init__(self, d_model, d_sae)
    +forward(self, x)
    +get_metrics(self, z)
    +measure_lc(model, x, epsilon)
    +__init__(self, d_in, d_h)
    +get_pre_acts(self, x)
  }
  class checkpointing_py_ICheckpointManager {
    <<class>>
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, config)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +get_latest_checkpoint_path(self)
  }
  class checkpointing_py_CheckpointManager {
    <<class>>
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, config)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +get_latest_checkpoint_path(self)
  }
  class config_py_ExperimentConfig {
    <<class>>
    +get_adaptive_train_size(self, n_bits)
    +get_adaptive_weight_decay(self, n_bits, hidden_dim)
    +get_adaptive_max_steps(self, n_bits, hidden_dim)
  }
  class data_generation_py_ParityDatasetGenerator {
    <<class>>
    +__init__(self, config)
    +generate(self, n_bits, k_bits, dataset_size)
  }
  class main_py_MultiSeedCurriculumRunner {
    <<class>>
    +main()
    +__init__(self, config)
    +_set_seed(self, seed)
    +run_single_seed(self, seed)
    +run_experiment(self, start_seed, end_seed)
  }
  class metrics_py_IMetricCalculator {
    <<class>>
    +calculate(self)
    +__init__(self, config)
    +calculate(self, model, x_batch)
    +__init__(self, config)
    +accumulate_gradient(self, model)
    +calculate_kappa(self)
    +reset(self)
    +__init__(self, config)
    +calculate(self, gradient_covariance)
    +calculate(self, model)
  }
  class metrics_py_LocalComplexityCalculator {
    <<class>>
    +calculate(self)
    +__init__(self, config)
    +calculate(self, model, x_batch)
    +__init__(self, config)
    +accumulate_gradient(self, model)
    +calculate_kappa(self)
    +reset(self)
    +__init__(self, config)
    +calculate(self, gradient_covariance)
    +calculate(self, model)
  }
  class metrics_py_GradientCovarianceCalculator {
    <<class>>
    +calculate(self)
    +__init__(self, config)
    +calculate(self, model, x_batch)
    +__init__(self, config)
    +accumulate_gradient(self, model)
    +calculate_kappa(self)
    +reset(self)
    +__init__(self, config)
    +calculate(self, gradient_covariance)
    +calculate(self, model)
  }
  class metrics_py_ThermodynamicMetricsCalculator {
    <<class>>
    +calculate(self)
    +__init__(self, config)
    +calculate(self, model, x_batch)
    +__init__(self, config)
    +accumulate_gradient(self, model)
    +calculate_kappa(self)
    +reset(self)
    +__init__(self, config)
    +calculate(self, gradient_covariance)
    +calculate(self, model)
  }
  class metrics_py_DeltaCalculator {
    <<class>>
    +calculate(self)
    +__init__(self, config)
    +calculate(self, model, x_batch)
    +__init__(self, config)
    +accumulate_gradient(self, model)
    +calculate_kappa(self)
    +reset(self)
    +__init__(self, config)
    +calculate(self, gradient_covariance)
    +calculate(self, model)
  }
  class metrics_py_ComprehensiveMetricsAggregator {
    <<class>>
    +calculate(self)
    +__init__(self, config)
    +calculate(self, model, x_batch)
    +__init__(self, config)
    +accumulate_gradient(self, model)
    +calculate_kappa(self)
    +reset(self)
    +__init__(self, config)
    +calculate(self, gradient_covariance)
    +calculate(self, model)
  }
  class models_py_IModelArchitecture {
    <<class>>
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
    +forward(self, x)
    +get_flat_parameters(self)
    +__init__(self, model_dim, sae_dim)
    +forward(self, x)
    +compute_superposition_metrics(self, z_encoded)
  }
  class models_py_GrokkingTransformer {
    <<class>>
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
    +forward(self, x)
    +get_flat_parameters(self)
    +__init__(self, model_dim, sae_dim)
    +forward(self, x)
    +compute_superposition_metrics(self, z_encoded)
  }
  class models_py_SuperpositionSAE {
    <<class>>
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
    +forward(self, x)
    +get_flat_parameters(self)
    +__init__(self, model_dim, sae_dim)
    +forward(self, x)
    +compute_superposition_metrics(self, z_encoded)
  }
  class streamlit_app_py_ThermodynamicAnalyzer {
    <<class>>
    +main()
    +compute_metrics(weights_list, phase, epoch)
    +__init__(self, config)
    +train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)
    +_create_3d_visualization(self, weights_list, phase_name, thermo_metrics)
    +_create_2d_visualization(self, weights_list, phase_name, thermo_metrics)
    +_create_metrics_plot(self, history, phase_name)
    +run_curriculum(self)
  }
  class streamlit_app_py_StreamlitTrainer {
    <<class>>
    +main()
    +compute_metrics(weights_list, phase, epoch)
    +__init__(self, config)
    +train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)
    +_create_3d_visualization(self, weights_list, phase_name, thermo_metrics)
    +_create_2d_visualization(self, weights_list, phase_name, thermo_metrics)
    +_create_metrics_plot(self, history, phase_name)
    +run_curriculum(self)
  }
  class training_py_CurriculumStageTrainer {
    <<class>>
    +__init__(self, config, seed)
    +train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)
    +_create_checkpoint_state(self, model, sae, optimizer, stage, n_bits, hidden_dim, step, metrics_history)
  }
  class training_dynamics_py_SmartWeightTransfer {
    <<class>>
    +transfer(self, previous_model, new_model, stage)
    +__init__(self, config)
    +is_stagnant(self, metrics_history, current_step, hidden_dim)
  }
  class training_dynamics_py_StagnationDetector {
    <<class>>
    +transfer(self, previous_model, new_model, stage)
    +__init__(self, config)
    +is_stagnant(self, metrics_history, current_step, hidden_dim)
  }
  class wandb_integration_py_WandBLogger {
    <<class>>
    +__init__(self, config)
    +initialize(self, run_name, run_config)
    +log_metrics(self, metrics, step)
    +finish(self)
  }
  class purity_analysis_py_PurityConfig {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_IModel {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_IPurityIndexCalculator {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_IEffectiveTemperatureCalculator {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_IPhaseClassifier {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_IPolycrystalAnalyzer {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_IPurityComparator {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_PurityIndexCalculator {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_EffectiveTemperatureCalculator {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_PhaseClassifier {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_PolycrystalAnalyzer {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_PurityComparator {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_CheckpointLoader {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_PurityAnalyzer {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class purity_analysis_py_PurityPipeline {
    <<class>>
    +main()
    +get_flat_parameters(self)
    +calculate(self, model)
    +calculate(self, loss_history)
    +classify(self, alpha, temperature)
    +analyze_polycrystal(self, model, pruning_level)
    +compare(self, original, polycrystal)
    +__init__(self, config)
    +calculate(self, model)
    +_compute_layer_purity(self, weights)
  }
  class realtime_train_py_ExperimentConfig {
    <<class>>
    +main()
    +calculate(self)
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
  }
  class realtime_train_py_IMetricCalculator {
    <<class>>
    +main()
    +calculate(self)
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
  }
  class realtime_train_py_IModelArchitecture {
    <<class>>
    +main()
    +calculate(self)
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
  }
  class realtime_train_py_ICheckpointManager {
    <<class>>
    +main()
    +calculate(self)
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
  }
  class realtime_train_py_GrokkingTransformer {
    <<class>>
    +main()
    +calculate(self)
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
  }
  class realtime_train_py_SuperpositionSAE {
    <<class>>
    +main()
    +calculate(self)
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
  }
  class realtime_train_py_ParityDatasetGenerator {
    <<class>>
    +main()
    +calculate(self)
    +forward(self, x)
    +get_pre_activations(self, x)
    +get_flat_parameters(self)
    +save(self, state, path)
    +load(self, path)
    +should_checkpoint(self)
    +__init__(self, input_dim, hidden_dim, output_dim)
    +get_pre_activations(self, x)
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [{"cohesion": 1.0, "id": 0, "label": "root", "size": 7}, {"cohesion": 1.0, "id": 1, "label": "new_experiment", "size": 12}], "god_nodes": [{"node_id": "new_experiment/config.py", "score": 20.4}, {"node_id": "new_experiment/training.py", "score": 16.4}, {"node_id": "app.py", "score": 13.8}, {"node_id": "new_experiment/streamlit_app.py", "score": 13.0}, {"node_id": "new_experiment/test_framework.py", "score": 12.8}, {"node_id": "new_experiment/metrics.py", "score": 12.0}, {"node_id": "new_experiment/models.py", "score": 11.3}, {"node_id": "purity_analysis.py", "score": 9.0}, {"node_id": "new_experiment/training_dynamics.py", "score": 8.5}, {"node_id": "new_experiment/data_generation.py", "score": 8.3}], "surprising_connections": []}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "128bits.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "128bits.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "128bits.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "128bits.py", "target": "app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "2048bits.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "2048bits.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "2048bits.py", "target": "app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app_wandb.py", "target": "wandb"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/checkpointing.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/checkpointing.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/checkpointing.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/checkpointing.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/checkpointing.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/checkpointing.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/checkpointing.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/config.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/config.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/config.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/config.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/config.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/config.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/data_generation.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/data_generation.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/data_generation.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/main.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/main.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/main.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/main.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/main.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/main.py", "target": "training"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/metrics.py", "target": "models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/models.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/models.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/models.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/models.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/models.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/models.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "streamlit"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "plotly.graph_objects"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "plotly.subplots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "sklearn.decomposition"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "sklearn.cluster"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "scipy.spatial.distance"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "data_generation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "metrics"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "training_dynamics"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/streamlit_app.py", "target": "wandb_integration"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "data_generation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "metrics"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "checkpointing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/test_framework.py", "target": "training_dynamics"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "torch.optim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "data_generation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "metrics"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "checkpointing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "training_dynamics"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "wandb_integration"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training_dynamics.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training_dynamics.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training_dynamics.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/training_dynamics.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/wandb_integration.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/wandb_integration.py", "target": "wandb"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "new_experiment/wandb_integration.py", "target": "config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "scipy.stats"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "new_experiment.config"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "new_experiment.models"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "purity_analysis.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "torch.optim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "signal"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "matplotlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "matplotlib.gridspec"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "realtime_train.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test.py", "target": "app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test_wandb_ablation.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test_wandb_ablation.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test_wandb_ablation.py", "target": "wandb"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "test_wandb_ablation.py", "target": "app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "streamlit"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "plotly.graph_objects"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "plotly.subplots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "sklearn.decomposition"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "sklearn.cluster"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "scipy.spatial.distance"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "view_streamlit.py", "target": "app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "mpl_toolkits.mplot3d"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "sklearn.decomposition"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "sklearn.manifold"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "app"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "visualizador.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "128bits.py", "target": "app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "2048bits.py", "target": "app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/checkpointing.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/data_generation.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/main.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/main.py", "target": "new_experiment/training.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/metrics.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/metrics.py", "target": "new_experiment/models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/streamlit_app.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/streamlit_app.py", "target": "new_experiment/models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/streamlit_app.py", "target": "new_experiment/data_generation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/streamlit_app.py", "target": "new_experiment/metrics.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/streamlit_app.py", "target": "new_experiment/training_dynamics.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/streamlit_app.py", "target": "new_experiment/wandb_integration.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/test_framework.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/test_framework.py", "target": "new_experiment/models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/test_framework.py", "target": "new_experiment/data_generation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/test_framework.py", "target": "new_experiment/metrics.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/test_framework.py", "target": "new_experiment/checkpointing.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/test_framework.py", "target": "new_experiment/training_dynamics.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training.py", "target": "new_experiment/models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training.py", "target": "new_experiment/data_generation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training.py", "target": "new_experiment/metrics.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training.py", "target": "new_experiment/checkpointing.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training.py", "target": "new_experiment/training_dynamics.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training.py", "target": "new_experiment/wandb_integration.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/training_dynamics.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "new_experiment/wandb_integration.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "purity_analysis.py", "target": "new_experiment/config.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "purity_analysis.py", "target": "new_experiment/models.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "test.py", "target": "app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "test_wandb_ablation.py", "target": "app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "view_streamlit.py", "target": "app.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "visualizador.py", "target": "app.py"}], "generator": "readmenator", "metadata": {"edge_count": 2777, "file_count": 22, "language_count": 2, "symbol_count": 282}, "nodes": [{"doc": "-*- coding: utf-8 -*-", "id": "128bits.py", "kind": "module", "label": "128bits.py", "language": "py", "sha256": "97eff33c5c279cd2", "symbol_count": 3, "symbols": [{"kind": "function", "line": 34, "name": "evaluate", "signature": "def evaluate(model, x, y)"}, {"kind": "function", "line": 39, "name": "load_64bit_model", "signature": "def load_64bit_model()"}, {"kind": "function", "line": 49, "name": "run_experiment", "signature": "def run_experiment(use_padding)"}]}, {"doc": "-*- coding: utf-8 -*-", "id": "2048bits.py", "kind": "module", "label": "2048bits.py", "language": "py", "sha256": "596dd87b790e2034", "symbol_count": 3, "symbols": [{"kind": "function", "line": 44, "name": "evaluate", "signature": "def evaluate(model, x, y)"}, {"kind": "function", "line": 49, "name": "load_base_model", "signature": "def load_base_model()"}, {"kind": "function", "line": 59, "name": "zero_shot_test", "signature": "def zero_shot_test(prev_model, n_bits, d_h, use_padding)"}]}, {"doc": "_*_ coding: utf8 _*_", "id": "app.py", "kind": "module", "label": "app.py", "language": "py", "sha256": "b535afbfeb034fb4", "symbol_count": 18, "symbols": [{"kind": "class", "line": 32, "name": "SuperpositionSAE", "signature": "class SuperpositionSAE(Module)"}, {"kind": "class", "line": 55, "name": "ComplexityAnalyzer", "signature": "class ComplexityAnalyzer"}, {"kind": "class", "line": 67, "name": "GrokkingTransformer", "signature": "class GrokkingTransformer(Module)"}, {"kind": "method", "line": 87, "name": "get_parity_dataset", "signature": "def get_parity_dataset(n_bits, k, size)"}, {"kind": "class", "line": 92, "name": "AdaptiveCurriculumTrainer", "signature": "class AdaptiveCurriculumTrainer"}, {"kind": "method", "line": 33, "name": "__init__", "signature": "def __init__(self, d_model, d_sae)"}, {"kind": "method", "line": 40, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 45, "name": "get_metrics", "signature": "def get_metrics(self, z)"}, {"kind": "method", "line": 57, "name": "measure_lc", "signature": "def measure_lc(model, x, epsilon)"}, {"kind": "method", "line": 68, "name": "__init__", "signature": "def __init__(self, d_in, d_h)"}, {"kind": "method", "line": 74, "name": "get_pre_acts", "signature": "def get_pre_acts(self, x)"}, {"kind": "method", "line": 80, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 93, "name": "__init__", "signature": "def __init__(self)"}, {"doc": "Calcula parámetros adaptativos según la complejidad de la etapa", "kind": "method", "line": 109, "name": "calculate_adaptive_params", "signature": "def calculate_adaptive_params(self, n_bits, d_h, stage)"}, {"doc": "Transferencia inteligente de pesos con padding/interpolación", "kind": "method", "line": 126, "name": "smart_weight_transfer", "signature": "def smart_weight_transfer(self, prev_model, new_model, stage)"}, {"doc": "Detecta si el modelo está estancado y necesita reinicio", "kind": "method", "line": 166, "name": "detect_stagnation", "signature": "def detect_stagnation(self, history, current_lc, d_h, step)"}, {"doc": "Entrena una etapa individual con parámetros adaptativos", "kind": "method", "line": 184, "name": "train_stage", "signature": "def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)"}, {"doc": "Ejecuta el curriculum completo con adaptación automática", "kind": "method", "line": 316, "name": "run_curriculum", "signature": "def run_curriculum(self)"}]}, {"doc": "_*_ coding: utf8 _*_", "id": "app_wandb.py", "kind": "module", "label": "app_wandb.py", "language": "py", "sha256": "cd5bfb9222849d7a", "symbol_count": 21, "symbols": [{"doc": "Initialize wandb tracking", "kind": "function", "line": 35, "name": "init_wandb", "signature": "def init_wandb(project_name, config)"}, {"doc": "Log metrics to wandb", "kind": "function", "line": 43, "name": "log_training_step", "signature": "def log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)"}, {"doc": "Finish wandb run", "kind": "function", "line": 59, "name": "finish_wandb", "signature": "def finish_wandb()"}, {"kind": "class", "line": 63, "name": "SuperpositionSAE", "signature": "class SuperpositionSAE(Module)"}, {"kind": "class", "line": 86, "name": "ComplexityAnalyzer", "signature": "class ComplexityAnalyzer"}, {"kind": "class", "line": 98, "name": "GrokkingTransformer", "signature": "class GrokkingTransformer(Module)"}, {"kind": "method", "line": 118, "name": "get_parity_dataset", "signature": "def get_parity_dataset(n_bits, k, size)"}, {"kind": "class", "line": 123, "name": "AdaptiveCurriculumTrainer", "signature": "class AdaptiveCurriculumTrainer"}, {"kind": "method", "line": 64, "name": "__init__", "signature": "def __init__(self, d_model, d_sae)"}, {"kind": "method", "line": 71, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 76, "name": "get_metrics", "signature": "def get_metrics(self, z)"}, {"kind": "method", "line": 88, "name": "measure_lc", "signature": "def measure_lc(model, x, epsilon)"}, {"kind": "method", "line": 99, "name": "__init__", "signature": "def __init__(self, d_in, d_h)"}, {"kind": "method", "line": 105, "name": "get_pre_acts", "signature": "def get_pre_acts(self, x)"}, {"kind": "method", "line": 111, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 124, "name": "__init__", "signature": "def __init__(self)"}, {"doc": "Calculate adaptive parameters according to stage complexity", "kind": "method", "line": 140, "name": "calculate_adaptive_params", "signature": "def calculate_adaptive_params(self, n_bits, d_h, stage)"}, {"doc": "Intelligent weight transfer with padding/interpolation", "kind": "method", "line": 157, "name": "smart_weight_transfer", "signature": "def smart_weight_transfer(self, prev_model, new_model, stage)"}, {"doc": "Detect if model is stagnant and needs restart", "kind": "method", "line": 196, "name": "detect_stagnation", "signature": "def detect_stagnation(self, history, current_lc, d_h, step)"}, {"doc": "Train individual stage with adaptive parameters", "kind": "method", "line": 212, "name": "train_stage", "signature": "def train_stage(self, stage, n_bits, d_h, prev_model, prev_sae)"}, {"doc": "Execute complete curriculum with automatic adaptation", "kind": "method", "line": 345, "name": "run_curriculum", "signature": "def run_curriculum(self)"}]}, {"id": "install.sh", "kind": "module", "label": "install.sh", "language": "sh", "sha256": "c907d80fd6734993", "symbol_count": 0, "symbols": []}, {"id": "new_experiment/checkpointing.py", "kind": "module", "label": "checkpointing.py", "language": "py", "sha256": "d8dbe5baa2a3fce6", "symbol_count": 10, "symbols": [{"doc": "Interface for checkpoint management.", "kind": "class", "line": 16, "name": "ICheckpointManager", "signature": "class ICheckpointManager(ABC)"}, {"doc": "Manage experiment checkpoints with automatic interval-based saving.\n\nSaves both timestamped checkpoints and a latest checkpoint that\ncan be used for resuming training.", "kind": "class", "line": 35, "name": "CheckpointManager", "signature": "class CheckpointManager(ICheckpointManager)"}, {"doc": "Save checkpoint and return path.", "kind": "method", "line": 20, "name": "save", "signature": "def save(self, state, path)"}, {"doc": "Load checkpoint from path.", "kind": "method", "line": 25, "name": "load", "signature": "def load(self, path)"}, {"doc": "Determine if checkpoint should be saved.", "kind": "method", "line": 30, "name": "should_checkpoint", "signature": "def should_checkpoint(self)"}, {"doc": "Initialize checkpoint manager.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 43, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Save checkpoint to disk.\n\nArgs:\n    state: State dictionary to save\n    path: Optional specific path for checkpoint\n    \nReturns:\n    Path where checkpoint was saved", "kind": "method", "line": 55, "name": "save", "signature": "def save(self, state, path)"}, {"doc": "Load checkpoint from disk.\n\nArgs:\n    path: Path to checkpoint file\n    \nReturns:\n    Loaded state dictionary or None if load fails", "kind": "method", "line": 85, "name": "load", "signature": "def load(self, path)"}, {"doc": "Check if checkpoint interval has elapsed.\n\nReturns:\n    True if time to save checkpoint", "kind": "method", "line": 101, "name": "should_checkpoint", "signature": "def should_checkpoint(self)"}, {"doc": "Get path to latest checkpoint if exists.\n\nReturns:\n    Path to latest checkpoint or None", "kind": "method", "line": 111, "name": "get_latest_checkpoint_path", "signature": "def get_latest_checkpoint_path(self)"}]}, {"id": "new_experiment/config.py", "kind": "module", "label": "config.py", "language": "py", "sha256": "ced4e23c549c0a63", "symbol_count": 4, "symbols": [{"doc": "Centralized configuration for all experimental parameters.\nAll magic numbers are eliminated and made explicit.", "kind": "class", "line": 13, "name": "ExperimentConfig", "signature": "class ExperimentConfig"}, {"doc": "Calculate adaptive training size based on input dimensionality.", "kind": "method", "line": 111, "name": "get_adaptive_train_size", "signature": "def get_adaptive_train_size(self, n_bits)"}, {"doc": "Calculate adaptive weight decay based on problem complexity.", "kind": "method", "line": 117, "name": "get_adaptive_weight_decay", "signature": "def get_adaptive_weight_decay(self, n_bits, hidden_dim)"}, {"doc": "Calculate adaptive maximum steps based on problem complexity.", "kind": "method", "line": 126, "name": "get_adaptive_max_steps", "signature": "def get_adaptive_max_steps(self, n_bits, hidden_dim)"}]}, {"id": "new_experiment/data_generation.py", "kind": "module", "label": "data_generation.py", "language": "py", "sha256": "d12f3809533f5777", "symbol_count": 3, "symbols": [{"doc": "Generates binary parity learning datasets.\n\nThe parity function computes whether the sum of the first k bits\nof an n-bit input vector is odd (1) or even (0).", "kind": "class", "line": 11, "name": "ParityDatasetGenerator", "signature": "class ParityDatasetGenerator"}, {"doc": "Initialize dataset generator.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 19, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate random binary vectors with k-bit parity labels.\n\nArgs:\n    n_bits: Total number of input bits\n    k_bits: Number of bits used for parity calculation\n    dataset_size: Number of samples to generate\n    \nReturns:\n    Tuple of (inputs, labels) where inputs are binary vectors\n    and labels are parity values", "kind": "method", "line": 28, "name": "generate", "signature": "def generate(self, n_bits, k_bits, dataset_size)"}]}, {"id": "new_experiment/main.py", "kind": "module", "label": "main.py", "language": "py", "sha256": "711271b6a7fa9365", "symbol_count": 6, "symbols": [{"doc": "Run curriculum training across multiple random seeds.\n\nExecutes the full curriculum for each seed, collecting\ncomprehensive results and metrics.", "kind": "class", "line": 16, "name": "MultiSeedCurriculumRunner", "signature": "class MultiSeedCurriculumRunner"}, {"doc": "Main entry point for command-line execution.", "kind": "method", "line": 130, "name": "main", "signature": "def main()"}, {"doc": "Initialize runner.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 24, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Set random seed for reproducibility.\n\nArgs:\n    seed: Random seed value", "kind": "method", "line": 35, "name": "_set_seed", "signature": "def _set_seed(self, seed)"}, {"doc": "Run curriculum for a single seed.\n\nArgs:\n    seed: Random seed value\n    \nReturns:\n    True if curriculum completed successfully", "kind": "method", "line": 48, "name": "run_single_seed", "signature": "def run_single_seed(self, seed)"}, {"doc": "Run experiment across multiple seeds.\n\nArgs:\n    start_seed: Starting seed number\n    end_seed: Ending seed number", "kind": "method", "line": 90, "name": "run_experiment", "signature": "def run_experiment(self, start_seed, end_seed)"}]}, {"id": "new_experiment/metrics.py", "kind": "module", "label": "metrics.py", "language": "py", "sha256": "79505e55316e848a", "symbol_count": 20, "symbols": [{"doc": "Interface for metric calculation strategies.", "kind": "class", "line": 17, "name": "IMetricCalculator", "signature": "class IMetricCalculator(ABC)"}, {"doc": "Calculate local complexity as effective local dimensionality.\n\nLocal complexity measures the number of near-zero pre-activations,\nindicating representational sparsity.", "kind": "class", "line": 26, "name": "LocalComplexityCalculator", "signature": "class LocalComplexityCalculator(IMetricCalculator)"}, {"doc": "Calculate gradient covariance matrix and condition number.\n\nThe condition number kappa measures the ratio of largest to smallest\neigenvalues of the gradient covariance matrix, indicating optimization\nlandscape geometry.", "kind": "class", "line": 81, "name": "GradientCovarianceCalculator", "signature": "class GradientCovarianceCalculator"}, {"doc": "Calculate thermodynamic metrics: effective temperature and Planck constant.\n\nThese metrics characterize the energy landscape and quantum-like properties\nof the learning dynamics.", "kind": "class", "line": 166, "name": "ThermodynamicMetricsCalculator", "signature": "class ThermodynamicMetricsCalculator(IMetricCalculator)"}, {"doc": "Calculate discretization margin delta.\n\nDelta measures how close parameter values are to integers,\nindicating algorithmic crystallization.", "kind": "class", "line": 253, "name": "DeltaCalculator", "signature": "class DeltaCalculator(IMetricCalculator)"}, {"doc": "Aggregate all thermodynamic and learning metrics.\n\nCentralizes metric calculation and provides unified interface.", "kind": "class", "line": 282, "name": "ComprehensiveMetricsAggregator", "signature": "class ComprehensiveMetricsAggregator"}, {"doc": "Calculate metrics and return dictionary of results.", "kind": "method", "line": 21, "name": "calculate", "signature": "def calculate(self)"}, {"doc": "Initialize calculator.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 34, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Measure LC as count of near-zero pre-activations.\n\nArgs:\n    model: Neural network model\n    x_batch: Input batch\n    \nReturns:\n    Dictionary containing local complexity value", "kind": "method", "line": 44, "name": "calculate", "signature": "def calculate(self, model, x_batch)"}, {"doc": "Initialize calculator.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 90, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Store current gradient vector.\n\nArgs:\n    model: Neural network model", "kind": "method", "line": 102, "name": "accumulate_gradient", "signature": "def accumulate_gradient(self, model)"}, {"doc": "Calculate condition number of gradient covariance matrix.\n\nReturns:\n    Tuple of (kappa, covariance_matrix)", "kind": "method", "line": 121, "name": "calculate_kappa", "signature": "def calculate_kappa(self)"}, {"doc": "Clear gradient buffer.", "kind": "method", "line": 161, "name": "reset", "signature": "def reset(self)"}, {"doc": "Initialize calculator.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 174, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Calculate effective temperature and Planck constant.\n\nArgs:\n    gradient_covariance: Gradient covariance matrix\n    \nReturns:\n    Dictionary containing thermodynamic metrics", "kind": "method", "line": 183, "name": "calculate", "signature": "def calculate(self, gradient_covariance)"}, {"doc": "Calculate mean squared distance to nearest integer.\n\nArgs:\n    model: Neural network model\n    \nReturns:\n    Dictionary containing delta value", "kind": "method", "line": 261, "name": "calculate", "signature": "def calculate(self, model)"}, {"doc": "Initialize aggregator.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 289, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute comprehensive metric suite.\n\nArgs:\n    model: Neural network model\n    sae: Sparse autoencoder\n    train_loader: Training data\n    train_labels: Training labels\n    test_loader: Test data\n    test_labels: Test labels\n    current_loss: Current loss value\n    z_sae: SAE encoded features\n    step: Current training step\n    \nReturns:\n    Dictionary containing all computed metrics", "kind": "method", "line": 302, "name": "compute_all_metrics", "signature": "def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, step)"}, {"doc": "Accumulate gradient for kappa calculation.\n\nArgs:\n    model: Neural network model", "kind": "method", "line": 374, "name": "accumulate_gradient", "signature": "def accumulate_gradient(self, model)"}, {"doc": "Reset all stateful calculators.", "kind": "method", "line": 383, "name": "reset", "signature": "def reset(self)"}]}, {"id": "new_experiment/models.py", "kind": "module", "label": "models.py", "language": "py", "sha256": "892f9c8cff3774fa", "symbol_count": 13, "symbols": [{"doc": "Interface for neural network architectures.", "kind": "class", "line": 14, "name": "IModelArchitecture", "signature": "class IModelArchitecture(ABC)"}, {"doc": "Two-layer MLP for parity learning experiments.\n\nArchitecture:\n    input -> fc1 -> ReLU -> fc2 -> ReLU -> output", "kind": "class", "line": 33, "name": "GrokkingTransformer", "signature": "class GrokkingTransformer(Module, IModelArchitecture)"}, {"doc": "Sparse Autoencoder for superposition analysis.\n\nUsed to measure effective feature dimensionality and\nsuperposition coefficient in learned representations.", "kind": "class", "line": 101, "name": "SuperpositionSAE", "signature": "class SuperpositionSAE(Module)"}, {"doc": "Forward pass returning logits and latent representation.", "kind": "method", "line": 18, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Get pre-activation tensors for complexity analysis.", "kind": "method", "line": 23, "name": "get_pre_activations", "signature": "def get_pre_activations(self, x)"}, {"doc": "Get flattened parameter vector.", "kind": "method", "line": 28, "name": "get_flat_parameters", "signature": "def get_flat_parameters(self)"}, {"doc": "Initialize network.\n\nArgs:\n    input_dim: Number of input features\n    hidden_dim: Hidden layer dimensionality\n    output_dim: Number of output classes", "kind": "method", "line": 41, "name": "__init__", "signature": "def __init__(self, input_dim, hidden_dim, output_dim)"}, {"doc": "Get pre-activation tensors for local complexity calculation.\n\nArgs:\n    x: Input tensor\n    \nReturns:\n    List of pre-activation tensors", "kind": "method", "line": 59, "name": "get_pre_activations", "signature": "def get_pre_activations(self, x)"}, {"doc": "Forward pass through network.\n\nArgs:\n    x: Input tensor\n    \nReturns:\n    Tuple of (logits, latent_representation)", "kind": "method", "line": 74, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Get flattened parameter vector.\n\nReturns:\n    1D tensor containing all model parameters", "kind": "method", "line": 91, "name": "get_flat_parameters", "signature": "def get_flat_parameters(self)"}, {"doc": "Initialize SAE.\n\nArgs:\n    model_dim: Dimensionality of model representations\n    sae_dim: Expanded SAE feature dimensionality", "kind": "method", "line": 109, "name": "__init__", "signature": "def __init__(self, model_dim, sae_dim)"}, {"doc": "Encode and decode with ReLU activation.\n\nArgs:\n    x: Input representations\n    \nReturns:\n    Tuple of (reconstructed, encoded_features)", "kind": "method", "line": 126, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Calculate superposition coefficient and effective features.\n\nThe superposition coefficient measures how efficiently the model\npacks information into its representation space.\n\nArgs:\n    z_encoded: Encoded feature activations\n    \nReturns:\n    Tuple of (psi_coefficient, effective_features)", "kind": "method", "line": 140, "name": "compute_superposition_metrics", "signature": "def compute_superposition_metrics(self, z_encoded)"}]}, {"id": "new_experiment/streamlit_app.py", "kind": "module", "label": "streamlit_app.py", "language": "py", "sha256": "3094e8ad278a8ca6", "symbol_count": 10, "symbols": [{"doc": "Complete thermodynamic analysis of phase transitions.", "kind": "class", "line": 75, "name": "ThermodynamicAnalyzer", "signature": "class ThermodynamicAnalyzer"}, {"doc": "Real-time training with Streamlit visualization.", "kind": "class", "line": 143, "name": "StreamlitTrainer", "signature": "class StreamlitTrainer"}, {"doc": "Main Streamlit application.", "kind": "method", "line": 596, "name": "main", "signature": "def main()"}, {"doc": "Calculate complete thermodynamic state.", "kind": "method", "line": 79, "name": "compute_metrics", "signature": "def compute_metrics(weights_list, phase, epoch)"}, {"doc": "Initialize trainer.", "kind": "method", "line": 146, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Train stage with real-time Streamlit visualization.", "kind": "method", "line": 163, "name": "train_stage_with_visualization", "signature": "def train_stage_with_visualization(self, stage, n_bits, hidden_dim, previous_model, previous_sae)"}, {"doc": "Create 3D PCA visualization.", "kind": "method", "line": 424, "name": "_create_3d_visualization", "signature": "def _create_3d_visualization(self, weights_list, phase_name, thermo_metrics)"}, {"doc": "Create 2D texture visualization.", "kind": "method", "line": 478, "name": "_create_2d_visualization", "signature": "def _create_2d_visualization(self, weights_list, phase_name, thermo_metrics)"}, {"doc": "Create comprehensive metrics plot.", "kind": "method", "line": 526, "name": "_create_metrics_plot", "signature": "def _create_metrics_plot(self, history, phase_name)"}, {"doc": "Execute complete curriculum.", "kind": "method", "line": 570, "name": "run_curriculum", "signature": "def run_curriculum(self)"}]}, {"id": "new_experiment/test_framework.py", "kind": "module", "label": "test_framework.py", "language": "py", "sha256": "8c1f18a9c221a23a", "symbol_count": 8, "symbols": [{"doc": "Test configuration creation and parameter calculation.", "kind": "function", "line": 17, "name": "test_configuration", "signature": "def test_configuration()"}, {"doc": "Test dataset generation.", "kind": "function", "line": 38, "name": "test_data_generation", "signature": "def test_data_generation()"}, {"doc": "Test model architectures.", "kind": "function", "line": 53, "name": "test_models", "signature": "def test_models()"}, {"doc": "Test metric calculation.", "kind": "function", "line": 80, "name": "test_metrics", "signature": "def test_metrics()"}, {"doc": "Test checkpoint management.", "kind": "function", "line": 119, "name": "test_checkpointing", "signature": "def test_checkpointing()"}, {"doc": "Test smart weight transfer.", "kind": "function", "line": 142, "name": "test_weight_transfer", "signature": "def test_weight_transfer()"}, {"doc": "Test stagnation detector.", "kind": "function", "line": 158, "name": "test_stagnation_detection", "signature": "def test_stagnation_detection()"}, {"doc": "Run all tests.", "kind": "function", "line": 178, "name": "run_all_tests", "signature": "def run_all_tests()"}]}, {"id": "new_experiment/training.py", "kind": "module", "label": "training.py", "language": "py", "sha256": "deddc55dd831464e", "symbol_count": 4, "symbols": [{"doc": "Train a single curriculum stage with full metric tracking.\n\nHandles training loop, metric computation, checkpoint management,\nand stagnation detection for one stage of the curriculum.", "kind": "class", "line": 21, "name": "CurriculumStageTrainer", "signature": "class CurriculumStageTrainer"}, {"doc": "Initialize stage trainer.\n\nArgs:\n    config: Experiment configuration\n    seed: Random seed for reproducibility", "kind": "method", "line": 29, "name": "__init__", "signature": "def __init__(self, config, seed)"}, {"doc": "Train a single curriculum stage.\n\nArgs:\n    stage: Stage number\n    n_bits: Number of input bits\n    hidden_dim: Hidden layer dimensionality\n    previous_model: Model from previous stage\n    previous_sae: SAE from previous stage\n    \nReturns:\n    Tuple of (model, sae, success, metrics_history)", "kind": "method", "line": 48, "name": "train_stage", "signature": "def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)"}, {"doc": "Create checkpoint state dictionary.\n\nArgs:\n    model: Neural network model\n    sae: Sparse autoencoder\n    optimizer: Optimizer\n    stage: Current stage\n    n_bits: Number of bits\n    hidden_dim: Hidden dimensionality\n    step: Current step\n    metrics_history: Training metrics\n    \nReturns:\n    State dictionary for checkpointing", "kind": "method", "line": 289, "name": "_create_checkpoint_state", "signature": "def _create_checkpoint_state(self, model, sae, optimizer, stage, n_bits, hidden_dim, step, metrics_history)"}]}, {"id": "new_experiment/training_dynamics.py", "kind": "module", "label": "training_dynamics.py", "language": "py", "sha256": "b20d723abf92a1de", "symbol_count": 5, "symbols": [{"doc": "Transfer weights intelligently between curriculum stages.\n\nHandles dimension mismatches through padding and cropping\nwhile preserving learned algorithmic structure.", "kind": "class", "line": 13, "name": "SmartWeightTransfer", "signature": "class SmartWeightTransfer"}, {"doc": "Detect training stagnation and trigger optimizer resets.\n\nMonitors test accuracy improvement and local complexity to\nidentify when training is stuck in poor local minima.", "kind": "class", "line": 83, "name": "StagnationDetector", "signature": "class StagnationDetector"}, {"doc": "Transfer weights with padding or cropping as needed.\n\nArgs:\n    previous_model: Model from previous curriculum stage\n    new_model: New model for current stage\n    stage: Current stage number\n    \nReturns:\n    New model with transferred weights", "kind": "method", "line": 21, "name": "transfer", "signature": "def transfer(self, previous_model, new_model, stage)"}, {"doc": "Initialize detector.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 91, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Determine if training is stagnant.\n\nArgs:\n    metrics_history: List of historical metrics\n    current_step: Current training step\n    hidden_dim: Hidden layer dimensionality\n    \nReturns:\n    Tuple of (is_stagnant, reason)", "kind": "method", "line": 101, "name": "is_stagnant", "signature": "def is_stagnant(self, metrics_history, current_step, hidden_dim)"}]}, {"id": "new_experiment/wandb_integration.py", "kind": "module", "label": "wandb_integration.py", "language": "py", "sha256": "8f5ca22a30c3bd27", "symbol_count": 5, "symbols": [{"doc": "Wrapper for Weights and Biases logging functionality.\n\nHandles initialization, metric logging, and cleanup.", "kind": "class", "line": 12, "name": "WandBLogger", "signature": "class WandBLogger"}, {"doc": "Initialize WandB logger.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 19, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Initialize WandB run.\n\nArgs:\n    run_name: Name for this run\n    run_config: Configuration dictionary to log", "kind": "method", "line": 30, "name": "initialize", "signature": "def initialize(self, run_name, run_config)"}, {"doc": "Log metrics to WandB.\n\nArgs:\n    metrics: Dictionary of metric names to values\n    step: Optional step number", "kind": "method", "line": 58, "name": "log_metrics", "signature": "def log_metrics(self, metrics, step)"}, {"doc": "Finish WandB run.", "kind": "method", "line": 77, "name": "finish", "signature": "def finish(self)"}]}, {"id": "purity_analysis.py", "kind": "module", "label": "purity_analysis.py", "language": "py", "sha256": "30faa1bdd9522d53", "symbol_count": 50, "symbols": [{"doc": "Configuration for purity index analysis.", "kind": "class", "line": 25, "name": "PurityConfig", "signature": "class PurityConfig"}, {"doc": "Protocol for models supporting purity analysis.", "kind": "class", "line": 49, "name": "IModel", "signature": "class IModel(Protocol)"}, {"doc": "Protocol for purity index calculation.", "kind": "class", "line": 56, "name": "IPurityIndexCalculator", "signature": "class IPurityIndexCalculator(Protocol)"}, {"doc": "Protocol for effective temperature calculation.", "kind": "class", "line": 63, "name": "IEffectiveTemperatureCalculator", "signature": "class IEffectiveTemperatureCalculator(Protocol)"}, {"doc": "Protocol for phase classification.", "kind": "class", "line": 70, "name": "IPhaseClassifier", "signature": "class IPhaseClassifier(Protocol)"}, {"doc": "Protocol for polycrystal analysis.", "kind": "class", "line": 77, "name": "IPolycrystalAnalyzer", "signature": "class IPolycrystalAnalyzer(Protocol)"}, {"doc": "Protocol for purity comparison.", "kind": "class", "line": 88, "name": "IPurityComparator", "signature": "class IPurityComparator(Protocol)"}, {"doc": "Calculate purity index for neural network models.\n\nMeasures how close weights are to integer values (crystallization).", "kind": "class", "line": 98, "name": "PurityIndexCalculator", "signature": "class PurityIndexCalculator"}, {"doc": "Calculate effective temperature from loss dynamics.\n\nTemperature measures training volatility and convergence.", "kind": "class", "line": 235, "name": "EffectiveTemperatureCalculator", "signature": "class EffectiveTemperatureCalculator"}, {"doc": "Classify crystallization phase based on purity and temperature.\n\nIdentifies gas, liquid, transition, and crystalline phases.", "kind": "class", "line": 314, "name": "PhaseClassifier", "signature": "class PhaseClassifier"}, {"doc": "Analyze polycrystalline structure through weight pruning.\n\nTests structural robustness and phase stability.", "kind": "class", "line": 393, "name": "PolycrystalAnalyzer", "signature": "class PolycrystalAnalyzer"}, {"doc": "Compare purity metrics between original and perturbed states.\n\nQuantifies structural memory and thermal damage.", "kind": "class", "line": 501, "name": "PurityComparator", "signature": "class PurityComparator"}, {"doc": "Load and validate checkpoints for purity analysis.\n\nHandles different checkpoint formats and model configurations.", "kind": "class", "line": 576, "name": "CheckpointLoader", "signature": "class CheckpointLoader"}, {"doc": "Main purity analysis orchestrator.\n\nCoordinates all analysis components and generates comprehensive reports.", "kind": "class", "line": 643, "name": "PurityAnalyzer", "signature": "class PurityAnalyzer"}, {"doc": "Pipeline for batch processing checkpoints.\n\nHandles multiple checkpoints and generates aggregate statistics.", "kind": "class", "line": 818, "name": "PurityPipeline", "signature": "class PurityPipeline"}, {"doc": "Main entry point for purity analysis.", "kind": "method", "line": 1049, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 52, "name": "get_flat_parameters", "signature": "def get_flat_parameters(self)"}, {"kind": "method", "line": 59, "name": "calculate", "signature": "def calculate(self, model)"}, {"kind": "method", "line": 66, "name": "calculate", "signature": "def calculate(self, loss_history)"}, {"kind": "method", "line": 73, "name": "classify", "signature": "def classify(self, alpha, temperature)"}, {"kind": "method", "line": 80, "name": "analyze_polycrystal", "signature": "def analyze_polycrystal(self, model, pruning_level)"}, {"kind": "method", "line": 91, "name": "compare", "signature": "def compare(self, original, polycrystal)"}, {"doc": "Initialize calculator.\n\nArgs:\n    config: Purity analysis configuration", "kind": "method", "line": 105, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Calculate comprehensive purity metrics.\n\nArgs:\n    model: Neural network model\n    \nReturns:\n    Dictionary containing purity metrics", "kind": "method", "line": 114, "name": "calculate", "signature": "def calculate(self, model)"}, {"doc": "Compute purity metrics for a single layer.\n\nArgs:\n    weights: Layer weight tensor\n    \nReturns:\n    Tuple of (alpha, delta)", "kind": "method", "line": 159, "name": "_compute_layer_purity", "signature": "def _compute_layer_purity(self, weights)"}, {"doc": "Convert discretization margin to purity index.\n\nArgs:\n    delta: Discretization margin\n    \nReturns:\n    Purity index alpha", "kind": "method", "line": 177, "name": "_delta_to_alpha", "signature": "def _delta_to_alpha(self, delta)"}, {"doc": "Assess overall purity quality.\n\nArgs:\n    alpha: Global purity index\n    variance: Alpha variance across layers\n    \nReturns:\n    Quality assessment string", "kind": "method", "line": 191, "name": "_assess_purity_quality", "signature": "def _assess_purity_quality(self, alpha, variance)"}, {"doc": "Compute overall crystallization quality score.\n\nArgs:\n    alpha: Global purity index\n    variance: Alpha variance\n    \nReturns:\n    Crystallization score [0, 1]", "kind": "method", "line": 215, "name": "_compute_crystallization_score", "signature": "def _compute_crystallization_score(self, alpha, variance)"}, {"doc": "Initialize calculator.\n\nArgs:\n    config: Purity analysis configuration", "kind": "method", "line": 242, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Calculate thermodynamic metrics from loss history.\n\nArgs:\n    loss_history: List of loss values over training\n    \nReturns:\n    Dictionary containing temperature metrics", "kind": "method", "line": 251, "name": "calculate", "signature": "def calculate(self, loss_history)"}, {"doc": "Initialize classifier.\n\nArgs:\n    config: Purity analysis configuration", "kind": "method", "line": 321, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Classify current phase state.\n\nArgs:\n    alpha: Purity index\n    temperature: Effective temperature\n    \nReturns:\n    Phase classification string", "kind": "method", "line": 330, "name": "classify", "signature": "def classify(self, alpha, temperature)"}, {"doc": "Classify polycrystal state after perturbation.\n\nArgs:\n    original_alpha: Original purity index\n    original_temp: Original temperature\n    poly_alpha: Polycrystal purity index\n    poly_temp: Polycrystal temperature\n    \nReturns:\n    Polycrystal state classification", "kind": "method", "line": 359, "name": "classify_polycrystal_state", "signature": "def classify_polycrystal_state(self, original_alpha, original_temp, poly_alpha, poly_temp)"}, {"doc": "Initialize analyzer.\n\nArgs:\n    config: Purity analysis configuration", "kind": "method", "line": 400, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Analyze model after weight pruning.\n\nArgs:\n    model: Neural network model\n    pruning_level: Fraction of weights to prune [0, 1]\n    loss_history: Training loss history\n    \nReturns:\n    Dictionary containing polycrystal analysis", "kind": "method", "line": 412, "name": "analyze_polycrystal", "signature": "def analyze_polycrystal(self, model, pruning_level, loss_history)"}, {"doc": "Prune smallest magnitude weights.\n\nArgs:\n    model: Neural network model\n    sparsity: Fraction of weights to zero out", "kind": "method", "line": 461, "name": "_prune_model", "signature": "def _prune_model(self, model, sparsity)"}, {"doc": "Assess how well structure survives pruning.\n\nArgs:\n    alpha: Purity index after pruning\n    pruning_level: Fraction of weights pruned\n    \nReturns:\n    Structural integrity score [0, 1]", "kind": "method", "line": 480, "name": "_assess_structural_integrity", "signature": "def _assess_structural_integrity(self, alpha, pruning_level)"}, {"doc": "Initialize comparator.\n\nArgs:\n    config: Purity analysis configuration", "kind": "method", "line": 508, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compare original and polycrystal states.\n\nArgs:\n    original: Original state metrics\n    polycrystal: Polycrystal state metrics\n    \nReturns:\n    Dictionary containing comparison metrics", "kind": "method", "line": 518, "name": "compare", "signature": "def compare(self, original, polycrystal)"}, {"doc": "Initialize loader.\n\nArgs:\n    config: Experiment configuration", "kind": "method", "line": 583, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load checkpoint and extract model.\n\nArgs:\n    checkpoint_path: Path to checkpoint file\n    \nReturns:\n    Tuple of (model, sae, checkpoint_data)", "kind": "method", "line": 592, "name": "load", "signature": "def load(self, checkpoint_path)"}, {"doc": "Initialize analyzer.\n\nArgs:\n    checkpoint_path: Path to checkpoint file\n    experiment_config: Experiment configuration\n    purity_config: Purity analysis configuration", "kind": "method", "line": 650, "name": "__init__", "signature": "def __init__(self, checkpoint_path, experiment_config, purity_config)"}, {"doc": "Load checkpoint and extract components.", "kind": "method", "line": 677, "name": "_load_checkpoint", "signature": "def _load_checkpoint(self)"}, {"doc": "Perform comprehensive purity analysis.\n\nReturns:\n    Dictionary containing complete analysis results", "kind": "method", "line": 694, "name": "analyze", "signature": "def analyze(self)"}, {"doc": "Print analysis report to console.\n\nArgs:\n    results: Analysis results dictionary", "kind": "method", "line": 759, "name": "_print_report", "signature": "def _print_report(self, results)"}, {"doc": "Initialize pipeline.\n\nArgs:\n    experiment_config: Experiment configuration\n    purity_config: Purity analysis configuration", "kind": "method", "line": 825, "name": "__init__", "signature": "def __init__(self, experiment_config, purity_config)"}, {"doc": "Process single checkpoint.\n\nArgs:\n    checkpoint_path: Path to checkpoint file\n    output_dir: Directory for output files\n    \nReturns:\n    Analysis results dictionary", "kind": "method", "line": 840, "name": "process_checkpoint", "signature": "def process_checkpoint(self, checkpoint_path, output_dir)"}, {"doc": "Process all checkpoints in directory.\n\nArgs:\n    checkpoint_dir: Directory containing checkpoints\n    n_latest: Number of latest checkpoints to process\n    output_dir: Directory for output files\n    \nReturns:\n    List of analysis results", "kind": "method", "line": 874, "name": "process_directory", "signature": "def process_directory(self, checkpoint_dir, n_latest, output_dir)"}, {"doc": "Generate summary statistics across all checkpoints.\n\nArgs:\n    all_results: List of analysis results\n    output_dir: Directory for output files", "kind": "method", "line": 917, "name": "generate_summary", "signature": "def generate_summary(self, all_results, output_dir)"}, {"doc": "Generate human-readable text report.\n\nArgs:\n    summary: Summary statistics dictionary\n    output_dir: Directory for output files", "kind": "method", "line": 996, "name": "_generate_text_report", "signature": "def _generate_text_report(self, summary, output_dir)"}]}, {"id": "realtime_train.py", "kind": "module", "label": "realtime_train.py", "language": "py", "sha256": "80a652ad5598beca", "symbol_count": 72, "symbols": [{"doc": "Immutable configuration for thermodynamic grokking experiments.", "kind": "class", "line": 63, "name": "ExperimentConfig", "signature": "class ExperimentConfig"}, {"doc": "Interface for metric calculation strategies.", "kind": "class", "line": 130, "name": "IMetricCalculator", "signature": "class IMetricCalculator(ABC)"}, {"doc": "Interface for neural network architectures.", "kind": "class", "line": 139, "name": "IModelArchitecture", "signature": "class IModelArchitecture(ABC)"}, {"doc": "Interface for checkpoint management.", "kind": "class", "line": 158, "name": "ICheckpointManager", "signature": "class ICheckpointManager(ABC)"}, {"doc": "Two-layer MLP for parity learning experiments.", "kind": "class", "line": 177, "name": "GrokkingTransformer", "signature": "class GrokkingTransformer(Module, IModelArchitecture)"}, {"doc": "Sparse autoencoder for superposition analysis.", "kind": "class", "line": 211, "name": "SuperpositionSAE", "signature": "class SuperpositionSAE(Module)"}, {"doc": "Generate parity learning datasets.", "kind": "class", "line": 245, "name": "ParityDatasetGenerator", "signature": "class ParityDatasetGenerator"}, {"doc": "Calculate local complexity as effective local dimensionality.", "kind": "class", "line": 259, "name": "LocalComplexityCalculator", "signature": "class LocalComplexityCalculator(IMetricCalculator)"}, {"doc": "Calculate gradient covariance matrix and kappa.", "kind": "class", "line": 288, "name": "GradientCovarianceCalculator", "signature": "class GradientCovarianceCalculator"}, {"doc": "Calculate thermodynamic metrics: T_eff and h_bar_eff.", "kind": "class", "line": 349, "name": "ThermodynamicMetricsCalculator", "signature": "class ThermodynamicMetricsCalculator(IMetricCalculator)"}, {"doc": "Calculate discretization margin delta.", "kind": "class", "line": 412, "name": "DeltaCalculator", "signature": "class DeltaCalculator(IMetricCalculator)"}, {"doc": "Aggregate all thermodynamic and learning metrics.", "kind": "class", "line": 424, "name": "ComprehensiveMetricsAggregator", "signature": "class ComprehensiveMetricsAggregator"}, {"doc": "Manage experiment checkpoints.", "kind": "class", "line": 497, "name": "CheckpointManager", "signature": "class CheckpointManager(ICheckpointManager)"}, {"doc": "Detect training stagnation and trigger resets.", "kind": "class", "line": 543, "name": "StagnationDetector", "signature": "class StagnationDetector"}, {"doc": "Transfer weights intelligently between curriculum stages.", "kind": "class", "line": 579, "name": "SmartWeightTransfer", "signature": "class SmartWeightTransfer"}, {"doc": "Calculate adaptive training parameters based on problem complexity.", "kind": "class", "line": 630, "name": "AdaptiveParameterCalculator", "signature": "class AdaptiveParameterCalculator"}, {"doc": "Train a single curriculum stage with full metric tracking.", "kind": "class", "line": 665, "name": "CurriculumStageTrainer", "signature": "class CurriculumStageTrainer"}, {"doc": "Analyze experimental results and generate comprehensive statistics.", "kind": "class", "line": 898, "name": "ResultsAnalyzer", "signature": "class ResultsAnalyzer"}, {"doc": "Generate comprehensive visualizations of experimental results.", "kind": "class", "line": 1157, "name": "ResultsVisualizer", "signature": "class ResultsVisualizer"}, {"doc": "Run curriculum training across multiple random seeds.", "kind": "class", "line": 1367, "name": "MultiSeedCurriculumRunner", "signature": "class MultiSeedCurriculumRunner"}, {"doc": "Main entry point.", "kind": "method", "line": 1527, "name": "main", "signature": "def main()"}, {"doc": "Calculate metrics and return dictionary of results.", "kind": "method", "line": 134, "name": "calculate", "signature": "def calculate(self)"}, {"doc": "Forward pass returning logits and latent representation.", "kind": "method", "line": 143, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Get pre-activation tensors for complexity analysis.", "kind": "method", "line": 148, "name": "get_pre_activations", "signature": "def get_pre_activations(self, x)"}, {"doc": "Get flattened parameter vector.", "kind": "method", "line": 153, "name": "get_flat_parameters", "signature": "def get_flat_parameters(self)"}, {"doc": "Save checkpoint and return path.", "kind": "method", "line": 162, "name": "save", "signature": "def save(self, state, path)"}, {"doc": "Load checkpoint from path.", "kind": "method", "line": 167, "name": "load", "signature": "def load(self, path)"}, {"doc": "Determine if checkpoint should be saved.", "kind": "method", "line": 172, "name": "should_checkpoint", "signature": "def should_checkpoint(self)"}, {"kind": "method", "line": 180, "name": "__init__", "signature": "def __init__(self, input_dim, hidden_dim, output_dim)"}, {"doc": "Get pre-activation tensors for LC calculation.", "kind": "method", "line": 190, "name": "get_pre_activations", "signature": "def get_pre_activations(self, x)"}, {"doc": "Forward pass returning logits and latent representation.", "kind": "method", "line": 197, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Get flattened parameter vector.", "kind": "method", "line": 206, "name": "get_flat_parameters", "signature": "def get_flat_parameters(self)"}, {"kind": "method", "line": 214, "name": "__init__", "signature": "def __init__(self, model_dim, sae_dim)"}, {"doc": "Encode and decode with ReLU activation.", "kind": "method", "line": 224, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Calculate psi (superposition coefficient) and effective features.", "kind": "method", "line": 230, "name": "compute_superposition_metrics", "signature": "def compute_superposition_metrics(self, z_encoded)"}, {"kind": "method", "line": 248, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate random binary vectors with k-bit parity labels.", "kind": "method", "line": 251, "name": "generate", "signature": "def generate(self, n_bits, k_bits, dataset_size)"}, {"kind": "method", "line": 262, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Measure LC as count of near-zero pre-activations.", "kind": "method", "line": 266, "name": "calculate", "signature": "def calculate(self, model, x_batch)"}, {"kind": "method", "line": 291, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Store current gradient vector.", "kind": "method", "line": 297, "name": "accumulate_gradient", "signature": "def accumulate_gradient(self, model)"}, {"doc": "Calculate condition number of gradient covariance matrix.", "kind": "method", "line": 311, "name": "calculate_kappa", "signature": "def calculate_kappa(self)"}, {"doc": "Clear gradient buffer.", "kind": "method", "line": 344, "name": "reset", "signature": "def reset(self)"}, {"kind": "method", "line": 352, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Calculate effective temperature and Planck constant.", "kind": "method", "line": 355, "name": "calculate", "signature": "def calculate(self, gradient_covariance)"}, {"doc": "Calculate mean squared distance to nearest integer.", "kind": "method", "line": 415, "name": "calculate", "signature": "def calculate(self, model)"}, {"kind": "method", "line": 427, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute comprehensive metric suite.", "kind": "method", "line": 434, "name": "compute_all_metrics", "signature": "def compute_all_metrics(self, model, sae, train_loader, train_labels, test_loader, test_labels, current_loss, z_sae, step)"}, {"doc": "Accumulate gradient for kappa calculation.", "kind": "method", "line": 488, "name": "accumulate_gradient", "signature": "def accumulate_gradient(self, model)"}, {"doc": "Reset all stateful calculators.", "kind": "method", "line": 492, "name": "reset", "signature": "def reset(self)"}, {"kind": "method", "line": 500, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Save checkpoint to disk.", "kind": "method", "line": 506, "name": "save", "signature": "def save(self, state, path)"}, {"doc": "Load checkpoint from disk.", "kind": "method", "line": 524, "name": "load", "signature": "def load(self, path)"}, {"doc": "Check if checkpoint interval has elapsed.", "kind": "method", "line": 532, "name": "should_checkpoint", "signature": "def should_checkpoint(self)"}, {"doc": "Get path to latest checkpoint if exists.", "kind": "method", "line": 537, "name": "get_latest_checkpoint_path", "signature": "def get_latest_checkpoint_path(self)"}, {"kind": "method", "line": 546, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Determine if training is stagnant.", "kind": "method", "line": 550, "name": "is_stagnant", "signature": "def is_stagnant(self, metrics_history, current_step, hidden_dim)"}, {"doc": "Transfer weights with padding/cropping as needed.", "kind": "method", "line": 582, "name": "transfer", "signature": "def transfer(self, previous_model, new_model, stage)"}, {"kind": "method", "line": 633, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Calculate training parameters for current stage.", "kind": "method", "line": 636, "name": "calculate", "signature": "def calculate(self, n_bits, hidden_dim, stage)"}, {"kind": "method", "line": 668, "name": "__init__", "signature": "def __init__(self, config, seed)"}, {"doc": "Train a single curriculum stage.", "kind": "method", "line": 680, "name": "train_stage", "signature": "def train_stage(self, stage, n_bits, hidden_dim, previous_model, previous_sae)"}, {"kind": "method", "line": 901, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Generate comprehensive analysis of all seed results.", "kind": "method", "line": 905, "name": "analyze_seed_results", "signature": "def analyze_seed_results(self, all_results)"}, {"doc": "Print comprehensive analysis report to console.", "kind": "method", "line": 1067, "name": "print_analysis_report", "signature": "def print_analysis_report(self, analysis)"}, {"kind": "method", "line": 1160, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Create training dynamics visualization for a single seed.", "kind": "method", "line": 1166, "name": "create_seed_training_dynamics", "signature": "def create_seed_training_dynamics(self, seed_result)"}, {"doc": "Create aggregate visualizations across all seeds.", "kind": "method", "line": 1269, "name": "create_aggregate_visualizations", "signature": "def create_aggregate_visualizations(self, all_results)"}, {"kind": "method", "line": 1370, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Handle interrupt signal.", "kind": "method", "line": 1381, "name": "_signal_handler", "signature": "def _signal_handler(self, signum, frame)"}, {"doc": "Set random seed for reproducibility.", "kind": "method", "line": 1386, "name": "_set_seed", "signature": "def _set_seed(self, seed)"}, {"doc": "Run multi-seed curriculum experiment.", "kind": "method", "line": 1394, "name": "run_experiment", "signature": "def run_experiment(self)"}]}, {"doc": "-*- coding: utf-8 -*-", "id": "test.py", "kind": "module", "label": "test.py", "language": "py", "sha256": "179f964a6173ff0a", "symbol_count": 3, "symbols": [{"kind": "function", "line": 31, "name": "accuracy", "signature": "def accuracy(model, x, y)"}, {"kind": "function", "line": 36, "name": "load_base", "signature": "def load_base()"}, {"kind": "function", "line": 43, "name": "zero_shot_test", "signature": "def zero_shot_test(prev_model, n_bits, d_h, use_transfer)"}]}, {"doc": "-*- coding: utf-8 -*-", "id": "test_wandb_ablation.py", "kind": "module", "label": "test_wandb_ablation.py", "language": "py", "sha256": "b33ac1b020fce2f2", "symbol_count": 6, "symbols": [{"doc": "Initialize wandb for ablation experiment", "kind": "function", "line": 24, "name": "init_ablation_wandb", "signature": "def init_ablation_wandb(project_name)"}, {"doc": "Log results for each scale to wandb", "kind": "function", "line": 37, "name": "log_scale_results", "signature": "def log_scale_results(n_bits, d_h, train_acc_transfer, test_acc_transfer, train_acc_control, test_acc_control, time_elapsed, generalization_success)"}, {"doc": "Finish wandb run", "kind": "function", "line": 54, "name": "finish_ablation_wandb", "signature": "def finish_ablation_wandb()"}, {"kind": "function", "line": 59, "name": "accuracy", "signature": "def accuracy(model, x, y)"}, {"kind": "function", "line": 63, "name": "load_base", "signature": "def load_base()"}, {"kind": "function", "line": 69, "name": "zero_shot_test", "signature": "def zero_shot_test(prev_model, n_bits, d_h, use_transfer)"}]}, {"doc": "-*- coding: utf-8 -*-", "id": "view_streamlit.py", "kind": "module", "label": "view_streamlit.py", "language": "py", "sha256": "59cbb8f53468556d", "symbol_count": 13, "symbols": [{"doc": "Complete thermodynamic analysis of phase transitions", "kind": "class", "line": 82, "name": "ThermodynamicAnalyzer", "signature": "class ThermodynamicAnalyzer"}, {"doc": "Complete 3D visualization with clustering and geometry", "kind": "method", "line": 256, "name": "visualize_3d_geometry", "signature": "def visualize_3d_geometry(weights_list, phase_name, thermo_metrics)"}, {"doc": "Complete 2D texture: heatmap, distribution, FFT, histogram", "kind": "method", "line": 346, "name": "visualize_2d_texture", "signature": "def visualize_2d_texture(weights_list, phase_name, thermo_metrics)"}, {"doc": "Wraps app.py training with complete real-time visualization", "kind": "class", "line": 426, "name": "CompleteCurriculumWrapper", "signature": "class CompleteCurriculumWrapper"}, {"kind": "method", "line": 863, "name": "main", "signature": "def main()"}, {"doc": "Calculate complete thermodynamic state", "kind": "method", "line": 86, "name": "compute_metrics", "signature": "def compute_metrics(weights_list, phase, epoch)"}, {"doc": "Complete thermal engine visualization", "kind": "method", "line": 149, "name": "visualize_thermal_engine", "signature": "def visualize_thermal_engine(thermo_history)"}, {"kind": "method", "line": 429, "name": "__init__", "signature": "def __init__(self)"}, {"doc": "EXACTO app.py: Calcula parámetros adaptativos", "kind": "method", "line": 454, "name": "calculate_adaptive_params", "signature": "def calculate_adaptive_params(self, n_bits, d_h, stage)"}, {"doc": "Capture complete snapshot", "kind": "method", "line": 473, "name": "capture_snapshot", "signature": "def capture_snapshot(self, model, sae, stage, n_bits, d_h, step, metrics)"}, {"doc": "EXACTO app.py: Transferencia inteligente de pesos", "kind": "method", "line": 502, "name": "smart_weight_transfer", "signature": "def smart_weight_transfer(self, prev_model, new_model, stage)"}, {"doc": "Train stage with REAL-TIME 3D/2D visualization every 500 steps", "kind": "method", "line": 527, "name": "train_stage_complete", "signature": "def train_stage_complete(self, stage, n_bits, d_h, prev_model)"}, {"doc": "Execute complete curriculum - EXACTO app.py", "kind": "method", "line": 821, "name": "run_full_curriculum", "signature": "def run_full_curriculum(self)"}]}, {"doc": "visualizador.py SIMULACIÓN: This is a simulatión if you want see the views need exec: streamlit run view_stramlit.py", "id": "visualizador.py", "kind": "module", "label": "visualizador.py", "language": "py", "sha256": "acb2fc44d8ad0c1a", "symbol_count": 5, "symbols": [{"doc": "Carga el MODELO entrenado y el SAE", "kind": "function", "line": 24, "name": "load_full_system", "signature": "def load_full_system(n_bits, d_h, stage)"}, {"doc": "Calcula la precisión real del modelo cargado", "kind": "function", "line": 50, "name": "calculate_model_accuracy", "signature": "def calculate_model_accuracy(model, x, y)"}, {"doc": "Obtiene las activaciones latentes REALES del modelo", "kind": "function", "line": 58, "name": "get_real_activations", "signature": "def get_real_activations(model, x)"}, {"doc": "Extrae métricas del SAE sobre las activaciones reales", "kind": "function", "line": 64, "name": "extract_sae_metrics", "signature": "def extract_sae_metrics(sae, h2)"}, {"doc": "Visualización centrada en la verdad del Modelo", "kind": "function", "line": 80, "name": "plot_sae_autopsy", "signature": "def plot_sae_autopsy(data, accuracy, n_bits, d_h, sae)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (21 files)

#### `128bits.py`
**Path:** `128bits.py`
**File Doc:** *-*- coding: utf-8 -*-*

**Functions:**
- `evaluate` (line 34) `def evaluate(model, x, y)`
- `load_64bit_model` (line 39) `def load_64bit_model()`
- `run_experiment` (line 49) `def run_experiment(use_padding)`

#### `2048bits.py`
**Path:** `2048bits.py`
**File Doc:** *-*- coding: utf-8 -*-*

**Functions:**
- `evaluate` (line 44) `def evaluate(model, x, y)`
- `load_base_model` (line 49) `def load_base_model()`
- `zero_shot_test` (line 59) `def zero_shot_test(prev_model, n_bits, d_h, use_padding)`

#### `app.py`
**Path:** `app.py`
**File Doc:** *_*_ coding: utf8 _*_*

**Classes:**
- `SuperpositionSAE` (line 32) `class SuperpositionSAE(Module)`
- `ComplexityAnalyzer` (line 55) `class ComplexityAnalyzer`
- `GrokkingTransformer` (line 67) `class GrokkingTransformer(Module)`
- `AdaptiveCurriculumTrainer` (line 92) `class AdaptiveCurriculumTrainer`

**Methods:**
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
**File Doc:** *_*_ coding: utf8 _*_*

**Classes:**
- `SuperpositionSAE` (line 63) `class SuperpositionSAE(Module)`
- `ComplexityAnalyzer` (line 86) `class ComplexityAnalyzer`
- `GrokkingTransformer` (line 98) `class GrokkingTransformer(Module)`
- `AdaptiveCurriculumTrainer` (line 123) `class AdaptiveCurriculumTrainer`

**Functions:**
- `init_wandb` (line 35) `def init_wandb(project_name, config)` - *Initialize wandb tracking*
- `log_training_step` (line 43) `def log_training_step(step, train_acc, test_acc, psi, lc, loss_cls, loss_sae)` - *Log metrics to wandb*
- `finish_wandb` (line 59) `def finish_wandb()` - *Finish wandb run*

**Methods:**
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

**Methods:**
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

**Methods:**
- `get_adaptive_train_size` (line 111) `def get_adaptive_train_size(self, n_bits)` - *Calculate adaptive training size based on input dimensionality.*
- `get_adaptive_weight_decay` (line 117) `def get_adaptive_weight_decay(self, n_bits, hidden_dim)` - *Calculate adaptive weight decay based on problem complexity.*
- `get_adaptive_max_steps` (line 126) `def get_adaptive_max_steps(self, n_bits, hidden_dim)` - *Calculate adaptive maximum steps based on problem complexity.*

#### `data_generation.py`
**Path:** `new_experiment/data_generation.py`

**Classes:**
- `ParityDatasetGenerator` (line 11) `class ParityDatasetGenerator` - *Generates binary parity learning datasets.

The parity function computes whether the sum of the first k bits
of an n-bit input vector is odd (1) or even (0).*

**Methods:**
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

**Methods:**
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

**Methods:**
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
- `GrokkingTransformer` (line 33) `class GrokkingTransformer(Module, IModelArchitecture)` - *Two-layer MLP for parity learning experiments.

Architecture:
    input -> fc1 -> ReLU -> fc2 -> ReLU -> output*
- `SuperpositionSAE` (line 101) `class SuperpositionSAE(Module)` - *Sparse Autoencoder for superposition analysis.

Used to measure effective feature dimensionality and
superposition coefficient in learned representations.*

**Methods:**
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

**Methods:**
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

**Methods:**
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

**Methods:**
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

**Methods:**
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

**Methods:**
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
- `GrokkingTransformer` (line 177) `class GrokkingTransformer(Module, IModelArchitecture)` - *Two-layer MLP for parity learning experiments.*
- `SuperpositionSAE` (line 211) `class SuperpositionSAE(Module)` - *Sparse autoencoder for superposition analysis.*
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

**Methods:**
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
**File Doc:** *-*- coding: utf-8 -*-*

**Functions:**
- `accuracy` (line 31) `def accuracy(model, x, y)`
- `load_base` (line 36) `def load_base()`
- `zero_shot_test` (line 43) `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)`

#### `test_wandb_ablation.py`
**Path:** `test_wandb_ablation.py`
**File Doc:** *-*- coding: utf-8 -*-*

**Functions:**
- `init_ablation_wandb` (line 24) `def init_ablation_wandb(project_name)` - *Initialize wandb for ablation experiment*
- `log_scale_results` (line 37) `def log_scale_results(n_bits, d_h, train_acc_transfer, test_acc_transfer, train_acc_control, test_acc_control, time_elapsed, generalization_success)` - *Log results for each scale to wandb*
- `finish_ablation_wandb` (line 54) `def finish_ablation_wandb()` - *Finish wandb run*
- `accuracy` (line 59) `def accuracy(model, x, y)`
- `load_base` (line 63) `def load_base()`
- `zero_shot_test` (line 69) `def zero_shot_test(prev_model, n_bits, d_h, use_transfer)`

#### `view_streamlit.py`
**Path:** `view_streamlit.py`
**File Doc:** *-*- coding: utf-8 -*-*

**Classes:**
- `ThermodynamicAnalyzer` (line 82) `class ThermodynamicAnalyzer` - *Complete thermodynamic analysis of phase transitions*
- `CompleteCurriculumWrapper` (line 426) `class CompleteCurriculumWrapper` - *Wraps app.py training with complete real-time visualization*

**Methods:**
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
**File Doc:** *visualizador.py SIMULACIÓN: This is a simulatión if you want see the views need exec: streamlit run view_stramlit.py*

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
