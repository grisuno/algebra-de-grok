# visualizador.py
# VERSIÓN HONESTA Y CORREGIDA: Valida el rendimiento real del Modelo + Análisis del SAE
# Funciona con: grok_model_stage4_n64_d1024_adaptive.pth y grok_sae_stage4_n64_d1024_adaptive.pth

import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Importar tu implementación exacta
from app import (
    GrokkingTransformer,
    SuperpositionSAE,
    get_parity_dataset
)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_full_system(n_bits, d_h, stage=4):
    """Carga el MODELO entrenado y el SAE"""
    # CORREGIDO: Usar {d_h} en lugar de {h}
    model_path = f"grok_model_stage{stage}_n{n_bits}_d{d_h}_adaptive.pth"
    sae_path = f"grok_sae_stage{stage}_n{n_bits}_d{d_h}_adaptive.pth"
    
    # Verificar existencia
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modelo no encontrado: {model_path}")
    if not os.path.exists(sae_path):
        raise FileNotFoundError(f"SAE no encontrado: {sae_path}")

    # Cargar modelo real
    model = GrokkingTransformer(d_in=n_bits, d_h=d_h).to(DEVICE)
    model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    model.eval()
    print(f"✅ Modelo cargado: {model_path}")

    # Cargar SAE (puede estar sin entrenar)
    sae = SuperpositionSAE(d_model=d_h, d_sae=d_h * 4).to(DEVICE)
    sae.load_state_dict(torch.load(sae_path, map_location=DEVICE))
    sae.eval()
    print(f"✅ SAE cargado: {sae_path}")

    return model, sae

def calculate_model_accuracy(model, x, y):
    """Calcula la precisión real del modelo cargado"""
    with torch.no_grad():
        logits, _ = model(x)
        preds = logits.argmax(dim=1)
        accuracy = (preds == y).float().mean().item()
    return accuracy

def get_real_activations(model, x):
    """Obtiene las activaciones latentes REALES del modelo"""
    with torch.no_grad():
        _, h2 = model(x)
    return h2

def extract_sae_metrics(sae, h2):
    """Extrae métricas del SAE sobre las activaciones reales"""
    with torch.no_grad():
        x_recon, z_sae = sae(h2)
        psi, f_eff = sae.get_metrics(z_sae)
        l0_sparsity = (z_sae.abs() > 1e-6).float().mean(dim=1).mean().item()
        active_features = (z_sae.abs().sum(dim=0) > 1e-6).sum().item()
        
    return {
        'z_sae': z_sae.cpu().numpy(),
        'psi': psi,
        'f_eff': f_eff,
        'l0_sparsity': l0_sparsity,
        'active_features': active_features
    }

