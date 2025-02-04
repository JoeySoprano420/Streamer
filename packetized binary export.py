import hashlib

def secure_export(filename, data):
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    with open(filename, "wb") as f:
        f.write(hash_value.encode() + b'\n' + data.encode())

def secure_load(filename):
    with open(filename, "rb") as f:
        lines = f.readlines()
        stored_hash = lines[0].strip()
        code = b'\n'.join(lines[1:]).decode()

        # Validate integrity
        if stored_hash == hashlib.sha256(code.encode()).hexdigest().encode():
            print("[SECURITY] Hash Verified. Running Binary...")
            return code
        else:
            raise ValueError("[SECURITY] Hash Mismatch! File Integrity Compromised.")

# Example Usage
secure_export("program.spk", "MOV R1, #20\nADD R1, R2")
print(secure_load("program.spk"))
