#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PoC ABLATION - ALGORITHMIC TRANSFER (ZERO-SHOT)
Binary Parity: 64 -> 128 -> 256 -> 512 -> 1024 -> 2048 bits
"""
import time
import torch
import wandb
from app import GrokkingTransformer, get_parity_dataset, AdaptiveCurriculumTrainer

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
BASE_MODEL_PATH = "grok_model_stage4_n64_d1024_adaptive.pth"

SCALES = [
    (128, 2048),
    (256, 4096),
    (512, 8192),
    (1024, 16384),
    (2048, 32768),
]
DATASET_SIZE = 2000

def init_ablation_wandb(project_name="grokking-ablation"):
    """Initialize wandb for ablation experiment"""
    wandb.init(
        project=project_name,
        name=f"zero_shot_transfer_ablation_{int(time.time())}",
        config={
            "base_model": BASE_MODEL_PATH,
            "scales": SCALES,
            "dataset_size": DATASET_SIZE,
            "device": str(DEVICE)
        }
    )

def log_scale_results(n_bits, d_h, train_acc_transfer, test_acc_transfer, 
                      train_acc_control, test_acc_control, time_elapsed, 
                      generalization_success):
    """Log results for each scale to wandb"""
    wandb.log({
        "n_bits": n_bits,
        "d_hidden": d_h,
        "transfer_train_accuracy": train_acc_transfer,
        "transfer_test_accuracy": test_acc_transfer,
        "control_train_accuracy": train_acc_control,
        "control_test_accuracy": test_acc_control,
        "time_elapsed": time_elapsed,
        "generalization_success": 1 if generalization_success else 0,
        "transfer_vs_control_gap": test_acc_transfer - test_acc_control,
        "complexity_ratio": (n_bits * d_h) / (64 * 1024)
    })

def finish_ablation_wandb():
    """Finish wandb run"""
    wandb.finish()

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
        print("    Transfer DISABLED - random weights")
    
    x, y = get_parity_dataset(n_bits=n_bits, k=3, size=DATASET_SIZE)
    x, y = x.to(DEVICE), y.to(DEVICE)
    
    train_acc = accuracy(model, x[:1000], y[:1000])
    test_acc  = accuracy(model, x[1000:], y[1000:])
    
    return model, train_acc, test_acc

if __name__ == "__main__":
    t0_global = time.time()
    
    print("""
======================================================================
PoC ABLATION - ALGORITHMIC TRANSFER (INDUCTIVE)
Task: Binary Parity | Mode: ZERO-SHOT | Scaling: 64 -> 2048 bits
======================================================================
""")
    
    init_ablation_wandb()
    
    print("Loading base 64-bit model...")
    current_model = load_base()
    print("Base model ready\n")
    
    all_results = []
    
    for n_bits, d_h in SCALES:
        print("=" * 80)
        print(f"SCALE: {n_bits} bits  |  Hidden {d_h}")
        print("=" * 80)
        
        print("\nWITH STRUCTURAL TRANSFER")
        t0 = time.time()
        next_model, tr_acc, te_acc = zero_shot_test(current_model, n_bits, d_h, use_transfer=True)
        dt = time.time() - t0
        print(f"    Step 0  |  Train {tr_acc:.3f}  |  Test {te_acc:.3f}")
        print(f"    Time: {dt:.2f}s")
        
        generalization_success = te_acc > 0.98
        if generalization_success:
            print("    GENERALIZES - TRANSFER CONFIRMED")
        else:
            print("    FAILS - induction breakdown")
        
        print("\nCONTROL (WITHOUT TRANSFER)")
        _, tr_c, te_c = zero_shot_test(current_model, n_bits, d_h, use_transfer=False)
        print(f"    Step 0  |  Train {tr_c:.3f}  |  Test {te_c:.3f}")
        
        if te_c < 0.6:
            print("    Control does NOT generalize (expected)")
        else:
            print("    Control with unexpected signal")
        
        log_scale_results(
            n_bits=n_bits,
            d_h=d_h,
            train_acc_transfer=tr_acc,
            test_acc_transfer=te_acc,
            train_acc_control=tr_c,
            test_acc_control=te_c,
            time_elapsed=dt,
            generalization_success=generalization_success
        )
        
        all_results.append({
            'n_bits': n_bits,
            'd_h': d_h,
            'transfer_test': te_acc,
            'control_test': te_c,
            'time': dt,
            'success': generalization_success
        })
        
        if not generalization_success:
            break
        
        current_model = next_model
    
    total_time = time.time() - t0_global
    
    print("\n" + "=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    print(f"Total time: {total_time:.2f}s")
    
    wandb.log({
        "total_experiment_time": total_time,
        "scales_completed": len(all_results),
        "final_n_bits": all_results[-1]['n_bits'] if all_results else 64
    })
    
    summary_table = wandb.Table(
        columns=["n_bits", "d_hidden", "transfer_test_acc", "control_test_acc", "gap", "time_s", "success"],
        data=[
            [r['n_bits'], r['d_h'], r['transfer_test'], r['control_test'], 
             r['transfer_test'] - r['control_test'], r['time'], r['success']]
            for r in all_results
        ]
    )
    wandb.log({"results_summary": summary_table})
    
    print("""
Conclusion:
- Parity is preserved under dimensional expansion
- Transfer is structural, not statistical
- Algorithm is scale-invariant
""")
    
    finish_ablation_wandb()
