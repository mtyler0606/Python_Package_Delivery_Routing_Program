import MyHashTable
import truck
import Package
import Addresses
import datetime

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
    truck1 = truck.Truck(1)
    truck1.current_location = dictionary_of_addresses["HUB"]
    truck2 = truck.Truck(2)
    truck2.current_location = dictionary_of_addresses["HUB"]

    load_truck1_first_time = [14, 15, 16, 34, 26, 20, 21, 19, 12, 17, 31, 4, 40, 1, 2, 13]
    load_truck2_first_time = [11, 23, 18, 35, 27, 39, 3, 36, 38, 30, 8, 37, 5, 10, 29, 22]

    load_truck1_second_time = [9, 24]
    load_truck2_second_time = [6, 25, 28, 32, 7, 33]

    for item in set(load_truck1_first_time):
        truck1.load_package(package_hash.search(item))
    for item in set(load_truck2_first_time):
        truck2.load_package(package_hash.search(item))

    truck1.set_route_nearest_neighbor()
    truck2.set_route_nearest_neighbor()
    truck1.current_location = dictionary_of_addresses["HUB"]
    truck2.current_location = dictionary_of_addresses["HUB"]

    for item in load_truck1_second_time:
        truck1.load_package(package_hash.search(item))
    for item in load_truck2_second_time:
        truck2.load_package(package_hash.search(item))

    truck1.set_route_nearest_neighbor()
    truck2.set_route_nearest_neighbor()

    for i in range(1, 41):
        the_package = package_hash.search(i)
        #print(the_package.package_id, the_package.time_delivered, the_package.truck)
        #print(truck1.time, truck1.distance_traveled)

    for p in sorted(packages_at_hub, key = lambda x: x.time_delivered):
        print(p.package_id, p.time_delivered, p.truck, p.time_loaded, p.truck.distance_traveled)




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

