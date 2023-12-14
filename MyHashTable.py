class MyChainedHashTable:
    def __init__(self, initial_size=64):
        self.size = initial_size
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    def insert(self, key, item):
        bucket = self.hash_function(key)
        # search all items in "bucket" to see if key has been used
        for item in self.table[bucket]:
            if item[0] == key:
                # raises exception if a new item is inserted with a key  that is already present
                if item[1] != item:
                    raise Exception("ID in use. ID's must be unique")
                # if key and item are inserted again, just returns with no effect
                else:
                    return
        # if key has not been used inserts item into hash table
        self.table[bucket].append([key, item])

    def search(self, key):
        bucket = self.hash_function(key)
        for item in self.table[bucket]:
            if item[0] == key:
                return item[1]

    def remove(self, key):
        bucket = self.hash_function(key)
        for item in self.table[bucket]:
            if item[0] == key:
                self.table[bucket].remove(item)

    def hash_function(self, key):
        return key % self.size
        # Alternate - return hash(key) % self.size


class MyHashTable:
    def __init__(self, initial_size=64):
        self.size = initial_size
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    def insert(self, key, item):
        bucket = self.hash_function(key)
        if len(self.table[bucket]) != 0:
            raise Exception("Key already in use. Remove previous item at key before inserting new item.")
        else:
            self.table[bucket] = item

    def search(self, key):
        if len(self.table[key]) != 0:
            return self.table[key]
        else:
            return "Item not found"

    def remove(self, key):
        self.table[key] = []

    def hash_function(self, key):
        return key % self.size
        # Alternate - return hash(key) % self.size


