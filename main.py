import MyHashTable
import truck
import Package
import Addresses


def main():

    # Address names, and address objects extracted from excel/csv document
    dictionary_of_addresses = Addresses.get_addresses()
    # address_names = get_addresses[0] # list of address names
    # address_objects = get_addresses[1] # list of address objects

    # Get Packages
    packages_from_file = Package.get_packages()
    package_hash = packages_from_file[0]
    packages_at_hub = packages_from_file[1]

    # Set package addresses to address objects instead of strings
    for package in packages_at_hub:
        for value in dictionary_of_addresses.values():
            if package.address == value.name:
                package.address = value

    # Create trucks (only use 2)
    truck1 = truck.Truck()
    truck1.current_location = dictionary_of_addresses["HUB"]
    truck2 = truck.Truck()
    truck2.current_location = dictionary_of_addresses["HUB"]

    for i in range(1,41):
        truck1.load_package(package_hash.search(i))

    print(truck1.set_route_nearest_neighbor())





'''''''''''
    print(package_hash.search(1))
    print(packages_at_hub[0])
    print()

    for package in packages_at_hub:
        print(package.package_id, package.address, package.address.name)

    for i in range(1, 41):
        print(package_hash.search(i).address)
'''


if __name__ == '__main__':
    main()

