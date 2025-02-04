def type_check(value, expected_type):
    if not isinstance(value, expected_type):
        raise TypeError(f"Expected {expected_type}, got {type(value)}")

# Example Usage
type_check(42, int)  # ✅ Pass
type_check("hello", int)  # ❌ Raises TypeError
