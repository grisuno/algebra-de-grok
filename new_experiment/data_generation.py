#!/usr/bin/env python3
"""
Data generation module for parity learning tasks.
"""

import torch
from typing import Tuple
from config import ExperimentConfig


class ParityDatasetGenerator:
    """
    Generates binary parity learning datasets.
    
    The parity function computes whether the sum of the first k bits
    of an n-bit input vector is odd (1) or even (0).
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize dataset generator.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
    
    def generate(
        self, 
        n_bits: int, 
        k_bits: int, 
        dataset_size: int
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Generate random binary vectors with k-bit parity labels.
        
        Args:
            n_bits: Total number of input bits
            k_bits: Number of bits used for parity calculation
            dataset_size: Number of samples to generate
            
        Returns:
            Tuple of (inputs, labels) where inputs are binary vectors
            and labels are parity values
        """
        inputs = (torch.rand(dataset_size, n_bits) > 0.5).float()
        labels = (inputs[:, :k_bits].sum(dim=1) % 2).long()
        return inputs, labels
