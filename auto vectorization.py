import numpy as np

def vectorized_addition(a, b):
    a_vec = np.array(a, dtype=np.float32)
    b_vec = np.array(b, dtype=np.float32)
    return np.add(a_vec, b_vec)

# Example Usage
a = [1.0, 2.0, 3.0, 4.0]
b = [5.0, 6.0, 7.0, 8.0]
result = vectorized_addition(a, b)

print(result)  # ✅ SIMD Optimized Computation
