import os
import subprocess

def safe_execute(binary_path):
    try:
        result = subprocess.run([binary_path], capture_output=True, timeout=2)
        print(result.stdout.decode())
    except subprocess.TimeoutExpired:
        print("[SAFE-ISOLATION] Execution Timeout. Binary Halted.")
    except Exception as e:
        print(f"[SAFE-ISOLATION] Error: {e}")

safe_execute("compiled_output.bin")
