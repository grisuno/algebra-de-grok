#!/usr/bin/env python3
"""
Thermodynamic Grokking Curriculum Framework
===========================================

A comprehensive framework for studying phase transitions in neural network learning
through curriculum-based training with full thermodynamic metric tracking.

This framework trains models across multiple random seeds, tracking:
- Gradient covariance condition number (kappa)
- Discretization margin (delta)
- Effective temperature (T_eff)
- Effective Planck constant (h_bar_eff)
- Local complexity (LC)
- Superposition coefficient (psi)
- Train/validation accuracy
- Loss metrics

Key features:
- Curriculum learning with adaptive complexity
- Smart weight transfer between stages
- Comprehensive thermodynamic analysis
- Automatic checkpoint management
- Phase transition detection
- Multi-seed experimental design

Repository: https://github.com/grisuno/thermodynamic-grokking
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import math
import json
import time
import signal
import sys
from pathlib import Path
from dataclasses import dataclass, replace
from typing import Dict, List, Tuple, Optional, Any, Deque
from collections import deque
from datetime import datetime
from copy import deepcopy
from abc import ABC, abstractmethod
import warnings

warnings.filterwarnings('ignore')

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Warning: matplotlib not available. Visualizations will be skipped.")


@dataclass(frozen=True)
class ExperimentConfig:
    """Immutable configuration for thermodynamic grokking experiments."""
    
    seed_range_start: int = 1
    seed_range_end: int = 100
    
    parity_k_bits: int = 3
    base_n_bits: int = 10
    base_hidden_dim: int = 128
    
    sae_expansion_factor: int = 4
    
    base_train_size: int = 300
    base_weight_decay: float = 1.0
    base_learning_rate: float = 1e-3
    base_max_steps: int = 600000
    
    curriculum_stages: Tuple[Tuple[int, int], ...] = (
        (10, 128),
        (24, 256),
        (32, 512),
        (64, 1024)
    )
    
    min_test_accuracy_improvement: float = 0.01
    max_steps_without_improvement: int = 50000
    lc_stagnation_threshold_factor: float = 0.95
    
    grokking_threshold: float = 0.98
    partial_success_threshold: float = 0.7
    
    optimizer_restart_lr_decay: float = 0.5
    
    metrics_log_interval: int = 50
    checkpoint_interval_minutes: float = 5.0
    
    visualization_dpi: int = 150
    figure_width: float = 16.0
    figure_height: float = 12.0
    
    local_complexity_epsilon: float = 0.01
    superposition_sparsity_l1_weight: float = 0.01
    
    gradient_window_size: int = 100
    kappa_min_samples: int = 50
    spectral_regularization: float = 1e-6
    eigenvalue_filter_threshold: float = 1e-10
    
    planck_constant_regularization: float = 1e-6
    boltzmann_constant: float = 1.0
    
    test_set_size: int = 2000
    max_train_size_limit: int = 2000
    max_steps_limit: int = 2000000
    min_weight_decay_limit: float = 0.01
    
    checkpoint_dir: str = "checkpoints_grokking"
    results_dir: str = "results_grokking"
    latest_checkpoint_name: str = "latest_checkpoint.pt"
    
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    
    curriculum_test_size: int = 10000
    
    class_count: int = 2


class IMetricCalculator(ABC):
    """Interface for metric calculation strategies."""
    
    @abstractmethod
    def calculate(self, **kwargs) -> Dict[str, float]:
        """Calculate metrics and return dictionary of results."""
        pass


class IModelArchitecture(ABC):
    """Interface for neural network architectures."""
    
    @abstractmethod
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Forward pass returning logits and latent representation."""
        pass
    
    @abstractmethod
    def get_pre_activations(self, x: torch.Tensor) -> List[torch.Tensor]:
        """Get pre-activation tensors for complexity analysis."""
        pass
    
    @abstractmethod
    def get_flat_parameters(self) -> torch.Tensor:
        """Get flattened parameter vector."""
        pass


class ICheckpointManager(ABC):
    """Interface for checkpoint management."""
    
    @abstractmethod
    def save(self, state: Dict[str, Any], path: Optional[str] = None) -> str:
        """Save checkpoint and return path."""
        pass
    
    @abstractmethod
    def load(self, path: str) -> Optional[Dict[str, Any]]:
        """Load checkpoint from path."""
        pass
    
    @abstractmethod
    def should_checkpoint(self) -> bool:
        """Determine if checkpoint should be saved."""
        pass


class GrokkingTransformer(nn.Module, IModelArchitecture):
    """Two-layer MLP for parity learning experiments."""
    
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.output_layer = nn.Linear(hidden_dim, output_dim)
    
    def get_pre_activations(self, x: torch.Tensor) -> List[torch.Tensor]:
        """Get pre-activation tensors for LC calculation."""
        z1 = self.fc1(x)
        h1 = F.relu(z1)
        z2 = self.fc2(h1)
        return [z1, z2]
    
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Forward pass returning logits and latent representation."""
        z1 = self.fc1(x)
        h1 = F.relu(z1)
        z2 = self.fc2(h1)
        h2 = F.relu(z2)
        logits = self.output_layer(h2)
        return logits, h2
    
    def get_flat_parameters(self) -> torch.Tensor:
        """Get flattened parameter vector."""
        return torch.cat([p.flatten() for p in self.parameters()])


class SuperpositionSAE(nn.Module):
    """Sparse autoencoder for superposition analysis."""
    
    def __init__(self, model_dim: int, sae_dim: int):
        super().__init__()
        self.model_dim = model_dim
        self.sae_dim = sae_dim
        
        self.encoder_weight = nn.Parameter(
            torch.randn(model_dim, sae_dim) / math.sqrt(model_dim)
        )
        self.encoder_bias = nn.Parameter(torch.zeros(sae_dim))
    
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Encode and decode with ReLU activation."""
        z_encoded = F.relu(x @ self.encoder_weight + self.encoder_bias)
        x_reconstructed = z_encoded @ self.encoder_weight.t()
        return x_reconstructed, z_encoded
    
    def compute_superposition_metrics(self, z_encoded: torch.Tensor) -> Tuple[float, float]:
        """Calculate psi (superposition coefficient) and effective features."""
        with torch.no_grad():
            feature_importance = z_encoded.abs().sum(dim=0)
            probability_distribution = feature_importance / (feature_importance.sum() + 1e-12)
            
            p_safe = probability_distribution[probability_distribution > 1e-10]
            shannon_entropy = -torch.sum(p_safe * torch.log(p_safe + 1e-12))
            
            effective_features = torch.exp(shannon_entropy)
            psi = effective_features / self.model_dim
            
            return psi.item(), effective_features.item()


