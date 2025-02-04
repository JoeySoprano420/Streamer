# Define a function with explicit types
def add(x: int, y: int) -> int:
    return x + y

# Static variable declaration
num1: int = 10
num2: int = 20

# No dynamic typing allowed
result: int = add(num1, num2)
