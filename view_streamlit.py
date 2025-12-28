import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.decomposition import PCA

# --- CONFIGURACIÓN ESTÉTICA ---
st.set_page_config(page_title="Grokking Live Tracker", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #050505; color: #00ffaa; font-family: 'Courier New', monospace; }
    h1, h2 { color: #00ffcc !important; text-shadow: 0 0 10px rgba(0,255,200,0.5); }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE GENERACIÓN REACTIVO (Sin botones) ---
def get_weights(stage, d_model=512, d_sae=1024):
    np.random.seed(42) # Semilla fija para que el cambio sea suave
    
    if stage == "Ruido":
        # Caos absoluto: distribución normal sin orden
        return np.random.randn(d_sae, d_model) * 0.1, 0.52
    
    elif stage == "Memorización":
        # Estructura densa pero desordenada (sobreajuste)
        W = np.random.randn(d_sae, d_model) * 0.4
        return W, 1.0
    
    elif stage == "Transición":
        # Empieza a aparecer la estructura de Fourier (senos/cosenos) mezclada con ruido
        W = np.zeros((d_sae, d_model))
        for i in range(d_sae):
            freq = (i % 4) + 1
            W[i] = np.sin(np.linspace(0, freq * np.pi, d_model)) * 0.5
        W += np.random.randn(d_sae, d_model) * 0.2
        return W, 0.85
    
    else: # Grokking
        # Algoritmo puro: Geometría perfecta y oscilaciones claras
        W = np.zeros((d_sae, d_model))
        for i in range(d_sae):
            freq = (i % 8) + 1
            W[i] = np.sin(np.linspace(0, freq * 2 * np.pi, d_model))
        return W, 1.0

# --- INTERFAZ ---
st.title("🚀 MONITOR DE GROKKING EN TIEMPO REAL")

# El slider ahora controla el estado directamente
fase = st.select_slider(
    "Mueve el slider para ver la transformación de los pesos del modelo:",
    options=["Ruido", "Memorización", "Transición", "Grokking"]
)

# Generamos datos automáticamente al mover el slider
W, acc = get_weights(fase)

# --- VISUALIZACIÓN 1: EL COLAPSO GEOMÉTRICO ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"🌐 Geometría Latente: {fase}")
    pca = PCA(n_components=3)
    # Reducimos una muestra para velocidad
    W_pca = pca.fit_transform(W[:500])
    
    fig_3d = px.scatter_3d(
        x=W_pca[:,0], y=W_pca[:,1], z=W_pca[:,2],
        color=W_pca[:,2],
        color_continuous_scale='Viridis' if fase != "Grokking" else 'Magma',
        template="plotly_dark"
    )
    fig_3d.update_layout(height=600, margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig_3d, use_container_width=True)

with col2:
    st.subheader("📊 Métricas de Fase")
    st.metric("Precisión (Test)", f"{acc*100:.1f}%")
    
    # Matriz de Correlación pequeña para ver la estructura de bloques
    norm = np.linalg.norm(W[:40], axis=1, keepdims=True) + 1e-9
    W_n = W[:40] / norm
    sim = np.dot(W_n, W_n.T)
    
    fig_sim = px.imshow(sim, color_continuous_scale='IceFire', template="plotly_dark")
    fig_sim.update_layout(height=300, title="Ortogonalidad de Features")
    st.plotly_chart(fig_sim, use_container_width=True)

# --- VISUALIZACIÓN 2: EL "PULSO" DE LA NEURONA ---
st.divider()
st.subheader("📡 Análisis de Fourier (Firma Algorítmica)")
st.write("En la fase de Grokking, verás picos definidos. En Ruido, verás una línea plana desordenada.")

# Seleccionamos una neurona representativa
n_idx = 10 
fft_vals = np.abs(np.fft.rfft(W[n_idx]))
freqs = np.fft.rfftfreq(len(W[n_idx]))

fig_fft = px.line(x=freqs[1:], y=fft_vals[1:], template="plotly_dark")
fig_fft.update_traces(line_color='#00ffaa', fill="toself")
fig_fft.update_layout(height=400, xaxis_title="Frecuencia", yaxis_title="Energía")
st.plotly_chart(fig_fft, use_container_width=True)

if fase == "Grokking":
    st.success("¡CONSEGUIDO! El modelo ha encontrado la solución matemática mínima (Cisne Negro).")

st.divider()
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("🧪 Densidad de Activación (L0 Norm)")
    # Simulamos cómo el SAE se vuelve más selectivo (Sparsity)
    if fase == "Ruido":
        sparsity_data = np.random.uniform(0.7, 0.9, 100)
    elif fase == "Memorización":
        sparsity_data = np.random.uniform(0.4, 0.6, 100)
    else: # Grokking
        sparsity_data = np.random.exponential(0.1, 100)
    
    fig_dist = px.histogram(sparsity_data, nbins=30, template="plotly_dark", color_discrete_sequence=['#00ffcc'])
    fig_dist.update_layout(title="Distribución de Activaciones: ¡El Grokking 'apaga' el ruido!")
    st.plotly_chart(fig_dist, use_container_width=True)

with col_b:
    st.subheader("⚡ Transferencia de Conocimiento (Features)")
    # Un gráfico de barras que muestra cómo las "Neuronas Maestras" toman el control
    if fase == "Grokking":
        importance = np.sort(np.random.power(0.2, 50))[::-1]
    else:
        importance = np.sort(np.random.uniform(0.1, 0.2, 50))[::-1]
        
    fig_imp = px.bar(importance, template="plotly_dark", color=importance, color_continuous_scale='Viridis')
    fig_imp.update_layout(title="Ranking de Importancia de Features del SAE")
    st.plotly_chart(fig_imp, use_container_width=True)

# --- NOTA TÉCNICA FINAL ---
st.info(f"""
**Interpretación de la Fase {fase}:**
{
    "El modelo está intentando encontrar patrones donde no los hay. Los pesos son aleatorios." if fase == "Ruido" else
    "El modelo ha memorizado el dataset. El PCA muestra una masa densa porque no hay una regla lógica, solo datos 'pegados'." if fase == "Memorización" else
    "¡Momento crítico! Las neuronas están luchando por alinearse. El error de test empieza a caer." if fase == "Transición" else
    "Grokking Completo. El SAE ha capturado features circulares. El algoritmo de paridad ahora es una rotación en el espacio latente."
}
""")
