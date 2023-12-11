import csv
from MyHashTable import MyChainedHashTable
from enum import Enum
import datetime


class PackageStatus(Enum):
    NOT_AVAILABLE = 0
    AT_HUB = 1
    ON_TRUCK = 2
    DELIVERED = 3


class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        # String. Convert to time?
        self.deliver_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = PackageStatus.AT_HUB
        self.time_delivered = None
        self.time_loaded = None
        self.truck = None


    def __str__(self):
        return f"{self.package_id}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.deliver_deadline}, {self.weight}, {self.special_notes}"


def get_packages():
    PackageHashtable = MyChainedHashTable(41)
    package_list = []

    with open('WGUPS Package File cleaned.csv', 'r') as Package_CSV:
        Package_info = csv.reader(Package_CSV)

        next(Package_CSV)
        for line in Package_info:
            newPackage = Package(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6], line[7])
            PackageHashtable.insert(int(line[0]), newPackage)
            package_list.append(newPackage)
    return PackageHashtable, package_list


