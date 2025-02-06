import llvmlite.ir as ir
import llvmlite.binding as llvm

# Create a new LLVM module
module = ir.Module(name="simple_module")

# Define the function type: int -> int -> int (takes two integers, returns an integer)
func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
func = ir.Function(module, func_type, name="add")

# Create a basic block in the function
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

# Get the function arguments
arg1, arg2 = func.args

# Add the two arguments and return the result
result = builder.add(arg1, arg2)
builder.ret(result)

# Print the generated LLVM IR
print(module)

# If you want to execute it, you can use llvmlite.binding to create a JIT engine (optional)
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Create a target machine
target_machine = llvm.Target.from_default_triple().create_target_machine()

# Compile the module to machine code
with open("add.o", "wb") as f:
    f.write(target_machine.emit_object(module))

print("LLVM IR and object file generated successfully!")

import ast
import llvmlite.ir as ir
import llvmlite.binding as llvm

class PythonToLLVMCompiler:
    def __init__(self):
        self.module = ir.Module(name="PythonModule")
        self.builder = None
        self.function = None
        self.local_vars = {}  # Local variables storage
        self.exception_block = None

    def compile(self, code):
        tree = ast.parse(code)
        for node in tree.body:
            self.compile_node(node)
        return str(self.module)

    def compile_node(self, node):
        """Dispatch to the appropriate function for compiling each AST node."""
        if isinstance(node, ast.FunctionDef):
            self.compile_function(node)
        elif isinstance(node, ast.Assign):
            self.compile_assign(node)
        elif isinstance(node, ast.Expr):
            self.compile_expr(node)
        elif isinstance(node, ast.Return):
            self.compile_return(node)
        elif isinstance(node, ast.If):
            self.compile_if(node)
        elif isinstance(node, ast.For):
            self.compile_for(node)
        elif isinstance(node, ast.List):
            self.compile_list(node)
        elif isinstance(node, ast.Dict):
            self.compile_dict(node)
        elif isinstance(node, ast.Try):
            self.compile_try(node)
        elif isinstance(node, ast.ListComp):
            self.compile_list_comprehension(node)
        elif isinstance(node, ast.Tuple):
            self.compile_tuple(node)
        elif isinstance(node, ast.Set):
            self.compile_set(node)

    def compile_function(self, node):
        """Compile a function definition to LLVM IR."""
        # Define the function signature (using int for simplicity)
        arg_types = [ir.IntType(32)] * len(node.args.args)  # assuming all arguments are integers for simplicity
        func_type = ir.FunctionType(ir.IntType(32), arg_types)
        self.function = ir.Function(self.module, func_type, name=node.name)
        
        # Create the entry block and builder
        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        
        # Compile the body of the function
        for n in node.body:
            self.compile_node(n)
        
        # Return statement (if present)
        self.builder.ret(self.builder.load(self.function.args[0]))  # Just return the first argument for now.

    def compile_assign(self, node):
        """Compile assignments."""
        var_name = node.targets[0].id
        value = self.compile_expr(node.value)
        self.local_vars[var_name] = value  # Store the value in the local_vars dictionary
        self.builder.store(value, self.function.args[0])  # Store value into argument (expand for local variables).

    def compile_expr(self, node):
        """Compile expressions."""
        if isinstance(node, ast.BinOp):
            left = self.compile_expr(node.left)
            right = self.compile_expr(node.right)
            if isinstance(node.op, ast.Add):
                return self.builder.add(left, right)
            elif isinstance(node.op, ast.Sub):
                return self.builder.sub(left, right)
            elif isinstance(node.op, ast.Mult):
                return self.builder.mul(left, right)
            elif isinstance(node.op, ast.Div):
                return self.builder.sdiv(left, right)
        elif isinstance(node, ast.Constant):
            return ir.Constant(ir.IntType(32), node.value)
        elif isinstance(node, ast.Name):
            return self.local_vars.get(node.id, ir.Constant(ir.IntType(32), 0))  # Load local variable
        elif isinstance(node, ast.List):
            return self.compile_list(node)
        elif isinstance(node, ast.Dict):
            return self.compile_dict(node)
        elif isinstance(node, ast.Tuple):
            return self.compile_tuple(node)
        elif isinstance(node, ast.Set):
            return self.compile_set(node)

    def compile_return(self, node):
        """Handle return statements."""
        value = self.compile_expr(node.value)
        self.builder.ret(value)

    def compile_if(self, node):
        """Handle if-else logic."""
        cond = self.compile_expr(node.test)
        true_block = self.function.append_basic_block(name="true")
        false_block = self.function.append_basic_block(name="false")
        merge_block = self.function.append_basic_block(name="merge")

        self.builder.cbranch(cond, true_block, false_block)

        # True block
        self.builder.position_at_end(true_block)
        self.builder.branch(merge_block)

        # False block
        self.builder.position_at_end(false_block)
        self.builder.branch(merge_block)

        # Merge block
        self.builder.position_at_end(merge_block)

    def compile_for(self, node):
        """Handle for loops."""
        loop_block = self.function.append_basic_block(name="loop")
        after_block = self.function.append_basic_block(name="after")
        
        # Just an example: iterate a range of 10
        range_start = ir.Constant(ir.IntType(32), 0)
        range_end = ir.Constant(ir.IntType(32), 10)
        counter = ir.Alloca(self.builder.function.args[0].type)  # Allocate space for counter
        self.builder.store(range_start, counter)
        
        self.builder.branch(loop_block)

        # Loop body
        self.builder.position_at_end(loop_block)
        counter_value = self.builder.load(counter)
        self.builder.add(counter_value, ir.Constant(ir.IntType(32), 1))
        self.builder.store(counter_value, counter)
        self.builder.branch(after_block)

        self.builder.position_at_end(after_block)

    def compile_list(self, node):
        """Compile a Python list."""
        elements = [self.compile_expr(e) for e in node.elts]
        # Here we would generate an array in LLVM IR. For simplicity, we simulate it with a pointer to elements.
        list_type = ir.PointerType(ir.IntType(32))  # Type for list elements (int in this case)
        return elements  # In real code, create and return a pointer to the list

    def compile_dict(self, node):
        """Compile a Python dictionary."""
        elements = {self.compile_expr(k): self.compile_expr(v) for k, v in zip(node.keys, node.values)}
        # In a real implementation, we'd create a struct or other data structure in LLVM to hold this.
        dict_type = ir.StructType([ir.IntType(32), ir.IntType(32)])  # Just a simple example for key-value pairs
        return elements

    def compile_try(self, node):
        """Compile try-except-finally."""
        # Setup the exception handling block
        exception_block = self.function.append_basic_block(name="exception")
        merge_block = self.function.append_basic_block(name="merge")

        self.builder.invoke(self.compile_expr(node.body[0]), [], exception_block, merge_block)

        # Exception handling block
        self.builder.position_at_end(exception_block)
        self.builder.branch(merge_block)

        # Merge block
        self.builder.position_at_end(merge_block)

    def compile_list_comprehension(self, node):
        """Compile a list comprehension."""
        # List comprehension needs iteration and conditional checks.
        comprehension_list = [self.compile_expr(e) for e in node.elt]
        return comprehension_list

    def compile_tuple(self, node):
        """Compile a tuple."""
        elements = [self.compile_expr(e) for e in node.elts]
        # Tuples are simple structs in LLVM.
        tuple_type = ir.StructType([ir.IntType(32)] * len(elements))
        return elements

    def compile_set(self, node):
        """Compile a set."""
        elements = [self.compile_expr(e) for e in node.elts]
        set_type = ir.ArrayType(ir.IntType(32), len(elements))  # Using array to simulate set
        return elements

# Example usage
compiler = PythonToLLVMCompiler()
code = """
def main():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        return 42
    return 0
"""
llvm_ir = compiler.compile(code)
print(llvm_ir)
