# Architecture

## Internal Dependencies

- `128bits.py` -> `app.py`
- `2048bits.py` -> `app.py`
- `new_experiment/checkpointing.py` -> `new_experiment/config.py`
- `new_experiment/data_generation.py` -> `new_experiment/config.py`
- `new_experiment/main.py` -> `new_experiment/config.py`
- `new_experiment/main.py` -> `new_experiment/training.py`
- `new_experiment/metrics.py` -> `new_experiment/config.py`
- `new_experiment/metrics.py` -> `new_experiment/models.py`
- `new_experiment/streamlit_app.py` -> `new_experiment/config.py`
- `new_experiment/streamlit_app.py` -> `new_experiment/data_generation.py`
- `new_experiment/streamlit_app.py` -> `new_experiment/metrics.py`
- `new_experiment/streamlit_app.py` -> `new_experiment/models.py`
- `new_experiment/streamlit_app.py` -> `new_experiment/training_dynamics.py`
- `new_experiment/streamlit_app.py` -> `new_experiment/wandb_integration.py`
- `new_experiment/test_framework.py` -> `new_experiment/checkpointing.py`
- `new_experiment/test_framework.py` -> `new_experiment/config.py`
- `new_experiment/test_framework.py` -> `new_experiment/data_generation.py`
- `new_experiment/test_framework.py` -> `new_experiment/metrics.py`
- `new_experiment/test_framework.py` -> `new_experiment/models.py`
- `new_experiment/test_framework.py` -> `new_experiment/training_dynamics.py`
- `new_experiment/training.py` -> `new_experiment/checkpointing.py`
- `new_experiment/training.py` -> `new_experiment/config.py`
- `new_experiment/training.py` -> `new_experiment/data_generation.py`
- `new_experiment/training.py` -> `new_experiment/metrics.py`
- `new_experiment/training.py` -> `new_experiment/models.py`
- `new_experiment/training.py` -> `new_experiment/training_dynamics.py`
- `new_experiment/training.py` -> `new_experiment/wandb_integration.py`
- `new_experiment/training_dynamics.py` -> `new_experiment/config.py`
- `new_experiment/wandb_integration.py` -> `new_experiment/config.py`
- `purity_analysis.py` -> `new_experiment/config.py`
- `purity_analysis.py` -> `new_experiment/models.py`
- `test.py` -> `app.py`
- `test_wandb_ablation.py` -> `app.py`
- `view_streamlit.py` -> `app.py`
- `visualizador.py` -> `app.py`

## External Imports

- `128bits.py` -> copy, time, torch
- `2048bits.py` -> time, torch
- `app.py` -> copy, math, numpy, os, torch, torch.nn, torch.nn.functional
- `app_wandb.py` -> copy, math, numpy, os, torch, torch.nn, torch.nn.functional, wandb
- `new_experiment/checkpointing.py` -> abc, datetime, pathlib, time, torch, typing
- `new_experiment/config.py` -> dataclasses, math, torch, typing
- `new_experiment/data_generation.py` -> torch, typing
- `new_experiment/main.py` -> argparse, numpy, pathlib, torch
- `new_experiment/metrics.py` -> abc, collections, numpy, torch, torch.nn, typing
- `new_experiment/models.py` -> abc, math, torch, torch.nn, torch.nn.functional, typing
- `new_experiment/streamlit_app.py` -> copy, numpy, pathlib, plotly.graph_objects, plotly.subplots, scipy, scipy.spatial.distance, sklearn.cluster, sklearn.decomposition, streamlit, time, torch, torch.nn.functional, typing
- `new_experiment/test_framework.py` -> numpy, torch
- `new_experiment/training.py` -> copy, datetime, torch, torch.nn.functional, torch.optim, typing
- `new_experiment/training_dynamics.py` -> torch, torch.nn, typing
- `new_experiment/wandb_integration.py` -> typing, wandb
- `purity_analysis.py` -> argparse, dataclasses, datetime, glob, json, numpy, os, pathlib, scipy.stats, torch, torch.nn, traceback, typing
- `realtime_train.py` -> abc, argparse, collections, copy, dataclasses, datetime, json, math, matplotlib, matplotlib.gridspec, matplotlib.pyplot, numpy, pathlib, signal, sys, time, torch, torch.nn, torch.nn.functional, torch.optim, typing, warnings
- `test.py` -> time, torch
- `test_wandb_ablation.py` -> time, torch, wandb
- `view_streamlit.py` -> copy, datetime, math, numpy, os, plotly.graph_objects, plotly.subplots, scipy, scipy.spatial.distance, sklearn.cluster, sklearn.decomposition, streamlit, sys, torch, torch.nn, torch.nn.functional
- `visualizador.py` -> matplotlib.pyplot, mpl_toolkits.mplot3d, numpy, os, sklearn.decomposition, sklearn.manifold, torch, traceback, warnings
