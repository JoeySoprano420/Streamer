from llvmlite import ir, binding

def generate_binary():
    module = ir.Module(name="streamer_module")
    func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
    func = ir.Function(module, func_type, name="add")

    entry_block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(entry_block)
    
    x, y = func.args
    result = builder.add(x, y)
    builder.ret(result)

    print(module)

generate_binary()
