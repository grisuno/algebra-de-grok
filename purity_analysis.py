#!/usr/bin/env python3
"""
Purity index analysis for binary parity grokking models.
Analyzes crystallization quality and phase transitions in learned representations.
"""

import torch
import torch.nn as nn
import numpy as np
import json
import os
import argparse
from datetime import datetime
from typing import Dict, Any, List, Tuple, Optional, Protocol, runtime_checkable
from pathlib import Path
import glob
from dataclasses import dataclass, replace
from scipy.stats import entropy

from new_experiment.config import ExperimentConfig
from new_experiment.models import GrokkingTransformer, SuperpositionSAE


@dataclass(frozen=True)
class PurityConfig:
    """Configuration for purity index analysis."""
    
    discretization_margin: float = 0.1
    entropy_bins: int = 50
    temperature_window: int = 100
    specific_heat_window: int = 50
    
    pruning_levels: Tuple[float, ...] = (0.0, 0.1, 0.3, 0.5, 0.7, 0.9)
    
    alpha_saturation: float = 20.0
    alpha_threshold_crystal: float = 7.0
    alpha_threshold_glass: float = 1.0
    
    glass_temperature_threshold: float = 0.1
    crystal_temperature_threshold: float = 0.01
    
    figure_dpi: int = 150
    save_format: str = 'png'
    
    device: str = 'cuda' if torch.cuda.is_available() else 'cpu'


@runtime_checkable
class IModel(Protocol):
    """Protocol for models supporting purity analysis."""
    
    def get_flat_parameters(self) -> torch.Tensor: ...


@runtime_checkable
class IPurityIndexCalculator(Protocol):
    """Protocol for purity index calculation."""
    
    def calculate(self, model: IModel) -> Dict[str, float]: ...


@runtime_checkable
class IEffectiveTemperatureCalculator(Protocol):
    """Protocol for effective temperature calculation."""
    
    def calculate(self, loss_history: List[float]) -> Dict[str, float]: ...


@runtime_checkable
class IPhaseClassifier(Protocol):
    """Protocol for phase classification."""
    
    def classify(self, alpha: float, temperature: float) -> str: ...


@runtime_checkable
class IPolycrystalAnalyzer(Protocol):
    """Protocol for polycrystal analysis."""
    
    def analyze_polycrystal(
        self, 
        model: IModel, 
        pruning_level: float
    ) -> Dict[str, Any]: ...


@runtime_checkable
class IPurityComparator(Protocol):
    """Protocol for purity comparison."""
    
    def compare(
        self, 
        original: Dict[str, float], 
        polycrystal: Dict[str, float]
    ) -> Dict[str, Any]: ...


