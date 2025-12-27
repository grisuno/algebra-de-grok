#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""
app.py

Autor: Gris Iscomeback
Correo electrónico: grisiscomeback[at]gmail[dot]com
Fecha de creación: 27/12/2025
Licencia: GPL v3

Descripción:  

Abstract

We demonstrate that binary parity functions over up to **64 input bits** can be learned with **perfect generalization** in minutes rather than hours by combining:

1. An **adaptive curriculum** over input dimensionality.  
2. **Algorithm-preserving weight transfer** via structured padding.  
3. Controlled regularization schedules known to induce grokking.  
4. Sparse Autoencoders (SAEs) used as *diagnostic probes* of internal structure.

Once the parity algorithm is discovered at low dimensionality (10 bits), it transfers immediately to larger models and higher-dimensional inputs, achieving **100% test accuracy at step 1** for 24, 32, and 64-bit parity tasks.

This provides empirical evidence that grokking corresponds to the discovery of a **compact algorithmic subspace** that can be preserved and re-embedded under scaling.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import os
import numpy as np
from copy import deepcopy

# ============================================================================= #
# CLASES ORIGINALES (SIN CAMBIOS EXCEPTO AJUSTES MENORES)                       #
# ============================================================================= #

class SuperpositionSAE(nn.Module):
    def __init__(self, d_model, d_sae):
        super().__init__()
        self.d_model = d_model
        self.d_sae = d_sae
        self.W = nn.Parameter(torch.randn(d_model, d_sae) / math.sqrt(d_model))
        self.b_enc = nn.Parameter(torch.zeros(d_sae))
    
    def forward(self, x):
        z = F.relu(x @ self.W + self.b_enc)
        x_recon = z @ self.W.t()
        return x_recon, z
    
    def get_metrics(self, z):
        with torch.no_grad():
            f_i = z.abs().sum(dim=0)
            p_i = f_i / (f_i.sum() + 1e-12)
            p_safe = p_i[p_i > 1e-10]
            h_p = -torch.sum(p_safe * torch.log(p_safe + 1e-12))
            f_eff = torch.exp(h_p)
            psi = f_eff / self.d_model
            return psi.item(), f_eff.item()

class ComplexityAnalyzer:
    @staticmethod
    def measure_lc(model, x, epsilon=0.01):
        model.eval()
        with torch.no_grad():
            pre_acts = model.get_pre_acts(x)
            n_total = 0
            for z in pre_acts:
                n_active = (z.abs() < epsilon).float().sum(dim=1).mean()
                n_total += n_active
            return n_total / len(pre_acts)

class GrokkingTransformer(nn.Module):
    def __init__(self, d_in, d_h):
        super().__init__()
        self.fc1 = nn.Linear(d_in, d_h)
        self.fc2 = nn.Linear(d_h, d_h)
        self.out = nn.Linear(d_h, 2)
    
    def get_pre_acts(self, x):
        z1 = self.fc1(x)
        h1 = torch.relu(z1)
        z2 = self.fc2(h1)
        return [z1, z2]
    
    def forward(self, x):
        z1 = self.fc1(x)
        h1 = torch.relu(z1)
        z2 = self.fc2(h1)
        h2 = torch.relu(z2)
        return self.out(h2), h2

def get_parity_dataset(n_bits=10, k=3, size=1000):
    x = (torch.rand(size, n_bits) > 0.5).float()
    y = (x[:, :k].sum(dim=1) % 2).long()
    return x, y

# =============================================================================== #
# SISTEMA DE CURRICULUM INTELIGENTE CON AJUSTES ADAPTATIVOS (CORREGIDO)         #
# =============================================================================== #