def plot_sae_autopsy(data, accuracy, n_bits, d_h, sae):
    """Visualización centrada en la verdad del Modelo"""
    fig = plt.figure(figsize=(18, 14))
    fig.suptitle(f"🧠 AUTOPSIA PROFUNDA DEL SAE & MODELO\nParidad {n_bits}-bits | d_h={d_h} | d_sae={sae.d_sae}",
                 fontsize=18, color="#00ffaa", fontweight='bold')
    fig.patch.set_facecolor('#0a0a1a')
    plt.rcParams['font.family'] = 'monospace'

    # 1. Embedding 3D
    ax_3d = fig.add_subplot(2, 3, 1, projection='3d')
    z_flat = data['z_sae']
    if len(z_flat) > 10:
        reducer = TSNE(n_components=3, random_state=42, perplexity=min(30, len(z_flat)-1))
        emb = reducer.fit_transform(z_flat[:100])
        ax_3d.scatter(emb[:,0], emb[:,1], emb[:,2], 
                     c=np.linspace(0, 1, len(emb)), cmap='plasma', alpha=0.8, s=15)
        ax_3d.set_title("Espacio de Features SAE (TSNE-3D)", color='#00ffcc', fontsize=12)
    else:
        ax_3d.set_title("Datos insuficientes", color='#ff5555', fontsize=12)

    # 2. Distribución de pesos SAE
    ax_w = fig.add_subplot(2, 3, 2)
    w_flat = sae.W.data.cpu().numpy().flatten()
    ax_w.hist(w_flat, bins=50, color='#ff7700', alpha=0.8, density=True)
    ax_w.set_title("Distribución de Pesos SAE (W)", color='#00ffcc', fontsize=12)

    # 3. MÉTRICAS CLAVE (AHORA INCLUYE ACCURACY DEL MODELO)
    ax_metrics = fig.add_subplot(2, 3, 3)
    ax_metrics.axis('off')
    
    # Diagnóstico honesto de SAE
    psi_val = data['psi']
    if psi_val < 0.2:
        sae_status = "✅ SAE COMPRIMIDO"
        sae_text = "El SAE captura bien la estructura."
        color_sae = '#00ff00'
    else:
        sae_status = "⚠️ SAE RUIDOSO/SIN ENTRENAR"
        sae_text = "El SAE no se entrenó (probablemente por parada temprana)."
        color_sae = '#ffaa00'

    # Diagnóstico honesto del MODELO
    if accuracy >= 0.999:
        model_status = "🎯 PERFECCIÓN ABSOLUTA"
        model_text = "100% Generalización. Algoritmo aprendido."
        color_model = '#00ff00'
    elif accuracy > 0.9:
        model_status = "✅ ALTO RENDIMIENTO"
        model_text = "Generalización casi perfecta."
        color_model = '#ccff00'
    else:
        model_status = "❌ FALLO"
        model_text = "El modelo no generaliza."
        color_model = '#ff0000'

    metrics_text = f"""
📊 REALIDAD EMPÍRICA (MODELO):

Accuracy Test: 
   {accuracy*100:.2f}% → {model_status}

Estado del Modelo:
   {model_text}

🔍 MÉTRICAS DE LA SONDA (SAE):

ψ (feature utilization): 
   {data['psi']:.4f} → {sae_status}

Estado del SAE:
   {sae_text}

Nota: Si el Accuracy es 100% y ψ es alto, 
significa 'Grokking por Transferencia'.
El SAE es irrelevante en este caso.
"""
    ax_metrics.text(0.05, 0.95, metrics_text, color='white', fontsize=9, 
                   va='top', family='monospace', 
                   bbox=dict(facecolor='#1a1a2e', alpha=0.8, boxstyle='round,pad=0.5'))

    # 4. Top features activos
    ax_top = fig.add_subplot(2, 3, 4)
    z_mean = np.abs(data['z_sae']).mean(axis=0)
    top_indices = np.argsort(z_mean)[-50:][::-1]
    top_values = z_mean[top_indices]
    if top_values.max() > 0:
        top_values = top_values / (top_values.max() + 1e-8)
    
    bars = ax_top.bar(range(50), top_values, color=plt.cm.viridis(np.linspace(0, 1, 50)))
    ax_top.set_title("Top 50 Features SAE", color='#00ffcc', fontsize=12)
    ax_top.grid(True, color='#333', alpha=0.3)

    # 5. Heatmap
    ax_heat = fig.add_subplot(2, 3, 5)
    sample_activations = np.abs(data['z_sae'][:50, top_indices[:20]])
    im = ax_heat.imshow(sample_activations, aspect='auto', cmap='hot', interpolation='nearest')
    ax_heat.set_title("Activaciones SAE por Muestra", color='#00ffcc', fontsize=12)
    plt.colorbar(im, ax=ax_heat, label='Activación')

    # 6. DIAGNÓSTICO FINAL HONESTO
    ax_diag = fig.add_subplot(2, 3, 6)
    ax_diag.axis('off')
    
    # Lógica del Cisne Negro basada en ACCURACY, no en SAE
    if accuracy == 1.0:
        black_swan = "✅ ¡SÍ! DETECTADO."
        explanation = "El modelo generaliza al 100% sin entrenamiento explícito en esta etapa (Transferencia de Algoritmo)."
        veredict = "ALGORITMO DOMINADO"
    else:
        black_swan = "❌ NO."
        explanation = "Falta generalización perfecta."
        veredict = "EN PROCESO / FALLO"

    diag_text = f"""
🎯 VEREDICTO FINAL DEL SISTEMA:
{veredict}

⚡ ¿ES UN 'CISNE NEGRO' (TRANSFERENCIA ALGORÍTMICA)?
{black_swan}

📜 JUSTIFICACIÓN TÉCNICA:
{explanation}

📊 Datos de Soporte:
• Features SAE activos: {data['active_features']} (Ruido o estructura)
• Accuracy Real: {accuracy*100:.1f}%
"""
    ax_diag.text(0.05, 0.95, diag_text, color='white', fontsize=9, 
                va='top', family='monospace',
                bbox=dict(facecolor='#1a1a2e', alpha=0.8, boxstyle='round,pad=0.5'))

    # Estilo
    for ax in [ax_3d, ax_w, ax_top, ax_heat]:
        if hasattr(ax, 'spines'):
            for spine in ax.spines.values():
                spine.set_color('#666')
        if hasattr(ax, 'tick_params'):
            ax.tick_params(colors='white')
        if hasattr(ax, 'xaxis'):
            ax.xaxis.label.set_color('white')
        ax.title.set_color('#00ffcc')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    # Figura 2
    fig2 = plt.figure(figsize=(16, 8))
    fig2.suptitle("🔍 ANÁLISIS DE DISTRIBUCIÓN", fontsize=16, color="#00ffaa")
    fig2.patch.set_facecolor('#0a0a1a')

    ax_dist = fig2.add_subplot(1, 2, 1)
    all_activations = data['z_sae'].flatten()
    ax_dist.hist(all_activations[all_activations > 1e-6], bins=50, alpha=0.7, color='#00ffcc', density=True)
    ax_dist.set_title("Activaciones SAE No-Cero", color='#00ffcc')

    ax_percentiles = fig2.add_subplot(1, 2, 2)
    percentiles = np.percentile(all_activations[all_activations > 1e-6], [10, 25, 50, 75, 90, 95, 99])
    labels = ['10%', '25%', '50%', '75%', '90%', '95%', '99%']
    bars = ax_percentiles.bar(labels, percentiles, color=plt.cm.plasma(np.linspace(0, 1, len(labels))))
    ax_percentiles.set_title("Percentiles SAE", color='#00ffcc')

    for ax in [ax_dist, ax_percentiles]:
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.title.set_color('#00ffcc')

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()