class ParityDatasetGenerator:
    """Generate parity learning datasets."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
    
    def generate(self, n_bits: int, k_bits: int, 
                dataset_size: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """Generate random binary vectors with k-bit parity labels."""
        x = (torch.rand(dataset_size, n_bits) > 0.5).float()
        y = (x[:, :k_bits].sum(dim=1) % 2).long()
        return x, y


class LocalComplexityCalculator(IMetricCalculator):
    """Calculate local complexity as effective local dimensionality."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.epsilon = config.local_complexity_epsilon
    
    def calculate(self, model: IModelArchitecture, 
                  x_batch: torch.Tensor, **kwargs) -> Dict[str, float]:
        """Measure LC as count of near-zero pre-activations."""
        model.eval()
        with torch.no_grad():
            pre_activations = model.get_pre_activations(x_batch)
            
            total_inactive = 0.0
            layer_count = len(pre_activations)
            
            for z_layer in pre_activations:
                inactive_per_sample = (z_layer.abs() < self.epsilon).float().sum(dim=1)
                mean_inactive = inactive_per_sample.mean()
                total_inactive += mean_inactive
            
            lc_value = total_inactive / max(layer_count, 1)
            
        return {
            'local_complexity': lc_value.item() if hasattr(lc_value, 'item') else lc_value
        }


class GradientCovarianceCalculator:
    """Calculate gradient covariance matrix and kappa."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.gradient_buffer: Deque[torch.Tensor] = deque(
            maxlen=config.gradient_window_size
        )
    
    def accumulate_gradient(self, model: nn.Module) -> None:
        """Store current gradient vector."""
        if not any(p.grad is not None for p in model.parameters()):
            return
        
        grad_vector = []
        for param in model.parameters():
            if param.grad is not None:
                grad_vector.append(param.grad.detach().flatten().cpu())
            else:
                grad_vector.append(torch.zeros(param.numel()))
        
        self.gradient_buffer.append(torch.cat(grad_vector))
    
    def calculate_kappa(self) -> Tuple[Optional[float], Optional[torch.Tensor]]:
        """Calculate condition number of gradient covariance matrix."""
        if len(self.gradient_buffer) < self.config.kappa_min_samples:
            return None, None
        
        try:
            G = torch.stack(list(self.gradient_buffer))
            G_centered = G - G.mean(dim=0, keepdim=True)
            
            n_samples = G.shape[0]
            covariance_matrix = (G_centered.T @ G_centered) / (n_samples - 1)
            
            regularization = (torch.eye(covariance_matrix.shape[0]) * 
                            self.config.spectral_regularization)
            covariance_regularized = covariance_matrix + regularization
            
            eigenvalues = torch.linalg.eigvalsh(covariance_regularized)
            eigenvalues = eigenvalues[
                eigenvalues > self.config.eigenvalue_filter_threshold
            ]
            
            if len(eigenvalues) == 0:
                return float('inf'), None
            
            lambda_max = eigenvalues.max().item()
            lambda_min = eigenvalues.min().item()
            kappa = lambda_max / (lambda_min + 1e-12)
            
            return kappa, covariance_regularized
            
        except Exception:
            return None, None
    
    def reset(self) -> None:
        """Clear gradient buffer."""
        self.gradient_buffer.clear()


class ThermodynamicMetricsCalculator(IMetricCalculator):
    """Calculate thermodynamic metrics: T_eff and h_bar_eff."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
    
    def calculate(self, gradient_covariance: Optional[torch.Tensor],
                  **kwargs) -> Dict[str, float]:
        """Calculate effective temperature and Planck constant."""
        if gradient_covariance is None:
            return {
                'T_eff': 0.0,
                'h_bar_eff': 0.0,
                'thermodynamic_entropy': 0.0,
                'trace_gradient_covariance': 0.0
            }
        
        try:
            eigenvalues = torch.linalg.eigvalsh(gradient_covariance)
            eigenvalues = eigenvalues[
                eigenvalues > self.config.eigenvalue_filter_threshold
            ]
            
            if len(eigenvalues) == 0:
                return {
                    'T_eff': 0.0,
                    'h_bar_eff': 0.0,
                    'thermodynamic_entropy': 0.0,
                    'trace_gradient_covariance': 0.0
                }
            
            trace_sigma = eigenvalues.sum().item()
            dimension = len(eigenvalues)
            
            T_eff = trace_sigma / dimension if dimension > 0 else 0.0
            
            position_uncertainty = torch.sqrt(eigenvalues.mean()).item()
            h_bar_eff = (position_uncertainty * 
                        self.config.planck_constant_regularization)
            
            if T_eff > 0:
                boltzmann_entropy = -torch.sum(
                    eigenvalues * torch.log(eigenvalues + 1e-300)
                ).item() / (self.config.boltzmann_constant * T_eff)
            else:
                boltzmann_entropy = 0.0
            
            return {
                'T_eff': T_eff,
                'h_bar_eff': h_bar_eff,
                'thermodynamic_entropy': boltzmann_entropy,
                'trace_gradient_covariance': trace_sigma
            }
            
        except Exception:
            return {
                'T_eff': 0.0,
                'h_bar_eff': 0.0,
                'thermodynamic_entropy': 0.0,
                'trace_gradient_covariance': 0.0
            }


class DeltaCalculator(IMetricCalculator):
    """Calculate discretization margin delta."""
    
    def calculate(self, model: IModelArchitecture, **kwargs) -> Dict[str, float]:
        """Calculate mean squared distance to nearest integer."""
        params = model.get_flat_parameters()
        rounded = torch.round(params)
        delta = torch.mean((params - rounded) ** 2).item()
        
        return {'delta': delta}


