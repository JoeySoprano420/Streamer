class StreamerASM:
    def __init__(self):
        self.asm_code = []

    def add_instruction(self, instruction):
        self.asm_code.append(instruction)

    def compile_to_binary(self):
        binary_output = "\n".join(self.asm_code).encode()
        return binary_output

# Example Usage
streamer_asm = StreamerASM()
streamer_asm.add_instruction("MOV R1, #10")
streamer_asm.add_instruction("ADD R1, R2")
binary_code = streamer_asm.compile_to_binary()

with open("output.sbin", "wb") as f:
    f.write(binary_code)