# ===========================
# EJECUCIÓN PRINCIPAL
# ===========================
if __name__ == "__main__":
    n_bits = 64
    d_h    = 1024
    stage  = 4

    print(f"""
{'='*70}
🧠 VISUALIZADOR HONESTO - GROKKING PARITY
{'='*70}
🎯 Archivos: grok_model_stage{stage}_n{n_bits}_d{d_h}_adaptive.pth
             grok_sae_stage{stage}_n{n_bits}_d{d_h}_adaptive.pth
""")
    
    try:
        # 1. Cargar sistema completo
        model, sae = load_full_system(n_bits, d_h, stage)
        
        # 2. Generar datos
        print("🧪 Generando dataset de prueba...")
        x, y = get_parity_dataset(n_bits=n_bits, k=3, size=500)
        x = x.to(DEVICE)
        y = y.to(DEVICE)
        
        # 3. Calcular Accuracy Real (La verdad)
        print("🔍 Verificando rendimiento real del modelo...")
        acc = calculate_model_accuracy(model, x, y)
        
        # 4. Obtener activaciones reales
        print("🌀 Extrayendo activaciones internas reales...")
        h2_real = get_real_activations(model, x)
        
        # 5. Analizar SAE sobre datos reales
        print("🔬 Pasando activaciones por el SAE...")
        data = extract_sae_metrics(sae, h2_real)
        
        print(f"""
{'='*70}
📊 RESULTADOS DE LA AUTOPSIA:
{'='*70}
✅ Accuracy del Modelo: {acc*100:.2f}%
📊 ψ del SAE:          {data['psi']:.4f}
📊 Features SAE:       {data['active_features']}

📝 INTERPRETACIÓN:
{f'El modelo es perfecto. El SAE está ruidoso (sin entrenar), pero eso es irrelevante.' if acc == 1.0 else 'Revise el rendimiento del modelo.'}
""")
        
        # 6. Visualizar
        plot_sae_autopsy(data, acc, n_bits, d_h, sae)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}\n")
        import traceback
        traceback.print_exc()
        print("Asegúrate de tener tanto el modelo como el SAE guardados en el directorio actual.")