import ast

class StreamerDirectiveAssembler:
    def __init__(self):
        self.directives = []

    def compile_node(self, node):
        if isinstance(node, ast.FunctionDef):
            self.directives.append(f".function {node.name}")
        elif isinstance(node, ast.Return):
            self.directives.append(f"  .ret {ast.literal_eval(node.value)}")

    def compile_code(self, source_code):
        tree = ast.parse(source_code)
        for node in tree.body:
            self.compile_node(node)
        return "\n".join(self.directives)

# Example Streamer Python-like Code
code = """
def main():
    return 42
"""

compiler = StreamerDirectiveAssembler()
directive_asm = compiler.compile_code(code)
print(directive_asm)
