#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PoC ABLACIÓN — TRANSFERENCIA ALGORÍTMICA
Paridad Binaria
Escala: 128 bits | 2048 hidden
ZERO-SHOT (sin entrenamiento)
"""

import time
import torch
from copy import deepcopy

# 🔁 IMPORTAMOS TODO DESDE TU APP ORIGINAL
from app import (
    GrokkingTransformer,
    get_parity_dataset,
    AdaptiveCurriculumTrainer
)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

TIMEOUT = 300  # segundos
N_BITS = 128
D_H = 2048

MODEL_64 = "grok_model_stage4_n64_d1024_adaptive.pth"

# ---------------------------------------------------------------------
# Utils
# ---------------------------------------------------------------------

def evaluate(model, x, y):
    with torch.no_grad():
        logits, _ = model(x)
        return (logits.argmax(1) == y).float().mean().item()

def load_64bit_model():
    model = GrokkingTransformer(d_in=64, d_h=1024).to(DEVICE)
    model.load_state_dict(torch.load(MODEL_64, map_location=DEVICE))
    model.eval()
    return model

# ---------------------------------------------------------------------
# EXPERIMENTO
# ---------------------------------------------------------------------

def run_experiment(use_padding: bool):
    start = time.time()

    print("📦 Cargando modelos 64-bit (base algorítmica)...")
    base_model = load_64bit_model()
    print("✅ Modelos 64-bit cargados correctamente")

    # Modelo 128 bits
    model = GrokkingTransformer(d_in=N_BITS, d_h=D_H).to(DEVICE)
    model.eval()

    if use_padding:
        trainer = AdaptiveCurriculumTrainer()
        model = trainer.smart_weight_transfer(
            prev_model=base_model,
            new_model=model,
            stage=4
        )
    else:
        print("❌ Transferencia DESACTIVADA — pesos aleatorios")

    # Dataset
    x, y = get_parity_dataset(n_bits=N_BITS, k=3, size=2000)
    x = x.to(DEVICE)
    y = y.to(DEVICE)

    # ZERO-SHOT EVALUATION
    train_acc = evaluate(model, x[:1000], y[:1000])
    test_acc  = evaluate(model, x[1000:], y[1000:])

    elapsed = time.time() - start

    print(f"Step 0      | Train {train_acc:.3f} | Test {test_acc:.3f}")
    print(f"⏱ Tiempo: {elapsed:.2f}s")

    if test_acc > 0.98:
        print("🎯 GENERALIZA — TRANSFERENCIA ALGORÍTMICA CONFIRMADA")
        return True
    else:
        print("❌ NO GENERALIZA")
        return False

# ---------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------

if __name__ == "__main__":

    print(f"""
======================================================================
🧠 PoC ABLACIÓN — TRANSFERENCIA ALGORÍTMICA
Tarea: Paridad Binaria
Escala: 128 bits | 2048 hidden
Modo: ZERO-SHOT (sin entrenamiento)
Timeout: {TIMEOUT} segundos
======================================================================
""")

    print("\n" + "="*80)
    print("🧪 EXPERIMENTO: CON PADDING INTELIGENTE")
    print("="*80)
    ok_padding = run_experiment(use_padding=True)

    print("\n" + "="*80)
    print("🧪 EXPERIMENTO: SIN PADDING (CONTROL)")
    print("="*80)
    ok_control = run_experiment(use_padding=False)

    print("\n" + "="*80)
    print("📊 RESULTADO FINAL")
    print("="*80)

    if ok_padding and not ok_control:
        print("✅ ABLACIÓN EXITOSA: la transferencia NO es azar")
    elif ok_padding:
        print("⚠️ Padding ayuda, pero el control también aprende algo")
    else:
        print("❌ No se observó transferencia")