class ComprehensiveMetricsAggregator:
    """Aggregate all thermodynamic and learning metrics."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.gradient_calculator = GradientCovarianceCalculator(config)
        self.thermodynamic_calculator = ThermodynamicMetricsCalculator(config)
        self.lc_calculator = LocalComplexityCalculator(config)
        self.delta_calculator = DeltaCalculator()
    
    def compute_all_metrics(self,
                           model: IModelArchitecture,
                           sae: SuperpositionSAE,
                           train_loader: torch.Tensor,
                           train_labels: torch.Tensor,
                           test_loader: torch.Tensor,
                           test_labels: torch.Tensor,
                           current_loss: float,
                           z_sae: torch.Tensor,
                           step: int) -> Dict[str, float]:
        """Compute comprehensive metric suite."""
        metrics = {
            'step': float(step),
            'loss': current_loss
        }
        
        model.eval()
        with torch.no_grad():
            train_logits, _ = model(train_loader)
            test_logits, _ = model(test_loader)
            
            train_accuracy = (
                (train_logits.argmax(1) == train_labels).float().mean().item()
            )
            test_accuracy = (
                (test_logits.argmax(1) == test_labels).float().mean().item()
            )
            
            metrics['train_accuracy'] = train_accuracy
            metrics['test_accuracy'] = test_accuracy
        
        kappa, grad_covariance = self.gradient_calculator.calculate_kappa()
        if kappa is not None:
            metrics['kappa'] = kappa
        else:
            metrics['kappa'] = float('inf')
        
        thermo_metrics = self.thermodynamic_calculator.calculate(
            gradient_covariance=grad_covariance
        )
        metrics.update(thermo_metrics)
        
        lc_metrics = self.lc_calculator.calculate(model, train_loader)
        metrics.update(lc_metrics)
        
        delta_metrics = self.delta_calculator.calculate(model)
        metrics.update(delta_metrics)
        
        psi, effective_features = sae.compute_superposition_metrics(z_sae)
        metrics['psi'] = psi
        metrics['effective_features'] = effective_features
        
        return metrics
    
    def accumulate_gradient(self, model: nn.Module) -> None:
        """Accumulate gradient for kappa calculation."""
        self.gradient_calculator.accumulate_gradient(model)
    
    def reset(self) -> None:
        """Reset all stateful calculators."""
        self.gradient_calculator.reset()


class CheckpointManager(ICheckpointManager):
    """Manage experiment checkpoints."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.checkpoint_dir = Path(config.checkpoint_dir)
        self.checkpoint_dir.mkdir(exist_ok=True, parents=True)
        self.last_checkpoint_time = time.time()
    
    def save(self, state: Dict[str, Any], 
            path: Optional[str] = None) -> str:
        """Save checkpoint to disk."""
        if path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = str(self.checkpoint_dir / f"checkpoint_{timestamp}.pt")
        
        path_obj = Path(path)
        path_obj.parent.mkdir(parents=True, exist_ok=True)
        
        torch.save(state, path)
        
        latest_path = self.checkpoint_dir / self.config.latest_checkpoint_name
        torch.save(state, latest_path)
        
        self.last_checkpoint_time = time.time()
        return str(path)
    
    def load(self, path: str) -> Optional[Dict[str, Any]]:
        """Load checkpoint from disk."""
        try:
            return torch.load(path, map_location=self.config.device)
        except Exception as e:
            print(f"Failed to load checkpoint from {path}: {e}")
            return None
    
    def should_checkpoint(self) -> bool:
        """Check if checkpoint interval has elapsed."""
        elapsed_minutes = (time.time() - self.last_checkpoint_time) / 60.0
        return elapsed_minutes >= self.config.checkpoint_interval_minutes
    
    def get_latest_checkpoint_path(self) -> Optional[str]:
        """Get path to latest checkpoint if exists."""
        latest = self.checkpoint_dir / self.config.latest_checkpoint_name
        return str(latest) if latest.exists() else None


class StagnationDetector:
    """Detect training stagnation and trigger resets."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.history_window_size = 10
    
    def is_stagnant(self, metrics_history: List[Dict[str, float]],
                    current_step: int, hidden_dim: int) -> Tuple[bool, Optional[str]]:
        """Determine if training is stagnant."""
        if len(metrics_history) < self.history_window_size:
            return False, None
        
        recent_metrics = metrics_history[-self.history_window_size:]
        
        test_accuracies = [m['test_accuracy'] for m in recent_metrics]
        accuracy_improvement = test_accuracies[-1] - test_accuracies[0]
        
        if accuracy_improvement < self.config.min_test_accuracy_improvement:
            local_complexities = [m.get('local_complexity', 0) 
                                for m in recent_metrics]
            avg_lc = sum(local_complexities) / len(local_complexities)
            
            lc_threshold = (self.config.lc_stagnation_threshold_factor * 
                          hidden_dim)
            
            if avg_lc > lc_threshold:
                steps_since_first = (current_step - 
                                   recent_metrics[0]['step'])
                
                if steps_since_first > self.config.max_steps_without_improvement:
                    return True, "high_lc_stagnation"
        
        return False, None


class SmartWeightTransfer:
    """Transfer weights intelligently between curriculum stages."""
    
    def transfer(self, previous_model: Optional[nn.Module],
                new_model: nn.Module, stage: int) -> nn.Module:
        """Transfer weights with padding/cropping as needed."""
        if previous_model is None:
            return new_model
        
        prev_state = previous_model.state_dict()
        new_state = new_model.state_dict()
        
        print(f"\nWeight Transfer Stage {stage}:")
        
        for param_name, new_param in new_state.items():
            if param_name in prev_state:
                prev_param = prev_state[param_name]
                
                if prev_param.shape == new_param.shape:
                    new_state[param_name].copy_(prev_param)
                    print(f"  {param_name}: Direct copy {list(new_param.shape)}")
                
                elif 'weight' in param_name and len(prev_param.shape) == 2:
                    if (new_param.shape[0] >= prev_param.shape[0] and
                        new_param.shape[1] >= prev_param.shape[1]):
                        
                        padded = torch.zeros_like(new_param)
                        min_rows = min(prev_param.shape[0], new_param.shape[0])
                        min_cols = min(prev_param.shape[1], new_param.shape[1])
                        padded[:min_rows, :min_cols] = prev_param[:min_rows, :min_cols]
                        new_state[param_name].copy_(padded)
                        print(f"  {param_name}: Padded "
                              f"{list(prev_param.shape)} to {list(new_param.shape)}")
                    else:
                        cropped = prev_param[:new_param.shape[0], :new_param.shape[1]]
                        new_state[param_name].copy_(cropped)
                        print(f"  {param_name}: Cropped "
                              f"{list(prev_param.shape)} to {list(new_param.shape)}")
                
                elif 'bias' in param_name and len(prev_param.shape) == 1:
                    if new_param.shape[0] >= prev_param.shape[0]:
                        padded = torch.zeros_like(new_param)
                        padded[:prev_param.shape[0]] = prev_param
                        new_state[param_name].copy_(padded)
                        print(f"  {param_name}: Padded bias "
                              f"{prev_param.shape[0]} to {new_param.shape[0]}")
        
        new_model.load_state_dict(new_state)
        return new_model


class AdaptiveParameterCalculator:
    """Calculate adaptive training parameters based on problem complexity."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
    
    def calculate(self, n_bits: int, hidden_dim: int, 
                 stage: int) -> Dict[str, Any]:
        """Calculate training parameters for current stage."""
        train_size = int(
            self.config.base_train_size * math.log2(n_bits + 1)
        )
        train_size = min(train_size, self.config.max_train_size_limit)
        
        complexity_factor = (n_bits * hidden_dim) / (
            self.config.base_n_bits * self.config.base_hidden_dim
        )
        
        weight_decay = (self.config.base_weight_decay / 
                       (complexity_factor ** 0.5))
        weight_decay = max(weight_decay, self.config.min_weight_decay_limit)
        
        max_steps = int(
            self.config.base_max_steps * math.log2(complexity_factor + 1)
        )
        max_steps = min(max_steps, self.config.max_steps_limit)
        
        return {
            'train_size': train_size,
            'weight_decay': weight_decay,
            'max_steps': max_steps,
            'learning_rate': self.config.base_learning_rate
        }


