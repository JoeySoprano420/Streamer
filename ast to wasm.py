from wasmer import Store, Module, Instance

wasm_code = """
(module
  (func $main (export "main") (result i32)
    i32.const 42
  )
)
"""

# Compile & Execute WebAssembly
store = Store()
module = Module(store, wasm_code)
instance = Instance(module)
result = instance.exports.main()

print("Streamer WASM Output:", result)  # ✅ Returns 42!
