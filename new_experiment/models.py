#!/usr/bin/env python3
"""
Neural network architectures for grokking experiments.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from typing import Tuple, List
from abc import ABC, abstractmethod


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


class GrokkingTransformer(nn.Module, IModelArchitecture):
    """
    Two-layer MLP for parity learning experiments.
    
    Architecture:
        input -> fc1 -> ReLU -> fc2 -> ReLU -> output
    """
    
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        """
        Initialize network.
        
        Args:
            input_dim: Number of input features
            hidden_dim: Hidden layer dimensionality
            output_dim: Number of output classes
        """
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.output_layer = nn.Linear(hidden_dim, output_dim)
    
    def get_pre_activations(self, x: torch.Tensor) -> List[torch.Tensor]:
        """
        Get pre-activation tensors for local complexity calculation.
        
        Args:
            x: Input tensor
            
        Returns:
            List of pre-activation tensors
        """
        z1 = self.fc1(x)
        h1 = F.relu(z1)
        z2 = self.fc2(h1)
        return [z1, z2]
    
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Forward pass through network.
        
        Args:
            x: Input tensor
            
        Returns:
            Tuple of (logits, latent_representation)
        """
        z1 = self.fc1(x)
        h1 = F.relu(z1)
        z2 = self.fc2(h1)
        h2 = F.relu(z2)
        logits = self.output_layer(h2)
        return logits, h2
    
    def get_flat_parameters(self) -> torch.Tensor:
        """
        Get flattened parameter vector.
        
        Returns:
            1D tensor containing all model parameters
        """
        return torch.cat([p.flatten() for p in self.parameters()])


class SuperpositionSAE(nn.Module):
    """
    Sparse Autoencoder for superposition analysis.
    
    Used to measure effective feature dimensionality and
    superposition coefficient in learned representations.
    """
    
    def __init__(self, model_dim: int, sae_dim: int):
        """
        Initialize SAE.
        
        Args:
            model_dim: Dimensionality of model representations
            sae_dim: Expanded SAE feature dimensionality
        """
        super().__init__()
        self.model_dim = model_dim
        self.sae_dim = sae_dim
        
        self.encoder_weight = nn.Parameter(
            torch.randn(model_dim, sae_dim) / math.sqrt(model_dim)
        )
        self.encoder_bias = nn.Parameter(torch.zeros(sae_dim))
    
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Encode and decode with ReLU activation.
        
        Args:
            x: Input representations
            
        Returns:
            Tuple of (reconstructed, encoded_features)
        """
        z_encoded = F.relu(x @ self.encoder_weight + self.encoder_bias)
        x_reconstructed = z_encoded @ self.encoder_weight.t()
        return x_reconstructed, z_encoded
    
    def compute_superposition_metrics(
        self, 
        z_encoded: torch.Tensor
    ) -> Tuple[float, float]:
        """
        Calculate superposition coefficient and effective features.
        
        The superposition coefficient measures how efficiently the model
        packs information into its representation space.
        
        Args:
            z_encoded: Encoded feature activations
            
        Returns:
            Tuple of (psi_coefficient, effective_features)
        """
        with torch.no_grad():
            feature_importance = z_encoded.abs().sum(dim=0)
            probability_distribution = feature_importance / (
                feature_importance.sum() + 1e-12
            )
            
            p_safe = probability_distribution[probability_distribution > 1e-10]
            shannon_entropy = -torch.sum(
                p_safe * torch.log(p_safe + 1e-12)
            )
            
            effective_features = torch.exp(shannon_entropy)
            psi = effective_features / self.model_dim
            
            return psi.item(), effective_features.item()
