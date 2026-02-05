#!/usr/bin/env python3
"""
Streamlit application for real-time grokking phase transition visualization.
"""

import streamlit as st
import torch
import torch.nn.functional as F
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import cdist
from scipy import fft
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from copy import deepcopy

from config import ExperimentConfig
from models import GrokkingTransformer, SuperpositionSAE
from data_generation import ParityDatasetGenerator
from metrics import ComprehensiveMetricsAggregator
from training_dynamics import SmartWeightTransfer
from wandb_integration import WandBLogger

st.set_page_config(
    page_title="Thermodynamic Grokking Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0a0e17 0%, #0d1b2a 100%);
        color: #e0e0ff;
    }
    .phase-gas {
        background: linear-gradient(45deg, #ff0000, #ff6600);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .phase-liquid {
        background: linear-gradient(45deg, #ff6600, #ffff00);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .phase-transition {
        background: linear-gradient(45deg, #ffff00, #00ff00);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .phase-solid {
        background: linear-gradient(45deg, #00ff00, #00ffff);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    h1, h2, h3 {
        color: #64b5f6 !important;
    }
</style>
""", unsafe_allow_html=True)


class ThermodynamicAnalyzer:
    """Complete thermodynamic analysis of phase transitions."""
    
    @staticmethod
    def compute_metrics(
        weights_list: List[np.ndarray], 
        phase: str, 
        epoch: int
    ) -> Dict[str, float]:
        """Calculate complete thermodynamic state."""
        W = np.concatenate([w.flatten() for w in weights_list])
        W = np.nan_to_num(W, nan=0.0, posinf=1e6, neginf=-1e6)
        
        temperature = float(np.std(W) * 100)
        
        hist, _ = np.histogram(W, bins=50, density=True)
        hist = hist[hist > 0]
        entropy = float(-np.sum(hist * np.log(hist + 1e-10)))
        
        energy = float(np.linalg.norm(W))
        
        max_ent = float(np.log(len(hist) + 1))
        order = float(1 - entropy / max_ent if max_ent > 0 else 0)
        
        if len(W) > 100:
            sample_size = min(2000, len(W))
            sample = W[:sample_size].reshape(
                min(20, int(np.sqrt(sample_size))), -1
            )
            corr = np.corrcoef(sample)
            coherence = float(
                np.mean(np.abs(corr[np.triu_indices_from(corr, k=1)]))
            )
        else:
            coherence = 0.0
        
        sample_2d = W[:min(1000, len(W))].reshape(-1, 1)
        if len(sample_2d) > 10:
            distances = cdist(sample_2d, sample_2d)
            threshold = np.percentile(distances, 20)
            local_density = float(np.mean(np.sum(distances < threshold, axis=1)))
        else:
            local_density = 0.0
        
        try:
            sample_size = min(1000, len(weights_list[0]))
            W_sample = (weights_list[1][:sample_size] if len(weights_list) > 1 
                       else weights_list[0][:sample_size])
            pca = PCA(n_components=min(50, W_sample.shape[1], sample_size))
            pca.fit(W_sample)
            explained_variance = pca.explained_variance_ratio_
            fractal_dim = float(np.sum(explained_variance > 1e-3))
        except:
            fractal_dim = 1.0
        
        return {
            'temperature': temperature,
            'entropy': entropy,
            'energy': energy,
            'order': order,
            'coherence': coherence,
            'local_density': local_density,
            'fractal_dim': fractal_dim,
            'phase': phase,
            'epoch': epoch
        }


class StreamlitTrainer:
    """Real-time training with Streamlit visualization."""
    
    def __init__(self, config: ExperimentConfig):
        """Initialize trainer."""
        self.config = config
        self.device = torch.device(config.device)
        
        self.data_generator = ParityDatasetGenerator(config)
        self.metrics_aggregator = ComprehensiveMetricsAggregator(config)
        self.weight_transfer = SmartWeightTransfer()
        self.wandb_logger = WandBLogger(config)
        
        self.stage_to_phase = {
            0: "Gas",
            1: "Liquid",
            2: "Transition",
            3: "Crystalline"
        }
    
    def train_stage_with_visualization(
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
        """Train stage with real-time Streamlit visualization."""
        phase_name = self.stage_to_phase[stage]
        
        header_container = st.container()
        metrics_container = st.container()
        thermo_container = st.container()
        phase_container = st.container()
        viz_3d_container = st.container()
        viz_2d_container = st.container()
        chart_container = st.container()
        
        with header_container:
            st.markdown(f"### Stage {stage+1}: {phase_name}")
            st.markdown(f"**Configuration:** n_bits={n_bits}, hidden_dim={hidden_dim}")
            progress_bar = st.progress(0)
            step_display = st.empty()
        
        with metrics_container:
            st.markdown("#### Core Metrics")
            cols = st.columns(6)
            m_train = cols[0].empty()
            m_test = cols[1].empty()
            m_psi = cols[2].empty()
            m_lc = cols[3].empty()
            m_bits = cols[4].empty()
            m_hidden = cols[5].empty()
        
        with thermo_container:
            st.markdown("#### Thermodynamic State")
            cols2 = st.columns(5)
            m_temp = cols2[0].empty()
            m_entropy = cols2[1].empty()
            m_order = cols2[2].empty()
            m_energy = cols2[3].empty()
            m_coherence = cols2[4].empty()
        
        train_size = self.config.get_adaptive_train_size(n_bits)
        weight_decay = self.config.get_adaptive_weight_decay(n_bits, hidden_dim)
        max_steps = self.config.get_adaptive_max_steps(n_bits, hidden_dim)
        learning_rate = self.config.base_learning_rate
        
        run_name = f"streamlit_stage_{stage}_n{n_bits}_d{hidden_dim}"
        run_config = {
            'stage': stage,
            'n_bits': n_bits,
            'hidden_dim': hidden_dim,
            'train_size': train_size,
            'weight_decay': weight_decay,
            'max_steps': max_steps,
            'learning_rate': learning_rate
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
            except:
                pass
        
        optimizer = torch.optim.AdamW(
            model.parameters(),
            lr=learning_rate,
            weight_decay=weight_decay
        )
        
        sae_optimizer = torch.optim.AdamW(
            sae.parameters(),
            lr=learning_rate
        )
        
        stage_history = {
            'steps': [], 'train_acc': [], 'test_acc': [], 
            'psi': [], 'lc': [], 'kappa': [], 'delta': [],
            'T_eff': [], 'h_bar_eff': []
        }
        
        best_test_acc = 0.0
        last_thermo = None
        
        m_bits.metric("Bits", n_bits)
        m_hidden.metric("Hidden", hidden_dim)
        
        viz_3d_placeholder = None
        viz_2d_placeholder = None
        chart_placeholder = None
        
        for step in range(1, max_steps + 1):
            model.train()
            
            logits, h_latent = model(train_x)
            loss_cls = F.cross_entropy(logits, train_y)
            
            x_recon, z_sae = sae(h_latent.detach())
            loss_sae = (
                F.mse_loss(x_recon, h_latent.detach()) + 
                self.config.sae_l1_coefficient * z_sae.norm(p=1)
            )
            
            optimizer.zero_grad()
            loss_cls.backward()
            self.metrics_aggregator.accumulate_gradient(model)
            optimizer.step()
            
            sae_optimizer.zero_grad()
            loss_sae.backward()
            sae_optimizer.step()
            
            if step % self.config.metrics_log_interval == 0 or step == 1:
                model.eval()
                with torch.no_grad():
                    t_logits, _ = model(test_x)
                    train_acc = (logits.argmax(1) == train_y).float().mean().item()
                    test_acc = (t_logits.argmax(1) == test_y).float().mean().item()
                    
                    psi, _ = sae.compute_superposition_metrics(z_sae)
                    
                    metrics = self.metrics_aggregator.compute_all_metrics(
                        model=model,
                        sae=sae,
                        train_loader=train_x,
                        train_labels=train_y,
                        test_loader=test_x,
                        test_labels=test_y,
                        current_loss=loss_cls.item(),
                        z_sae=z_sae,
                        step=step
                    )
                    
                    stage_history['steps'].append(step)
                    stage_history['train_acc'].append(train_acc)
                    stage_history['test_acc'].append(test_acc)
                    stage_history['psi'].append(psi)
                    stage_history['lc'].append(metrics['local_complexity'])
                    stage_history['kappa'].append(
                        metrics['kappa'] if metrics['kappa'] != float('inf') else 0
                    )
                    stage_history['delta'].append(metrics['delta'])
                    stage_history['T_eff'].append(metrics['T_eff'])
                    stage_history['h_bar_eff'].append(metrics['h_bar_eff'])
                    
                    weights_list = [
                        model.fc1.weight.detach().cpu().numpy().copy(),
                        model.fc2.weight.detach().cpu().numpy().copy(),
                        model.output_layer.weight.detach().cpu().numpy().copy()
                    ]
                    last_thermo = ThermodynamicAnalyzer.compute_metrics(
                        weights_list, phase_name, step
                    )
                    
                    self.wandb_logger.log_metrics(metrics, step=step)
                    
                    with header_container:
                        progress_bar.progress(min(step / max_steps, 1.0))
                        step_display.markdown(f"**Step: {step:,} / {max_steps:,}**")
                    
                    m_train.metric("Train", f"{train_acc:.2%}")
                    m_test.metric("Test", f"{test_acc:.2%}")
                    m_psi.metric("Psi", f"{psi:.3f}")
                    m_lc.metric("LC", f"{metrics['local_complexity']:.1f}")
                    
                    m_temp.metric("Temp", f"{last_thermo['temperature']:.2f}")
                    m_entropy.metric("Entropy", f"{last_thermo['entropy']:.3f}")
                    m_order.metric("Order", f"{last_thermo['order']:.3f}")
                    m_energy.metric("Energy", f"{last_thermo['energy']:.1f}")
                    m_coherence.metric("Coherence", f"{last_thermo['coherence']:.3f}")
                    
                    if step % self.config.visualization_update_interval == 0 or step == 1:
                        with viz_3d_container:
                            st.markdown(f"#### 3D Neural Geometry - Step {step:,}")
                            if viz_3d_placeholder is None:
                                viz_3d_placeholder = st.empty()
                            
                            fig_3d = self._create_3d_visualization(
                                weights_list, phase_name, last_thermo
                            )
                            viz_3d_placeholder.plotly_chart(
                                fig_3d, use_container_width=True
                            )
                        
                        with viz_2d_container:
                            st.markdown(f"#### 2D Weight Texture - Step {step:,}")
                            if viz_2d_placeholder is None:
                                viz_2d_placeholder = st.empty()
                            
                            fig_2d = self._create_2d_visualization(
                                weights_list, phase_name, last_thermo
                            )
                            viz_2d_placeholder.plotly_chart(
                                fig_2d, use_container_width=True
                            )
                    
                    if step % (self.config.metrics_log_interval * 2) == 0 or step == 1:
                        with chart_container:
                            if chart_placeholder is None:
                                st.markdown("#### Training Metrics")
                                chart_placeholder = st.empty()
                            
                            fig_metrics = self._create_metrics_plot(stage_history, phase_name)
                            chart_placeholder.plotly_chart(
                                fig_metrics, use_container_width=True
                            )
                    
                    if test_acc > best_test_acc:
                        best_test_acc = test_acc
                    
                    if test_acc > self.config.grokking_threshold:
                        st.balloons()
                        with phase_container:
                            st.success(f"GROKKING ACHIEVED at step {step}!")
                        
                        self.wandb_logger.finish()
                        return model, sae, True, stage_history
        
        if best_test_acc > self.config.partial_success_threshold:
            self.wandb_logger.finish()
            return model, sae, True, stage_history
        else:
            self.wandb_logger.finish()
            return None, None, False, stage_history
    
    def _create_3d_visualization(
        self, 
        weights_list: List[np.ndarray], 
        phase_name: str, 
        thermo_metrics: Dict[str, float]
    ) -> go.Figure:
        """Create 3D PCA visualization."""
        weights = weights_list[1] if len(weights_list) > 1 else weights_list[0]
        
        W_flat = weights.reshape(len(weights), -1)
        n_samples = min(self.config.pca_max_samples, len(W_flat))
        W_sample = W_flat[:n_samples]
        
        pca = PCA(n_components=self.config.pca_components)
        proj = pca.fit_transform(W_sample)
        
        norms = np.linalg.norm(W_sample, axis=1)
        
        distances = cdist(proj, proj)
        threshold = np.percentile(distances, self.config.dbscan_percentile_threshold)
        local_density = np.sum(distances < threshold, axis=1)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter3d(
            x=proj[:, 0],
            y=proj[:, 1],
            z=proj[:, 2],
            mode='markers',
            marker=dict(
                size=6,
                color=local_density,
                colorscale='Turbo',
                colorbar=dict(title="Density"),
                opacity=0.8
            ),
            text=[f"Neuron {i}<br>Norm: {norms[i]:.3f}" 
                  for i in range(len(proj))],
            hovertemplate="<b>%{text}</b><extra></extra>"
        ))
        
        fig.update_layout(
            template="plotly_dark",
            height=700,
            title=f"3D Neural Geometry: {phase_name}",
            scene=dict(
                xaxis=dict(title='PC1'),
                yaxis=dict(title='PC2'),
                zaxis=dict(title='PC3')
            )
        )
        
        return fig
    
    def _create_2d_visualization(
        self,
        weights_list: List[np.ndarray],
        phase_name: str,
        thermo_metrics: Dict[str, float]
    ) -> go.Figure:
        """Create 2D texture visualization."""
        weights = weights_list[1] if len(weights_list) > 1 else weights_list[0]
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Weight Heatmap', 'Distribution',
                           'FFT Spectrum', 'Histogram')
        )
        
        size = min(self.config.texture_max_size, weights.shape[0])
        fig.add_trace(
            go.Heatmap(z=weights[:size, :size], colorscale='RdBu_r'),
            row=1, col=1
        )
        
        W_flat = weights.flatten()
        sample = W_flat[::max(1, len(W_flat)//self.config.texture_sample_reduction)]
        
        fig.add_trace(
            go.Scatter(x=np.arange(len(sample)), y=sample, mode='markers'),
            row=1, col=2
        )
        
        fft_vals = np.abs(fft.rfft(weights[0]))
        fig.add_trace(
            go.Scatter(x=np.arange(len(fft_vals)), y=fft_vals, fill='tozeroy'),
            row=2, col=1
        )
        
        fig.add_trace(
            go.Histogram(x=W_flat, nbinsx=self.config.histogram_bins),
            row=2, col=2
        )
        
        fig.update_layout(
            template="plotly_dark",
            height=600,
            title=f"2D Weight Texture - {phase_name}"
        )
        
        return fig
    
    def _create_metrics_plot(
        self, 
        history: Dict[str, List[float]], 
        phase_name: str
    ) -> go.Figure:
        """Create comprehensive metrics plot."""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Accuracy', 'Superposition', 'LC', 'Kappa & Delta')
        )
        
        fig.add_trace(go.Scatter(
            x=history['steps'], y=history['train_acc'],
            mode='lines', name='Train'
        ), row=1, col=1)
        
        fig.add_trace(go.Scatter(
            x=history['steps'], y=history['test_acc'],
            mode='lines', name='Test'
        ), row=1, col=1)
        
        fig.add_trace(go.Scatter(
            x=history['steps'], y=history['psi'],
            mode='lines', name='Psi', fill='tozeroy'
        ), row=1, col=2)
        
        fig.add_trace(go.Scatter(
            x=history['steps'], y=history['lc'],
            mode='lines', name='LC'
        ), row=2, col=1)
        
        fig.add_trace(go.Scatter(
            x=history['steps'], y=history['kappa'],
            mode='lines', name='Kappa'
        ), row=2, col=2)
        
        fig.update_layout(
            template="plotly_dark",
            height=600,
            title_text=f"Training Metrics: {phase_name}"
        )
        
        return fig
    
    def run_curriculum(self) -> bool:
        """Execute complete curriculum."""
        st.markdown("## Complete Adaptive Curriculum")
        st.markdown("---")
        
        previous_model = None
        previous_sae = None
        
        for stage, (n_bits, hidden_dim) in enumerate(self.config.curriculum_stages):
            model, sae, success, history = self.train_stage_with_visualization(
                stage, n_bits, hidden_dim, previous_model, previous_sae
            )
            
            if not success:
                st.error(f"Curriculum stopped at stage {stage+1}")
                return False
            
            previous_model = model
            previous_sae = sae
            
            st.markdown("---")
        
        st.success("Complete curriculum finished!")
        return True


def main():
    """Main Streamlit application."""
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #0f2042, #1e3a5f); 
    border-radius: 20px; margin-bottom: 30px;'>
    <h1 style='font-size: 3em;'>Thermodynamic Grokking Analyzer</h1>
    <h2 style='font-size: 1.5em; color: #bbdefb;'>Real-Time Phase Transitions</h2>
    </div>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        st.header("Control Panel")
        st.markdown("---")
        
        seed = st.number_input("Random Seed", min_value=1, max_value=10000, value=42)
        
        use_wandb = st.checkbox("Enable WandB Logging", value=True)
        
        if st.button("Start Training", type="primary", use_container_width=True):
            st.session_state['start_training'] = True
            st.session_state['seed'] = seed
            st.session_state['use_wandb'] = use_wandb
        
        if st.button("Reset", use_container_width=True):
            st.session_state.clear()
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        ### Curriculum Stages
        1. Gas (10 bits, 128 hidden)
        2. Liquid (24 bits, 256 hidden)
        3. Transition (32 bits, 512 hidden)
        4. Crystalline (64 bits, 1024 hidden)
        """)
    
    if 'start_training' in st.session_state and st.session_state['start_training']:
        config = ExperimentConfig(
            seed=st.session_state.get('seed', 42),
            use_wandb=st.session_state.get('use_wandb', True)
        )
        
        torch.manual_seed(config.seed)
        np.random.seed(config.seed)
        
        trainer = StreamlitTrainer(config)
        trainer.run_curriculum()
        
        st.session_state['start_training'] = False
    else:
        st.info("Configure settings and press 'Start Training' to begin")


if __name__ == "__main__":
    main()
