.section .text
.global _start
_start:
    li a0, 42        # Load immediate 42 into register a0
    li a7, 93        # Exit syscall
    ecall            # Execute system call
