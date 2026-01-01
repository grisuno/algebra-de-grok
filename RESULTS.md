```text
======================================================================
======================================================================
========================       T E S T       =========================
======================================================================
======================================================================

❯ python3 app.py

======================================================================
 Stage 1 Adaptative: n_bits=10, d_h=128
======================================================================
 Adaptative parameters:
   - Train size: 1037
   - Weight decay: 1.0000
   - Max steps: 600,000
   - Learning rate: 0.0010

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 0.51 | 0.48 | 1.976 | 4.0 |    
2000     | 1.00 | 1.00 | 0.012 | 36.3 |    

[+] GROKKING found in stage 1 (n_bits=10) in STEP 2000
   Best test accuracy: 1.0000
💾 Checkpoints saved: grok_model_stage1_n10_d128_adaptive.pth, grok_sae_stage1_n10_d128_adaptive.pth

======================================================================
 Stage 2 Adaptative: n_bits=24, d_h=256
======================================================================
 Adaptative parameters:
   - Train size: 1393
   - Weight decay: 0.4564
   - Max steps: 1,521,631
   - Learning rate: 0.0010

[+] Structural Weight Transfer (Stage 1):
 - fc1.weight: Smart Padding ([128, 10] → [256, 24])
 - fc1.bias: Padding of bias (128 → 256)
 - fc2.weight: Smart Padding ([128, 128] → [256, 256])
 - fc2.bias: Padding of bias (128 → 256)
 - out.weight: Smart Padding ([2, 128] → [2, 256])
 out.bias: Direct copy ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.246 | 146.2 |    

[+] GROKKING found in stage 2 (n_bits=24) in STEP 1
   Best test accuracy: 1.0000
💾 Checkpoints saved: grok_model_stage2_n24_d256_adaptive.pth, grok_sae_stage2_n24_d256_adaptive.pth

======================================================================
 Stage 3 Adaptative: n_bits=32, d_h=512
======================================================================
 Adaptative parameters:
   - Train size: 1513
   - Weight decay: 0.2795
   - Max steps: 2,000,000
   - Learning rate: 0.0010

[+] Structural Weight Transfer (Stage 2):
 - fc1.weight: Smart Padding ([256, 24] → [512, 32])
 - fc1.bias: Padding of bias (256 → 512)
 - fc2.weight: Smart Padding ([256, 256] → [512, 512])
 - fc2.bias: Padding of bias (256 → 512)
 - out.weight: Smart Padding ([2, 256] → [2, 512])
 out.bias: Direct copy ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.152 | 402.8 |    

[+] GROKKING found in stage 3 (n_bits=32) in STEP 1
   Best test accuracy: 1.0000
💾 Checkpoints saved: grok_model_stage3_n32_d512_adaptive.pth, grok_sae_stage3_n32_d512_adaptive.pth

======================================================================
 Stage 4 Adaptative: n_bits=64, d_h=1024
======================================================================
 Adaptative parameters:
   - Train size: 1806
   - Weight decay: 0.1398
   - Max steps: 2,000,000
   - Learning rate: 0.0010

[+] Structural Weight Transfer (Stage 3):
 - fc1.weight: Smart Padding ([512, 32] → [1024, 64])
 - fc1.bias: Padding of bias (512 → 1024)
 - fc2.weight: Smart Padding ([512, 512] → [1024, 1024])
 - fc2.bias: Padding of bias (512 → 1024)
 - out.weight: Smart Padding ([2, 512] → [2, 1024])
 out.bias: Direct copy ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.297 | 901.7 |    

[+] GROKKING found in stage 4 (n_bits=64) in STEP 1
   Best test accuracy: 0.9990
💾 Checkpoints saved: grok_model_stage4_n64_d1024_adaptive.pth, grok_sae_stage4_n64_d1024_adaptive.pth

======================================================================
CV Success
======================================================================
❯ python3 app.py

======================================================================
 Stage 1 Adaptative: n_bits=10, d_h=128
======================================================================
 Adaptative parameters:
   - Train size: 1037
   - Weight decay: 1.0000
   - Max steps: 600,000
   - Learning rate: 0.0010

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 0.51 | 0.54 | 2.113 | 4.0 |    
2000     | 1.00 | 1.00 | 0.008 | 26.6 |    

[+] GROKKING found in stage 1 (n_bits=10) in STEP 2000
   Best test accuracy: 1.0000
[+] Checkpoints saved: grok_model_stage1_n10_d128_adaptive.pth, grok_sae_stage1_n10_d128_adaptive.pth

======================================================================
 Stage 2 Adaptative: n_bits=24, d_h=256
======================================================================
 Adaptative parameters:
   - Train size: 1393
   - Weight decay: 0.4564
   - Max steps: 1,521,631
   - Learning rate: 0.0010

[+] Structural Weight Transfer (Stage 1):
 - fc1.weight: Smart Padding ([128, 10] → [256, 24])
 - fc1.bias: Padding of bias (128 → 256)
 - fc2.weight: Smart Padding ([128, 128] → [256, 256])
 - fc2.bias: Padding of bias (128 → 256)
 - out.weight: Smart Padding ([2, 128] → [2, 256])
 out.bias: Direct copy ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.517 | 139.7 |    

[+] GROKKING found in stage 2 (n_bits=24) in STEP 1
   Best test accuracy: 1.0000
[+] Checkpoints saved: grok_model_stage2_n24_d256_adaptive.pth, grok_sae_stage2_n24_d256_adaptive.pth

======================================================================
 Stage 3 Adaptative: n_bits=32, d_h=512
======================================================================
 Adaptative parameters:
   - Train size: 1513
   - Weight decay: 0.2795
   - Max steps: 2,000,000
   - Learning rate: 0.0010

[+] Structural Weight Transfer (Stage 2):
 - fc1.weight: Smart Padding ([256, 24] → [512, 32])
 - fc1.bias: Padding of bias (256 → 512)
 - fc2.weight: Smart Padding ([256, 256] → [512, 512])
 - fc2.bias: Padding of bias (256 → 512)
 - out.weight: Smart Padding ([2, 256] → [2, 512])
 out.bias: Direct copy ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.480 | 399.7 |    

[+] GROKKING found in stage 3 (n_bits=32) in STEP 1
   Best test accuracy: 1.0000
[+] Checkpoints saved: grok_model_stage3_n32_d512_adaptive.pth, grok_sae_stage3_n32_d512_adaptive.pth

======================================================================
 Stage 4 Adaptative: n_bits=64, d_h=1024
======================================================================
 Adaptative parameters:
   - Train size: 1806
   - Weight decay: 0.1398
   - Max steps: 2,000,000
   - Learning rate: 0.0010

[+] Structural Weight Transfer (Stage 3):
 - fc1.weight: Smart Padding ([512, 32] → [1024, 64])
 - fc1.bias: Padding of bias (512 → 1024)
 - fc2.weight: Smart Padding ([512, 512] → [1024, 1024])
 - fc2.bias: Padding of bias (512 → 1024)
 - out.weight: Smart Padding ([2, 512] → [2, 1024])
 out.bias: Direct copy ([2])

Step     | T-Acc  | V-Acc  | ψ      | LC     | Status      
--------------------------------------------------------------------------------
1        | 1.00 | 1.00 | 2.478 | 900.8 |    

[+] GROKKING found in stage 4 (n_bits=64) in STEP 1
   Best test accuracy: 1.0000
[+] Checkpoints saved: grok_model_stage4_n64_d1024_adaptive.pth, grok_sae_stage4_n64_d1024_adaptive.pth

======================================================================
CV Success
======================================================================



======================================================================
======================================================================
========================   A B L A T I O N   =========================
======================================================================
======================================================================


❯ python3 test_wandb.py

======================================================================
PoC ABLATION - ALGORITHMIC TRANSFER (INDUCTIVE)
Task: Binary Parity | Mode: ZERO-SHOT | Scaling: 64 -> 2048 bits

Loading base 64-bit model...
Base model ready

================================================================================
SCALE: 128 bits  |  Hidden 2048
================================================================================

WITH STRUCTURAL TRANSFER

[+] Structural Weight Transfer (Stage 0):
 - fc1.weight: Smart Padding ([1024, 64] -> [2048, 128])
 - fc1.bias: Padding of bias (1024 -> 2048)
 - fc2.weight: Smart Padding ([1024, 1024] -> [2048, 2048])
 - fc2.bias: Padding of bias (1024 -> 2048)
 - out.weight: Smart Padding ([2, 1024] -> [2, 2048])
 out.bias: Direct copy ([2])
    Step 0  |  Train 1.000  |  Test 1.000
    Time: 0.13s
    GENERALIZES - TRANSFER CONFIRMED

CONTROL (WITHOUT TRANSFER)
    Transfer DISABLED - random weights
    Step 0  |  Train 0.495  |  Test 0.494
    Control does NOT generalize (expected)
================================================================================
SCALE: 256 bits  |  Hidden 4096
================================================================================

WITH STRUCTURAL TRANSFER

[+] Structural Weight Transfer (Stage 0):
 - fc1.weight: Smart Padding ([2048, 128] -> [4096, 256])
 - fc1.bias: Padding of bias (2048 -> 4096)
 - fc2.weight: Smart Padding ([2048, 2048] -> [4096, 4096])
 - fc2.bias: Padding of bias (2048 -> 4096)
 - out.weight: Smart Padding ([2, 2048] -> [2, 4096])
 out.bias: Direct copy ([2])
    Step 0  |  Train 1.000  |  Test 1.000
    Time: 0.35s
    GENERALIZES - TRANSFER CONFIRMED

CONTROL (WITHOUT TRANSFER)
    Transfer DISABLED - random weights
    Step 0  |  Train 0.521  |  Test 0.496
    Control does NOT generalize (expected)
================================================================================
SCALE: 512 bits  |  Hidden 8192
================================================================================

WITH STRUCTURAL TRANSFER

[+] Structural Weight Transfer (Stage 0):
 - fc1.weight: Smart Padding ([4096, 256] -> [8192, 512])
 - fc1.bias: Padding of bias (4096 -> 8192)
 - fc2.weight: Smart Padding ([4096, 4096] -> [8192, 8192])
 - fc2.bias: Padding of bias (4096 -> 8192)
 - out.weight: Smart Padding ([2, 4096] -> [2, 8192])
 out.bias: Direct copy ([2])
    Step 0  |  Train 1.000  |  Test 1.000
    Time: 1.21s
    GENERALIZES - TRANSFER CONFIRMED

CONTROL (WITHOUT TRANSFER)
    Transfer DISABLED - random weights
    Step 0  |  Train 0.504  |  Test 0.502
    Control does NOT generalize (expected)
================================================================================
SCALE: 1024 bits  |  Hidden 16384
================================================================================

WITH STRUCTURAL TRANSFER

[+] Structural Weight Transfer (Stage 0):
 - fc1.weight: Smart Padding ([8192, 512] -> [16384, 1024])
 - fc1.bias: Padding of bias (8192 -> 16384)
 - fc2.weight: Smart Padding ([8192, 8192] -> [16384, 16384])
 - fc2.bias: Padding of bias (8192 -> 16384)
 - out.weight: Smart Padding ([2, 8192] -> [2, 16384])
 out.bias: Direct copy ([2])
    Step 0  |  Train 1.000  |  Test 1.000
    Time: 4.45s
    GENERALIZES - TRANSFER CONFIRMED

CONTROL (WITHOUT TRANSFER)
    Transfer DISABLED - random weights
    Step 0  |  Train 0.497  |  Test 0.499
    Control does NOT generalize (expected)
================================================================================
SCALE: 2048 bits  |  Hidden 32768
================================================================================

WITH STRUCTURAL TRANSFER

[+] Structural Weight Transfer (Stage 0):
 - fc1.weight: Smart Padding ([16384, 1024] -> [32768, 2048])
 - fc1.bias: Padding of bias (16384 -> 32768)
 - fc2.weight: Smart Padding ([16384, 16384] -> [32768, 32768])
 - fc2.bias: Padding of bias (16384 -> 32768)
 - out.weight: Smart Padding ([2, 16384] -> [2, 32768])
 out.bias: Direct copy ([2])
    Step 0  |  Train 1.000  |  Test 1.000
    Time: 39.75s
    GENERALIZES - TRANSFER CONFIRMED

CONTROL (WITHOUT TRANSFER)
    Transfer DISABLED - random weights
    Step 0  |  Train 0.508  |  Test 0.518
    Control does NOT generalize (expected)

================================================================================
FINAL RESULTS
================================================================================
Total time: 88.87s

Conclusion:
- Parity is preserved under dimensional expansion
- Transfer is structural, not statistical
- Algorithm is scale-invariant

wandb: 
wandb: Run history:
wandb:       complexity_ratio ▁▁▁▃█
wandb:  control_test_accuracy ▁▂▃▂█
wandb: control_train_accuracy ▁█▃▂▄
wandb:               d_hidden ▁▁▂▄█
wandb:           final_n_bits ▁
wandb: generalization_success ▁▁▁▁▁
wandb:                 n_bits ▁▁▂▄█
wandb:       scales_completed ▁
wandb:           time_elapsed ▁▁▁▂█
wandb:  total_experiment_time ▁
wandb:                     +3 ...
wandb: 
wandb: Run summary:
wandb:       complexity_ratio 1024
wandb:  control_test_accuracy 0.518
wandb: control_train_accuracy 0.508
wandb:               d_hidden 32768
wandb:           final_n_bits 2048
wandb: generalization_success 1
wandb:                 n_bits 2048
wandb:       scales_completed 5
wandb:           time_elapsed 39.74625
wandb:  total_experiment_time 88.86953

```
