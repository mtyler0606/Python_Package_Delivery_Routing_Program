import Package

class chained_hash_table_alternate:
    def __init__(self, initial_size=64):
        self.size = initial_size
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    def insert(self, key: int, item):
        """insert: inserts a value into the hash table.
        Time complexity: O(N), Space complexity: O(N) where N is the length of each bucket
        :param key: integer
        :param item: any type
        :raises: error if exact key and item are already in the hash table
        """
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

    # Alternate insert method. Takes list parameter and inserts Package type into hash table
    def insert_alternate_new_package(self, key, new_item: list):
        """insert: inserts a value into the hash table. This alternate version takes as a parameter and creates and
        inserts a Package type object into the hash table
            Time complexity: O(N), Space complexity: O(N) where N is the length of each bucket
            :param key: integer
            :param new_item: Package type only
            :raises: error if exact key and item are already in the hash table
        """
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
        if len(new_item) < 8:
            raise Exception("List must be at least 8 items long")
        package_item = Package.Package(int(new_item[0]), new_item[1], new_item[2], new_item[3], new_item[4], new_item[5], new_item[6], new_item[7])
        self.table[bucket].append([key, package_item])

    # Time O(N), Space O(N) where N is the length of each bucket
    def search(self, key):
        bucket = self.hash_function(key)
        for item in self.table[bucket]:
            if item[0] == key:
                return item[1]

    def alternate_search(self, key: int):
        bucket = self.hash_function(key)
        for item in self.table[bucket]:
            if item[0] == key:
                package = item[1]
                return package.address, package.delivery_deadline, package.city, package.zip_code, package.weight, package.status, package.time_delivered

    # Time O(N), Space O(N) where N is the length of each bucket
    def remove(self, key):
        bucket = self.hash_function(key)
        for item in self.table[bucket]:
            if item[0] == key:
                self.table[bucket].remove(item)

    def hash_function(self, key):
        return key % self.size
        # Alternate - return hash(key) % self.size

# This is a simpler version of the hash table.
# Because pacakge id's should be unique, there should be no collisions.
# This version should run faster because the insert and search functions are simpler, but it does not handle collisions
# I did not end up using it anywhere else in my program
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