class PurityIndexCalculator:
    """
    Calculate purity index for neural network models.
    
    Measures how close weights are to integer values (crystallization).
    """
    
    def __init__(self, config: PurityConfig = PurityConfig()):
        """
        Initialize calculator.
        
        Args:
            config: Purity analysis configuration
        """
        self.config = config
    
    def calculate(self, model: IModel) -> Dict[str, float]:
        """
        Calculate comprehensive purity metrics.
        
        Args:
            model: Neural network model
            
        Returns:
            Dictionary containing purity metrics
        """
        layer_alphas = {}
        layer_deltas = {}
        global_deltas = []
        
        for name, param in model.named_parameters():
            if param.requires_grad:
                layer_alpha, layer_delta = self._compute_layer_purity(param.data)
                layer_alphas[name] = layer_alpha
                layer_deltas[name] = layer_delta
                global_deltas.append(layer_delta)
        
        global_delta = max(global_deltas) if global_deltas else 1.0
        global_alpha = self._delta_to_alpha(global_delta)
        
        alpha_values = list(layer_alphas.values())
        alpha_variance = float(np.var(alpha_values)) if alpha_values else 0.0
        alpha_mean = float(np.mean(alpha_values)) if alpha_values else 0.0
        
        purity_quality = self._assess_purity_quality(global_alpha, alpha_variance)
        
        return {
            'global_alpha': global_alpha,
            'global_delta': global_delta,
            'layer_alphas': layer_alphas,
            'layer_deltas': layer_deltas,
            'alpha_variance': alpha_variance,
            'alpha_mean': alpha_mean,
            'alpha_std': float(np.std(alpha_values)) if alpha_values else 0.0,
            'purity_quality': purity_quality,
            'is_homogeneous': alpha_variance < 0.1,
            'crystallization_score': self._compute_crystallization_score(
                global_alpha, alpha_variance
            )
        }
    
    def _compute_layer_purity(
        self, 
        weights: torch.Tensor
    ) -> Tuple[float, float]:
        """
        Compute purity metrics for a single layer.
        
        Args:
            weights: Layer weight tensor
            
        Returns:
            Tuple of (alpha, delta)
        """
        rounded = torch.round(weights)
        delta = torch.max(torch.abs(weights - rounded)).item()
        alpha = self._delta_to_alpha(delta)
        return alpha, delta
    
    def _delta_to_alpha(self, delta: float) -> float:
        """
        Convert discretization margin to purity index.
        
        Args:
            delta: Discretization margin
            
        Returns:
            Purity index alpha
        """
        if delta < 1e-10:
            return self.config.alpha_saturation
        return min(-np.log(delta + 1e-15), self.config.alpha_saturation)
    
    def _assess_purity_quality(
        self, 
        alpha: float, 
        variance: float
    ) -> str:
        """
        Assess overall purity quality.
        
        Args:
            alpha: Global purity index
            variance: Alpha variance across layers
            
        Returns:
            Quality assessment string
        """
        if alpha > self.config.alpha_threshold_crystal and variance < 0.1:
            return 'high_purity_crystal'
        elif alpha > self.config.alpha_threshold_crystal:
            return 'crystal_with_defects'
        elif alpha > self.config.alpha_threshold_glass:
            return 'transitional_phase'
        else:
            return 'low_purity_glass'
    
    def _compute_crystallization_score(
        self, 
        alpha: float, 
        variance: float
    ) -> float:
        """
        Compute overall crystallization quality score.
        
        Args:
            alpha: Global purity index
            variance: Alpha variance
            
        Returns:
            Crystallization score [0, 1]
        """
        alpha_normalized = min(alpha / self.config.alpha_saturation, 1.0)
        homogeneity = max(0, 1.0 - variance)
        return float(alpha_normalized * 0.7 + homogeneity * 0.3)


class EffectiveTemperatureCalculator:
    """
    Calculate effective temperature from loss dynamics.
    
    Temperature measures training volatility and convergence.
    """
    
    def __init__(self, config: PurityConfig = PurityConfig()):
        """
        Initialize calculator.
        
        Args:
            config: Purity analysis configuration
        """
        self.config = config
    
    def calculate(self, loss_history: List[float]) -> Dict[str, float]:
        """
        Calculate thermodynamic metrics from loss history.
        
        Args:
            loss_history: List of loss values over training
            
        Returns:
            Dictionary containing temperature metrics
        """
        if len(loss_history) < self.config.temperature_window:
            return {
                'temperature': 0.0,
                'specific_heat': 0.0,
                'thermal_energy': 0.0,
                'entropy_production': 0.0,
                'is_equilibrated': False,
                'temperature_trend': 0.0
            }
        
        recent_losses = loss_history[-self.config.temperature_window:]
        
        temperature = float(np.var(recent_losses))
        
        if len(loss_history) >= self.config.specific_heat_window * 2:
            recent = loss_history[-self.config.specific_heat_window:]
            previous = loss_history[
                -(self.config.specific_heat_window * 2):
                -self.config.specific_heat_window
            ]
            specific_heat = float(np.var(recent) - np.var(previous))
        else:
            specific_heat = 0.0
        
        thermal_energy = float(np.mean(recent_losses))
        
        if len(recent_losses) > 1:
            entropy_production = float(np.sum(np.diff(recent_losses) ** 2))
        else:
            entropy_production = 0.0
        
        is_equilibrated = temperature < self.config.crystal_temperature_threshold
        
        if len(loss_history) >= self.config.temperature_window * 2:
            earlier = loss_history[
                -(self.config.temperature_window * 2):
                -self.config.temperature_window
            ]
            temperature_trend = float(np.var(recent_losses) - np.var(earlier))
        else:
            temperature_trend = 0.0
        
        return {
            'temperature': temperature,
            'specific_heat': specific_heat,
            'thermal_energy': thermal_energy,
            'entropy_production': entropy_production,
            'is_equilibrated': bool(is_equilibrated),
            'temperature_trend': temperature_trend,
            'cooling_rate': -temperature_trend if temperature_trend < 0 else 0.0
        }


