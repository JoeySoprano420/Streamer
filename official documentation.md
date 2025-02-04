# **Streamer Official Documentation**

## **📌 Introduction**
**Streamer** is a high-performance, binary-level programming language designed for ultra-fast execution, direct hardware optimization, and seamless embedded system integration. It combines **AOT compilation, directive assembly AST, and frame-by-frame JIT inference** to deliver unparalleled speed while maintaining a modern, high-level syntax.

---

## **🚀 Getting Started**
### **🔹 Installation**
#### **Using NuGet (For .NET Integration)**
```sh
 dotnet add package Streamer --version 1.0.0
```

#### **Using the Streamer SDK**
Download the **Streamer SDK** from the official repository and install it using:
```sh
 streamer install
```

### **🔹 Running Your First Streamer Program**
Save the following as `hello.stream`:
```streamer
 function main() {
     print("Hello, Streamer!");
 }
```
Compile and run using:
```sh
 streamer compile hello.stream -o hello.bin
 streamer run hello.bin
```

---

## **📌 Language Features**
### **🔹 Compilation Model**
| **Feature** | **Implementation** |
|------------|--------------------|
| **Compilation Type** | AOT + JIT (frame-by-frame inference) |
| **AST Representation** | Directive Assembly + WebAssembly |
| **Execution Model** | Superlative Binary Execution |
| **Memory Model** | Protocol-Based Register Allocation |
| **Security** | Built-in, grain-level security syntax |
| **Concurrency Handling** | Synchronization via sets |
| **Garbage Collection** | Imperative, event-driven GC |

### **🔹 Syntax Overview**
#### **Variables & Types**
```streamer
 let x: int = 42;
 let y: float = 3.14;
 let name: string = "Streamer";
```

#### **Functions**
```streamer
 function add(a: int, b: int) -> int {
     return a + b;
 }
```

#### **Control Flow**
```streamer
 if (x > 10) {
     print("X is greater than 10");
 } else {
     print("X is 10 or less");
 }
```

#### **Loops**
```streamer
 for (let i = 0; i < 5; i++) {
     print(i);
 }
```

#### **Concurrency**
```streamer
 set process_tasks {
     task_one();
     task_two();
 }
```

---

## **📌 Standard Library Overview**
### **🔹 Built-in Modules**
| **Module** | **Functionality** |
|------------|--------------------|
| `math` | Mathematical operations |
| `io` | Input/output operations |
| `net` | Networking utilities |
| `crypto` | Cryptographic functions |
| `fs` | File system handling |

### **🔹 Example: Using the `math` Module**
```streamer
 import math;
 let result = math.sqrt(25);
 print(result);
```

---

## **📌 Debugging & Optimization**
### **🔹 Debugging with Streamer Debugger**
Use the **Streamer Debugger (`streamerd`)** for binary-level profiling:
```sh
 streamer debug my_program.bin
```

### **🔹 Optimization Flags**
| **Flag** | **Effect** |
|---------|-----------|
| `-O1` | Basic optimizations |
| `-O2` | Advanced optimizations |
| `-O3` | Maximum performance optimizations |

Compile with optimizations:
```sh
 streamer compile my_code.stream -O3 -o my_code.bin
```

---

## **📌 Embedded & Systems-Level Support**
### **🔹 Supported Architectures**
✅ **x86_64**  
✅ **ARM & RISC-V**  
✅ **FPGAs & IoT Devices**  

Compile for embedded targets:
```sh
 streamer compile my_code.stream --target arm64 -o my_embedded.bin
```

---

## **📌 Security & Safe Execution**
### **🔹 Built-in Security Features**
- **Memory Safety** – No buffer overflows or memory leaks
- **Protocol-Based Access Control** – Register-level security management
- **Safe-Isolation Mode** – Execute untrusted code in a **sandboxed** environment

Enable safe isolation:
```sh
 streamer run my_code.bin --safe-mode
```

---

## **📌 Deployment & Integration**
### **🔹 Integrating with .NET**
Streamer integrates seamlessly with .NET applications:
```csharp
using Streamer;
class Program {
    static void Main() {
        Streamer.Execute("my_code.bin");
    }
}
```

### **🔹 Creating a WebAssembly Module**
Export to WebAssembly using:
```sh
 streamer compile my_code.stream --target wasm -o my_module.wasm
```

---

## **📌 Community & Support**

📌 **NuGet Package:** [Streamer on NuGet]  
📌 **Discord Community:** [Join the Discussion]  

🚀 **Welcome to the future of computing.** **Welcome to Streamer.**

