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


class MyChainedHashTable:
    def __init__(self, initial_size=64):
        self.size = initial_size
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    def insert(self, key, item):
        bucket = self.hash_function(key)
        for item in self.table[bucket]:
            if item[0] == key:
                if item[1] != item:
                    raise Exception("ID in use. ID's must be unique")
                else:
                    return
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




bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]
'''
myHash = MyChainedHashTable(10)

print("\nInsert:")
myHash.insert(bestMovies[0][0], bestMovies[0][1])  # 2nd bucket; Key=1, item="CITIZEN KANE - 1941"
print(myHash.table)

myHash.insert(bestMovies[10][0], bestMovies[10][1])  # 2nd bucket as well; Key=11, item="STAR WARS - 1977"
print(myHash.table)

print("\nSearch:")
print(myHash.search(1))  # Key=1, item="CITIZEN KANE - 1941"
print(myHash.search(11))  # Key=11, item="STAR WARS - 1977"; so same bucket and Chainin is working

#print("\nUpdate:")
myHash.insert(1, "Star Trek - 1979")  # 2nd bucket; Key=1, item="Star Trek - 1979"
#print(myHash.table)

print("\nRemove:")
myHash.remove(1)  # Key=1, item="Star Trek - 1979" to remove
print(myHash.table)

myHash.remove(11)  # Key=11, item="STAR WARS - 1977" to remove
print(myHash.table)

'''