class CurriculumStageTrainer:
    """Train a single curriculum stage with full metric tracking."""
    
    def __init__(self, config: ExperimentConfig, seed: int):
        self.config = config
        self.seed = seed
        self.device = config.device
        
        self.data_generator = ParityDatasetGenerator(config)
        self.metrics_aggregator = ComprehensiveMetricsAggregator(config)
        self.checkpoint_manager = CheckpointManager(config)
        self.stagnation_detector = StagnationDetector(config)
        self.weight_transfer = SmartWeightTransfer()
        self.param_calculator = AdaptiveParameterCalculator(config)
    
    def train_stage(self,
                   stage: int,
                   n_bits: int,
                   hidden_dim: int,
                   previous_model: Optional[nn.Module] = None,
                   previous_sae: Optional[nn.Module] = None) -> Tuple[
                       Optional[nn.Module],
                       Optional[nn.Module],
                       bool,
                       List[Dict[str, float]]
                   ]:
        """Train a single curriculum stage."""
        print(f"\n{'='*80}")
        print(f"SEED {self.seed} | Stage {stage + 1} | "
              f"n_bits={n_bits} | hidden_dim={hidden_dim}")
        print(f"{'='*80}")
        
        params = self.param_calculator.calculate(n_bits, hidden_dim, stage)
        
        print(f"Adaptive Parameters:")
        print(f"  Train size: {params['train_size']}")
        print(f"  Weight decay: {params['weight_decay']:.4f}")
        print(f"  Max steps: {params['max_steps']:,}")
        print(f"  Learning rate: {params['learning_rate']:.4f}")
        
        x_full, y_full = self.data_generator.generate(
            n_bits=n_bits,
            k_bits=self.config.parity_k_bits,
            dataset_size=self.config.curriculum_test_size
        )
        
        train_x = x_full[:params['train_size']].to(self.device)
        train_y = y_full[:params['train_size']].to(self.device)
        
        test_end_idx = params['train_size'] + self.config.test_set_size
        test_x = x_full[params['train_size']:test_end_idx].to(self.device)
        test_y = y_full[params['train_size']:test_end_idx].to(self.device)
        
        model = GrokkingTransformer(
            input_dim=n_bits,
            hidden_dim=hidden_dim,
            output_dim=self.config.class_count
        ).to(self.device)
        
        sae_dim = hidden_dim * self.config.sae_expansion_factor
        sae = SuperpositionSAE(
            model_dim=hidden_dim,
            sae_dim=sae_dim
        ).to(self.device)
        
        if previous_model is not None:
            model = self.weight_transfer.transfer(previous_model, model, stage)
        
        if previous_sae is not None and hidden_dim == previous_sae.model_dim:
            try:
                sae.load_state_dict(previous_sae.state_dict())
                print("SAE: Loaded previous weights")
            except:
                print("SAE: New initialization (dimension changed)")
        
        optimizer = optim.AdamW(
            model.parameters(),
            lr=params['learning_rate'],
            weight_decay=params['weight_decay']
        )
        
        sae_optimizer = optim.AdamW(
            sae.parameters(),
            lr=params['learning_rate']
        )
        
        metrics_history = []
        best_test_accuracy = 0.0
        best_model_state = None
        
        header = (f"{'Step':<8} | {'T-Acc':<6} | {'V-Acc':<6} | {'Loss':<9} | "
                 f"{'kappa':<8} | {'delta':<8} | {'T_eff':<8} | {'h_bar':<8} | "
                 f"{'LC':<6} | {'psi':<6} | {'Status':<8}")
        print(f"\n{header}")
        print("-" * len(header))
        
        for step in range(1, params['max_steps'] + 1):
            model.train()
            sae.train()
            
            logits, h_latent = model(train_x)
            loss_classification = F.cross_entropy(logits, train_y)
            
            x_reconstructed, z_sae = sae(h_latent.detach())
            loss_sae = (F.mse_loss(x_reconstructed, h_latent.detach()) +
                       self.config.superposition_sparsity_l1_weight * 
                       z_sae.norm(p=1))
            
            optimizer.zero_grad()
            loss_classification.backward()
            self.metrics_aggregator.accumulate_gradient(model)
            optimizer.step()
            
            sae_optimizer.zero_grad()
            loss_sae.backward()
            sae_optimizer.step()
            
            if (step % self.config.metrics_log_interval == 0 or 
                step == 1 or 
                step == params['max_steps']):
                
                metrics = self.metrics_aggregator.compute_all_metrics(
                    model=model,
                    sae=sae,
                    train_loader=train_x,
                    train_labels=train_y,
                    test_loader=test_x,
                    test_labels=test_y,
                    current_loss=loss_classification.item(),
                    z_sae=z_sae,
                    step=step
                )
                
                metrics_history.append(metrics)
                
                kappa_str = (f"{metrics['kappa']:8.2f}" 
                           if metrics['kappa'] != float('inf') 
                           else "     inf")
                
                is_stagnant, reason = self.stagnation_detector.is_stagnant(
                    metrics_history, step, hidden_dim
                )
                status = "STAGNANT" if is_stagnant else "OK"
                
                print(f"{step:<8} | "
                      f"{metrics['train_accuracy']:.4f} | "
                      f"{metrics['test_accuracy']:.4f} | "
                      f"{metrics['loss']:.2e} | "
                      f"{kappa_str} | "
                      f"{metrics['delta']:.6f} | "
                      f"{metrics['T_eff']:.6f} | "
                      f"{metrics['h_bar_eff']:.2e} | "
                      f"{metrics['local_complexity']:6.2f} | "
                      f"{metrics['psi']:6.4f} | "
                      f"{status:<8}")
                
                if metrics['test_accuracy'] > best_test_accuracy:
                    best_test_accuracy = metrics['test_accuracy']
                    best_model_state = deepcopy(model.state_dict())
                
                if metrics['test_accuracy'] > self.config.grokking_threshold:
                    print(f"\nGROKKING ACHIEVED at step {step}")
                    print(f"  Test accuracy: {metrics['test_accuracy']:.4f}")
                    
                    checkpoint_state = {
                        'seed': self.seed,
                        'stage': stage,
                        'n_bits': n_bits,
                        'hidden_dim': hidden_dim,
                        'step': step,
                        'model_state_dict': model.state_dict(),
                        'sae_state_dict': sae.state_dict(),
                        'optimizer_state_dict': optimizer.state_dict(),
                        'metrics_history': metrics_history,
                        'config': self.config,
                        'timestamp': datetime.now().isoformat()
                    }
                    
                    path = self.checkpoint_manager.save(
                        checkpoint_state,
                        path=str(Path(self.config.checkpoint_dir) / 
                               f"seed_{self.seed}_stage_{stage}_grokked.pt")
                    )
                    print(f"  Checkpoint saved: {path}")
                    
                    return model, sae, True, metrics_history
                
                if is_stagnant:
                    print(f"\nSTAGNATION DETECTED: {reason}")
                    
                    if best_model_state is not None:
                        model.load_state_dict(best_model_state)
                        print("  Loaded best model state")
                    
                    new_lr = params['learning_rate'] * self.config.optimizer_restart_lr_decay
                    optimizer = optim.AdamW(
                        model.parameters(),
                        lr=new_lr,
                        weight_decay=params['weight_decay']
                    )
                    print(f"  Optimizer restarted with lr={new_lr:.6f}")
                    
                    continue
                
                if self.checkpoint_manager.should_checkpoint():
                    checkpoint_state = {
                        'seed': self.seed,
                        'stage': stage,
                        'n_bits': n_bits,
                        'hidden_dim': hidden_dim,
                        'step': step,
                        'model_state_dict': model.state_dict(),
                        'sae_state_dict': sae.state_dict(),
                        'optimizer_state_dict': optimizer.state_dict(),
                        'metrics_history': metrics_history,
                        'config': self.config,
                        'timestamp': datetime.now().isoformat()
                    }
                    
                    path = self.checkpoint_manager.save(checkpoint_state)
                    print(f"\n[CHECKPOINT] {path}\n")
        
        print(f"\nMax steps reached. Best test accuracy: {best_test_accuracy:.4f}")
        
        if (best_model_state is not None and 
            best_test_accuracy > self.config.partial_success_threshold):
            model.load_state_dict(best_model_state)
            print("Loaded best model (partial success)")
            return model, sae, True, metrics_history
        else:
            return None, None, False, metrics_history


