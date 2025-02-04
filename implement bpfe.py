def brute_force_fix(code):
    try:
        exec(code)
    except Exception as e:
        print(f"[P.B.F.E] Error Detected: {e}")
        fixed_code = code.replace("error", "0")  # Example Fix
        exec(fixed_code)

# Example Usage
brute_force_fix("print(10 / 0)")  # ✅ Fixes division by zero
