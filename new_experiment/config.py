#!/usr/bin/env python3
"""
Configuration module for thermodynamic grokking experiments.
All hyperparameters are centralized and adjustable.
"""

from dataclasses import dataclass, field
from typing import Tuple, List
import torch


@dataclass
class ExperimentConfig:
    """
    Centralized configuration for all experimental parameters.
    All magic numbers are eliminated and made explicit.
    """
    
    # Seed configuration
    seed: int = 42
    
    # Parity task configuration
    parity_k_bits: int = 3
    curriculum_stages: Tuple[Tuple[int, int], ...] = (
        (10, 128),
        (24, 256),
        (32, 512),
        (64, 1024)
    )
    
    # Sparse Autoencoder configuration
    sae_expansion_factor: int = 4
    sae_l1_coefficient: float = 0.01
    
    # Training configuration
    base_train_size: int = 300
    base_weight_decay: float = 1.0
    base_learning_rate: float = 1e-3
    base_max_steps: int = 600000
    
    # Adaptive parameter bounds
    max_train_size_limit: int = 2000
    min_weight_decay_limit: float = 0.01
    max_steps_limit: int = 2000000
    
    # Optimization configuration
    optimizer_restart_lr_decay: float = 0.5
    
    # Convergence thresholds
    grokking_threshold: float = 0.98
    partial_success_threshold: float = 0.70
    
    # Stagnation detection
    min_test_accuracy_improvement: float = 0.01
    max_steps_without_improvement: int = 50000
    lc_stagnation_threshold_factor: float = 0.95
    stagnation_history_window: int = 10
    
    # Complexity analysis
    local_complexity_epsilon: float = 0.01
    
    # Gradient covariance tracking
    gradient_window_size: int = 100
    kappa_min_samples: int = 50
    spectral_regularization: float = 1e-6
    eigenvalue_filter_threshold: float = 1e-10
    
    # Thermodynamic constants
    planck_constant_regularization: float = 1e-6
    boltzmann_constant: float = 1.0
    
    # Dataset configuration
    test_set_size: int = 2000
    curriculum_test_size: int = 10000
    class_count: int = 2
    
    # Logging configuration
    metrics_log_interval: int = 500
    checkpoint_interval_seconds: float = 300.0
    
    # Visualization configuration
    visualization_update_interval: int = 2000
    streamlit_refresh_rate: float = 1.0
    
    # Checkpoint configuration
    checkpoint_dir: str = "checkpoints"
    results_dir: str = "results"
    latest_checkpoint_name: str = "latest_checkpoint.pt"
    
    # WandB configuration
    wandb_project: str = "thermodynamic_grokking"
    wandb_entity: str = None
    use_wandb: bool = True
    
    # Device configuration
    device: str = field(default_factory=lambda: "cuda" if torch.cuda.is_available() else "cpu")
    
    # 3D visualization PCA configuration
    pca_components: int = 3
    pca_max_samples: int = 128
    
    # 2D texture visualization
    texture_max_size: int = 128
    texture_sample_reduction: int = 2000
    histogram_bins: int = 50
    
    # Clustering configuration
    dbscan_percentile_threshold: int = 20
    dbscan_min_samples: int = 3
    
    def get_adaptive_train_size(self, n_bits: int) -> int:
        """Calculate adaptive training size based on input dimensionality."""
        import math
        train_size = int(self.base_train_size * math.log2(n_bits + 1))
        return min(train_size, self.max_train_size_limit)
    
    def get_adaptive_weight_decay(self, n_bits: int, hidden_dim: int) -> float:
        """Calculate adaptive weight decay based on problem complexity."""
        import math
        base_n_bits = self.curriculum_stages[0][0]
        base_hidden_dim = self.curriculum_stages[0][1]
        complexity_factor = (n_bits * hidden_dim) / (base_n_bits * base_hidden_dim)
        weight_decay = self.base_weight_decay / (complexity_factor ** 0.5)
        return max(weight_decay, self.min_weight_decay_limit)
    
    def get_adaptive_max_steps(self, n_bits: int, hidden_dim: int) -> int:
        """Calculate adaptive maximum steps based on problem complexity."""
        import math
        base_n_bits = self.curriculum_stages[0][0]
        base_hidden_dim = self.curriculum_stages[0][1]
        complexity_factor = (n_bits * hidden_dim) / (base_n_bits * base_hidden_dim)
        max_steps = int(self.base_max_steps * math.log2(complexity_factor + 1))
        return min(max_steps, self.max_steps_limit)
