import lldb

def start_debugger(binary_path):
    debugger = lldb.SBDebugger.Create()
    target = debugger.CreateTargetWithFileAndArch(binary_path, lldb.LLDB_ARCH_DEFAULT)

    if not target:
        print("Failed to create target.")
        return

    process = target.LaunchSimple(None, None, "/")
    if not process:
        print("Failed to launch process.")
        return

    for thread in process:
        for frame in thread:
            print(f"Function: {frame.GetFunctionName()}")
            print(f"Registers: {frame.GetRegisters()}")
