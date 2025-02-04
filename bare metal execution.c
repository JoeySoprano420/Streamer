// Streamer in ARM Assembly (Bare-Metal)
.section .text
.global _start

_start:
    MOV R0, #1         // Load 1 into register R0
    ADD R1, R0, #42    // Add 42 to R0, store in R1
    B _start           // Loop infinitely (bare-metal)
