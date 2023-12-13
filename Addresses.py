import csv


class Address:
    def __init__(self, name):
        self.name = name
        # Adjacent addresses as a dictionary with address name as key
        self.edges = {}
        # Adjacent addresses a list of tuples sorted by distance. first value is distance, second value is address object
        self.distances = []
        self.packages = []

    def get_distance(self, other_address: str):
        return self.edges[other_address]

    def __str__(self):
        return "Address:" + self.name


def get_addresses():
    with open('WGUPS Distance Table(1).csv', 'r') as distance_CSV:
        reader = csv.reader(distance_CSV)

        # All lines in CSV as list of lists
        reader_lines = []
        for line in reader:
            reader_lines.append(line)

        # All addresses as strings (split from zip codes)
        address_strings = []
        for i in range(2, len(reader_lines[0])-2):
            address_strings.append(reader_lines[0][i].split("\n")[0].strip())

        # dictionary of address objects, for each address object, extract distances to other addresses
        addresses = {}
        for i in range(len(address_strings)):
            newAddress = Address(address_strings[i])
            city_distances = {}
            city_tuples = []
            for j in range(len(address_strings)):
                city_distances[address_strings[j]] = float(reader_lines[i+1][j+2])
                city_tuples.append((float(reader_lines[i+1][j+2]), address_strings[j]))
            newAddress.edges = city_distances
            newAddress.distances = sorted(city_tuples[1:])
            addresses[newAddress.name] = newAddress

        return addresses

'''
X = get_addresses()
y = X["HUB"]


print(y)
print(y.name)
print(y.edges)
print(y.distances)
'''