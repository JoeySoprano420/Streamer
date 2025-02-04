def process_data(x: int) -> int:
    if x < 0:
        warn("Negative value detected")  # Try-catch is for warnings only
    return x * 2
