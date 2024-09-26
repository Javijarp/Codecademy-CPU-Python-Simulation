from time import sleep

# Memory class used to create different memory types within the simulation
class Memory:
    def __init__(self, name="", access_time=0):
        self.name = name
        self.access_time = access_time
        self.exec_time = 0

    # Output read message and update process execution time
    def read(self, output=True):
        if output:
            print(f" - {self.name} read: ", end="")
        self.exec_time += self.access_time

    # Output write message and update process execution time
    def write(self, output=True):
        if output:
            print(f" - {self.name} write: ", end="")
        self.exec_time += self.access_time

    # Return total execution time
    def get_exec_time(self):
        return self.exec_time


# MainMemory class used for the main memory data storage
class MainMemory(Memory):
    def __init__(self):
        super().__init__(name="Main Memory", access_time=30)
        self.data = [""] * 16  # Initialize memory with 16 empty slots

    # Return data from main memory address
    def read(self, address):
        if 0 <= address < len(self.data):
            data = self.data[address]
            super().read()
            print(f"data '{data}' from address {address}")
            return data
        else:
            raise ValueError("Address out of range")

    # Write data to main memory address
    def write(self, address, data):
        if 0 <= address < len(self.data):
            self.data[address] = data
            super().write()
            print(f"data '{data}' to address {address}")
        else:
            raise ValueError("Address out of range")
    
    # Display a portion of the memory for debugging
    def display_memory(self, start=0, end=10):
        if end > len(self.data):
            end = len(self.data)
        print("\nMain Memory Contents:")
        for i in range(start, end):
            print(f"Address {i}: {self.data[i]}")