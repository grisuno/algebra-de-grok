#!/usr/bin/env python3
"""
Checkpoint management for saving and loading training state.
"""

import torch
import time
from pathlib import Path
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod
from datetime import datetime

from config import ExperimentConfig


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


class CheckpointManager(ICheckpointManager):
    """
    Manage experiment checkpoints with automatic interval-based saving.
    
    Saves both timestamped checkpoints and a latest checkpoint that
    can be used for resuming training.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize checkpoint manager.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
        self.checkpoint_dir = Path(config.checkpoint_dir)
        self.checkpoint_dir.mkdir(exist_ok=True, parents=True)
        self.last_checkpoint_time = time.time()
    
    def save(
        self, 
        state: Dict[str, Any], 
        path: Optional[str] = None
    ) -> str:
        """
        Save checkpoint to disk.
        
        Args:
            state: State dictionary to save
            path: Optional specific path for checkpoint
            
        Returns:
            Path where checkpoint was saved
        """
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
        """
        Load checkpoint from disk.
        
        Args:
            path: Path to checkpoint file
            
        Returns:
            Loaded state dictionary or None if load fails
        """
        try:
            return torch.load(path, map_location=self.config.device)
        except Exception as e:
            print(f"Failed to load checkpoint from {path}: {e}")
            return None
    
    def should_checkpoint(self) -> bool:
        """
        Check if checkpoint interval has elapsed.
        
        Returns:
            True if time to save checkpoint
        """
        elapsed_seconds = time.time() - self.last_checkpoint_time
        return elapsed_seconds >= self.config.checkpoint_interval_seconds
    
    def get_latest_checkpoint_path(self) -> Optional[str]:
        """
        Get path to latest checkpoint if exists.
        
        Returns:
            Path to latest checkpoint or None
        """
        latest = self.checkpoint_dir / self.config.latest_checkpoint_name
        return str(latest) if latest.exists() else None
