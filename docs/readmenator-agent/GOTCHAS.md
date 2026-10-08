# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `new_experiment/config.py` (score: 20.40, imported by 10 files)
- `new_experiment/training.py` (score: 16.40, imported by 1 files)
- `app.py` (score: 13.80, imported by 6 files)
- `new_experiment/streamlit_app.py` (score: 13.00)
- `new_experiment/metrics.py` (score: 12.00, imported by 3 files)
- `new_experiment/models.py` (score: 11.30, imported by 5 files)
- `purity_analysis.py` (score: 9.00)
- `new_experiment/training_dynamics.py` (score: 8.50, imported by 3 files)
- `new_experiment/data_generation.py` (score: 8.30, imported by 3 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `new_experiment/config.py` -- 10 direct, 10 total dependents
- `app.py` -- 6 direct, 6 total dependents
- `new_experiment/models.py` -- 5 direct, 6 total dependents
- `new_experiment/data_generation.py` -- 3 direct, 4 total dependents
- `new_experiment/metrics.py` -- 3 direct, 4 total dependents
- `new_experiment/training_dynamics.py` -- 3 direct, 4 total dependents
- `new_experiment/checkpointing.py` -- 2 direct, 3 total dependents
- `new_experiment/wandb_integration.py` -- 2 direct, 3 total dependents
- `new_experiment/training.py` -- 1 direct, 1 total dependents

## Hotspots (complexity + centrality)

- `realtime_train.py` -- complexity: 1.0, centrality: 0.8, combined: 0.9
- `purity_analysis.py` -- complexity: 0.7, centrality: 0.7, combined: 0.7
- `new_experiment/streamlit_app.py` -- complexity: 0.1, centrality: 1.0, combined: 0.7
- `new_experiment/training.py` -- complexity: 0.1, centrality: 0.8, combined: 0.5
- `view_streamlit.py` -- complexity: 0.2, centrality: 0.7, combined: 0.5
- `new_experiment/metrics.py` -- complexity: 0.3, centrality: 0.5, combined: 0.4
- `app.py` -- complexity: 0.2, centrality: 0.5, combined: 0.4
- `new_experiment/config.py` -- complexity: 0.1, centrality: 0.6, combined: 0.4
- `new_experiment/models.py` -- complexity: 0.2, centrality: 0.4, combined: 0.3
- `app_wandb.py` -- complexity: 0.3, centrality: 0.3, combined: 0.3
