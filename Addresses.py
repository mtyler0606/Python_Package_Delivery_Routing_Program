import csv


# One address object for each address. Stores distance information to other addresses
class Address:
    def __init__(self, name):
        self.name = name
        # dictionary of distances to other addresses with address name as key and distance as value
        self.distance_lookup = {}
        # sorted list of tuples sorted by distance. first value is distance, second value is address object
        self.ordered_distances = []
        self.packages = []


    def __str__(self):
        return "Address:" + self.name


def get_addresses():
    """get_addresses: reads distance information from CSV file and creates Address objects.
        Returns a dictionary of Address objects to main.py
        time complexity of O(N^2) [nested FOR loops], space O(N^2) each address stores information about every other address

    :return: dictionary of Address objects with address name (string) as key
    """
    with open('WGUPS Distance Table(1).csv', 'r') as distance_CSV:
        reader = csv.reader(distance_CSV)

        # All lines in CSV (a list of lists)
        reader_lines = []
        for line in reader:
            reader_lines.append(line)

        # pulls address names from reader_lines
        address_strings = []
        for i in range(2, len(reader_lines[0])-2):
            address_strings.append(reader_lines[0][i].split("\n")[0].strip())

        # dictionary of address objects, for each address object, extract distances to all other addresses
        addresses = {}
        # for each address name
        for i in range(len(address_strings)):
            # create new Address object
            newAddress = Address(address_strings[i])
            # will become newAddress.distance_lookup
            city_distances = {}
            # will become newAddress.ordered_distances
            city_tuples = []
            # nested loop gets distance to every other address
            for j in range(len(address_strings)):
                city_distances[address_strings[j]] = float(reader_lines[i+1][j+2])
                city_tuples.append((float(reader_lines[i+1][j+2]), address_strings[j]))
            newAddress.distance_lookup = city_distances
            newAddress.ordered_distances = sorted(city_tuples[1:])
            # stores newAddress in dictionary
            addresses[newAddress.name] = newAddress
        # returns dictionary of Addresses to main
        return addresses


def get_packages_for_every_address(self, dictionary_of_addresses: dict, package_list: list):
    """Populates a list of Package objects to be delivered Address object
    Can be Helpful for manually loading trucks. Not critical to program functionality
    Time Complexity O(N^2) or (Addresses * Packages), Space O(N)

    :param self:
    :param dictionary_of_addresses:
    :param package_list:
    :return:
    """
    for address in dictionary_of_addresses.values():
        for package in package_list:
            if package.address == address:
                address.packages_to_be_delivered.append(package.__str__())