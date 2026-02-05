#!/usr/bin/env python3
"""
Metrics calculation module for thermodynamic and learning analysis.
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Dict, List, Optional, Tuple, Deque
from collections import deque
from abc import ABC, abstractmethod

from config import ExperimentConfig
from models import IModelArchitecture, SuperpositionSAE


class IMetricCalculator(ABC):
    """Interface for metric calculation strategies."""
    
    @abstractmethod
    def calculate(self, **kwargs) -> Dict[str, float]:
        """Calculate metrics and return dictionary of results."""
        pass


class LocalComplexityCalculator(IMetricCalculator):
    """
    Calculate local complexity as effective local dimensionality.
    
    Local complexity measures the number of near-zero pre-activations,
    indicating representational sparsity.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize calculator.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
        self.epsilon = config.local_complexity_epsilon
    
    def calculate(
        self, 
        model: IModelArchitecture, 
        x_batch: torch.Tensor, 
        **kwargs
    ) -> Dict[str, float]:
        """
        Measure LC as count of near-zero pre-activations.
        
        Args:
            model: Neural network model
            x_batch: Input batch
            
        Returns:
            Dictionary containing local complexity value
        """
        model.eval()
        with torch.no_grad():
            pre_activations = model.get_pre_activations(x_batch)
            
            total_inactive = 0.0
            layer_count = len(pre_activations)
            
            for z_layer in pre_activations:
                inactive_per_sample = (
                    z_layer.abs() < self.epsilon
                ).float().sum(dim=1)
                mean_inactive = inactive_per_sample.mean()
                total_inactive += mean_inactive
            
            lc_value = total_inactive / max(layer_count, 1)
            
        return {
            'local_complexity': lc_value.item() if hasattr(lc_value, 'item') else lc_value
        }


class GradientCovarianceCalculator:
    """
    Calculate gradient covariance matrix and condition number.
    
    The condition number kappa measures the ratio of largest to smallest
    eigenvalues of the gradient covariance matrix, indicating optimization
    landscape geometry.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize calculator.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
        self.gradient_buffer: Deque[torch.Tensor] = deque(
            maxlen=config.gradient_window_size
        )
    
    def accumulate_gradient(self, model: nn.Module) -> None:
        """
        Store current gradient vector.
        
        Args:
            model: Neural network model
        """
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
        """
        Calculate condition number of gradient covariance matrix.
        
        Returns:
            Tuple of (kappa, covariance_matrix)
        """
        if len(self.gradient_buffer) < self.config.kappa_min_samples:
            return None, None
        
        try:
            G = torch.stack(list(self.gradient_buffer))
            G_centered = G - G.mean(dim=0, keepdim=True)
            
            n_samples = G.shape[0]
            covariance_matrix = (G_centered.T @ G_centered) / (n_samples - 1)
            
            regularization = (
                torch.eye(covariance_matrix.shape[0]) * 
                self.config.spectral_regularization
            )
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
    """
    Calculate thermodynamic metrics: effective temperature and Planck constant.
    
    These metrics characterize the energy landscape and quantum-like properties
    of the learning dynamics.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize calculator.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
    
    def calculate(
        self, 
        gradient_covariance: Optional[torch.Tensor],
        **kwargs
    ) -> Dict[str, float]:
        """
        Calculate effective temperature and Planck constant.
        
        Args:
            gradient_covariance: Gradient covariance matrix
            
        Returns:
            Dictionary containing thermodynamic metrics
        """
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
            h_bar_eff = (
                position_uncertainty * 
                self.config.planck_constant_regularization
            )
            
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
    """
    Calculate discretization margin delta.
    
    Delta measures how close parameter values are to integers,
    indicating algorithmic crystallization.
    """
    
    def calculate(
        self, 
        model: IModelArchitecture, 
        **kwargs
    ) -> Dict[str, float]:
        """
        Calculate mean squared distance to nearest integer.
        
        Args:
            model: Neural network model
            
        Returns:
            Dictionary containing delta value
        """
        params = model.get_flat_parameters()
        rounded = torch.round(params)
        delta = torch.mean((params - rounded) ** 2).item()
        
        return {'delta': delta}


class ComprehensiveMetricsAggregator:
    """
    Aggregate all thermodynamic and learning metrics.
    
    Centralizes metric calculation and provides unified interface.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize aggregator.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
        self.gradient_calculator = GradientCovarianceCalculator(config)
        self.thermodynamic_calculator = ThermodynamicMetricsCalculator(config)
        self.lc_calculator = LocalComplexityCalculator(config)
        self.delta_calculator = DeltaCalculator()
    
    def compute_all_metrics(
        self,
        model: IModelArchitecture,
        sae: SuperpositionSAE,
        train_loader: torch.Tensor,
        train_labels: torch.Tensor,
        test_loader: torch.Tensor,
        test_labels: torch.Tensor,
        current_loss: float,
        z_sae: torch.Tensor,
        step: int
    ) -> Dict[str, float]:
        """
        Compute comprehensive metric suite.
        
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
            Dictionary containing all computed metrics
        """
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
        """
        Accumulate gradient for kappa calculation.
        
        Args:
            model: Neural network model
        """
        self.gradient_calculator.accumulate_gradient(model)
    
    def reset(self) -> None:
        """Reset all stateful calculators."""
        self.gradient_calculator.reset()
