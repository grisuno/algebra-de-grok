#!/usr/bin/env python3
"""
Weight transfer and training dynamics management.
"""

import torch
import torch.nn as nn
from typing import Optional, Tuple, List, Dict, Any

from config import ExperimentConfig


class SmartWeightTransfer:
    """
    Transfer weights intelligently between curriculum stages.
    
    Handles dimension mismatches through padding and cropping
    while preserving learned algorithmic structure.
    """
    
    def transfer(
        self, 
        previous_model: Optional[nn.Module],
        new_model: nn.Module, 
        stage: int
    ) -> nn.Module:
        """
        Transfer weights with padding or cropping as needed.
        
        Args:
            previous_model: Model from previous curriculum stage
            new_model: New model for current stage
            stage: Current stage number
            
        Returns:
            New model with transferred weights
        """
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


class StagnationDetector:
    """
    Detect training stagnation and trigger optimizer resets.
    
    Monitors test accuracy improvement and local complexity to
    identify when training is stuck in poor local minima.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize detector.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
        self.history_window_size = config.stagnation_history_window
    
    def is_stagnant(
        self, 
        metrics_history: List[Dict[str, float]],
        current_step: int, 
        hidden_dim: int
    ) -> Tuple[bool, Optional[str]]:
        """
        Determine if training is stagnant.
        
        Args:
            metrics_history: List of historical metrics
            current_step: Current training step
            hidden_dim: Hidden layer dimensionality
            
        Returns:
            Tuple of (is_stagnant, reason)
        """
        if len(metrics_history) < self.history_window_size:
            return False, None
        
        recent_metrics = metrics_history[-self.history_window_size:]
        
        test_accuracies = [m['test_accuracy'] for m in recent_metrics]
        accuracy_improvement = test_accuracies[-1] - test_accuracies[0]
        
        if accuracy_improvement < self.config.min_test_accuracy_improvement:
            local_complexities = [
                m.get('local_complexity', 0) 
                for m in recent_metrics
            ]
            avg_lc = sum(local_complexities) / len(local_complexities)
            
            lc_threshold = (
                self.config.lc_stagnation_threshold_factor * hidden_dim
            )
            
            if avg_lc > lc_threshold:
                steps_since_first = (
                    current_step - recent_metrics[0]['step']
                )
                
                if steps_since_first > self.config.max_steps_without_improvement:
                    return True, "high_lc_stagnation"
        
        return False, None
