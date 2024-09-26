from time import sleep
from Memory import Memory
from Memory import MainMemory
from Cache import Cache


# MemoryBus class that interacts with different memory types
class MemoryBus:
    def __init__(self, cache=None, main_memory=None):
        self.cache = cache if cache else Cache()
        self.main_memory = main_memory if main_memory else MainMemory()

    def read_memory(self, address):
        # Try reading from the cache first
        data = self.cache.read(address)
        if data is None:
            # If cache miss, read from main memory and update cache
            data = self.main_memory.read(address)
            self.cache.write(address, data)
        sleep(self.cache.access_time / 1000)
        return data

    def write_memory(self, address, data):
        # Write to both cache and main memory
        self.cache.write(address, data)
        self.main_memory.write(address, data)
        sleep(self.cache.access_time / 1000)