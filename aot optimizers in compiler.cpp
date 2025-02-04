// Optimized AOT Compilation: Inline Functions & CPU-Specific Instructions
#define FORCE_INLINE __attribute__((always_inline))

FORCE_INLINE int fast_mul(int a, int b) {
    return __builtin_mul_overflow(a, b, &a) ? 0 : a;
}
