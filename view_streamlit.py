#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPLETE GROKKING PHASE TRANSITION VISUALIZER
Imports app.py without modifications and adds full visualization capabilities
"""
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import cdist
from scipy import fft
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import sys
import os
from copy import deepcopy
from datetime import datetime

st.set_page_config(
    page_title="🔬 Complete Grokking Analyzer",
    layout="wide",
    page_icon="🧠",
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
        text-shadow: 0 0 10px rgba(100, 181, 246, 0.3);
    }
</style>
""", unsafe_allow_html=True)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

try:
    import app
    st.sidebar.success("✅ app.py imported successfully")
except ImportError as e:
    st.sidebar.error(f"❌ Cannot import app.py: {e}")
    st.stop()

class ThermodynamicAnalyzer:
    """Complete thermodynamic analysis of phase transitions"""
    
    @staticmethod
    def compute_metrics(weights_list, phase, epoch):
        """Calculate complete thermodynamic state"""
        
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
            sample = W[:sample_size].reshape(min(20, int(np.sqrt(sample_size))), -1)
            corr = np.corrcoef(sample)
            coherence = float(np.mean(np.abs(corr[np.triu_indices_from(corr, k=1)])))
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
            W_sample = weights_list[1][:sample_size] if len(weights_list) > 1 else weights_list[0][:sample_size]
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
    
    @staticmethod
    def visualize_thermal_engine(thermo_history):
        """Complete thermal engine visualization"""
        if not thermo_history:
            return None
        
        phases = list(thermo_history.keys())
        temps = [thermo_history[p]['temperature'] for p in phases]
        entropies = [thermo_history[p]['entropy'] for p in phases]
        orders = [thermo_history[p]['order'] for p in phases]
        energies = [thermo_history[p]['energy'] for p in phases]
        coherences = [thermo_history[p]['coherence'] for p in phases]
        densities = [thermo_history[p]['local_density'] for p in phases]
        epochs = [thermo_history[p]['epoch'] for p in phases]
        
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=('🌡️ Temperature vs Entropy (Phase Diagram)',
                          '⚡ Energy vs Order',
                          '🔄 Coherence Evolution',
                          '📊 Density Evolution',
                          '💎 Phase Metrics Bar',
                          '🌀 Fractal Dimension'),
            vertical_spacing=0.1,
            horizontal_spacing=0.1
        )
        
        colors = {'Ruido': 'red', 'Memorización': 'orange', 
                 'Transición': 'yellow', 'Grokking': 'lime'}
        
        
        fig.add_trace(go.Scatter(
            x=temps, y=entropies,
            mode='lines+markers+text',
            marker=dict(size=20, color=[colors.get(p, 'white') for p in phases],
                       line=dict(width=2, color='white')),
            line=dict(width=4, color='cyan'),
            text=phases,
            textposition="top center",
            name="Phase Transition"
        ), row=1, col=1)
        
        
        fig.add_trace(go.Scatter(
            x=energies, y=orders,
            mode='markers+text',
            marker=dict(size=15, color=temps, colorscale='Hot',
                       colorbar=dict(title="Temp", x=1.15, len=0.25, y=0.85)),
            text=phases,
            textposition="top center",
            name="Energy-Order"
        ), row=1, col=2)
        
        
        fig.add_trace(go.Scatter(
            x=epochs, y=coherences,
            mode='lines+markers',
            marker=dict(size=10, color=temps, colorscale='Viridis'),
            line=dict(width=3),
            fill='tozeroy',
            name="Coherence"
        ), row=2, col=1)
        
        
        fig.add_trace(go.Scatter(
            x=epochs, y=densities,
            mode='lines+markers',
            marker=dict(size=10, color=[colors.get(p, 'white') for p in phases]),
            line=dict(width=3),
            fill='tozeroy',
            name="Local Density"
        ), row=2, col=2)
        
        
        metrics = ['Temp/10', 'Entropy', 'Order', 'Energy/100']
        for i, phase in enumerate(phases):
            values = [temps[i]/10, entropies[i], orders[i], energies[i]/100]
            fig.add_trace(go.Bar(
                x=metrics,
                y=values,
                name=phase,
                marker_color=colors.get(phase, 'white')
            ), row=3, col=1)
        
        
        fractal_dims = [thermo_history[p].get('fractal_dim', 1.0) for p in phases]
        fig.add_trace(go.Scatter(
            x=epochs, y=fractal_dims,
            mode='lines+markers',
            marker=dict(size=12, color=[colors.get(p, 'white') for p in phases]),
            line=dict(width=3),
            name="Fractal Dim"
        ), row=3, col=2)
        
        fig.update_layout(
            height=1000,
            template="plotly_dark",
            title_text="🌡️ COMPLETE THERMAL ENGINE: Gas → Liquid → Crystal",
            showlegend=True,
            paper_bgcolor='rgba(10, 14, 23, 1)',
            plot_bgcolor='rgba(10, 14, 23, 1)'
        )
        
        return fig