class PhaseClassifier:
    """
    Classify crystallization phase based on purity and temperature.
    
    Identifies gas, liquid, transition, and crystalline phases.
    """
    
    def __init__(self, config: PurityConfig = PurityConfig()):
        """
        Initialize classifier.
        
        Args:
            config: Purity analysis configuration
        """
        self.config = config
    
    def classify(self, alpha: float, temperature: float) -> str:
        """
        Classify current phase state.
        
        Args:
            alpha: Purity index
            temperature: Effective temperature
            
        Returns:
            Phase classification string
        """
        if (alpha > self.config.alpha_threshold_crystal and 
            temperature < self.config.crystal_temperature_threshold):
            return 'perfect_crystal'
        elif (alpha > self.config.alpha_threshold_crystal and 
              temperature < self.config.glass_temperature_threshold):
            return 'crystal_with_thermal_fluctuations'
        elif alpha > self.config.alpha_threshold_crystal:
            return 'hot_crystal'
        elif (alpha > self.config.alpha_threshold_glass and 
              temperature < self.config.crystal_temperature_threshold):
            return 'cold_polycrystal'
        elif alpha > self.config.alpha_threshold_glass:
            return 'warm_polycrystal'
        elif temperature < self.config.crystal_temperature_threshold:
            return 'cold_glass'
        else:
            return 'hot_glass'
    
    def classify_polycrystal_state(
        self, 
        original_alpha: float, 
        original_temp: float,
        poly_alpha: float, 
        poly_temp: float
    ) -> str:
        """
        Classify polycrystal state after perturbation.
        
        Args:
            original_alpha: Original purity index
            original_temp: Original temperature
            poly_alpha: Polycrystal purity index
            poly_temp: Polycrystal temperature
            
        Returns:
            Polycrystal state classification
        """
        alpha_retention = poly_alpha / original_alpha if original_alpha > 0 else 0
        temp_ratio = poly_temp / original_temp if original_temp > 0 else float('inf')
        
        if alpha_retention > 0.8 and temp_ratio > 2.0:
            return 'polycrystal_with_residual_heat'
        elif alpha_retention > 0.5 and temp_ratio > 1.5:
            return 'fragmented_but_recognizable'
        elif alpha_retention > 0.5:
            return 'cold_fragmentation'
        elif temp_ratio > 2.0:
            return 'thermal_amorphization'
        else:
            return 'complete_amorphization'