class ResultsAnalyzer:
    """Analyze experimental results and generate comprehensive statistics."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.results_dir = Path(config.results_dir)
    
    def analyze_seed_results(self, all_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive analysis of all seed results."""
        analysis = {
            'summary': {},
            'rankings': {},
            'phase_transitions': {},
            'convergence_statistics': {}
        }
        
        successful_seeds = []
        failed_seeds = []
        
        for seed_result in all_results:
            seed = seed_result['seed']
            stages = seed_result['stages']
            
            if stages and all(s['success'] for s in stages):
                successful_seeds.append(seed)
            else:
                failed_seeds.append(seed)
        
        analysis['summary']['total_seeds'] = len(all_results)
        analysis['summary']['successful_seeds'] = len(successful_seeds)
        analysis['summary']['failed_seeds'] = len(failed_seeds)
        analysis['summary']['success_rate'] = (
            len(successful_seeds) / len(all_results) * 100 
            if all_results else 0
        )
        
        phase_transition_data = []
        final_kappa_data = []
        final_delta_data = []
        final_lc_data = []
        final_psi_data = []
        
        for seed_result in all_results:
            if seed_result['stages']:
                last_stage = seed_result['stages'][-1]
                
                if 'phase_transition_step' in last_stage and last_stage['phase_transition_step']:
                    phase_transition_data.append({
                        'seed': seed_result['seed'],
                        'transition_step': last_stage['phase_transition_step'],
                        'pre_kappa': last_stage['pre_transition'].get('kappa', float('inf')),
                        'post_kappa': last_stage['post_transition'].get('kappa', float('inf')),
                        'pre_delta': last_stage['pre_transition'].get('delta', 1.0),
                        'post_delta': last_stage['post_transition'].get('delta', 1.0),
                        'pre_T_eff': last_stage['pre_transition'].get('T_eff', 0.0),
                        'post_T_eff': last_stage['post_transition'].get('T_eff', 0.0)
                    })
                
                if 'final_metrics' in last_stage:
                    final_metrics = last_stage['final_metrics']
                    
                    kappa_val = final_metrics.get('kappa', float('inf'))
                    if kappa_val != float('inf'):
                        final_kappa_data.append({
                            'seed': seed_result['seed'],
                            'kappa': kappa_val
                        })
                    
                    final_delta_data.append({
                        'seed': seed_result['seed'],
                        'delta': final_metrics.get('delta', 1.0)
                    })
                    
                    final_lc_data.append({
                        'seed': seed_result['seed'],
                        'lc': final_metrics.get('local_complexity', 0.0)
                    })
                    
                    final_psi_data.append({
                        'seed': seed_result['seed'],
                        'psi': final_metrics.get('psi', 0.0)
                    })
        
        if phase_transition_data:
            sorted_by_transition = sorted(
                phase_transition_data, 
                key=lambda x: x['transition_step']
            )
            analysis['rankings']['fastest_phase_transitions'] = sorted_by_transition[:10]
            analysis['rankings']['slowest_phase_transitions'] = sorted_by_transition[-10:]
            
            transition_steps = [d['transition_step'] for d in phase_transition_data]
            analysis['phase_transitions']['mean_transition_step'] = np.mean(transition_steps)
            analysis['phase_transitions']['median_transition_step'] = np.median(transition_steps)
            analysis['phase_transitions']['std_transition_step'] = np.std(transition_steps)
            analysis['phase_transitions']['min_transition_step'] = np.min(transition_steps)
            analysis['phase_transitions']['max_transition_step'] = np.max(transition_steps)
            
            kappa_changes = [
                d['post_kappa'] - d['pre_kappa'] 
                for d in phase_transition_data 
                if d['pre_kappa'] != float('inf') and d['post_kappa'] != float('inf')
            ]
            if kappa_changes:
                analysis['phase_transitions']['mean_kappa_change'] = np.mean(kappa_changes)
                analysis['phase_transitions']['median_kappa_change'] = np.median(kappa_changes)
        
        if final_kappa_data:
            sorted_by_kappa = sorted(final_kappa_data, key=lambda x: x['kappa'])
            analysis['rankings']['best_final_kappa'] = sorted_by_kappa[:10]
            analysis['rankings']['worst_final_kappa'] = sorted_by_kappa[-10:]
        
        if final_delta_data:
            sorted_by_delta = sorted(final_delta_data, key=lambda x: x['delta'])
            analysis['rankings']['best_final_delta'] = sorted_by_delta[:10]
            analysis['rankings']['worst_final_delta'] = sorted_by_delta[-10:]
        
        if final_lc_data:
            sorted_by_lc = sorted(final_lc_data, key=lambda x: x['lc'])
            analysis['rankings']['lowest_final_lc'] = sorted_by_lc[:10]
            analysis['rankings']['highest_final_lc'] = sorted_by_lc[-10:]
        
        if final_psi_data:
            sorted_by_psi = sorted(final_psi_data, key=lambda x: x['psi'])
            analysis['rankings']['best_final_psi'] = sorted_by_psi[:10]
        
        kappa_values = [d['kappa'] for d in final_kappa_data]
        delta_values = [d['delta'] for d in final_delta_data]
        lc_values = [d['lc'] for d in final_lc_data]
        psi_values = [d['psi'] for d in final_psi_data]
        
        if kappa_values:
            analysis['convergence_statistics']['kappa'] = {
                'mean': float(np.mean(kappa_values)),
                'median': float(np.median(kappa_values)),
                'std': float(np.std(kappa_values)),
                'min': float(np.min(kappa_values)),
                'max': float(np.max(kappa_values))
            }
        
        if delta_values:
            analysis['convergence_statistics']['delta'] = {
                'mean': float(np.mean(delta_values)),
                'median': float(np.median(delta_values)),
                'std': float(np.std(delta_values)),
                'min': float(np.min(delta_values)),
                'max': float(np.max(delta_values))
            }
        
        if lc_values:
            analysis['convergence_statistics']['local_complexity'] = {
                'mean': float(np.mean(lc_values)),
                'median': float(np.median(lc_values)),
                'std': float(np.std(lc_values)),
                'min': float(np.min(lc_values)),
                'max': float(np.max(lc_values))
            }
        
        if psi_values:
            analysis['convergence_statistics']['psi'] = {
                'mean': float(np.mean(psi_values)),
                'median': float(np.median(psi_values)),
                'std': float(np.std(psi_values)),
                'min': float(np.min(psi_values)),
                'max': float(np.max(psi_values))
            }
        
        return analysis
    
    def print_analysis_report(self, analysis: Dict[str, Any]) -> None:
        """Print comprehensive analysis report to console."""
        print(f"\n{'='*100}")
        print("EXPERIMENTAL RESULTS ANALYSIS")
        print(f"{'='*100}\n")
        
        print("SUMMARY")
        print("-" * 100)
        summary = analysis['summary']
        print(f"Total seeds processed: {summary['total_seeds']}")
        print(f"Successful seeds: {summary['successful_seeds']}")
        print(f"Failed seeds: {summary['failed_seeds']}")
        print(f"Success rate: {summary['success_rate']:.2f}%")
        
        if 'phase_transitions' in analysis and analysis['phase_transitions']:
            print(f"\nPHASE TRANSITION STATISTICS")
            print("-" * 100)
            pt = analysis['phase_transitions']
            print(f"Mean transition step: {pt.get('mean_transition_step', 0):.0f}")
            print(f"Median transition step: {pt.get('median_transition_step', 0):.0f}")
            print(f"Std deviation: {pt.get('std_transition_step', 0):.0f}")
            print(f"Min transition step: {pt.get('min_transition_step', 0):.0f}")
            print(f"Max transition step: {pt.get('max_transition_step', 0):.0f}")
            
            if 'mean_kappa_change' in pt:
                print(f"\nMean kappa change at transition: {pt['mean_kappa_change']:.4f}")
                print(f"Median kappa change at transition: {pt['median_kappa_change']:.4f}")
        
        if 'convergence_statistics' in analysis:
            print(f"\nCONVERGENCE STATISTICS")
            print("-" * 100)
            conv = analysis['convergence_statistics']
            
            for metric_name, stats in conv.items():
                print(f"\n{metric_name.upper()}:")
                print(f"  Mean: {stats['mean']:.6f}")
                print(f"  Median: {stats['median']:.6f}")
                print(f"  Std: {stats['std']:.6f}")
                print(f"  Range: [{stats['min']:.6f}, {stats['max']:.6f}]")
        
        if 'rankings' in analysis:
            rankings = analysis['rankings']
            
            if 'fastest_phase_transitions' in rankings and rankings['fastest_phase_transitions']:
                print(f"\nTOP 10 FASTEST PHASE TRANSITIONS")
                print("-" * 100)
                print(f"{'Rank':<6} {'Seed':<8} {'Step':<12} {'Pre-κ':<12} {'Post-κ':<12} {'Δκ':<12}")
                print("-" * 100)
                for i, entry in enumerate(rankings['fastest_phase_transitions'][:10], 1):
                    pre_k = entry['pre_kappa']
                    post_k = entry['post_kappa']
                    delta_k = post_k - pre_k if pre_k != float('inf') and post_k != float('inf') else 0
                    print(f"{i:<6} {entry['seed']:<8} {entry['transition_step']:<12} "
                          f"{pre_k:<12.4f} {post_k:<12.4f} {delta_k:<12.4f}")
            
            if 'best_final_kappa' in rankings and rankings['best_final_kappa']:
                print(f"\nTOP 10 BEST FINAL KAPPA")
                print("-" * 100)
                print(f"{'Rank':<6} {'Seed':<8} {'Kappa':<12}")
                print("-" * 100)
                for i, entry in enumerate(rankings['best_final_kappa'][:10], 1):
                    print(f"{i:<6} {entry['seed']:<8} {entry['kappa']:<12.6f}")
            
            if 'best_final_delta' in rankings and rankings['best_final_delta']:
                print(f"\nTOP 10 BEST FINAL DELTA")
                print("-" * 100)
                print(f"{'Rank':<6} {'Seed':<8} {'Delta':<12}")
                print("-" * 100)
                for i, entry in enumerate(rankings['best_final_delta'][:10], 1):
                    print(f"{i:<6} {entry['seed']:<8} {entry['delta']:<12.8f}")
            
            if 'lowest_final_lc' in rankings and rankings['lowest_final_lc']:
                print(f"\nTOP 10 LOWEST FINAL LOCAL COMPLEXITY")
                print("-" * 100)
                print(f"{'Rank':<6} {'Seed':<8} {'LC':<12}")
                print("-" * 100)
                for i, entry in enumerate(rankings['lowest_final_lc'][:10], 1):
                    print(f"{i:<6} {entry['seed']:<8} {entry['lc']:<12.4f}")
            
            if 'best_final_psi' in rankings and rankings['best_final_psi']:
                print(f"\nTOP 10 BEST FINAL PSI")
                print("-" * 100)
                print(f"{'Rank':<6} {'Seed':<8} {'Psi':<12}")
                print("-" * 100)
                for i, entry in enumerate(rankings['best_final_psi'][:10], 1):
                    print(f"{i:<6} {entry['seed']:<8} {entry['psi']:<12.6f}")
        
        print(f"\n{'='*100}\n")


