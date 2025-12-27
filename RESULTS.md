```text

======================================================================
🚀 ETAPA 1 ADAPTATIVA: n_bits=10, d_h=128
======================================================================
🔧 Parámetros adaptativos calculados:
   - Tamaño entrenamiento: 1037
   - Weight decay: 1.0000
   - Límite de pasos: 600,000
   - Learning rate: 0.0010

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 0.52 | 0.49 | 1.957 | 3.8 |    
2000     | 1.00 | 1.00 | 0.008 | 25.4 |    

[🎯] GROKKING ALCANZADO EN ETAPA 1 (n_bits=10) EN STEP 2000
   Mejor test accuracy: 1.0000
💾 Checkpoints guardados: grok_model_stage1_n10_d128_adaptive.pth, grok_sae_stage1_n10_d128_adaptive.pth

======================================================================
🚀 ETAPA 2 ADAPTATIVA: n_bits=24, d_h=256
======================================================================
🔧 Parámetros adaptativos calculados:
   - Tamaño entrenamiento: 1393
   - Weight decay: 0.4564
   - Límite de pasos: 1,521,631
   - Learning rate: 0.0010

🧠 TRANSFERENCIA INTELIGENTE DE PESOS (Etapa 1):
🔄 fc1.weight: Padding inteligente ([128, 10] → [256, 24])
🔄 fc1.bias: Padding de bias (128 → 256)
🔄 fc2.weight: Padding inteligente ([128, 128] → [256, 256])
🔄 fc2.bias: Padding de bias (128 → 256)
🔄 out.weight: Padding inteligente ([2, 128] → [2, 256])
✅ out.bias: Copia directa ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.529 | 140.8 |    

[🎯] GROKKING ALCANZADO EN ETAPA 2 (n_bits=24) EN STEP 1
   Mejor test accuracy: 1.0000
💾 Checkpoints guardados: grok_model_stage2_n24_d256_adaptive.pth, grok_sae_stage2_n24_d256_adaptive.pth

======================================================================
🚀 ETAPA 3 ADAPTATIVA: n_bits=32, d_h=512
======================================================================
🔧 Parámetros adaptativos calculados:
   - Tamaño entrenamiento: 1513
   - Weight decay: 0.2795
   - Límite de pasos: 2,000,000
   - Learning rate: 0.0010

🧠 TRANSFERENCIA INTELIGENTE DE PESOS (Etapa 2):
🔄 fc1.weight: Padding inteligente ([256, 24] → [512, 32])
🔄 fc1.bias: Padding de bias (256 → 512)
🔄 fc2.weight: Padding inteligente ([256, 256] → [512, 512])
🔄 fc2.bias: Padding de bias (256 → 512)
🔄 out.weight: Padding inteligente ([2, 256] → [2, 512])
✅ out.bias: Copia directa ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.391 | 399.6 |    

[🎯] GROKKING ALCANZADO EN ETAPA 3 (n_bits=32) EN STEP 1
   Mejor test accuracy: 1.0000
💾 Checkpoints guardados: grok_model_stage3_n32_d512_adaptive.pth, grok_sae_stage3_n32_d512_adaptive.pth

======================================================================
🚀 ETAPA 4 ADAPTATIVA: n_bits=64, d_h=1024
======================================================================
🔧 Parámetros adaptativos calculados:
   - Tamaño entrenamiento: 1806
   - Weight decay: 0.1398
   - Límite de pasos: 2,000,000
   - Learning rate: 0.0010

🧠 TRANSFERENCIA INTELIGENTE DE PESOS (Etapa 3):
🔄 fc1.weight: Padding inteligente ([512, 32] → [1024, 64])
🔄 fc1.bias: Padding de bias (512 → 1024)
🔄 fc2.weight: Padding inteligente ([512, 512] → [1024, 1024])
🔄 fc2.bias: Padding de bias (512 → 1024)
🔄 out.weight: Padding inteligente ([2, 512] → [2, 1024])
✅ out.bias: Copia directa ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.445 | 901.8 |    

[🎯] GROKKING ALCANZADO EN ETAPA 4 (n_bits=64) EN STEP 1
   Mejor test accuracy: 1.0000
💾 Checkpoints guardados: grok_model_stage4_n64_d1024_adaptive.pth, grok_sae_stage4_n64_d1024_adaptive.pth

======================================================================
✅ CURRICULUM COMPLETADO
======================================================================

```
