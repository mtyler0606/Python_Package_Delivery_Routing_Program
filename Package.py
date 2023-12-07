import csv
from MyHashTable import MyChainedHashTable


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

    def __str__(self):
        return f"{self.package_id}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.deliver_deadline}, {self.weight}, {self.special_notes}"

def getPackages():
    PackageHashtable = MyChainedHashTable(41)

    with open('WGUPS Package File cleaned.csv', 'r') as Package_CSV:
        Package_info = csv.reader(Package_CSV)

        next(Package_CSV)
        for line in Package_info:
            #print(line)
            newPackage = Package(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6], line[7])
            PackageHashtable.insert(int(line[0]), newPackage)
    return PackageHashtable