class ResultsVisualizer:
    """Generate comprehensive visualizations of experimental results."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.results_dir = Path(config.results_dir)
        self.visualization_dir = self.results_dir / "visualizations"
        self.visualization_dir.mkdir(exist_ok=True, parents=True)
    
    def create_seed_training_dynamics(self, seed_result: Dict[str, Any]) -> None:
        """Create training dynamics visualization for a single seed."""
        if not MATPLOTLIB_AVAILABLE:
            return
        
        seed = seed_result['seed']
        
        for stage_data in seed_result['stages']:
            if not stage_data['success'] or not stage_data['metrics_history']:
                continue
            
            stage = stage_data['stage']
            metrics_history = stage_data['metrics_history']
            
            fig = plt.figure(figsize=(self.config.figure_width, self.config.figure_height))
            gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)
            
            steps = [m['step'] for m in metrics_history]
            
            ax1 = fig.add_subplot(gs[0, :2])
            train_acc = [m['train_accuracy'] for m in metrics_history]
            test_acc = [m['test_accuracy'] for m in metrics_history]
            ax1.plot(steps, train_acc, label='Train Accuracy', linewidth=2)
            ax1.plot(steps, test_acc, label='Test Accuracy', linewidth=2)
            ax1.axhline(y=self.config.grokking_threshold, color='r', 
                       linestyle='--', label='Grokking Threshold')
            ax1.set_xlabel('Step')
            ax1.set_ylabel('Accuracy')
            ax1.set_title(f'Seed {seed} Stage {stage} - Accuracy Dynamics')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            ax2 = fig.add_subplot(gs[0, 2])
            loss = [m['loss'] for m in metrics_history]
            ax2.plot(steps, loss, color='orange', linewidth=2)
            ax2.set_xlabel('Step')
            ax2.set_ylabel('Loss')
            ax2.set_title('Loss')
            ax2.set_yscale('log')
            ax2.grid(True, alpha=0.3)
            
            ax3 = fig.add_subplot(gs[1, 0])
            kappa_values = [m['kappa'] if m['kappa'] != float('inf') else None 
                           for m in metrics_history]
            valid_steps = [s for s, k in zip(steps, kappa_values) if k is not None]
            valid_kappa = [k for k in kappa_values if k is not None]
            if valid_kappa:
                ax3.plot(valid_steps, valid_kappa, color='purple', linewidth=2)
                ax3.set_xlabel('Step')
                ax3.set_ylabel('κ (kappa)')
                ax3.set_title('Gradient Covariance Condition Number')
                ax3.set_yscale('log')
                ax3.grid(True, alpha=0.3)
            
            ax4 = fig.add_subplot(gs[1, 1])
            delta = [m['delta'] for m in metrics_history]
            ax4.plot(steps, delta, color='green', linewidth=2)
            ax4.set_xlabel('Step')
            ax4.set_ylabel('δ (delta)')
            ax4.set_title('Discretization Margin')
            ax4.set_yscale('log')
            ax4.grid(True, alpha=0.3)
            
            ax5 = fig.add_subplot(gs[1, 2])
            T_eff = [m['T_eff'] for m in metrics_history]
            ax5.plot(steps, T_eff, color='red', linewidth=2)
            ax5.set_xlabel('Step')
            ax5.set_ylabel('T_eff')
            ax5.set_title('Effective Temperature')
            ax5.grid(True, alpha=0.3)
            
            ax6 = fig.add_subplot(gs[2, 0])
            h_bar_eff = [m['h_bar_eff'] for m in metrics_history]
            ax6.plot(steps, h_bar_eff, color='brown', linewidth=2)
            ax6.set_xlabel('Step')
            ax6.set_ylabel('ħ_eff')
            ax6.set_title('Effective Planck Constant')
            ax6.set_yscale('log')
            ax6.grid(True, alpha=0.3)
            
            ax7 = fig.add_subplot(gs[2, 1])
            lc = [m['local_complexity'] for m in metrics_history]
            ax7.plot(steps, lc, color='teal', linewidth=2)
            ax7.set_xlabel('Step')
            ax7.set_ylabel('LC')
            ax7.set_title('Local Complexity')
            ax7.grid(True, alpha=0.3)
            
            ax8 = fig.add_subplot(gs[2, 2])
            psi = [m['psi'] for m in metrics_history]
            ax8.plot(steps, psi, color='magenta', linewidth=2)
            ax8.set_xlabel('Step')
            ax8.set_ylabel('ψ (psi)')
            ax8.set_title('Superposition Coefficient')
            ax8.grid(True, alpha=0.3)
            
            plt.suptitle(f'Thermodynamic Training Dynamics - Seed {seed} Stage {stage}',
                        fontsize=16, fontweight='bold')
            
            save_path = self.visualization_dir / f"seed_{seed:04d}_stage_{stage}_dynamics.png"
            plt.savefig(save_path, dpi=self.config.visualization_dpi, bbox_inches='tight')
            plt.close()
    
    def create_aggregate_visualizations(self, all_results: List[Dict[str, Any]]) -> None:
        """Create aggregate visualizations across all seeds."""
        if not MATPLOTLIB_AVAILABLE:
            return
        
        phase_transition_steps = []
        final_kappas = []
        final_deltas = []
        final_test_accs = []
        seeds_list = []
        
        for seed_result in all_results:
            if seed_result['stages']:
                last_stage = seed_result['stages'][-1]
                
                if 'phase_transition_step' in last_stage and last_stage['phase_transition_step']:
                    phase_transition_steps.append(last_stage['phase_transition_step'])
                    seeds_list.append(seed_result['seed'])
                
                if 'final_metrics' in last_stage:
                    fm = last_stage['final_metrics']
                    
                    kappa_val = fm.get('kappa', float('inf'))
                    if kappa_val != float('inf'):
                        final_kappas.append(kappa_val)
                    
                    final_deltas.append(fm.get('delta', 1.0))
                    final_test_accs.append(fm.get('test_accuracy', 0.0))
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        
        if phase_transition_steps:
            axes[0, 0].hist(phase_transition_steps, bins=30, color='blue', alpha=0.7, edgecolor='black')
            axes[0, 0].axvline(np.mean(phase_transition_steps), color='red', 
                              linestyle='--', linewidth=2, label=f'Mean: {np.mean(phase_transition_steps):.0f}')
            axes[0, 0].set_xlabel('Phase Transition Step')
            axes[0, 0].set_ylabel('Frequency')
            axes[0, 0].set_title('Distribution of Phase Transition Steps')
            axes[0, 0].legend()
            axes[0, 0].grid(True, alpha=0.3)
        
        if final_kappas:
            axes[0, 1].hist(final_kappas, bins=30, color='purple', alpha=0.7, edgecolor='black')
            axes[0, 1].axvline(np.mean(final_kappas), color='red', 
                              linestyle='--', linewidth=2, label=f'Mean: {np.mean(final_kappas):.2f}')
            axes[0, 1].set_xlabel('Final κ (kappa)')
            axes[0, 1].set_ylabel('Frequency')
            axes[0, 1].set_title('Distribution of Final Kappa Values')
            axes[0, 1].legend()
            axes[0, 1].grid(True, alpha=0.3)
        
        if final_deltas:
            axes[0, 2].hist(final_deltas, bins=30, color='green', alpha=0.7, edgecolor='black')
            axes[0, 2].axvline(np.mean(final_deltas), color='red', 
                              linestyle='--', linewidth=2, label=f'Mean: {np.mean(final_deltas):.4f}')
            axes[0, 2].set_xlabel('Final δ (delta)')
            axes[0, 2].set_ylabel('Frequency')
            axes[0, 2].set_title('Distribution of Final Delta Values')
            axes[0, 2].set_xscale('log')
            axes[0, 2].legend()
            axes[0, 2].grid(True, alpha=0.3)
        
        if final_test_accs:
            axes[1, 0].hist(final_test_accs, bins=30, color='orange', alpha=0.7, edgecolor='black')
            axes[1, 0].axvline(np.mean(final_test_accs), color='red', 
                              linestyle='--', linewidth=2, label=f'Mean: {np.mean(final_test_accs):.4f}')
            axes[1, 0].set_xlabel('Final Test Accuracy')
            axes[1, 0].set_ylabel('Frequency')
            axes[1, 0].set_title('Distribution of Final Test Accuracies')
            axes[1, 0].legend()
            axes[1, 0].grid(True, alpha=0.3)
        
        if phase_transition_steps and seeds_list:
            axes[1, 1].scatter(seeds_list, phase_transition_steps, alpha=0.6, color='blue')
            axes[1, 1].set_xlabel('Seed')
            axes[1, 1].set_ylabel('Phase Transition Step')
            axes[1, 1].set_title('Phase Transition Steps vs Seed')
            axes[1, 1].grid(True, alpha=0.3)
        
        if final_kappas and final_deltas and len(final_kappas) == len(final_deltas):
            axes[1, 2].scatter(final_kappas, final_deltas, alpha=0.6, color='purple')
            axes[1, 2].set_xlabel('Final κ (kappa)')
            axes[1, 2].set_ylabel('Final δ (delta)')
            axes[1, 2].set_title('Delta vs Kappa at Convergence')
            axes[1, 2].set_xscale('log')
            axes[1, 2].set_yscale('log')
            axes[1, 2].grid(True, alpha=0.3)
        
        plt.suptitle('Aggregate Experimental Results Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        save_path = self.visualization_dir / "aggregate_analysis.png"
        plt.savefig(save_path, dpi=self.config.visualization_dpi, bbox_inches='tight')
        plt.close()
        
        print(f"\nAggregate visualizations saved to: {save_path}")


class MultiSeedCurriculumRunner:
    """Run curriculum training across multiple random seeds."""
    
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.results_dir = Path(config.results_dir)
        self.results_dir.mkdir(exist_ok=True, parents=True)
        
        self.analyzer = ResultsAnalyzer(config)
        self.visualizer = ResultsVisualizer(config)
        
        self.interrupted = False
        signal.signal(signal.SIGINT, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle interrupt signal."""
        print("\n\nInterrupt received. Saving progress...")
        self.interrupted = True
    
    def _set_seed(self, seed: int) -> None:
        """Set random seed for reproducibility."""
        torch.manual_seed(seed)
        np.random.seed(seed)
        if self.config.device == 'cuda':
            torch.cuda.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)
    
    def run_experiment(self) -> None:
        """Run multi-seed curriculum experiment."""
        print(f"\n{'='*80}")
        print("THERMODYNAMIC GROKKING CURRICULUM EXPERIMENT")
        print(f"{'='*80}")
        print(f"Seeds: {self.config.seed_range_start} to {self.config.seed_range_end}")
        print(f"Curriculum stages: {len(self.config.curriculum_stages)}")
        print(f"Device: {self.config.device}")
        print(f"{'='*80}\n")
        
        all_results = []
        
        for seed in range(self.config.seed_range_start, 
                         self.config.seed_range_end + 1):
            
            if self.interrupted:
                print("Experiment interrupted by user.")
                break
            
            print(f"\n{'#'*80}")
            print(f"# SEED {seed} / {self.config.seed_range_end}")
            print(f"{'#'*80}")
            
            self._set_seed(seed)
            
            trainer = CurriculumStageTrainer(self.config, seed)
            
            previous_model = None
            previous_sae = None
            seed_results = {
                'seed': seed,
                'stages': []
            }
            
            for stage_idx, (n_bits, hidden_dim) in enumerate(
                self.config.curriculum_stages
            ):
                
                if self.interrupted:
                    break
                
                model, sae, success, metrics_history = trainer.train_stage(
                    stage=stage_idx,
                    n_bits=n_bits,
                    hidden_dim=hidden_dim,
                    previous_model=previous_model,
                    previous_sae=previous_sae
                )
                
                stage_result = {
                    'stage': stage_idx,
                    'n_bits': n_bits,
                    'hidden_dim': hidden_dim,
                    'success': success,
                    'metrics_history': metrics_history
                }
                
                if success and metrics_history:
                    final_metrics = metrics_history[-1]
                    
                    phase_transition_step = None
                    for i, m in enumerate(metrics_history):
                        if m['test_accuracy'] > self.config.grokking_threshold:
                            phase_transition_step = m['step']
                            break
                    
                    if phase_transition_step is not None:
                        pre_transition_idx = max(0, i - 5)
                        pre_transition_metrics = metrics_history[pre_transition_idx]
                        post_transition_metrics = final_metrics
                    else:
                        pre_transition_metrics = metrics_history[0]
                        post_transition_metrics = final_metrics
                    
                    stage_result['phase_transition_step'] = phase_transition_step
                    stage_result['pre_transition'] = pre_transition_metrics
                    stage_result['post_transition'] = post_transition_metrics
                    stage_result['final_metrics'] = final_metrics
                
                seed_results['stages'].append(stage_result)
                
                seed_result_path = (self.results_dir / 
                                  f"seed_{seed:04d}_stage_{stage_idx}.json")
                with open(seed_result_path, 'w') as f:
                    json.dump(stage_result, f, indent=2, default=str)
                
                if not success:
                    print(f"\nSeed {seed} failed at stage {stage_idx}. "
                          f"Moving to next seed.")
                    break
                
                previous_model = model
                previous_sae = sae
            
            all_results.append(seed_results)
            
            seed_summary_path = self.results_dir / f"seed_{seed:04d}_summary.json"
            with open(seed_summary_path, 'w') as f:
                json.dump(seed_results, f, indent=2, default=str)
            
            print(f"\nGenerating visualizations for seed {seed}...")
            self.visualizer.create_seed_training_dynamics(seed_results)
        
        final_results_path = self.results_dir / "experiment_results.json"
        with open(final_results_path, 'w') as f:
            json.dump(all_results, f, indent=2, default=str)
        
        print(f"\n{'='*100}")
        print("GENERATING COMPREHENSIVE ANALYSIS AND VISUALIZATIONS")
        print(f"{'='*100}\n")
        
        analysis = self.analyzer.analyze_seed_results(all_results)
        
        analysis_path = self.results_dir / "comprehensive_analysis.json"
        with open(analysis_path, 'w') as f:
            json.dump(analysis, f, indent=2, default=str)
        
        self.analyzer.print_analysis_report(analysis)
        
        print("\nGenerating aggregate visualizations...")
        self.visualizer.create_aggregate_visualizations(all_results)
        
        print(f"\n{'='*100}")
        print("EXPERIMENT COMPLETE")
        print(f"{'='*100}")
        print(f"Total seeds processed: {len(all_results)}")
        print(f"Results saved to: {final_results_path}")
        print(f"Analysis saved to: {analysis_path}")
        print(f"Individual seed results in: {self.results_dir}/")
        print(f"Visualizations in: {self.visualizer.visualization_dir}/")
        print(f"{'='*100}\n")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Thermodynamic Grokking Curriculum Experiment',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--seed-start', type=int, default=1,
                       help='Starting seed number')
    parser.add_argument('--seed-end', type=int, default=100,
                       help='Ending seed number')
    parser.add_argument('--base-lr', type=float, default=1e-3,
                       help='Base learning rate')
    parser.add_argument('--base-wd', type=float, default=1.0,
                       help='Base weight decay')
    parser.add_argument('--checkpoint-interval', type=float, default=5.0,
                       help='Checkpoint interval in minutes')
    
    args = parser.parse_args()
    
    config = replace(
        ExperimentConfig(),
        seed_range_start=args.seed_start,
        seed_range_end=args.seed_end,
        base_learning_rate=args.base_lr,
        base_weight_decay=args.base_wd,
        checkpoint_interval_minutes=args.checkpoint_interval
    )
    
    runner = MultiSeedCurriculumRunner(config)
    runner.run_experiment()


if __name__ == "__main__":
    main()