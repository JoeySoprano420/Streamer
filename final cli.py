import sys

def compile_streamer(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    # Convert to optimized binary
    binary_code = python_to_assembly(code)  

    with open(output_file, 'wb') as f:
        f.write(binary_code.encode())

if __name__ == "__main__":
    compile_streamer(sys.argv[1], sys.argv[2])
