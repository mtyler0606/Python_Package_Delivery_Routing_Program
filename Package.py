import csv
from MyHashTable import MyChainedHashTable
from enum import Enum
import datetime


class PackageStatus(Enum):
    NOT_AVAILABLE = 0
    AT_HUB = 1
    ON_TRUCK = 2
    DELIVERED = 3


# the Package class contains all the information about a package
class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deliver_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = PackageStatus.AT_HUB
        self.time_delivered = None
        self.time_loaded = None
        self.time_at_hub = datetime.time(8, 0, 0, 0)
        self.truck = None

    def __str__(self):
        return f"{self.package_id}, {self.address}, {self.deliver_deadline}, {self.special_notes}"



def get_packages():
    """get_packages: reads CSV file and extracts package data, creates a Package object for each package
    adds packages to hash table and list
    :return: hash table of packages and list of packages
    Time and space complexity: O(N) where N is the number of packages
    """
    package_hashtable = MyChainedHashTable(41)
    package_list = []

    with open('WGUPS Package File cleaned.csv', 'r') as Package_CSV:
        package_info = csv.reader(Package_CSV)

        next(Package_CSV)
        for line in package_info:
            # line[0] - package_id, line[1] - address, line[2] - city, line[3] - state, line[4] - zip_code
            # line[5] - delivery deadline, line[6] - weight, line[7] - special notes
            newPackage = Package(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6], line[7])
            # inserts new package into hash table with package id as key and package object as value
            package_hashtable.insert(int(line[0]), newPackage)
            package_list.append(newPackage)
    return package_hashtable, package_list


