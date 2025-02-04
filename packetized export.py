import struct

def export_packet(filename, data):
    with open(filename, "wb") as f:
        f.write(struct.pack("I", len(data)))
        f.write(data.encode())

def load_packet(filename):
    with open(filename, "rb") as f:
        size = struct.unpack("I", f.read(4))[0]
        return f.read(size).decode()

# Example Usage
export_packet("program.spk", "print('Hello, Streamer')")
print(load_packet("program.spk"))
