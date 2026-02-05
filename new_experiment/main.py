#!/usr/bin/env python3
"""
Main entry point for thermodynamic grokking curriculum training.
Supports both command-line and programmatic execution.
"""

import argparse
import torch
import numpy as np
from pathlib import Path

from config import ExperimentConfig
from training import CurriculumStageTrainer


class MultiSeedCurriculumRunner:
    """
    Run curriculum training across multiple random seeds.
    
    Executes the full curriculum for each seed, collecting
    comprehensive results and metrics.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize runner.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
        self.results_dir = Path(config.results_dir)
        self.results_dir.mkdir(exist_ok=True, parents=True)
    
    def _set_seed(self, seed: int) -> None:
        """
        Set random seed for reproducibility.
        
        Args:
            seed: Random seed value
        """
        torch.manual_seed(seed)
        np.random.seed(seed)
        if self.config.device == 'cuda':
            torch.cuda.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)
    
    def run_single_seed(self, seed: int) -> bool:
        """
        Run curriculum for a single seed.
        
        Args:
            seed: Random seed value
            
        Returns:
            True if curriculum completed successfully
        """
        print(f"\n{'#'*80}")
        print(f"# SEED {seed}")
        print(f"{'#'*80}")
        
        self._set_seed(seed)
        
        trainer = CurriculumStageTrainer(self.config, seed)
        
        previous_model = None
        previous_sae = None
        
        for stage_idx, (n_bits, hidden_dim) in enumerate(
            self.config.curriculum_stages
        ):
            model, sae, success, metrics_history = trainer.train_stage(
                stage=stage_idx,
                n_bits=n_bits,
                hidden_dim=hidden_dim,
                previous_model=previous_model,
                previous_sae=previous_sae
            )
            
            if not success:
                print(f"\nSeed {seed} failed at stage {stage_idx}.")
                return False
            
            previous_model = model
            previous_sae = sae
        
        print(f"\nSeed {seed} completed successfully!")
        return True
    
    def run_experiment(self, start_seed: int = 1, end_seed: int = 1) -> None:
        """
        Run experiment across multiple seeds.
        
        Args:
            start_seed: Starting seed number
            end_seed: Ending seed number
        """
        print(f"\n{'='*80}")
        print("THERMODYNAMIC GROKKING CURRICULUM EXPERIMENT")
        print(f"{'='*80}")
        print(f"Seeds: {start_seed} to {end_seed}")
        print(f"Curriculum stages: {len(self.config.curriculum_stages)}")
        print(f"Device: {self.config.device}")
        print(f"{'='*80}\n")
        
        successful_seeds = []
        failed_seeds = []
        
        for seed in range(start_seed, end_seed + 1):
            success = self.run_single_seed(seed)
            
            if success:
                successful_seeds.append(seed)
            else:
                failed_seeds.append(seed)
        
        print(f"\n{'='*80}")
        print("EXPERIMENT SUMMARY")
        print(f"{'='*80}")
        print(f"Total seeds: {end_seed - start_seed + 1}")
        print(f"Successful: {len(successful_seeds)}")
        print(f"Failed: {len(failed_seeds)}")
        
        if failed_seeds:
            print(f"Failed seeds: {failed_seeds}")
        
        print(f"{'='*80}\n")


def main():
    """Main entry point for command-line execution."""
    parser = argparse.ArgumentParser(
        description='Thermodynamic Grokking Curriculum Experiment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --seed 42
  python main.py --seed-start 1 --seed-end 10
  python main.py --seed 42 --base-lr 0.001 --base-wd 1.0
  python main.py --seed 42 --no-wandb
        """
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='Single seed to run (overrides seed-start and seed-end)'
    )
    
    parser.add_argument(
        '--seed-start',
        type=int,
        default=1,
        help='Starting seed number for multi-seed runs'
    )
    
    parser.add_argument(
        '--seed-end',
        type=int,
        default=1,
        help='Ending seed number for multi-seed runs'
    )
    
    parser.add_argument(
        '--base-lr',
        type=float,
        default=1e-3,
        help='Base learning rate'
    )
    
    parser.add_argument(
        '--base-wd',
        type=float,
        default=1.0,
        help='Base weight decay'
    )
    
    parser.add_argument(
        '--checkpoint-interval',
        type=float,
        default=300.0,
        help='Checkpoint interval in seconds'
    )
    
    parser.add_argument(
        '--no-wandb',
        action='store_true',
        help='Disable WandB logging'
    )
    
    parser.add_argument(
        '--device',
        type=str,
        default=None,
        help='Device to use (cuda or cpu)'
    )
    
    args = parser.parse_args()
    
    config_kwargs = {
        'base_learning_rate': args.base_lr,
        'base_weight_decay': args.base_wd,
        'checkpoint_interval_seconds': args.checkpoint_interval,
        'use_wandb': not args.no_wandb
    }
    
    if args.device is not None:
        config_kwargs['device'] = args.device
    
    config = ExperimentConfig(**config_kwargs)
    
    runner = MultiSeedCurriculumRunner(config)
    
    if args.seed is not None:
        runner.run_single_seed(args.seed)
    else:
        runner.run_experiment(args.seed_start, args.seed_end)


if __name__ == "__main__":
    main()
