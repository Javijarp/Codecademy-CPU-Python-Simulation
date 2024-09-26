from time import sleep
from Memory import MainMemory
from MemoryBus import MemoryBus
from Cache import Cache


# CPU class that uses the MemoryBus to execute instructions
class CPU:
    def __init__(self, memory_bus):
        self.memory_bus = memory_bus
        self.registers = [0] * 4  # Simple CPU with 4 general-purpose registers

    def execute(self, instruction):
        opcode, *args = instruction

        if opcode == "LOAD":
            register, address = args
            data = self.memory_bus.read_memory(address)
            self.registers[register] = data
            print(f"Executed LOAD: Register {register} = {data}")

        elif opcode == "STORE":
            register, address = args
            data = self.registers[register]
            self.memory_bus.write_memory(address, data)
            print(f"Executed STORE: Memory[{address}] = {data}")

        elif opcode == "ADD":
            register, value = args
            self.registers[register] += int(value)
            print(f"Executed ADD: Register {register} += {value}")

        elif opcode == "SUB":
            register, value = args
            self.registers[register] -= int(value)
            print(f"Executed SUB: Register {register} -= {value}")

        elif opcode == "MULT":
            register, value = args
            self.registers[register] *= int(value)
            print(f"Executed MUL: Register {register} *= {value}")

        elif opcode == "DIVI":
            register, value = args
            if int(value) == 0:
                print("Error: Division by zero")
            else:
                self.registers[register] //= int(value)
                print(f"Executed DIV: Register {register} /= {value}")

        elif opcode == "HALT":
            print("Execution halted.")
            return False

        else:
            print(f"Unknown instruction: {opcode}")

        return True