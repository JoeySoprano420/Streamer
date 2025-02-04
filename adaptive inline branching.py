def inline_branching(value):
    return (value > 0) * value + (value <= 0) * 0  # No if-else branching!

# Example Usage
print(inline_branching(10))  # ✅ Outputs 10
print(inline_branching(-5))  # ✅ Outputs 0