class PolycrystalAnalyzer:
    """
    Analyze polycrystalline structure through weight pruning.
    
    Tests structural robustness and phase stability.
    """
    
    def __init__(self, config: PurityConfig = PurityConfig()):
        """
        Initialize analyzer.
        
        Args:
            config: Purity analysis configuration
        """
        self.config = config
        self.purity_calculator = PurityIndexCalculator(config)
        self.temperature_calculator = EffectiveTemperatureCalculator(config)
        self.phase_classifier = PhaseClassifier(config)
    
    def analyze_polycrystal(
        self, 
        model: IModel, 
        pruning_level: float,
        loss_history: List[float] = None
    ) -> Dict[str, Any]:
        """
        Analyze model after weight pruning.
        
        Args:
            model: Neural network model
            pruning_level: Fraction of weights to prune [0, 1]
            loss_history: Training loss history
            
        Returns:
            Dictionary containing polycrystal analysis
        """
        original_state = {
            name: param.clone() 
            for name, param in model.named_parameters()
        }
        
        self._prune_model(model, pruning_level)
        
        purity = self.purity_calculator.calculate(model)
        
        temperature = self.temperature_calculator.calculate(
            loss_history if loss_history else []
        )
        
        phase = self.phase_classifier.classify(
            purity['global_alpha'], 
            temperature['temperature']
        )
        
        for name, param in model.named_parameters():
            param.data = original_state[name]
        
        return {
            'pruning_level': pruning_level,
            'purity': purity,
            'temperature': temperature,
            'phase': phase,
            'is_polycrystal': 'polycrystal' in phase or 'fragmented' in phase,
            'structural_integrity': self._assess_structural_integrity(
                purity['global_alpha'], pruning_level
            )
        }
    
    def _prune_model(self, model: IModel, sparsity: float) -> None:
        """
        Prune smallest magnitude weights.
        
        Args:
            model: Neural network model
            sparsity: Fraction of weights to zero out
        """
        with torch.no_grad():
            for param in model.parameters():
                if param.requires_grad:
                    flat = param.flatten()
                    k = int(sparsity * flat.numel())
                    if k > 0:
                        threshold = torch.topk(
                            torch.abs(flat), k, largest=False
                        ).values[-1]
                        param[torch.abs(param) < threshold] = 0
    
    def _assess_structural_integrity(
        self, 
        alpha: float, 
        pruning_level: float
    ) -> float:
        """
        Assess how well structure survives pruning.
        
        Args:
            alpha: Purity index after pruning
            pruning_level: Fraction of weights pruned
            
        Returns:
            Structural integrity score [0, 1]
        """
        expected_alpha_drop = pruning_level * 0.5
        alpha_normalized = min(alpha / self.config.alpha_saturation, 1.0)
        resistance = max(0, alpha_normalized - expected_alpha_drop)
        return float(resistance)


class PurityComparator:
    """
    Compare purity metrics between original and perturbed states.
    
    Quantifies structural memory and thermal damage.
    """
    
    def __init__(self, config: PurityConfig = PurityConfig()):
        """
        Initialize comparator.
        
        Args:
            config: Purity analysis configuration
        """
        self.config = config
        self.phase_classifier = PhaseClassifier(config)
    
    def compare(
        self, 
        original: Dict[str, float], 
        polycrystal: Dict[str, float]
    ) -> Dict[str, Any]:
        """
        Compare original and polycrystal states.
        
        Args:
            original: Original state metrics
            polycrystal: Polycrystal state metrics
            
        Returns:
            Dictionary containing comparison metrics
        """
        alpha_ratio = (
            polycrystal.get('alpha', 0) / 
            (original.get('alpha', 1e-10) + 1e-10)
        )
        temp_ratio = (
            polycrystal.get('temperature', 0) / 
            (original.get('temperature', 1e-10) + 1e-10)
        )
        
        alpha_retention = min(alpha_ratio, 1.0)
        
        thermal_excess = max(0, temp_ratio - 1.0)
        
        intermediate_phase = self.phase_classifier.classify_polycrystal_state(
            original.get('alpha', 0),
            original.get('temperature', 0),
            polycrystal.get('alpha', 0),
            polycrystal.get('temperature', 0)
        )
        
        is_intermediate_phase = (
            self.config.alpha_threshold_glass < 
            polycrystal.get('alpha', 0) < 
            self.config.alpha_threshold_crystal
            or intermediate_phase in [
                'fragmented_but_recognizable', 
                'polycrystal_with_residual_heat'
            ]
        )
        
        return {
            'alpha_ratio': float(alpha_ratio),
            'alpha_retention': float(alpha_retention),
            'temperature_ratio': float(temp_ratio),
            'thermal_excess': float(thermal_excess),
            'intermediate_phase_detected': is_intermediate_phase,
            'intermediate_phase_type': intermediate_phase,
            'structural_memory_preserved': alpha_retention > 0.5,
            'thermal_damage': thermal_excess > 1.0,
            'quality_degradation': float(1.0 - alpha_retention)
        }