def visualize_3d_geometry(weights_list, phase_name, thermo_metrics):
    """Complete 3D visualization with clustering and geometry"""
    
    
    weights = weights_list[1] if len(weights_list) > 1 else weights_list[0]
    
    W_flat = weights.reshape(len(weights), -1)
    n_samples = min(128, len(W_flat))
    W_sample = W_flat[:n_samples]
    
    
    pca = PCA(n_components=3)
    proj = pca.fit_transform(W_sample)
    
    
    norms = np.linalg.norm(W_sample, axis=1)
    
    
    distances = cdist(proj, proj)
    threshold = np.percentile(distances, 20)
    local_density = np.sum(distances < threshold, axis=1)
    
    
    clustering = DBSCAN(eps=threshold, min_samples=3).fit(proj)
    n_clusters = len(set(clustering.labels_)) - (1 if -1 in clustering.labels_ else 0)
    
    
    spread = np.std(distances[np.triu_indices_from(distances, k=1)])
    
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
            colorbar=dict(
                title="Local<br>Density",
                x=1.02,
                thickness=20
            ),
            opacity=0.8,
            line=dict(width=0.5, color='white')
        ),
        text=[f"Neuron {i}<br>Norm: {norms[i]:.3f}<br>Density: {local_density[i]}" 
              for i in range(len(proj))],
        hovertemplate="<b>%{text}</b><br>PC1: %{x:.3f}<br>PC2: %{y:.3f}<br>PC3: %{z:.3f}<extra></extra>",
        name="Neurons"
    ))
    
    
    phase_desc = {
        'Ruido': f'☁️ GAS PHASE: Stochastic cloud, max entropy<br>Clusters: {n_clusters}, Mean density: {local_density.mean():.1f}',
        'Memorización': f'💧 LIQUID PHASE: Cluster formation, high entropy<br>Clusters: {n_clusters}, Mean density: {local_density.mean():.1f}',
        'Transición': f'⚡ TRANSITION: Crystallization, entropy decreasing<br>Clusters: {n_clusters}, Mean density: {local_density.mean():.1f}',
        'Grokking': f'💎 SOLID PHASE: Compact crystal, min entropy<br>Clusters: {n_clusters}, Mean density: {local_density.mean():.1f}'
    }
    
    title_text = f"<b>🧠 3D Neural Geometry: {phase_name.upper()}</b><br>"
    title_text += f"<sub>{phase_desc.get(phase_name, '')}</sub><br>"
    title_text += f"<sub>Variance Explained: PC1={pca.explained_variance_ratio_[0]:.1%}, "
    title_text += f"PC2={pca.explained_variance_ratio_[1]:.1%}, PC3={pca.explained_variance_ratio_[2]:.1%}</sub><br>"
    title_text += f"<sub>Spread: {spread:.3f} | Mean Norm: {norms.mean():.3f} | "
    title_text += f"Temp: {thermo_metrics['temperature']:.2f} | Entropy: {thermo_metrics['entropy']:.3f}</sub>"
    
    fig.update_layout(
        template="plotly_dark",
        height=700,
        title=dict(text=title_text, x=0.5, xanchor='center'),
        scene=dict(
            xaxis=dict(title='Principal Component 1', backgroundcolor='rgb(10, 14, 23)',
                      gridcolor='gray', showbackground=True),
            yaxis=dict(title='Principal Component 2', backgroundcolor='rgb(10, 14, 23)',
                      gridcolor='gray', showbackground=True),
            zaxis=dict(title='Principal Component 3', backgroundcolor='rgb(10, 14, 23)',
                      gridcolor='gray', showbackground=True),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.3)),
            aspectmode='cube'
        ),
        paper_bgcolor='rgba(10, 14, 23, 1)',
        plot_bgcolor='rgba(10, 14, 23, 1)'
    )
    
    return fig

