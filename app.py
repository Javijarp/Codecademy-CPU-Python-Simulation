from time import sleep
from Memory import MainMemory
from MemoryBus import MemoryBus
from Cache import Cache
from CPU import CPU

# Sample program to demonstrate CPU with Cache and Main Memory
main_memory = MainMemory()
cache = Cache(size=4, access_time=10)
memory_bus = MemoryBus(cache=cache, main_memory=main_memory)
cpu = CPU(memory_bus)

# Sample instruction set
program = [
    ("LOAD", 0, 0),   
    ("ADD", 0, 5),     
    ("STORE", 0, 1),   
    ("LOAD", 1, 1),    
    ("SUB", 1, 2),     
    ("HALT",)          
]

# Load initial values into memory for testing
memory_bus.write_memory(0, 10)

# Interactive loop for entering instructions
print("\nCPU Simulator Interactive Mode")
print("Enter instructions in the format: OPCODE ARG1 ARG2")
print("Supported Instructions: LOAD, STORE, ADD, SUB, MULT, DIVI, HALT")
print("Examples: LOAD 0 0, ADD 0 5, MULT 0 5, STORE 0 1, HALT")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("Enter instruction: ").strip()
    if user_input.lower() == 'exit':
        break

    # Parse user input into opcode and arguments
    try:
        parts = user_input.split()
        opcode = parts[0].upper()
        args = [int(arg) for arg in parts[1:]]
        instruction = (opcode, *args)
        if not cpu.execute(instruction):
            break
    except Exception as e:
        print(f"Error: {e}. Please enter a valid instruction format.")

# Execute the program
# print("\nExecuting program...\n")
# for instruction in program:
#     if not cpu.execute(instruction):
#         break

# Display the final state of cache, memory, and registers
cache.display_cache()
main_memory.display_memory(0, 10)
print(f"\nFinal Registers: {cpu.registers}")
print(f"Total execution time: {main_memory.get_exec_time() + cache.get_exec_time()} cycles")