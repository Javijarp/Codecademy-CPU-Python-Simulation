from Memory import Memory

# Cache class inheriting from Memory
class Cache(Memory):
    def __init__(self, size=4, access_time=10):
        super().__init__(name="Cache", access_time=access_time)
        self.size = size
        self.cache = {}  # Dictionary to store cache data with address keys
        self.exec_time = 0

    def read(self, address):
        if address in self.cache:
            super().read()
            print(f"Cache hit: data '{self.cache[address]}' from address {address}")
            return self.cache[address]
        else:
            super().read()
            print(f"Cache miss at address {address}")
            return None

    def write(self, address, data):
        if len(self.cache) < self.size:
            self.cache[address] = data
        else:
            # Simple replacement policy: remove the first inserted item (FIFO)
            removed_address = next(iter(self.cache))
            print(f"Cache full. Removing data from address {removed_address}")
            del self.cache[removed_address]
            self.cache[address] = data
        super().write()
        print(f"Cache updated: data '{data}' to address {address}")

    def display_cache(self):
        print("\nCache Contents:")
        for address, data in self.cache.items():
            print(f"Address {address}: {data}")

    def get_exec_time(self):
        return self.exec_time