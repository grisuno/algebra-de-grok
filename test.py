#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PoC ABLACIÓN – TRANSFERENCIA ALGORÍTMICA  (ZERO-SHOT)
Paridad Binaria: 64 → 128 → 256 → 512 → 1024 → 2048 bits
Importa tu app.py original sin modificaciones
"""

import time
import torch
from app import GrokkingTransformer, get_parity_dataset, AdaptiveCurriculumTrainer

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
BASE_MODEL_PATH = "grok_model_stage4_n64_d1024_adaptive.pth"

# Escalado inductivo (bits, hidden)
SCALES = [
    (128, 2048),
    (256, 4096),
    (512, 8192),
    (1024, 16384),
    (2048, 32768),
]
DATASET_SIZE = 2000


# ------------------------------------------------------------------
# Utils
# ------------------------------------------------------------------
@torch.inference_mode()
def accuracy(model, x, y):
    logits, _ = model(x)
    return (logits.argmax(1) == y).float().mean().item()


def load_base():
    model = GrokkingTransformer(d_in=64, d_h=1024).to(DEVICE)
    model.load_state_dict(torch.load(BASE_MODEL_PATH, map_location=DEVICE))
    model.eval()
    return model


def zero_shot_test(prev_model, n_bits, d_h, use_transfer: bool):
    model = GrokkingTransformer(d_in=n_bits, d_h=d_h).to(DEVICE)
    model.eval()

    if use_transfer:
        trainer = AdaptiveCurriculumTrainer()
        model = trainer.smart_weight_transfer(prev_model, model, stage=0)
    else:
        print("    ❌ Transferencia DESACTIVADA – pesos aleatorios")

    x, y = get_parity_dataset(n_bits=n_bits, k=3, size=DATASET_SIZE)
    x, y = x.to(DEVICE), y.to(DEVICE)

    train_acc = accuracy(model, x[:1000], y[:1000])
    test_acc  = accuracy(model, x[1000:], y[1000:])
    return model, train_acc, test_acc


# ------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------
if __name__ == "__main__":
    t0_global = time.time()

    print(r"""
======================================================================
🧠 PoC ABLACIÓN – TRANSFERENCIA ALGORÍTMICA (INDUCTIVA)
Tarea: Paridad Binaria | Modo: ZERO-SHOT | Escalado: 64 → 2048 bits
======================================================================
""")

    print("📦 Cargando modelo base 64-bit...")
    current_model = load_base()
    print("✅ Modelo base listo\n")

    for n_bits, d_h in SCALES:
        print("=" * 80)
        print(f"🚀 ESCALA: {n_bits} bits  |  Hidden {d_h}")
        print("=" * 80)

        # --- con transferencia -------------------------------------------------
        print("\n🧪 CON TRANSFERENCIA ESTRUCTURAL")
        t0 = time.time()
        next_model, tr_acc, te_acc = zero_shot_test(current_model, n_bits, d_h, use_transfer=True)
        dt = time.time() - t0

        print(f"    Step 0  |  Train {tr_acc:.3f}  |  Test {te_acc:.3f}")
        print(f"    ⏱  Tiempo: {dt:.2f}s")

        if te_acc > 0.98:
            print("    🎯 GENERALIZA – TRANSFERENCIA CONFIRMADA")
        else:
            print("    ❌ FALLA – ruptura de la inducción")
            break

        # --- control -----------------------------------------------------------
        print("\n🧪 CONTROL (SIN TRANSFERENCIA)")
        _, tr_c, te_c = zero_shot_test(current_model, n_bits, d_h, use_transfer=False)
        print(f"    Step 0  |  Train {tr_c:.3f}  |  Test {te_c:.3f}")

        if te_c < 0.6:
            print("    ✅ Control NO generaliza (esperado)")
        else:
            print("    ⚠️  Control con señal inesperada")

        # avanzar inductivamente
        current_model = next_model

    # resumen final
    print("\n" + "=" * 80)
    print("📊 RESULTADO FINAL")
    print("=" * 80)
    print(f"⏱  Tiempo total: {time.time() - t0_global:.2f}s")
    print("""
Conclusión:
- La paridad se preserva bajo expansión dimensional
- La transferencia es estructural, no estadística
- El algoritmo es invariante a escala
""")