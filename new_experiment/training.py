#!/usr/bin/env python3
"""
Main training loop for curriculum-based grokking experiments.
"""

import torch
import torch.nn.functional as F
import torch.optim as optim
from typing import Tuple, List, Dict, Any, Optional
from copy import deepcopy

from config import ExperimentConfig
from models import GrokkingTransformer, SuperpositionSAE
from data_generation import ParityDatasetGenerator
from metrics import ComprehensiveMetricsAggregator
from checkpointing import CheckpointManager
from training_dynamics import SmartWeightTransfer, StagnationDetector
from wandb_integration import WandBLogger


class CurriculumStageTrainer:
    """
    Train a single curriculum stage with full metric tracking.
    
    Handles training loop, metric computation, checkpoint management,
    and stagnation detection for one stage of the curriculum.
    """
    
    def __init__(self, config: ExperimentConfig, seed: int):
        """
        Initialize stage trainer.
        
        Args:
            config: Experiment configuration
            seed: Random seed for reproducibility
        """
        self.config = config
        self.seed = seed
        self.device = config.device
        
        self.data_generator = ParityDatasetGenerator(config)
        self.metrics_aggregator = ComprehensiveMetricsAggregator(config)
        self.checkpoint_manager = CheckpointManager(config)
        self.stagnation_detector = StagnationDetector(config)
        self.weight_transfer = SmartWeightTransfer()
        self.wandb_logger = WandBLogger(config)
    
    def train_stage(
        self,
        stage: int,
        n_bits: int,
        hidden_dim: int,
        previous_model: Optional[torch.nn.Module] = None,
        previous_sae: Optional[torch.nn.Module] = None
    ) -> Tuple[
        Optional[torch.nn.Module],
        Optional[torch.nn.Module],
        bool,
        List[Dict[str, float]]
    ]:
        """
        Train a single curriculum stage.
        
        Args:
            stage: Stage number
            n_bits: Number of input bits
            hidden_dim: Hidden layer dimensionality
            previous_model: Model from previous stage
            previous_sae: SAE from previous stage
            
        Returns:
            Tuple of (model, sae, success, metrics_history)
        """
        print(f"\n{'='*80}")
        print(f"SEED {self.seed} | Stage {stage + 1} | "
              f"n_bits={n_bits} | hidden_dim={hidden_dim}")
        print(f"{'='*80}")
        
        train_size = self.config.get_adaptive_train_size(n_bits)
        weight_decay = self.config.get_adaptive_weight_decay(n_bits, hidden_dim)
        max_steps = self.config.get_adaptive_max_steps(n_bits, hidden_dim)
        learning_rate = self.config.base_learning_rate
        
        print(f"Adaptive Parameters:")
        print(f"  Train size: {train_size}")
        print(f"  Weight decay: {weight_decay:.4f}")
        print(f"  Max steps: {max_steps:,}")
        print(f"  Learning rate: {learning_rate:.4f}")
        
        run_name = f"stage_{stage}_n{n_bits}_d{hidden_dim}_seed{self.seed}"
        run_config = {
            'stage': stage,
            'n_bits': n_bits,
            'hidden_dim': hidden_dim,
            'train_size': train_size,
            'weight_decay': weight_decay,
            'max_steps': max_steps,
            'learning_rate': learning_rate,
            'seed': self.seed
        }
        self.wandb_logger.initialize(run_name, run_config)
        
        x_full, y_full = self.data_generator.generate(
            n_bits=n_bits,
            k_bits=self.config.parity_k_bits,
            dataset_size=self.config.curriculum_test_size
        )
        
        train_x = x_full[:train_size].to(self.device)
        train_y = y_full[:train_size].to(self.device)
        
        test_end_idx = train_size + self.config.test_set_size
        test_x = x_full[train_size:test_end_idx].to(self.device)
        test_y = y_full[train_size:test_end_idx].to(self.device)
        
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
            lr=learning_rate,
            weight_decay=weight_decay
        )
        
        sae_optimizer = optim.AdamW(
            sae.parameters(),
            lr=learning_rate
        )
        
        metrics_history = []
        best_test_accuracy = 0.0
        best_model_state = None
        
        header = (
            f"{'Step':<8} | {'Train':<6} | {'Test':<6} | {'Loss':<9} | "
            f"{'Kappa':<8} | {'Delta':<8} | {'T_eff':<8} | {'h_bar':<8} | "
            f"{'LC':<6} | {'Psi':<6} | {'Status':<8}"
        )
        print(f"\n{header}")
        print("-" * len(header))
        
        for step in range(1, max_steps + 1):
            model.train()
            sae.train()
            
            logits, h_latent = model(train_x)
            loss_classification = F.cross_entropy(logits, train_y)
            
            x_reconstructed, z_sae = sae(h_latent.detach())
            loss_sae = (
                F.mse_loss(x_reconstructed, h_latent.detach()) +
                self.config.sae_l1_coefficient * z_sae.norm(p=1)
            )
            
            optimizer.zero_grad()
            loss_classification.backward()
            self.metrics_aggregator.accumulate_gradient(model)
            optimizer.step()
            
            sae_optimizer.zero_grad()
            loss_sae.backward()
            sae_optimizer.step()
            
            if (step % self.config.metrics_log_interval == 0 or 
                step == 1 or 
                step == max_steps):
                
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
                
                metrics['loss_sae'] = loss_sae.item()
                metrics_history.append(metrics)
                
                self.wandb_logger.log_metrics(metrics, step=step)
                
                kappa_str = (
                    f"{metrics['kappa']:8.2f}" 
                    if metrics['kappa'] != float('inf') 
                    else "     inf"
                )
                
                is_stagnant, reason = self.stagnation_detector.is_stagnant(
                    metrics_history, step, hidden_dim
                )
                status = "STAGNANT" if is_stagnant else "OK"
                
                print(
                    f"{step:<8} | "
                    f"{metrics['train_accuracy']:.4f} | "
                    f"{metrics['test_accuracy']:.4f} | "
                    f"{metrics['loss']:.2e} | "
                    f"{kappa_str} | "
                    f"{metrics['delta']:.6f} | "
                    f"{metrics['T_eff']:.6f} | "
                    f"{metrics['h_bar_eff']:.2e} | "
                    f"{metrics['local_complexity']:6.2f} | "
                    f"{metrics['psi']:6.4f} | "
                    f"{status:<8}"
                )
                
                if metrics['test_accuracy'] > best_test_accuracy:
                    best_test_accuracy = metrics['test_accuracy']
                    best_model_state = deepcopy(model.state_dict())
                
                if metrics['test_accuracy'] > self.config.grokking_threshold:
                    print(f"\nGROKKING ACHIEVED at step {step}")
                    print(f"  Test accuracy: {metrics['test_accuracy']:.4f}")
                    
                    checkpoint_state = self._create_checkpoint_state(
                        model, sae, optimizer, stage, n_bits, 
                        hidden_dim, step, metrics_history
                    )
                    
                    path = self.checkpoint_manager.save(
                        checkpoint_state,
                        path=f"{self.config.checkpoint_dir}/seed_{self.seed}_stage_{stage}_grokked.pt"
                    )
                    print(f"  Checkpoint saved: {path}")
                    
                    self.wandb_logger.finish()
                    return model, sae, True, metrics_history
                
                if is_stagnant:
                    print(f"\nSTAGNATION DETECTED: {reason}")
                    
                    if best_model_state is not None:
                        model.load_state_dict(best_model_state)
                        print("  Loaded best model state")
                    
                    new_lr = learning_rate * self.config.optimizer_restart_lr_decay
                    optimizer = optim.AdamW(
                        model.parameters(),
                        lr=new_lr,
                        weight_decay=weight_decay
                    )
                    print(f"  Optimizer restarted with lr={new_lr:.6f}")
                    
                    continue
                
                if self.checkpoint_manager.should_checkpoint():
                    checkpoint_state = self._create_checkpoint_state(
                        model, sae, optimizer, stage, n_bits,
                        hidden_dim, step, metrics_history
                    )
                    
                    path = self.checkpoint_manager.save(checkpoint_state)
                    print(f"\nCHECKPOINT: {path}\n")
        
        print(f"\nMax steps reached. Best test accuracy: {best_test_accuracy:.4f}")
        
        if (best_model_state is not None and 
            best_test_accuracy > self.config.partial_success_threshold):
            model.load_state_dict(best_model_state)
            print("Loaded best model (partial success)")
            self.wandb_logger.finish()
            return model, sae, True, metrics_history
        else:
            self.wandb_logger.finish()
            return None, None, False, metrics_history
    
    def _create_checkpoint_state(
        self,
        model: torch.nn.Module,
        sae: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        stage: int,
        n_bits: int,
        hidden_dim: int,
        step: int,
        metrics_history: List[Dict[str, float]]
    ) -> Dict[str, Any]:
        """
        Create checkpoint state dictionary.
        
        Args:
            model: Neural network model
            sae: Sparse autoencoder
            optimizer: Optimizer
            stage: Current stage
            n_bits: Number of bits
            hidden_dim: Hidden dimensionality
            step: Current step
            metrics_history: Training metrics
            
        Returns:
            State dictionary for checkpointing
        """
        from datetime import datetime
        
        return {
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
