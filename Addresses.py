import csv


class Address:
    def __init__(self, name):
        self.name = name
        self.edges = {}
        self.distances = []


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

        # list of address objects, for each address object, extract distances to other addresses
        addresses = []
        for i in range(len(address_strings)):
            newAddress = Address(address_strings[i])
            city_distances = {}
            city_tuples = []
            for j in range(len(address_strings)):
                city_distances[address_strings[j]] = float(reader_lines[i+1][j+2])
                city_tuples.append((float(reader_lines[i+1][j+2]), address_strings[j]))
            newAddress.edges = city_distances
            newAddress.distances = sorted(city_tuples)
            addresses.append(newAddress)

        return address_strings, addresses