class CheckpointLoader:
    """
    Load and validate checkpoints for purity analysis.
    
    Handles different checkpoint formats and model configurations.
    """
    
    def __init__(self, config: ExperimentConfig):
        """
        Initialize loader.
        
        Args:
            config: Experiment configuration
        """
        self.config = config
    
    def load(
        self, 
        checkpoint_path: str
    ) -> Tuple[GrokkingTransformer, SuperpositionSAE, Dict[str, Any]]:
        """
        Load checkpoint and extract model.
        
        Args:
            checkpoint_path: Path to checkpoint file
            
        Returns:
            Tuple of (model, sae, checkpoint_data)
        """
        try:
            checkpoint = torch.load(
                checkpoint_path,
                map_location=self.config.device,
                weights_only=False
            )
        except Exception as e:
            raise RuntimeError(f"Failed to load checkpoint: {e}")
        
        n_bits = checkpoint.get('n_bits', self.config.curriculum_stages[0][0])
        hidden_dim = checkpoint.get('hidden_dim', self.config.curriculum_stages[0][1])
        
        model = GrokkingTransformer(
            input_dim=n_bits,
            hidden_dim=hidden_dim,
            output_dim=self.config.class_count
        ).to(self.config.device)
        
        sae_dim = hidden_dim * self.config.sae_expansion_factor
        sae = SuperpositionSAE(
            model_dim=hidden_dim,
            sae_dim=sae_dim
        ).to(self.config.device)
        
        if 'model_state_dict' in checkpoint:
            model.load_state_dict(checkpoint['model_state_dict'])
        else:
            raise RuntimeError("No model state dict in checkpoint")
        
        if 'sae_state_dict' in checkpoint:
            try:
                sae.load_state_dict(checkpoint['sae_state_dict'])
            except:
                pass
        
        return model, sae, checkpoint


