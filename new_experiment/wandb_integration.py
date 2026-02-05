#!/usr/bin/env python3
"""
Weights and Biases integration for experiment tracking.
"""

from typing import Dict, Any, Optional
import wandb

from config import ExperimentConfig


class WandBLogger:
    """
    Wrapper for Weights and Biases logging functionality.
    
    Handles initialization, metric logging, and cleanup.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize WandB logger.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
        self.enabled = config.use_wandb
        self.initialized = False
    
    def initialize(
        self, 
        run_name: str, 
        run_config: Dict[str, Any]
    ) -> None:
        """
        Initialize WandB run.
        
        Args:
            run_name: Name for this run
            run_config: Configuration dictionary to log
        """
        if not self.enabled:
            return
        
        try:
            wandb.init(
                project=self.config.wandb_project,
                entity=self.config.wandb_entity,
                name=run_name,
                config=run_config,
                reinit=True
            )
            self.initialized = True
        except Exception as e:
            print(f"Warning: WandB initialization failed: {e}")
            self.enabled = False
    
    def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None) -> None:
        """
        Log metrics to WandB.
        
        Args:
            metrics: Dictionary of metric names to values
            step: Optional step number
        """
        if not self.enabled or not self.initialized:
            return
        
        try:
            if step is not None:
                wandb.log(metrics, step=step)
            else:
                wandb.log(metrics)
        except Exception as e:
            print(f"Warning: WandB logging failed: {e}")
    
    def finish(self) -> None:
        """Finish WandB run."""
        if not self.enabled or not self.initialized:
            return
        
        try:
            wandb.finish()
            self.initialized = False
        except Exception as e:
            print(f"Warning: WandB finish failed: {e}")
