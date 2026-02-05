#!/usr/bin/env python3
"""
Test script to verify framework functionality.
"""

import torch
import numpy as np

from config import ExperimentConfig
from models import GrokkingTransformer, SuperpositionSAE
from data_generation import ParityDatasetGenerator
from metrics import ComprehensiveMetricsAggregator
from checkpointing import CheckpointManager
from training_dynamics import SmartWeightTransfer, StagnationDetector


def test_configuration():
    """Test configuration creation and parameter calculation."""
    print("\nTesting Configuration...")
    config = ExperimentConfig(seed=42)
    
    assert config.seed == 42
    assert len(config.curriculum_stages) == 4
    assert config.base_learning_rate == 1e-3
    
    train_size = config.get_adaptive_train_size(10)
    assert train_size > 0
    
    weight_decay = config.get_adaptive_weight_decay(10, 128)
    assert 0 < weight_decay <= config.base_weight_decay
    
    max_steps = config.get_adaptive_max_steps(10, 128)
    assert max_steps > 0
    
    print("  Configuration: PASSED")


def test_data_generation():
    """Test dataset generation."""
    print("\nTesting Data Generation...")
    config = ExperimentConfig()
    generator = ParityDatasetGenerator(config)
    
    x, y = generator.generate(n_bits=10, k_bits=3, dataset_size=100)
    
    assert x.shape == (100, 10)
    assert y.shape == (100,)
    assert torch.all((y == 0) | (y == 1))
    
    print("  Data Generation: PASSED")


def test_models():
    """Test model architectures."""
    print("\nTesting Models...")
    
    model = GrokkingTransformer(input_dim=10, hidden_dim=128, output_dim=2)
    sae = SuperpositionSAE(model_dim=128, sae_dim=512)
    
    x = torch.randn(32, 10)
    
    logits, h = model(x)
    assert logits.shape == (32, 2)
    assert h.shape == (32, 128)
    
    pre_acts = model.get_pre_activations(x)
    assert len(pre_acts) == 2
    
    x_recon, z = sae(h)
    assert x_recon.shape == (32, 128)
    assert z.shape == (32, 512)
    
    psi, eff_features = sae.compute_superposition_metrics(z)
    assert 0 <= psi <= 1
    assert eff_features > 0
    
    print("  Models: PASSED")


def test_metrics():
    """Test metric calculation."""
    print("\nTesting Metrics...")
    config = ExperimentConfig()
    aggregator = ComprehensiveMetricsAggregator(config)
    
    model = GrokkingTransformer(input_dim=10, hidden_dim=128, output_dim=2)
    sae = SuperpositionSAE(model_dim=128, sae_dim=512)
    
    x = torch.randn(32, 10)
    y = torch.randint(0, 2, (32,))
    
    logits, h = model(x)
    x_recon, z = sae(h)
    
    metrics = aggregator.compute_all_metrics(
        model=model,
        sae=sae,
        train_loader=x,
        train_labels=y,
        test_loader=x,
        test_labels=y,
        current_loss=0.5,
        z_sae=z,
        step=1
    )
    
    required_keys = [
        'step', 'loss', 'train_accuracy', 'test_accuracy',
        'kappa', 'T_eff', 'h_bar_eff', 'local_complexity',
        'delta', 'psi', 'effective_features'
    ]
    
    for key in required_keys:
        assert key in metrics, f"Missing metric: {key}"
    
    print("  Metrics: PASSED")


def test_checkpointing():
    """Test checkpoint management."""
    print("\nTesting Checkpointing...")
    config = ExperimentConfig()
    manager = CheckpointManager(config)
    
    state = {
        'model': torch.randn(10, 10),
        'step': 1000,
        'metrics': {'accuracy': 0.95}
    }
    
    path = manager.save(state)
    assert path is not None
    
    loaded = manager.load(path)
    assert loaded is not None
    assert 'model' in loaded
    assert 'step' in loaded
    
    print("  Checkpointing: PASSED")


def test_weight_transfer():
    """Test smart weight transfer."""
    print("\nTesting Weight Transfer...")
    
    model1 = GrokkingTransformer(input_dim=10, hidden_dim=128, output_dim=2)
    model2 = GrokkingTransformer(input_dim=24, hidden_dim=256, output_dim=2)
    
    transfer = SmartWeightTransfer()
    transferred = transfer.transfer(model1, model2, stage=1)
    
    assert transferred is not None
    assert isinstance(transferred, GrokkingTransformer)
    
    print("  Weight Transfer: PASSED")


def test_stagnation_detection():
    """Test stagnation detector."""
    print("\nTesting Stagnation Detection...")
    config = ExperimentConfig()
    detector = StagnationDetector(config)
    
    metrics_history = [
        {'step': i * 100, 'test_accuracy': 0.5, 'local_complexity': 100}
        for i in range(20)
    ]
    
    is_stagnant, reason = detector.is_stagnant(
        metrics_history, current_step=2000, hidden_dim=128
    )
    
    assert isinstance(is_stagnant, bool)
    
    print("  Stagnation Detection: PASSED")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("RUNNING FRAMEWORK TESTS")
    print("="*60)
    
    test_configuration()
    test_data_generation()
    test_models()
    test_metrics()
    test_checkpointing()
    test_weight_transfer()
    test_stagnation_detection()
    
    print("\n" + "="*60)
    print("ALL TESTS PASSED")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_all_tests()
