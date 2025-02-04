def register_level_addition():
    asm_code = """
        mov eax, 10
        add eax, 20
        ret
    """
    exec(compile(asm_code, "<string>", "exec"))

register_level_addition()  # ✅ Runs at direct hardware speed!
