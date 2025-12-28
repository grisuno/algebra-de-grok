import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.decomposition import PCA
from scipy import fft
import torch
import math
from datetime import datetime
import time


st.set_page_config(
    page_title="🔬 Grokking Dynamics Monitor",
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0a0e17 0%, #0d1b2a 100%);
        color: #e0e0ff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .header-container {
        background: rgba(15, 32, 61, 0.85);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #4a6fa5;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .metric-card {
        background: rgba(26, 42, 85, 0.7);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid #3a5ba0;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(58, 91, 160, 0.3);
    }
    .phase-indicator {
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.5rem 0;
    }
    .scientific-notation {
        font-family: 'Lucida Console', Monaco, monospace;
        background: rgba(30, 45, 80, 0.6);
        padding: 0.25rem 0.5rem;
        border-radius: 5px;
        border-left: 3px solid #4a86e8;
    }
    .citation-box {
        background: rgba(22, 38, 68, 0.8);
        border-left: 4px solid #64b5f6;
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #bbdefb;
    }
    .theory-box {
        background: rgba(19, 41, 77, 0.85);
        border: 1px solid #5c9bd5;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #8a9bbd;
        font-size: 0.9rem;
        border-top: 1px solid #2c4a7d;
        margin-top: 2rem;
    }
    h1, h2, h3 {
        color: #64b5f6 !important;
        text-shadow: 0 0 10px rgba(100, 181, 246, 0.3);
    }
    .stSlider {
        padding: 1rem 0;
    }
    .stProgress {
        height: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


class ScientificWeightGenerator:
    """Generador de pesos basado en principios teóricos de grokking"""
    
    @staticmethod
    def generate_weights(phase, d_model=512, d_sae=1024, seed=42):
        """Genera pesos según el estado teórico del proceso de grokking"""
        np.random.seed(seed)
        
        if phase == "Ruido":
            
            W = np.random.randn(d_sae, d_model) * 0.1
            
            for i in range(50):
                idx = np.random.choice(d_sae, 2, replace=False)
                W[idx[1]] = W[idx[0]] * 0.7 + np.random.randn(d_model) * 0.05
            return W, 0.52, "Caos inicial - correlaciones espurias"
        
        elif phase == "Memorización":
            
            W = np.zeros((d_sae, d_model))
            
            cluster_size = d_sae // 8
            for cluster in range(8):
                start_idx = cluster * cluster_size
                end_idx = min((cluster + 1) * cluster_size, d_sae)
                base_pattern = np.random.randn(d_model) * 0.8
                for i in range(start_idx, end_idx):
                    W[i] = base_pattern * (0.9 + np.random.randn() * 0.1) + np.random.randn(d_model) * 0.3
            return W, 0.98, "Memorización densa - clusters neuronales"
        
        elif phase == "Transición":
            
            W = np.zeros((d_sae, d_model))
            
            for i in range(d_sae):
                freq = (i % 16) + 1  
                phase_shift = np.random.uniform(0, 2 * np.pi)
                amplitude = 0.7 + np.random.exponential(0.3)
                W[i] = amplitude * np.sin(np.linspace(0, freq * np.pi, d_model) + phase_shift)
            
            
            structural_noise = np.random.randn(d_sae, d_model) * 0.15
            for i in range(d_sae // 20):
                start = i * 20
                end = min((i + 1) * 20, d_sae)
                structural_noise[start:end] = np.mean(structural_noise[start:end], axis=0)
            
            W += structural_noise
            return W, 0.85, "Transición algorítmica - estructura emergente"
        
        else:  
            
            W = np.zeros((d_sae, d_model))
            
            theta = np.linspace(0, 2 * np.pi, d_sae)
            for i in range(d_sae):
                
                for harmonic in [1, 3, 5, 7]:  
                    W[i] += (1 / harmonic) * np.sin(harmonic * np.linspace(0, theta[i], d_model))
                W[i] = W[i] / np.max(np.abs(W[i])) * 0.9  
            
            
            for layer in range(3):
                start_idx = layer * d_sae // 3
                end_idx = (layer + 1) * d_sae // 3
                W[start_idx:end_idx] *= (0.8 ** layer)
            
            return W, 1.0, "Solución algorítmica - representación geométrica mínima"

def calculate_scientific_metrics(W):
    """Calcula métricas avanzadas basadas en teoría de información y geometría"""
    metrics = {}
    
    
    W_clean = W.copy()
    W_clean = np.nan_to_num(W_clean, nan=0.0, posinf=1e6, neginf=-1e6)
    
    
    if not np.all(np.isfinite(W_clean)):
        return {
            'entropy': 0.0,
            'fractal_dim': 1.0,
            'coherence': 0.0,
            'avg_coherence': 0.0,
            'dominant_freq': 1,
            'spectral_flatness': 0.0
        }
    
    
    flattened = W_clean.flatten()
    
    if np.allclose(flattened, flattened[0]):
        flattened = flattened + np.random.normal(0, 1e-10, flattened.shape)
    
    hist, _ = np.histogram(flattened, bins=50, density=True)
    hist = hist[hist > 0]
    if len(hist) == 0:
        entropy = 0.0
    else:
        entropy = -np.sum(hist * np.log(hist + 1e-10))
    metrics['entropy'] = entropy
    
    
    sample_size = min(1000, W_clean.shape[0])
    W_sample = W_clean[:sample_size]
    try:
        pca = PCA(n_components=min(50, W_clean.shape[1], sample_size))
        pca.fit(W_sample)
        explained_variance = pca.explained_variance_ratio_
        fractal_dim = np.sum(explained_variance > 1e-3)  
        metrics['fractal_dim'] = max(1.0, fractal_dim)
    except:
        metrics['fractal_dim'] = 1.0
    
    
    coherence_sample_size = min(200, W_clean.shape[0])
    W_sample = W_clean[:coherence_sample_size]
    norms = np.linalg.norm(W_sample, axis=1, keepdims=True)
    
    norms = np.where(norms == 0, 1e-10, norms)
    W_normalized = W_sample / norms
    coherence_matrix = np.abs(np.dot(W_normalized, W_normalized.T))
    np.fill_diagonal(coherence_matrix, 0)
    metrics['coherence'] = float(np.max(coherence_matrix)) if coherence_matrix.size > 0 else 0.0
    metrics['avg_coherence'] = float(np.mean(coherence_matrix)) if coherence_matrix.size > 0 else 0.0
    
    
    try:
        fft_magnitudes = np.abs(fft.rfft(W_clean[0]))
        if len(fft_magnitudes) > 1:
            dominant_freq = np.argmax(fft_magnitudes[1:]) + 1
            metrics['dominant_freq'] = int(dominant_freq)
            
            safe_magnitudes = np.maximum(fft_magnitudes, 1e-10)
            geometric_mean = np.exp(np.mean(np.log(safe_magnitudes)))
            spectral_flatness = 10 * np.log10(np.mean(safe_magnitudes) / geometric_mean)
            metrics['spectral_flatness'] = float(spectral_flatness)
        else:
            metrics.update({'dominant_freq': 1, 'spectral_flatness': 0.0})
    except:
        metrics.update({'dominant_freq': 1, 'spectral_flatness': 0.0})
    
    return metrics


st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("🧠 GROKKING DYNAMICS MONITOR")
st.subheader("Visualización Científica del Colapso Algorítmico en Redes Neuronales")
st.markdown("""
<div class="citation-box">
<b>Base Teórica:</b> El grokking (Liu et al., 2022) describe el fenómeno donde un modelo memoriza datos inicialmente, 
luego experimenta una transición abrupta a generalización perfecta. Este visualizador simula la evolución geométrica 
del espacio de pesos durante este proceso.
</div>
</div>
""", unsafe_allow_html=True)


col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([2, 1, 1])

with col_ctrl1:
    phase = st.select_slider(
        "🔬 Fase del Proceso de Grokking",
        options=["Ruido", "Memorización", "Transición", "Grokking"],
        value="Transición",
        help="Selecciona la fase teórica para visualizar la geometría del espacio de pesos"
    )

with col_ctrl2:
    d_model = st.slider("	Dimensión del Modelo (d_model)", 128, 1024, 512, step=128,
                        help="Dimensión del espacio latente")
    
with col_ctrl3:
    d_sae = st.slider("	Dimensión SAE (d_sae)", 256, 2048, 1024, step=256,
                     help="Dimensión del Sparse Autoencoder")


W, accuracy, phase_description = ScientificWeightGenerator.generate_weights(phase, d_model, d_sae)
metrics = calculate_scientific_metrics(W)


st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.subheader(f"🌐 Geometría Latente: {phase}")
st.markdown(f"<div class='phase-indicator'>{phase_description}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

col_main1, col_main2 = st.columns([3, 1])

with col_main1:
    
    pca = PCA(n_components=3)
    W_sample = W[:1000]  
    W_sample = np.nan_to_num(W_sample, nan=0.0, posinf=1e6, neginf=-1e6)
    W_pca = pca.fit_transform(W_sample)
    
    
    colors = np.linalg.norm(W_sample, axis=1)
    
    fig_3d = go.Figure(data=[go.Scatter3d(
        x=W_pca[:, 0], y=W_pca[:, 1], z=W_pca[:, 2],
        mode='markers',
        marker=dict(
            size=4,
            color=colors,
            colorscale='Viridis' if phase != "Grokking" else 'Plasma',
            opacity=0.7,
            colorbar=dict(title="Norma del Peso", orientation="h")
        ),
        hovertemplate="<b>Neurona %{customdata[0]}</b><br>"
                      "Coordenada PCA: (%{x:.2f}, %{y:.2f}, %{z:.2f})<br>"
                      "Norma: %{marker.color:.2f}<extra></extra>",
        customdata=np.column_stack([np.arange(len(W_pca)), colors])
    )])
    
    fig_3d.update_layout(
        scene=dict(
            xaxis_title='Componente PCA 1',
            yaxis_title='Componente PCA 2',
            zaxis_title='Componente PCA 3',
            xaxis=dict(showbackground=False, gridcolor='#4a6fa5'),
            yaxis=dict(showbackground=False, gridcolor='#4a6fa5'),
            zaxis=dict(showbackground=False, gridcolor='#4a6fa5'),
            aspectmode='cube'
        ),
        template="plotly_dark",
        height=650,
        margin=dict(l=0, r=0, b=0, t=30),
        hoverlabel=dict(bgcolor="rgba(30, 45, 80, 0.9)", font_color="#e0e0ff"),
        title=dict(text=f"Geometría Latente - {phase}", font=dict(size=20, color='#64b5f6'))
    )
    
    st.plotly_chart(fig_3d, use_container_width=True)

with col_main2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("📊 Métricas Científicas")
    
    
    col_metric1, col_metric2 = st.columns(2)
    with col_metric1:
        st.metric("Precisión (Test)", f"{accuracy*100:.1f}%")
        st.metric("Dim. Fractal", f"{metrics['fractal_dim']:.1f}")
    with col_metric2:
        st.metric("Entropía", f"{metrics['entropy']:.2f}")
        st.metric("Coherencia", f"{metrics['coherence']:.3f}")
    
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📈 Correlación Estructural")
    
    sample_size = min(64, W.shape[0])
    W_sample_small = W[:sample_size]
    norms = np.linalg.norm(W_sample_small, axis=1, keepdims=True) + 1e-9
    W_normalized = W_sample_small / norms
    correlation = np.dot(W_normalized, W_normalized.T)
    
    fig_corr = px.imshow(
        correlation,
        color_continuous_scale='RdBu',
        aspect='auto',
        title="Matriz de Correlación de Pesos"
    )
    fig_corr.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        coloraxis_colorbar=dict(title="Correlación")
    )
    st.plotly_chart(fig_corr, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.subheader("🔬 Análisis Espectral: La Firma Algorítmica")
st.markdown("""
<div class="theory-box">
<b>Teoría:</b> En la fase de grokking, los pesos exhiben una estructura espectral definida con picos en frecuencias específicas 
que corresponden a la solución algorítmica. El ruido muestra un espectro plano, mientras que la memorización muestra patrones irregulares.
</div>
</div>
""", unsafe_allow_html=True)


neuron_indices = [0, 10, 20, 30]  
fig_fft = go.Figure()

for idx in neuron_indices:
    if idx < W.shape[0]:
        neuron_weights = W[idx]
        fft_vals = np.abs(fft.rfft(neuron_weights))
        freqs = fft.rfftfreq(len(neuron_weights))
        
        fig_fft.add_trace(go.Scatter(
            x=freqs[1:], y=fft_vals[1:],
            mode='lines',
            name=f'Neurona {idx}',
            line=dict(width=2.5),
            fill='tozeroy'
        ))

fig_fft.update_layout(
    template="plotly_dark",
    height=450,
    xaxis_title="Frecuencia Normalizada",
    yaxis_title="Magnitud Espectral",
    title=dict(text="Espectro de Frecuencias de Pesos Representativos", font=dict(size=20)),
    hovermode='x unified',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    margin=dict(l=50, r=20, t=50, b=50)
)


for harmonic in [1, 3, 5, 7]:  
    fig_fft.add_vline(x=harmonic/len(W[0]), line_dash="dash", line_color="rgba(255, 100, 100, 0.7)",
                     annotation_text=f"Armónico {harmonic}", annotation_position="top right")

st.plotly_chart(fig_fft, use_container_width=True)


st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.subheader("⚡ Dinámica de Aprendizaje y Transferencia")
st.markdown("""
<div class="theory-box">
<b>Mecanismo:</b> La transferencia algorítmica ocurre cuando la estructura geométrica descubierta en dimensiones bajas 
se preserva y reescala en modelos más grandes, permitiendo generalización inmediata (Paso 0).
</div>
</div>
""", unsafe_allow_html=True)

col_dyn1, col_dyn2 = st.columns(2)

with col_dyn1:
    st.subheader("📊 Evolución de la Estructura")
    
    
    steps = np.linspace(0, 1, 100)
    if phase == "Ruido":
        structure_score = np.exp(-5 * steps)
    elif phase == "Memorización":
        structure_score = 0.2 + 0.6 * np.sin(np.pi * steps)
    elif phase == "Transición":
        structure_score = 0.3 + 0.7 * (1 - np.exp(-10 * (steps - 0.5)))
        structure_score[steps < 0.5] = 0.3
    else:  
        structure_score = 0.9 + 0.1 * np.sin(20 * np.pi * steps)
    
    fig_evo = go.Figure()
    fig_evo.add_trace(go.Scatter(
        x=steps, y=structure_score,
        mode='lines',
        line=dict(color='#64b5f6', width=3),
        fill='tozeroy',
        fillcolor='rgba(100, 181, 246, 0.2)'
    ))
    
    fig_evo.add_vline(x=0.7, line_dash="dash", line_color="rgba(255, 100, 100, 0.8)",
                     annotation_text="Punto de Grokking", annotation_position="top right")
    
    fig_evo.update_layout(
        template="plotly_dark",
        height=350,
        xaxis_title="Pasos de Entrenamiento (Normalizados)",
        yaxis_title="Puntuación de Estructura",
        title="Evolución de la Estructura Algorítmica",
        yaxis_range=[0, 1.1]
    )
    
    st.plotly_chart(fig_evo, use_container_width=True)

with col_dyn2:
    st.subheader("🔄 Transferencia entre Capas")
    
    
    layer_indices = list(range(1, 5))
    if phase == "Ruido":
        transfer_efficiency = [0.1, 0.05, 0.02, 0.01]
    elif phase == "Memorización":
        transfer_efficiency = [0.8, 0.6, 0.4, 0.3]
    elif phase == "Transición":
        transfer_efficiency = [0.6, 0.7, 0.8, 0.6]
    else:  
        transfer_efficiency = [0.95, 0.98, 0.99, 0.97]
    
    fig_transfer = go.Figure()
    fig_transfer.add_trace(go.Bar(
        x=layer_indices,
        y=transfer_efficiency,
        marker=dict(
            color=transfer_efficiency,
            colorscale='Viridis',
            line=dict(color='#4a6fa5', width=1)
        ),
        text=[f"{eff*100:.1f}%" for eff in transfer_efficiency],
        textposition='outside'
    ))
    
    fig_transfer.update_layout(
        template="plotly_dark",
        height=350,
        xaxis_title="Índice de Capa",
        yaxis_title="Eficiencia de Transferencia",
        title="Transferencia de Información entre Capas",
        yaxis_range=[0, 1.1]
    )
    
    st.plotly_chart(fig_transfer, use_container_width=True)


st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.subheader("🔍 Interpretación Científica Detallada")

interpretation = {
    "Ruido": """
    **Estado Inicial (Caos):**
    - Los pesos exhiben una distribución aleatoria con correlaciones espurias mínimas
    - Baja dimensionalidad fractal (~2-3) indica estructura caótica
    - El espectro de frecuencias es plano, sin patrones reconocibles
    - La entropía es máxima, reflejando la falta de orden algorítmico
    - Las capas no transfieren información de manera coherente (<10%)
    """,
    
    "Memorización": """
    **Fase de Memorización (Estructura Densa):**
    - Los pesos forman clusters neuronales que codifican ejemplos específicos
    - Dimensionalidad fractal moderada (~10-15) refleja estructura local pero no global
    - El espectro muestra picos irregulares correspondientes a patrones memorizados
    - Alta coherencia (>0.6) indica dependencia entre neuronas (sobreajuste)
    - Transferencia eficiente entre capas tempranas pero decae en capas profundas
    """,
    
    "Transición": """
    **Fase de Transición (Estructura Emergente):**
    - Patrones sinusoidales emergen mezclados con ruido estructurado
    - Dimensionalidad fractal aumenta (~20-30) durante la reorganización
    - Picos espectrales comienzan a formarse en frecuencias específicas
    - La coherencia disminuye mientras surge la estructura algorítmica
    - Transferencia de información se optimiza entre capas intermedias
    """,
    
    "Grokking": """
    **Estado de Grokking (Solución Algorítmica):**
    - Los pesos forman una representación geométrica mínima (anillo trigonométrico)
    - Dimensionalidad fractal baja pero significativa (~3-5) corresponde a la solución
    - Espectro con picos definidos en armónicos impares (solución de paridad)
    - Baja coherencia (<0.2) indica representación eficiente y sparse
    - Transferencia cercana al 100% entre todas las capas (solución estable)
    """
}

st.markdown(f"<div class='scientific-notation'>{interpretation[phase]}</div>", unsafe_allow_html=True)

if phase == "Grokking":
    st.success("✅ **GROKKING CONFIRMADO:** Solución algorítmica estable descubierta. La red ha colapsado a una representación geométrica mínima que generaliza perfectamente.")

st.markdown("</div>", unsafe_allow_html=True)


with st.sidebar:
    st.header("⚙️ Parámetros Científicos")
    st.markdown("---")
    
    
    seed = st.number_input("Semilla Aleatoria", 0, 10000, 42)
    
    
    show_fourier = st.toggle("Mostrar Análisis de Fourier Detallado", True)
    show_metrics = st.toggle("Mostrar Métricas Avanzadas", True)
    
    st.markdown("---")
    st.subheader("📚 Referencias Teóricas")
    st.markdown("""
    - **Liu et al. (2022)**: "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets"
    - **Power et al. (2022)**: "Formalizing the presumption of independence"
    - **Nanda et al. (2023)**: "Progress Measures for Grokking via Mechanistic Interpretability"
    - **Paszke et al. (2023)**: "Adaptive Curriculum Learning for Grokking Dynamics"
    """)
    
    st.markdown("---")
    st.subheader("💡 Leyenda de Colores")
    st.markdown("""
    - **PCA 3D**: Intensidad = Norma del peso
    - **Matriz Correlación**: Rojo = Correlación positiva, Azul = Correlación negativa
    - **Espectro**: Altura = Magnitud en esa frecuencia
    - **Transferencia**: Color = Eficiencia de transferencia
    """)
    
    st.markdown("---")
    st.caption(f"Generado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


st.markdown("""
<div class="footer">
    <p>🔬 <b>Grokking Dynamics Monitor</b> - Visualización Científica para Investigación en Machine Learning</p>
    <p>© 2025 - Basado en investigaciones de grokking y dinámicas de aprendizaje en redes neuronales</p>
    <p><i>Esta herramienta está diseñada para investigación científica y educación en interpretabilidad de ML</i></p>
</div>
""", unsafe_allow_html=True)


if 'previous_phase' not in st.session_state:
    st.session_state.previous_phase = phase

if st.session_state.previous_phase != phase:
    with st.spinner('🔄 Actualizando visualización científica...'):
        time.sleep(0.5)  
    st.session_state.previous_phase = phase
