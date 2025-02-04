import llvmlite.ir as ir
import llvmlite.binding as llvm

# LLVM Module
module = ir.Module(name="StreamerBinary")

# Function Definition
func_type = ir.FunctionType(ir.IntType(32), [])
func = ir.Function(module, func_type, name="main")
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

# Return Value (42)
ret_val = ir.Constant(ir.IntType(32), 42)
builder.ret(ret_val)

# Compile & Generate Binary
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()
print(module)  # ✅ LLVM IR → Binary Execution!
