import ast

def python_to_assembly(code):
    tree = ast.parse(code)
    
    assembly = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            assembly.append(f"{node.name}:")
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            assembly.append("    ADD RAX, RBX")
        elif isinstance(node, ast.Return):
            assembly.append("    RET")
    
    return "\n".join(assembly)

code = "def add(x: int, y: int) -> int: return x + y"
print(python_to_assembly(code))