class PurityAnalyzer:
    """
    Main purity analysis orchestrator.
    
    Coordinates all analysis components and generates comprehensive reports.
    """
    
    def __init__(
        self, 
        checkpoint_path: str,
        experiment_config: ExperimentConfig = None,
        purity_config: PurityConfig = PurityConfig()
    ):
        """
        Initialize analyzer.
        
        Args:
            checkpoint_path: Path to checkpoint file
            experiment_config: Experiment configuration
            purity_config: Purity analysis configuration
        """
        self.checkpoint_path = checkpoint_path
        self.experiment_config = experiment_config or ExperimentConfig()
        self.purity_config = purity_config
        
        self.purity_calculator = PurityIndexCalculator(purity_config)
        self.temperature_calculator = EffectiveTemperatureCalculator(purity_config)
        self.phase_classifier = PhaseClassifier(purity_config)
        self.polycrystal_analyzer = PolycrystalAnalyzer(purity_config)
        self.comparator = PurityComparator(purity_config)
        self.loader = CheckpointLoader(self.experiment_config)
        
        self._load_checkpoint()
    
    def _load_checkpoint(self) -> None:
        """Load checkpoint and extract components."""
        self.model, self.sae, self.checkpoint = self.loader.load(
            self.checkpoint_path
        )
        
        self.epoch = self.checkpoint.get('step', 'unknown')
        self.stage = self.checkpoint.get('stage', 'unknown')
        self.n_bits = self.checkpoint.get('n_bits', 'unknown')
        self.hidden_dim = self.checkpoint.get('hidden_dim', 'unknown')
        
        metrics_history = self.checkpoint.get('metrics_history', [])
        if metrics_history and isinstance(metrics_history, list):
            self.loss_history = [m.get('loss', 0) for m in metrics_history]
        else:
            self.loss_history = []
    
    def analyze(self) -> Dict[str, Any]:
        """
        Perform comprehensive purity analysis.
        
        Returns:
            Dictionary containing complete analysis results
        """
        original_purity = self.purity_calculator.calculate(self.model)
        original_temperature = self.temperature_calculator.calculate(
            self.loss_history
        )
        original_phase = self.phase_classifier.classify(
            original_purity['global_alpha'],
            original_temperature['temperature']
        )
        
        polycrystal_analysis = {}
        for level in self.purity_config.pruning_levels:
            polycrystal_analysis[level] = (
                self.polycrystal_analyzer.analyze_polycrystal(
                    self.model, level, self.loss_history
                )
            )
        
        level_50 = polycrystal_analysis.get(0.5, {})
        comparison = self.comparator.compare(
            {
                'alpha': original_purity['global_alpha'], 
                'temperature': original_temperature['temperature']
            },
            {
                'alpha': level_50.get('purity', {}).get('global_alpha', 0), 
                'temperature': level_50.get('temperature', {}).get('temperature', 0)
            }
        )
        
        phase_transition_detected = any(
            pa['phase'] != original_phase 
            for pa in polycrystal_analysis.values()
        )
        
        results = {
            'metadata': {
                'checkpoint_path': self.checkpoint_path,
                'epoch': self.epoch,
                'stage': self.stage,
                'n_bits': self.n_bits,
                'hidden_dim': self.hidden_dim,
                'timestamp': datetime.now().isoformat()
            },
            'original': {
                'purity': original_purity,
                'temperature': original_temperature,
                'phase': original_phase
            },
            'polycrystal_analysis': polycrystal_analysis,
            'comparison': comparison,
            'phase_transition_detected': phase_transition_detected,
            'intermediate_phase_exists': comparison['intermediate_phase_detected']
        }
        
        self._print_report(results)
        
        return results
    
    def _print_report(self, results: Dict) -> None:
        """
        Print analysis report to console.
        
        Args:
            results: Analysis results dictionary
        """
        print("=" * 80)
        print("PURITY INDEX ANALYSIS REPORT")
        print("=" * 80)
        
        print(f"\n[METADATA]")
        meta = results['metadata']
        print(f"  Checkpoint: {meta['checkpoint_path']}")
        print(f"  Epoch/Step: {meta['epoch']}")
        print(f"  Stage: {meta['stage']}")
        print(f"  n_bits: {meta['n_bits']}")
        print(f"  hidden_dim: {meta['hidden_dim']}")
        
        print(f"\n[ORIGINAL STATE]")
        orig = results['original']
        print(f"  Alpha: {orig['purity']['global_alpha']:.6f}")
        print(f"  Delta: {orig['purity']['global_delta']:.6f}")
        print(f"  Temperature: {orig['temperature']['temperature']:.6e}")
        print(f"  Phase: {orig['phase']}")
        print(f"  Purity quality: {orig['purity']['purity_quality']}")
        print(f"  Is homogeneous: {orig['purity']['is_homogeneous']}")
        print(f"  Crystallization score: {orig['purity']['crystallization_score']:.4f}")
        
        print(f"\n[LAYER ALPHAS]")
        for name, alpha in orig['purity']['layer_alphas'].items():
            print(f"  {name}: {alpha:.6f}")
        
        print(f"\n[POLYCRYSTAL ANALYSIS]")
        for level, analysis in sorted(results['polycrystal_analysis'].items()):
            print(f"  Pruning {level*100:.0f}%:")
            print(f"    Alpha: {analysis['purity']['global_alpha']:.6f}")
            print(f"    Temperature: {analysis['temperature']['temperature']:.6e}")
            print(f"    Phase: {analysis['phase']}")
            print(f"    Structural integrity: {analysis['structural_integrity']:.4f}")
        
        print(f"\n[COMPARISON]")
        comp = results['comparison']
        print(f"  Alpha retention: {comp['alpha_retention']:.2%}")
        print(f"  Temperature ratio: {comp['temperature_ratio']:.2f}x")
        print(f"  Thermal excess: {comp['thermal_excess']:.2f}")
        print(f"  Quality degradation: {comp['quality_degradation']:.2%}")
        print(f"  Intermediate phase: {comp['intermediate_phase_detected']}")
        print(f"  Phase type: {comp['intermediate_phase_type']}")
        print(f"  Structural memory: {comp['structural_memory_preserved']}")
        print(f"  Thermal damage: {comp['thermal_damage']}")
        
        print(f"\n[CONCLUSION]")
        print(f"  Phase transition detected: {results['phase_transition_detected']}")
        print(f"  Intermediate phase exists: {results['intermediate_phase_exists']}")
        
        print("=" * 80)


