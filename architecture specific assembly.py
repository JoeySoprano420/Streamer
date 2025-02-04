import platform

def get_architecture():
    arch = platform.machine()
    if "x86" in arch:
        return "x86_64"
    elif "arm" in arch:
        return "ARM"
    elif "riscv" in arch:
        return "RISC-V"
    return "Unknown"

print(get_architecture())  # ✅ Dynamically detects CPU type
