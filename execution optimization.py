def inline_execution(op1, op2):
    return op1 + op2  # Inlining instead of function call overhead

# Example Usage
result = inline_execution(10, 20)
print(result)  # ✅ Outputs 30, without function call overhead