class PurityPipeline:
    """
    Pipeline for batch processing checkpoints.
    
    Handles multiple checkpoints and generates aggregate statistics.
    """
    
    def __init__(
        self, 
        experiment_config: ExperimentConfig = None,
        purity_config: PurityConfig = PurityConfig()
    ):
        """
        Initialize pipeline.
        
        Args:
            experiment_config: Experiment configuration
            purity_config: Purity analysis configuration
        """
        self.experiment_config = experiment_config or ExperimentConfig()
        self.purity_config = purity_config
    
    def process_checkpoint(
        self, 
        checkpoint_path: str, 
        output_dir: str
    ) -> Dict[str, Any]:
        """
        Process single checkpoint.
        
        Args:
            checkpoint_path: Path to checkpoint file
            output_dir: Directory for output files
            
        Returns:
            Analysis results dictionary
        """
        os.makedirs(output_dir, exist_ok=True)
        
        analyzer = PurityAnalyzer(
            checkpoint_path,
            self.experiment_config,
            self.purity_config
        )
        results = analyzer.analyze()
        
        base_name = Path(checkpoint_path).stem
        
        results_path = os.path.join(output_dir, f'{base_name}_purity.json')
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\nSaved results: {results_path}")
        
        return results
    
    def process_directory(
        self, 
        checkpoint_dir: str, 
        n_latest: Optional[int], 
        output_dir: str
    ) -> List[Dict[str, Any]]:
        """
        Process all checkpoints in directory.
        
        Args:
            checkpoint_dir: Directory containing checkpoints
            n_latest: Number of latest checkpoints to process
            output_dir: Directory for output files
            
        Returns:
            List of analysis results
        """
        pattern = os.path.join(checkpoint_dir, '*.pt')
        checkpoints = glob.glob(pattern)
        
        if not checkpoints:
            print(f"No checkpoints found in {checkpoint_dir}")
            return []
        
        checkpoints.sort(key=os.path.getmtime, reverse=True)
        
        if n_latest is not None:
            checkpoints = checkpoints[:n_latest]
        
        print(f"\nProcessing {len(checkpoints)} checkpoints...\n")
        
        all_results = []
        for cp in checkpoints:
            try:
                results = self.process_checkpoint(cp, output_dir)
                all_results.append(results)
            except Exception as e:
                print(f"Error processing {cp}: {e}")
                import traceback
                traceback.print_exc()
        
        return all_results
    
    def generate_summary(
        self, 
        all_results: List[Dict[str, Any]], 
        output_dir: str
    ) -> None:
        """
        Generate summary statistics across all checkpoints.
        
        Args:
            all_results: List of analysis results
            output_dir: Directory for output files
        """
        if not all_results:
            print("No results to summarize")
            return
        
        intermediate_count = sum(
            1 for r in all_results 
            if r.get('intermediate_phase_exists', False)
        )
        transition_count = sum(
            1 for r in all_results 
            if r.get('phase_transition_detected', False)
        )
        
        alpha_values = []
        alpha_retentions = []
        temp_ratios = []
        crystallization_scores = []
        
        for r in all_results:
            orig = r.get('original', {})
            purity = orig.get('purity', {})
            if 'global_alpha' in purity:
                alpha_values.append(purity['global_alpha'])
            if 'crystallization_score' in purity:
                crystallization_scores.append(purity['crystallization_score'])
            
            comp = r.get('comparison', {})
            if 'alpha_retention' in comp:
                alpha_retentions.append(comp['alpha_retention'])
            if 'temperature_ratio' in comp:
                temp_ratios.append(comp['temperature_ratio'])
        
        summary = {
            'total_checkpoints_analyzed': len(all_results),
            'intermediate_phase_count': intermediate_count,
            'phase_transition_count': transition_count,
            'intermediate_phase_rate': (
                intermediate_count / len(all_results) if all_results else 0
            ),
            'statistics': {
                'mean_alpha': float(np.mean(alpha_values)) if alpha_values else 0,
                'std_alpha': float(np.std(alpha_values)) if alpha_values else 0,
                'mean_crystallization_score': (
                    float(np.mean(crystallization_scores)) 
                    if crystallization_scores else 0
                ),
                'mean_alpha_retention': (
                    float(np.mean(alpha_retentions)) 
                    if alpha_retentions else 0
                ),
                'mean_temperature_ratio': (
                    float(np.mean(temp_ratios)) 
                    if temp_ratios else 0
                )
            },
            'timestamp': datetime.now().isoformat(),
            'individual_results': all_results
        }
        
        summary_path = os.path.join(output_dir, 'purity_summary.json')
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        self._generate_text_report(summary, output_dir)
        
        print(f"\nSaved summary: {summary_path}")
    
    def _generate_text_report(
        self, 
        summary: Dict[str, Any], 
        output_dir: str
    ) -> None:
        """
        Generate human-readable text report.
        
        Args:
            summary: Summary statistics dictionary
            output_dir: Directory for output files
        """
        report_path = os.path.join(output_dir, 'purity_report.txt')
        
        with open(report_path, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("PURITY INDEX ANALYSIS SUMMARY\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Total checkpoints: {summary['total_checkpoints_analyzed']}\n")
            f.write(f"Intermediate phases: {summary['intermediate_phase_count']}\n")
            f.write(f"Phase transitions: {summary['phase_transition_count']}\n")
            f.write(f"Intermediate rate: {summary['intermediate_phase_rate']:.2%}\n\n")
            
            stats = summary['statistics']
            f.write("STATISTICS\n")
            f.write(f"  Mean alpha: {stats['mean_alpha']:.6f}\n")
            f.write(f"  Std alpha: {stats['std_alpha']:.6f}\n")
            f.write(f"  Mean crystallization: {stats['mean_crystallization_score']:.4f}\n")
            f.write(f"  Mean retention: {stats['mean_alpha_retention']:.2%}\n")
            f.write(f"  Mean temp ratio: {stats['mean_temperature_ratio']:.2f}x\n\n")
            
            f.write("-" * 80 + "\n")
            f.write("INDIVIDUAL CHECKPOINTS\n")
            f.write("-" * 80 + "\n\n")
            
            for i, r in enumerate(summary['individual_results'], 1):
                meta = r['metadata']
                orig = r['original']
                comp = r['comparison']
                
                f.write(f"[{i}] {meta['checkpoint_path']}\n")
                f.write(f"    Stage: {meta['stage']}, Step: {meta['epoch']}\n")
                f.write(f"    Alpha: {orig['purity']['global_alpha']:.6f}\n")
                f.write(f"    Phase: {orig['phase']}\n")
                f.write(f"    Retention: {comp['alpha_retention']:.2%}\n")
                f.write(f"    Phase type: {comp['intermediate_phase_type']}\n\n")
            
            f.write("=" * 80 + "\n")
        
        print(f"Saved text report: {report_path}")


def main():
    """Main entry point for purity analysis."""
    parser = argparse.ArgumentParser(
        description='Purity index analysis for binary parity grokking models'
    )
    parser.add_argument(
        'checkpoint',
        nargs='?',
        default=None,
        help='Path to specific checkpoint file'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all checkpoints in directory'
    )
    parser.add_argument(
        '--latest',
        type=int,
        default=None,
        help='Process only N latest checkpoints'
    )
    parser.add_argument(
        '--dir',
        default='checkpoints',
        help='Checkpoint directory'
    )
    parser.add_argument(
        '--output',
        default='purity_analysis',
        help='Output directory for results'
    )
    
    args = parser.parse_args()
    
    experiment_config = ExperimentConfig()
    purity_config = PurityConfig()
    
    pipeline = PurityPipeline(experiment_config, purity_config)
    
    if args.checkpoint:
        if os.path.isfile(args.checkpoint):
            pipeline.process_checkpoint(args.checkpoint, args.output)
        else:
            print(f"Error: Checkpoint not found: {args.checkpoint}")
    elif args.all or args.latest is not None:
        n_to_process = args.latest if args.latest is not None else None
        results = pipeline.process_directory(args.dir, n_to_process, args.output)
        if results:
            pipeline.generate_summary(results, args.output)
    else:
        print("No checkpoint specified. Use --help for usage information.")


if __name__ == '__main__':
    main()