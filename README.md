# CPU Simulator

A Python-based CPU simulator that mimics the basic operations of a CPU, including instruction execution, memory access with caching, and register manipulation. This simulator allows users to enter assembly-like instructions interactively and see how the CPU processes them step-by-step.

## Features

- **Memory Management:** Simulates main memory and a cache system with configurable access times.
- **Instruction Set:** Supports a variety of instructions including arithmetic, branching, memory loading, and storing.
- **Interactive Mode:** Users can input instructions directly and see real-time execution.
- **Cache System:** Includes a cache with basic enable/disable and flush functionalities.
- **Error Handling:** Provides basic error handling for incorrect inputs or invalid operations.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/cpu-simulator.git
   cd cpu-simulator
   ```
1. Run the CPU simulation:

   ```bash
   python app.py
   ```

## How to Use

Once you run the script, the simulator will enter interactive mode where you can enter instructions directly.

### Instruction Format

- Instructions follow the format: `OPCODE ARG1 ARG2 ARG3`
- The simulator supports the following instructions:

| Instruction | Operands              | Description                                                |
|-------------|-----------------------|------------------------------------------------------------|
| `ADD`       | `Rd, Rs, Rt`          | Adds the values of `Rs` and `Rt` registers, storing in `Rd`. |
| `ADDI`      | `Rt, Rs, immd`        | Adds an immediate value to `Rs` and stores in `Rt`.        |
| `SUB`       | `Rd, Rs, Rt`          | Subtracts `Rt` from `Rs` and stores the result in `Rd`.    |
| `SLT`       | `Rd, Rs, Rt`          | Sets `Rd` to 1 if `Rs` < `Rt`, else sets to 0.             |
| `BNE`       | `Rs, Rt, offset`      | Branches if `Rs` != `Rt` by offset multiplied by 4.        |
| `J`         | `target`              | Jumps to the target address multiplied by 4.               |
| `JAL`       | `target`              | Jumps to the target address, saving the return address in `R7`. |
| `LW`        | `Rt, offset(Rs)`      | Loads a word from memory into `Rt` using base `Rs`.        |
| `SW`        | `Rt, offset(Rs)`      | Stores a word from `Rt` into memory at `Rs` + offset.      |
| `STORE`     | `value, address`      | Stores a constant value directly into a specified memory address. |
| `CACHE`     | `code`                | Cache operations: 0 = off, 1 = on, 2 = flush.              |
| `HALT`      | -                     | Stops execution.                                           |

### Examples of Usage

1. **Adding Two Numbers and Storing the Result:**

    ```plaintext
    ADD 0 1 2       # Register 0 = Register 1 + Register 2
    STORE 15 100    # Store constant 15 in memory address 100
    HALT            # Stop the CPU
    ```

2. **Using Memory Load and Store:**

    ```plaintext
    LW 1 0 0        # Load memory address 0 into Register 1
    SW 1 4 0        # Store Register 1 into memory address (Register 0 + 4)
    HALT
    ```

3. **Conditional Branching:**

    ```plaintext
    SLT 2 0 1       # Register 2 = 1 if Register 0 < Register 1 else 0
    BNE 0 1 2       # Branch to offset if Register 0 != Register 1
    HALT
    ```

### Understanding the Components

1. **Memory**: 
    - The `MainMemory` class simulates main memory with read and write capabilities.
    - The `Cache` class provides a fast-access storage with configurable size and access time, with hit and miss simulation.

2. **MemoryBus**: 
    - Manages data flow between the CPU, cache, and main memory.

3. **CPU**: 
    - Executes the instructions provided by the user.
    - Manages registers, program counter, and handles branching, arithmetic, and memory access operations.

4. **Interactive Mode**:
    - Users can enter instructions one by one and see the results immediately.
    - Enter `HALT` or `exit` to stop the simulator.

### Sample Session

Here's what a typical session might look like:

```plaintext
CPU Simulator Interactive Mode
Enter instructions in the format: OPCODE ARG1 ARG2 ARG3
Supported Instructions: ADD, ADDI, SUB, SLT, BNE, J, JAL, LW, SW, STORE, CACHE, HALT
Examples: ADD 0 1 2, ADDI 1 0 10, SLT 2 0 1, LW 0 0 1, STORE 20 100, HALT
Type 'exit' to stop.

> ADD 0 1 2
Executed ADD: Register 0 = Register 1 + Register 2
> STORE 20 100
Executed STORE: Stored value 20 at memory address 100
> HALT
Execution halted.