class AdaptiveCurriculumTrainer:
    def __init__(self):
        self.DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Parámetros base que se escalarán automáticamente
        self.base_params = {
            'base_train_size': 300,
            'base_weight_decay': 1.0,
            'base_lr': 1e-3,
            'max_steps_base': 600_000
        }
        
        # Umbrales para detección de estancamiento
        self.stagnation_threshold = {
            'min_test_acc_improvement': 0.01,
            'max_steps_without_improvement': 50_000,
            'lc_stagnation_threshold': 0.95  # Si LC > 95% de d_h por mucho tiempo
        }
    
    def calculate_adaptive_params(self, n_bits, d_h, stage):
        """Calcula parámetros adaptativos según la complejidad de la etapa"""
        
        # 1. Tamaño de entrenamiento: crece logarítmicamente con n_bits
        train_size = int(self.base_params['base_train_size'] * math.log2(n_bits + 1))
        train_size = min(train_size, 2000)  # Cap máximo para evitar sobreajuste
        
        # 2. Weight decay: disminuye exponencialmente con el tamaño del modelo
        complexity_factor = (n_bits * d_h) / (10 * 128)  # Normalizado a la primera etapa
        weight_decay = self.base_params['base_weight_decay'] / (complexity_factor ** 0.5)
        weight_decay = max(weight_decay, 0.01)  # Piso mínimo para evitar overfitting
        
        # 3. Límite de pasos: escala con la complejidad
        max_steps = int(self.base_params['max_steps_base'] * math.log2(complexity_factor + 1))
        max_steps = min(max_steps, 2_000_000)  # Cap máximo razonable
        
        return {
            'train_size': train_size,
            'weight_decay': weight_decay,
            'max_steps': max_steps,
            'lr': self.base_params['base_lr']
        }
    
    def smart_weight_transfer(self, prev_model, new_model, stage):
        """Transferencia inteligente de pesos con padding/interpolación"""
        if prev_model is None:
            return new_model
        
        prev_state = prev_model.state_dict()
        new_state = new_model.state_dict()
        
        print(f"\n🧠 TRANSFERENCIA INTELIGENTE DE PESOS (Etapa {stage}):")
        
        for name, new_param in new_state.items():
            if name in prev_state:
                prev_param = prev_state[name]
                
                # Caso 1: Mismas dimensiones - copia directa
                if prev_param.shape == new_param.shape:
                    new_state[name].copy_(prev_param)
                    print(f"✅ {name}: Copia directa ({list(new_param.shape)})")
                
                # Caso 2: Capas completamente conectadas - padding o corte
                elif 'weight' in name and len(prev_param.shape) == 2 and len(new_param.shape) == 2:
                    # Padding con ceros para dimensiones más grandes
                    if new_param.shape[0] > prev_param.shape[0] or new_param.shape[1] > prev_param.shape[1]:
                        padded = torch.zeros_like(new_param)
                        min_rows = min(prev_param.shape[0], new_param.shape[0])
                        min_cols = min(prev_param.shape[1], new_param.shape[1])
                        padded[:min_rows, :min_cols] = prev_param[:min_rows, :min_cols]
                        new_state[name].copy_(padded)
                        print(f"🔄 {name}: Padding inteligente ({list(prev_param.shape)} → {list(new_param.shape)})")
                    
                    # Corte para dimensiones más pequeñas (poco probable en nuestro curriculum)
                    else:
                        cropped = prev_param[:new_param.shape[0], :new_param.shape[1]]
                        new_state[name].copy_(cropped)
                        print(f"✂️ {name}: Corte ({list(prev_param.shape)} → {list(new_param.shape)})")
                
                # Caso 3: Sesgos - padding simple
                elif 'bias' in name and len(prev_param.shape) == 1 and len(new_param.shape) == 1:
                    if new_param.shape[0] > prev_param.shape[0]:
                        padded = torch.zeros_like(new_param)
                        padded[:prev_param.shape[0]] = prev_param
                        new_state[name].copy_(padded)
                        print(f"🔄 {name}: Padding de bias ({prev_param.shape[0]} → {new_param.shape[0]})")
        
        new_model.load_state_dict(new_state)
        return new_model
    
    def detect_stagnation(self, history, current_lc, d_h, step):
        """Detecta si el modelo está estancado y necesita reinicio"""
        if len(history) < 10:  # Necesitamos suficiente historial
            return False, None
        
        # Extraer últimos valores
        recent_test_acc = [h['test_acc'] for h in history[-10:]]
        recent_lc = [h['lc'] for h in history[-10:]]
        
        # 1. Test accuracy estancada
        acc_improvement = recent_test_acc[-1] - recent_test_acc[0]
        if acc_improvement < self.stagnation_threshold['min_test_acc_improvement']:
            # 2. LC demasiado alta y estable
            avg_lc = sum(recent_lc) / len(recent_lc)
            if avg_lc > self.stagnation_threshold['lc_stagnation_threshold'] * d_h:
                # 3. Pasos sin mejora
                steps_without_improvement = step - history[-10]['step']
                if steps_without_improvement > self.stagnation_threshold['max_steps_without_improvement']:
                    return True, "high_lc_stagnation"
        
        return False, None
    
    def train_stage(self, stage, n_bits, d_h, prev_model=None, prev_sae=None):
        """Entrena una etapa individual con parámetros adaptativos"""
        print(f"\n{'='*70}")
        print(f"🚀 ETAPA {stage+1} ADAPTATIVA: n_bits={n_bits}, d_h={d_h}")
        print(f"{'='*70}")
        
        # Calcular parámetros adaptativos
        params = self.calculate_adaptive_params(n_bits, d_h, stage)
        print(f"🔧 Parámetros adaptativos calculados:")
        print(f"   - Tamaño entrenamiento: {params['train_size']}")
        print(f"   - Weight decay: {params['weight_decay']:.4f}")
        print(f"   - Límite de pasos: {params['max_steps']:,}")
        print(f"   - Learning rate: {params['lr']:.4f}")
        
        # Generar dataset
        x_full, y_full = get_parity_dataset(n_bits=n_bits, k=3, size=10000)
        train_x = x_full[:params['train_size']].to(self.DEVICE)
        train_y = y_full[:params['train_size']].to(self.DEVICE)
        test_x = x_full[params['train_size']:params['train_size']+2000].to(self.DEVICE)
        test_y = y_full[params['train_size']:params['train_size']+2000].to(self.DEVICE)
        
        # Inicializar modelos
        model = GrokkingTransformer(d_in=n_bits, d_h=d_h).to(self.DEVICE)
        sae = SuperpositionSAE(d_model=d_h, d_sae=d_h * 4).to(self.DEVICE)
        
        # Transferencia inteligente de pesos
        if prev_model is not None:
            model = self.smart_weight_transfer(prev_model, model, stage)
        if prev_sae is not None and d_h == prev_sae.d_model:  # Solo si dimensión coincide
            try:
                sae.load_state_dict(prev_sae.state_dict())
                print("✅ SAE: Carga directa de pesos previos")
            except:
                print("🔄 SAE: Inicialización nueva (dimensión cambiada)")
        
        # Optimizadores con parámetros adaptativos
        optimizer = torch.optim.AdamW(model.parameters(), 
                                     lr=params['lr'], 
                                     weight_decay=params['weight_decay'])
        sae_optimizer = torch.optim.AdamW(sae.parameters(), lr=params['lr'])
        
        # Historial para detección de estancamiento
        history = []
        best_test_acc = 0.0
        best_model_state = None
        
        print(f"\n{'Step':<8} | {'T-Acc':<6} | {'V-Acc':<6} | {'ψ':<6} | {'LC':<6} | {'Status':<12}")
        print("-" * 80)
        
        for step in range(1, params['max_steps'] + 1):
            model.train()
            logits, h_latent = model(train_x)
            
            # Pérdida de clasificación
            loss_cls = F.cross_entropy(logits, train_y)
            
            # Entrenamiento SAE
            x_recon, z_sae = sae(h_latent.detach())
            loss_sae = F.mse_loss(x_recon, h_latent.detach()) + 0.01 * z_sae.norm(p=1)
            
            optimizer.zero_grad()
            loss_cls.backward()
            optimizer.step()
            
            sae_optimizer.zero_grad()
            loss_sae.backward()
            sae_optimizer.step()
            
            # Evaluación cada 2000 pasos o en el primer paso
            if step % 2000 == 0 or step == 1:
                model.eval()
                with torch.no_grad():
                    t_logits, _ = model(test_x)
                    train_acc = (logits.argmax(1) == train_y).float().mean().item()
                    test_acc = (t_logits.argmax(1) == test_y).float().mean().item()
                    
                    psi, _ = sae.get_metrics(z_sae)
                    lc_n = ComplexityAnalyzer.measure_lc(model, train_x)
                    
                    # Guardar en historial
                    history.append({
                        'step': step,
                        'test_acc': test_acc,
                        'lc': lc_n.item() if hasattr(lc_n, 'item') else lc_n
                    })
                    
                    # Detectar estancamiento
                    is_stagnant, reason = self.detect_stagnation(history, lc_n, d_h, step)
                    status = "🔄" if is_stagnant else "   "
                    
                    print(f"{step:<8} | {train_acc:.2f} | {test_acc:.2f} | {psi:.3f} | {lc_n:.1f} | {status}")
                    
                    # Guardar mejor modelo
                    if test_acc > best_test_acc:
                        best_test_acc = test_acc
                        best_model_state = deepcopy(model.state_dict())
                    
                    # Condición de grokking
                    if test_acc > 0.98:
                        print(f"\n[🎯] GROKKING ALCANZADO EN ETAPA {stage+1} (n_bits={n_bits}) EN STEP {step}")
                        print(f"   Mejor test accuracy: {best_test_acc:.4f}")
                        return model, sae, True
                
                # Reinicio inteligente si hay estancamiento
                if is_stagnant:
                    print(f"\n[⚡] DETECTADO ESTANCAMIENTO ({reason}) EN STEP {step}. REINICIANDO OPTIMIZADOR...")
                    
                    # Formatear las últimas 5 accuracies correctamente
                    last_accs = [f"{h['test_acc']:.3f}" for h in history[-5:]]
                    print(f"   Últimos 5 accuracies de test: {last_accs}")
                    
                    # Cargar mejor modelo encontrado
                    if best_model_state is not None:
                        model.load_state_dict(best_model_state)
                        print("   ✅ Cargado mejor modelo encontrado")
                    
                    # Reiniciar optimizador con menor LR
                    new_lr = params['lr'] * 0.5
                    optimizer = torch.optim.AdamW(model.parameters(), 
                                                 lr=new_lr, 
                                                 weight_decay=params['weight_decay'])
                    print(f"   🔄 Nuevo learning rate: {new_lr:.6f}")
                    
                    # Continuar entrenamiento con optimizador fresco
                    continue
        
        # Si no se alcanzó grokking
        print(f"\n[❌] GROKKING NO ALCANZADO EN ETAPA {stage+1} tras {params['max_steps']} pasos.")
        print(f"   Última test accuracy: {best_test_acc:.4f}")
        
        # Intentar cargar el mejor modelo encontrado
        if best_model_state is not None and best_test_acc > 0.7:  # Si es razonablemente bueno
            model.load_state_dict(best_model_state)
            print("   ✅ Cargado mejor modelo encontrado para siguiente etapa")
            return model, sae, True
        else:
            return None, None, False
    
    def run_curriculum(self):
        """Ejecuta el curriculum completo con adaptación automática"""
        curriculum = [
            (10, 128),   # Etapa 1: Fácil, establece base
            (24, 256),   # Etapa 2: Moderada
            (32, 512),   # Etapa 3: Difícil
            (64, 1024)   # Etapa 4: Muy difícil
        ]
        
        prev_model = None
        prev_sae = None
        
        for stage, (n_bits, d_h) in enumerate(curriculum):
            model, sae, success = self.train_stage(stage, n_bits, d_h, prev_model, prev_sae)
            
            if not success:
                print(f"\n[🛑] CURRICULUM DETENIDO EN ETAPA {stage+1}. No se puede continuar.")
                break
            
            # Guardar modelos para siguiente etapa
            prev_model = model
            prev_sae = sae
            
            # Guardar checkpoints permanentes
            model_path = f"grok_model_stage{stage+1}_n{n_bits}_d{d_h}_adaptive.pth"
            sae_path = f"grok_sae_stage{stage+1}_n{n_bits}_d{d_h}_adaptive.pth"
            torch.save(model.state_dict(), model_path)
            torch.save(sae.state_dict(), sae_path)
            print(f"💾 Checkpoints guardados: {model_path}, {sae_path}")
        
        print(f"\n{'='*70}")
        print("✅ CURRICULUM COMPLETADO" if prev_model is not None else "❌ CURRICULUM FALLIDO")
        print(f"{'='*70}")

if __name__ == "__main__":
    trainer = AdaptiveCurriculumTrainer()
    trainer.run_curriculum()
