import ctypes

class MemoryAllocator:
    def __init__(self):
        self.memory = {}

    def allocate(self, var_name, value):
        addr = id(value)  # Simulated register address
        self.memory[var_name] = addr
        print(f"Allocated {var_name} -> Register Address: {addr}")

    def deallocate(self, var_name):
        if var_name in self.memory:
            del self.memory[var_name]
            print(f"Deallocated {var_name}")

# Example Usage
mem_alloc = MemoryAllocator()
mem_alloc.allocate("x", 42)
mem_alloc.deallocate("x")