def visualize_2d_texture(weights_list, phase_name, thermo_metrics):
    """Complete 2D texture: heatmap, distribution, FFT, histogram"""
    
    weights = weights_list[1] if len(weights_list) > 1 else weights_list[0]
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Weight Heatmap', 'Weight Distribution',
                       'FFT Spectrum', 'Histogram'),
        specs=[[{"type": "heatmap"}, {"type": "scatter"}],
               [{"type": "scatter"}, {"type": "histogram"}]]
    )
    
    
    size = min(128, weights.shape[0])
    fig.add_trace(
        go.Heatmap(
            z=weights[:size, :size],
            colorscale='RdBu_r',
            colorbar=dict(title="Weight", x=0.45, len=0.4, y=0.75),
            zmid=0
        ),
        row=1, col=1
    )
    
    
    W_flat = weights.flatten()
    sample = W_flat[::max(1, len(W_flat)//2000)]
    
    fig.add_trace(
        go.Scatter(
            x=np.arange(len(sample)),
            y=sample,
            mode='markers',
            marker=dict(size=3, color=sample, colorscale='Turbo',
                       colorbar=dict(title="Value", x=1.02, len=0.4, y=0.75)),
            name="Weights"
        ),
        row=1, col=2
    )
    
    
    fft_vals = np.abs(fft.rfft(weights[0]))
    fig.add_trace(
        go.Scatter(
            x=np.arange(len(fft_vals)),
            y=fft_vals,
            mode='lines',
            line=dict(color='cyan', width=2),
            fill='tozeroy',
            name="FFT"
        ),
        row=2, col=1
    )
    
    
    fig.add_trace(
        go.Histogram(
            x=W_flat,
            nbinsx=50,
            marker_color='magenta',
            opacity=0.7,
            name="Distribution"
        ),
        row=2, col=2
    )
    
    stats_text = f"Mean: {W_flat.mean():.4f} | Std: {W_flat.std():.4f} | "
    stats_text += f"Range: [{W_flat.min():.4f}, {W_flat.max():.4f}] | "
    stats_text += f"Temp: {thermo_metrics['temperature']:.2f} | Order: {thermo_metrics['order']:.3f}"
    
    fig.update_layout(
        template="plotly_dark",
        height=600,
        title=f"2D Weight Texture - {phase_name}<br><sub>{stats_text}</sub>",
        showlegend=False
    )
    
    return fig

class CompleteCurriculumWrapper:
    """Wraps app.py training with complete real-time visualization"""
    
    def __init__(self):
        self.DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.phase_snapshots = {}
        self.thermo_history = {}
        self.full_history = {
            'stages': [], 'steps': [],
            'train_acc': [], 'test_acc': [],
            'psi': [], 'lc': []
        }
        
        self.stage_to_phase = {
            0: "Ruido",
            1: "Memorización",
            2: "Transición",
            3: "Grokking"
        }
        
        
        self.base_params = {
            'base_train_size': 300,
            'base_weight_decay': 1.0,
            'base_lr': 1e-3,
            'max_steps_base': 600_000
        }
    
    def calculate_adaptive_params(self, n_bits, d_h, stage):
        """EXACTO app.py: Calcula parámetros adaptativos"""
        train_size = int(self.base_params['base_train_size'] * math.log2(n_bits + 1))
        train_size = min(train_size, 2000)
        
        complexity_factor = (n_bits * d_h) / (10 * 128)
        weight_decay = self.base_params['base_weight_decay'] / (complexity_factor ** 0.5)
        weight_decay = max(weight_decay, 0.01)
        
        max_steps = int(self.base_params['max_steps_base'] * math.log2(complexity_factor + 1))
        max_steps = min(max_steps, 2_000_000)
        
        return {
            'train_size': train_size,
            'weight_decay': weight_decay,
            'max_steps': max_steps,
            'lr': self.base_params['base_lr']
        }
    
    def capture_snapshot(self, model, sae, stage, n_bits, d_h, step, metrics):
        """Capture complete snapshot"""
        phase_name = self.stage_to_phase[stage]
        
        model.eval()
        with torch.no_grad():
            weights_list = [
                model.fc1.weight.detach().cpu().numpy().copy(),
                model.fc2.weight.detach().cpu().numpy().copy(),
                model.out.weight.detach().cpu().numpy().copy()
            ]

        thermo = ThermodynamicAnalyzer.compute_metrics(weights_list, phase_name, step)
        
        self.phase_snapshots[phase_name] = {
            'weights': weights_list,
            'n_bits': n_bits,
            'd_h': d_h,
            'step': step,
            'metrics': metrics,
            'thermo': thermo
        }
        
        self.thermo_history[phase_name] = thermo
        
        st.success(f"✅ {phase_name} captured at step {step}")
        
        return thermo
    
    def smart_weight_transfer(self, prev_model, new_model, stage):
        """EXACTO app.py: Transferencia inteligente de pesos"""
        if prev_model is None:
            return new_model
        
        prev_state = prev_model.state_dict()
        new_state = new_model.state_dict()
        
        for name, new_param in new_state.items():
            if name in prev_state:
                prev_param = prev_state[name]
                
                if prev_param.shape == new_param.shape:
                    new_state[name].copy_(prev_param)
                elif 'weight' in name and len(prev_param.shape) == 2:
                    if new_param.shape[0] > prev_param.shape[0] or new_param.shape[1] > prev_param.shape[1]:
                        padded = torch.zeros_like(new_param)
                        min_rows = min(prev_param.shape[0], new_param.shape[0])
                        min_cols = min(prev_param.shape[1], new_param.shape[1])
                        padded[:min_rows, :min_cols] = prev_param[:min_rows, :min_cols]
                        new_state[name].copy_(padded)
        
        new_model.load_state_dict(new_state)
        return new_model
        
    def train_stage_complete(self, stage, n_bits, d_h, prev_model=None):
        """Train stage with REAL-TIME 3D/2D visualization every 500 steps"""
        
        phase_name = self.stage_to_phase[stage]
        
        
        header_container = st.container()
        metrics_basic = st.container()
        metrics_advanced = st.container()
        phase_container = st.container()
        

        viz_3d_container = st.container()
        viz_2d_container = st.container()
        chart_container = st.container()
        
        with header_container:
            st.markdown(f"### 🚀 Stage {stage+1}: {phase_name}")
            st.markdown(f"**Configuration:** n_bits={n_bits}, d_h={d_h}")
            progress_bar = st.progress(0)
            step_display = st.empty()
        
        with metrics_basic:
            st.markdown("#### 📊 Core Metrics")
            cols = st.columns(6)
            m_train = cols[0].empty()
            m_test = cols[1].empty()
            m_psi = cols[2].empty()
            m_lc = cols[3].empty()
            m_bits = cols[4].empty()
            m_hidden = cols[5].empty()
        
        with metrics_advanced:
            st.markdown("#### 🌡️ Thermodynamic State")
            cols2 = st.columns(5)
            m_temp = cols2[0].empty()
            m_entropy = cols2[1].empty()
            m_order = cols2[2].empty()
            m_energy = cols2[3].empty()
            m_coherence = cols2[4].empty()
        
        with phase_container:
            phase_banner = st.empty()
        
        
        params = self.calculate_adaptive_params(n_bits, d_h, stage)
        
        
        x_full, y_full = app.get_parity_dataset(n_bits=n_bits, k=3, size=10000)
        train_x = x_full[:params['train_size']].to(self.DEVICE)
        train_y = y_full[:params['train_size']].to(self.DEVICE)
        test_x = x_full[params['train_size']:params['train_size']+2000].to(self.DEVICE)
        test_y = y_full[params['train_size']:params['train_size']+2000].to(self.DEVICE)
        
        
        model = app.GrokkingTransformer(d_in=n_bits, d_h=d_h).to(self.DEVICE)
        sae = app.SuperpositionSAE(d_model=d_h, d_sae=d_h * 4).to(self.DEVICE)
        
        if prev_model is not None:
            model = self.smart_weight_transfer(prev_model, model, stage)
        
        
        optimizer = torch.optim.AdamW(model.parameters(), 
                                    lr=params['lr'], 
                                    weight_decay=params['weight_decay'])
        sae_optimizer = torch.optim.AdamW(sae.parameters(), lr=params['lr'])

        stage_history = {'steps': [], 'train_acc': [], 'test_acc': [], 'psi': [], 'lc': []}
        best_test_acc = 0.0
        snapshot_captured = False
        last_thermo = None

        m_bits.metric("Bits", n_bits)
        m_hidden.metric("Hidden", d_h)

        viz_3d_placeholder = None
        viz_2d_placeholder = None
        chart_placeholder = None
        
        
        for step in range(1, params['max_steps'] + 1):
            model.train()
            logits, h_latent = model(train_x)
            loss_cls = F.cross_entropy(logits, train_y)
            
            x_recon, z_sae = sae(h_latent.detach())
            loss_sae = F.mse_loss(x_recon, h_latent.detach()) + 0.01 * z_sae.norm(p=1)
            
            optimizer.zero_grad()
            loss_cls.backward()
            optimizer.step()
            
            sae_optimizer.zero_grad()
            loss_sae.backward()
            sae_optimizer.step()
            
            
            if step % 500 == 0 or step == 1:
                model.eval()
                with torch.no_grad():
                    t_logits, _ = model(test_x)
                    train_acc = (logits.argmax(1) == train_y).float().mean().item()
                    test_acc = (t_logits.argmax(1) == test_y).float().mean().item()
                    
                    psi, _ = sae.get_metrics(z_sae)
                    lc_n = app.ComplexityAnalyzer.measure_lc(model, train_x)
                    lc_val = lc_n.item() if hasattr(lc_n, 'item') else float(lc_n)

                    stage_history['steps'].append(step)
                    stage_history['train_acc'].append(train_acc)
                    stage_history['test_acc'].append(test_acc)
                    stage_history['psi'].append(psi)
                    stage_history['lc'].append(lc_val)
                    
                    
                    weights_list = [
                        model.fc1.weight.detach().cpu().numpy().copy(),
                        model.fc2.weight.detach().cpu().numpy().copy(),
                        model.out.weight.detach().cpu().numpy().copy()
                    ]
                    last_thermo = ThermodynamicAnalyzer.compute_metrics(
                        weights_list, phase_name, step
                    )
                    
                    
                    with header_container:
                        progress_bar.progress(min(step / params['max_steps'], 1.0))
                        step_display.markdown(f"**Step: {step:,} / {params['max_steps']:,}**")
                    
                    m_train.metric("Train", f"{train_acc:.2%}")
                    m_test.metric("Test", f"{test_acc:.2%}")
                    m_psi.metric("ψ", f"{psi:.3f}")
                    m_lc.metric("LC", f"{lc_val:.1f}")

                    m_temp.metric("Temp", f"{last_thermo['temperature']:.2f}")
                    m_entropy.metric("Entropy", f"{last_thermo['entropy']:.3f}")
                    m_order.metric("Order", f"{last_thermo['order']:.3f}")
                    m_energy.metric("Energy", f"{last_thermo['energy']:.1f}")
                    m_coherence.metric("Coherence", f"{last_thermo['coherence']:.3f}")
                    
                    
                    if step % 2000 == 0 or step == 1:
                        
   
                        with viz_3d_container:
                            st.markdown(f"#### 🧠 3D Neural Geometry - Step {step:,}")
                            if viz_3d_placeholder is None:
                                viz_3d_placeholder = st.empty()
                            
                            fig_3d = visualize_3d_geometry(weights_list, phase_name, last_thermo)
                            viz_3d_placeholder.plotly_chart(fig_3d, use_container_width=True, key=f"3d_{stage}_{step}")
                        
                        # GRÁFICO 2D - TEXTURA DE PESOS
                        with viz_2d_container:
                            st.markdown(f"#### 📉 2D Weight Texture - Step {step:,}")
                            if viz_2d_placeholder is None:
                                viz_2d_placeholder = st.empty()
                            
                            fig_2d = visualize_2d_texture(weights_list, phase_name, last_thermo)
                            viz_2d_placeholder.plotly_chart(fig_2d, use_container_width=True, key=f"2d_{stage}_{step}")
                    
                    
                    if step % 1000 == 0 or step == 1:
                        with chart_container:
                            if chart_placeholder is None:
                                st.markdown("#### 📈 Training Metrics")
                                chart_placeholder = st.empty()
                            
                            fig = make_subplots(
                                rows=2, cols=2,
                                subplot_titles=('Accuracy', 'Superposition ψ', 'LC', 'Test vs LC'),
                                vertical_spacing=0.12,
                                horizontal_spacing=0.1
                            )
                            
                            # Accuracy
                            fig.add_trace(go.Scatter(
                                x=stage_history['steps'],
                                y=stage_history['train_acc'],
                                mode='lines',
                                name='Train',
                                line=dict(color='#ff6b6b', width=2)
                            ), row=1, col=1)
                            
                            fig.add_trace(go.Scatter(
                                x=stage_history['steps'],
                                y=stage_history['test_acc'],
                                mode='lines',
                                name='Test',
                                line=dict(color='#4ecdc4', width=2)
                            ), row=1, col=1)
                            
                            # Superposition
                            fig.add_trace(go.Scatter(
                                x=stage_history['steps'],
                                y=stage_history['psi'],
                                mode='lines',
                                name='ψ',
                                line=dict(color='cyan', width=2),
                                fill='tozeroy'
                            ), row=1, col=2)
                            
                            # LC
                            fig.add_trace(go.Scatter(
                                x=stage_history['steps'],
                                y=stage_history['lc'],
                                mode='lines',
                                name='LC',
                                line=dict(color='magenta', width=2)
                            ), row=2, col=1)
                            
                            # Test vs LC
                            fig.add_trace(go.Scatter(
                                x=stage_history['lc'],
                                y=stage_history['test_acc'],
                                mode='markers',
                                marker=dict(size=6, color=stage_history['steps'], 
                                        colorscale='Viridis', showscale=True,
                                        colorbar=dict(title="Step", x=1.15)),
                                showlegend=False
                            ), row=2, col=2)
                            
                            fig.update_layout(
                                template="plotly_dark",
                                height=600,
                                showlegend=True,
                                title_text=f"Real-Time Training: {phase_name}"
                            )
                            
                            fig.update_yaxes(range=[0, 1.1], row=1, col=1)
                            fig.update_yaxes(range=[0, 1.1], row=1, col=2)
                            
                            chart_placeholder.plotly_chart(fig, use_container_width=True, key=f"chart_{stage}_{step}")
                    
                    
                    if test_acc > best_test_acc:
                        best_test_acc = test_acc
                    
                    
                    if test_acc > 0.95 and not snapshot_captured:
                        metrics_dict = {
                            'train_acc': train_acc,
                            'test_acc': test_acc,
                            'psi': psi,
                            'lc': lc_val
                        }
                        self.capture_snapshot(model, sae, stage, n_bits, d_h, step, metrics_dict)
                        snapshot_captured = True
                        
                        colors = {
                            'Ruido': 'phase-gas',
                            'Memorización': 'phase-liquid',
                            'Transición': 'phase-transition',
                            'Grokking': 'phase-solid'
                        }
                        
                        with phase_container:
                            phase_banner.markdown(f"""
                                <div class='{colors[phase_name]}'>
                                <h3>✨ {phase_name.upper()} PHASE CAPTURED!</h3>
                                </div>
                            """, unsafe_allow_html=True)
                    
                    
                    if test_acc > 0.98:
                        if not snapshot_captured:
                            metrics_dict = {
                                'train_acc': train_acc,
                                'test_acc': test_acc,
                                'psi': psi,
                                'lc': lc_val
                            }
                            self.capture_snapshot(model, sae, stage, n_bits, d_h, step, metrics_dict)
                        
                        st.balloons()
                        with phase_container:
                            phase_banner.success(f"🎯 GROKKING ACHIEVED at step {step}!")
                        
                        return model, sae, True, stage_history

        if best_test_acc > 0.7:
            if not snapshot_captured:
                metrics_dict = {
                    'train_acc': train_acc,
                    'test_acc': best_test_acc,
                    'psi': psi,
                    'lc': lc_val
                }
                self.capture_snapshot(model, sae, stage, n_bits, d_h, step, metrics_dict)
            return model, sae, True, stage_history
        else:
            return None, None, False, stage_history

            
    def run_full_curriculum(self):
        """Execute complete curriculum - EXACTO app.py"""
        curriculum = [
            (10, 128),
            (24, 256),
            (32, 512),
            (64, 1024)
        ]
        
        st.markdown("## 🔄 Complete Adaptive Curriculum")
        st.markdown("---")
        
        prev_model = None
        
        for stage, (n_bits, d_h) in enumerate(curriculum):
            model, sae, success, stage_history = self.train_stage_complete(
                stage, n_bits, d_h, prev_model
            )
            
            if not success:
                st.error(f"🛑 Curriculum stopped at stage {stage+1}")
                break
            
            prev_model = model
            
            # Save to global history
            for i in range(len(stage_history['steps'])):
                self.full_history['stages'].append(stage)
                self.full_history['steps'].append(stage_history['steps'][i])
                self.full_history['train_acc'].append(stage_history['train_acc'][i])
                self.full_history['test_acc'].append(stage_history['test_acc'][i])
                self.full_history['psi'].append(stage_history['psi'][i])
                self.full_history['lc'].append(stage_history['lc'][i])
            
            st.markdown("---")
        
        if len(self.phase_snapshots) == 4:
            st.balloons()
            st.success("✅ COMPLETE CURRICULUM! All phases captured")
        
        return True

def main():
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #0f2042, #1e3a5f); 
    border-radius: 20px; margin-bottom: 30px;'>
    <h1 style='font-size: 3em;'>🔬 COMPLETE GROKKING ANALYZER</h1>
    <h2 style='font-size: 1.5em; color: #bbdefb;'>Real-Time Phase Transitions + Full Geometry</h2>
    <p style='font-size: 1.1em;'>Gas ☁️ → Liquid 💧 → Transition ⚡ → Crystal 💎</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        st.header("🎛️ Control")
        st.markdown("---")
        
        if st.button("🚀 START TRAINING", type="primary", use_container_width=True):
            st.session_state['start_training'] = True
        
        if st.button("🔄 RESET", use_container_width=True):
            st.session_state.clear()
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        ### 📚 Curriculum
        1. **Ruido** (10 bits, 128h)
        2. **Memorización** (24 bits, 256h)
        3. **Transición** (32 bits, 512h)
        4. **Grokking** (64 bits, 1024h)
        """)
    
    if 'start_training' in st.session_state and st.session_state['start_training']:
        if 'wrapper' not in st.session_state:
            wrapper = CompleteCurriculumWrapper()
            success = wrapper.run_full_curriculum()
            
            if success:
                st.session_state['wrapper'] = wrapper
                st.session_state['curriculum_complete'] = True
                st.session_state['start_training'] = False
        else:
            wrapper = st.session_state['wrapper']
    
    if 'curriculum_complete' in st.session_state and st.session_state['curriculum_complete']:
        wrapper = st.session_state['wrapper']
        
        st.markdown("---")
        st.markdown("## 🎨 Explore Captured Phases")
        
        tabs = st.tabs([
            "🌡️ Thermal Engine",
            "🧠 3D Geometry",
            "📉 2D Texture",
            "📈 Full Metrics"
        ])
        
        with tabs[0]:
            st.subheader("Thermodynamic Phase Diagram")
            if wrapper.thermo_history:
                fig = ThermodynamicAnalyzer.visualize_thermal_engine(wrapper.thermo_history)
                st.plotly_chart(fig, use_container_width=True)
            
            for phase, data in wrapper.phase_snapshots.items():
                with st.expander(f"{phase} Phase - Step {data['step']:,}"):
                    col1, col2, col3, col4, col5 = st.columns(5)
                    thermo = data['thermo']
                    col1.metric("Temperature", f"{thermo['temperature']:.2f}")
                    col2.metric("Entropy", f"{thermo['entropy']:.3f}")
                    col3.metric("Order", f"{thermo['order']:.3f}")
                    col4.metric("Energy", f"{thermo['energy']:.1f}")
                    col5.metric("Coherence", f"{thermo['coherence']:.3f}")
        
        with tabs[1]:
            st.subheader("🧠 3D Weight Space Geometry")
            st.markdown("### 🎯 SELECT PHASE TO VISUALIZE:")
            
            available_phases = list(wrapper.phase_snapshots.keys())
            
            phase_colors = {
                'Ruido': '🔴 GAS (Stochastic Cloud)',
                'Memorización': '🟠 LIQUID (Cluster Formation)', 
                'Transición': '🟡 TRANSITION (Crystallizing)',
                'Grokking': '🟢 SOLID (Geometric Crystal)'
            }
            
            col1, col2 = st.columns([1, 3])
            
            with col1:
                selected_phase = st.radio(
                    "Phase:",
                    available_phases,
                    format_func=lambda x: phase_colors.get(x, x),
                    key="phase_selector_3d"
                )
            
            with col2:
                if selected_phase:
                    data = wrapper.phase_snapshots[selected_phase]
                    thermo = data['thermo']
                    
                    st.markdown(f"""
                    **Phase: {selected_phase}** | **Step: {data['step']:,}** | **Bits: {data['n_bits']}** | **Hidden: {data['d_h']}**
                    
                    **Thermodynamics:**
                    - 🌡️ Temperature: `{thermo['temperature']:.2f}` 
                    - 📊 Entropy: `{thermo['entropy']:.3f}` 
                    - 💎 Order: `{thermo['order']:.3f}` 
                    - ⚡ Energy: `{thermo['energy']:.1f}`
                    - 🔗 Coherence: `{thermo['coherence']:.3f}`
                    - 📍 Density: `{thermo['local_density']:.2f}`
                    - 🌀 Fractal Dim: `{thermo['fractal_dim']:.2f}`
                    """)
            
            st.markdown("---")
            
            if selected_phase:
                weights = wrapper.phase_snapshots[selected_phase]['weights']
                thermo = wrapper.phase_snapshots[selected_phase]['thermo']
                fig_3d = visualize_3d_geometry(weights, selected_phase, thermo)
                st.plotly_chart(fig_3d, use_container_width=True)
                
                phase_interpretations = {
                    'Ruido': '☁️ Random scattered points (high temperature, no structure)',
                    'Memorización': '💧 Clustering begins but unstable (medium temperature)',
                    'Transición': '⚡ Clear structure emerging (temperature dropping)',
                    'Grokking': '💎 Tight crystalline structure (minimum temperature, maximum order)'
                }
                
                st.info(f"""
                **Interpretation for {selected_phase} Phase:**
                
                {phase_interpretations.get(selected_phase, '')}
                """)
        
        with tabs[2]:
            st.subheader("📉 2D Weight Texture - Geometric Patterns")
            
            st.markdown("### 🎯 SELECT PHASE:")
            
            selected_phase_2d = st.selectbox(
                "Phase:",
                available_phases,
                format_func=lambda x: phase_colors.get(x, x),
                key="phase_selector_2d"
            )
            
            if selected_phase_2d:
                weights = wrapper.phase_snapshots[selected_phase_2d]['weights']
                thermo = wrapper.phase_snapshots[selected_phase_2d]['thermo']
                fig_2d = visualize_2d_texture(weights, selected_phase_2d, thermo)
                st.plotly_chart(fig_2d, use_container_width=True)
        
        with tabs[3]:
            st.subheader("📈 Complete Training History - All Stages")
            
            fig_full = make_subplots(
                rows=3, cols=2,
                subplot_titles=('Accuracy Evolution (All Stages)',
                              'Superposition ψ',
                              'Linear Complexity LC',
                              'Test Acc vs LC',
                              'Train vs Test Comparison',
                              'Stage Performance'),
                vertical_spacing=0.1,
                horizontal_spacing=0.1
            )
            
            stage_colors = {0: 'red', 1: 'orange', 2: 'yellow', 3: 'lime'}
            
            stages = wrapper.full_history['stages']
            steps = wrapper.full_history['steps']
            train_acc = wrapper.full_history['train_acc']
            test_acc = wrapper.full_history['test_acc']
            psi = wrapper.full_history['psi']
            lc = wrapper.full_history['lc']

            for stage_num in set(stages):
                idxs = [i for i, s in enumerate(stages) if s == stage_num]
                stage_steps = [steps[i] for i in idxs]
                stage_train = [train_acc[i] for i in idxs]
                stage_test = [test_acc[i] for i in idxs]
                stage_psi = [psi[i] for i in idxs]
                stage_lc = [lc[i] for i in idxs]
                
                fig_full.add_trace(go.Scatter(
                    x=stage_steps, y=stage_train,
                    mode='lines',
                    name=f'S{stage_num+1} Train',
                    line=dict(color=stage_colors[stage_num], width=2, dash='dot')
                ), row=1, col=1)
                
                fig_full.add_trace(go.Scatter(
                    x=stage_steps, y=stage_test,
                    mode='lines',
                    name=f'S{stage_num+1} Test',
                    line=dict(color=stage_colors[stage_num], width=2)
                ), row=1, col=1)
                
                # ψ
                fig_full.add_trace(go.Scatter(
                    x=stage_steps, y=stage_psi,
                    mode='lines',
                    name=f'Stage {stage_num+1}',
                    line=dict(color=stage_colors[stage_num], width=2)
                ), row=1, col=2)
                
                # LC
                fig_full.add_trace(go.Scatter(
                    x=stage_steps, y=stage_lc,
                    mode='lines',
                    name=f'Stage {stage_num+1}',
                    line=dict(color=stage_colors[stage_num], width=2)
                ), row=2, col=1)
                
                # LC vs Acc
                fig_full.add_trace(go.Scatter(
                    x=stage_lc, y=stage_test,
                    mode='markers',
                    marker=dict(size=4, color=stage_colors[stage_num]),
                    name=f'Stage {stage_num+1}',
                    showlegend=False
                ), row=2, col=2)
            

            fig_full.add_trace(go.Scatter(
                x=steps, y=train_acc,
                mode='lines',
                line=dict(color='#ff6b6b', width=1),
                name='All Train'
            ), row=3, col=1)
            
            fig_full.add_trace(go.Scatter(
                x=steps, y=test_acc,
                mode='lines',
                line=dict(color='#4ecdc4', width=1),
                name='All Test'
            ), row=3, col=1)
            
            stage_names = ['Ruido', 'Memorización', 'Transición', 'Grokking']
            max_accs = []
            for stage_num in sorted(set(stages)):
                stage_test_accs = [test_acc[i] for i, s in enumerate(stages) if s == stage_num]
                max_accs.append(max(stage_test_accs) if stage_test_accs else 0)
            
            fig_full.add_trace(go.Bar(
                x=stage_names[:len(max_accs)],
                y=max_accs,
                marker_color=[stage_colors[i] for i in range(len(max_accs))],
                name='Max Test Acc'
            ), row=3, col=2)
            
            fig_full.update_yaxes(range=[0, 1.1], row=1, col=1)
            fig_full.update_yaxes(range=[0, 1.1], row=1, col=2)
            fig_full.update_yaxes(range=[0, 1.1], row=3, col=1)
            
            fig_full.update_layout(
                template="plotly_dark",
                height=900,
                showlegend=True,
                title_text="Complete Training History - All Stages"
            )
            
            st.plotly_chart(fig_full, use_container_width=True)
            
            st.markdown("### 📊 Summary Statistics")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Steps", f"{max(steps):,}")
            col2.metric("Stages Completed", len(wrapper.phase_snapshots))
            col3.metric("Final Test Acc", f"{test_acc[-1]:.2%}")
            col4.metric("Max Test Acc", f"{max(test_acc):.2%}")
            
            st.markdown("### 🎯 Phase Snapshots Summary")
            for phase in available_phases:
                if phase in wrapper.phase_snapshots:
                    data = wrapper.phase_snapshots[phase]
                    metrics = data['metrics']
                    thermo = data['thermo']
                    
                    with st.expander(f"{phase} - Step {data['step']:,}"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown(f"""
                            **Model Configuration:**
                            - Bits: {data['n_bits']}
                            - Hidden: {data['d_h']}
                            - Step: {data['step']:,}
                            
                            **Performance:**
                            - Train Acc: {metrics['train_acc']:.2%}
                            - Test Acc: {metrics['test_acc']:.2%}
                            - ψ (Superposition): {metrics['psi']:.3f}
                            - LC (Complexity): {metrics['lc']:.1f}
                            """)
                        
                        with col2:
                            st.markdown(f"""
                            **Thermodynamics:**
                            - Temperature: {thermo['temperature']:.2f}
                            - Entropy: {thermo['entropy']:.3f}
                            - Order: {thermo['order']:.3f}
                            - Energy: {thermo['energy']:.1f}
                            - Coherence: {thermo['coherence']:.3f}
                            - Local Density: {thermo['local_density']:.2f}
                            - Fractal Dimension: {thermo['fractal_dim']:.2f}
                            """)
    
    else:
        st.info("👈 Press 'START TRAINING' to begin full curriculum with real-time visualization")

        st.markdown("---")
        st.header("📚 About This System")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### The Grokking Phenomenon
            
            **Grokking** is the sudden transition from memorization to generalization
            that occurs long after achieving zero training loss.
            
            **Key Characteristics:**
            - Delayed generalization
            - Sudden phase transition
            - Algorithm crystallization
            - Network weight reorganization
            
            **Physics Metaphor:**
            The network undergoes phase transitions analogous to
            gas → liquid → solid crystallization.
            """)
        
        with col2:
            st.markdown("""
            ### What This Tool Does
            
            This visualizer:
            
            1. **Imports your app.py** without modifications
            2. **Trains 4-stage curriculum** (10→24→32→64 bits)
            3. **Captures phase transitions** with weight snapshots
            4. **Analyzes thermodynamics** (temperature, entropy, order)
            5. **Visualizes geometry** in 3D (PCA) and 2D (texture)
            6. **Tracks metrics** (accuracy, ψ, LC)
            7. **Shows real-time progress** during training
            
            All training parameters are **identical to app.py** to preserve grokking.
            """)

if __name__ == "__main__":
    main()
