import MyHashTable
import truck
import Package
import Addresses
import datetime
import User_Interface

def main():

    # Address names, and address objects extracted from excel/csv document
    dictionary_of_addresses = Addresses.get_addresses()
    # address_names = get_addresses[0] # list of address names
    # address_objects = get_addresses[1] # list of address objects

    # Get Packages
    packages_from_file = Package.get_packages()
    package_hash = packages_from_file[0]
    packages_at_hub = packages_from_file[1]

    #Correct wrong address
    wrong_address = package_hash.search(9)
    wrong_address.address = '410 S State St'

    # set time_at_hub for late packages
    late_packages_by_id = [6 , 25, 28, 32]
    for package_id in late_packages_by_id:
        package_hash.search(package_id).time_at_hub = datetime.time(9, 5, 0, 0)

    # for each package set package.address to address object instead of string
    for package in packages_at_hub:
        for value in dictionary_of_addresses.values():
            if package.address == value.name:
                package.address = value

    # A list of packages to be delivered to each address. Helpful for manually loading trucks
    for address in dictionary_of_addresses.values():
        for package in packages_at_hub:
            if package.address == address:
                address.packages.append(package.__str__())

    # Create trucks (only use 2)
    truck1 = truck.Truck(1)
    truck1.current_location = dictionary_of_addresses["HUB"]
    truck2 = truck.Truck(2)
    truck2.current_location = dictionary_of_addresses["HUB"]


    # Load trucks
    load_truck1_first_time = [14, 15, 16, 34, 20, 21, 19, 12, 17, 4, 40, 1, 13, 39, 37]
    load_truck2_first_time = [11, 23, 18, 35, 27, 3, 36, 8, 10, 29, 22, 7, 30, 24, 2, 33]

    load_truck1_second_time = [6, 25, 28, 31, 32, 26]
    load_truck2_second_time = [9, 5, 38]

    for item in set(load_truck1_first_time):
        truck1.load_package(package_hash.search(item))
    for item in set(load_truck2_first_time):
        truck2.load_package(package_hash.search(item))

    # Start deliveries
    truck1.set_route_nearest_neighbor()
    truck2.set_route_nearest_neighbor()
    truck1.current_location = dictionary_of_addresses["HUB"]
    truck2.current_location = dictionary_of_addresses["HUB"]

    # Trucks must wait for late packages
    if(truck1.time.time() < datetime.time(9, 5, 0, 0)):
        truck1.time = datetime.datetime(2024, 1, 1, 9, 5, 0, 0)

    if(truck2.time.time() < datetime.time(10, 20, 0, 0 )):
        truck2.time = datetime.datetime(2024, 1,1,10, 20, 0 ,0)

    for item in load_truck1_second_time:
        truck1.load_package(package_hash.search(item))
    for item in load_truck2_second_time:
        truck2.load_package(package_hash.search(item))

    truck1.set_route_nearest_neighbor()
    truck2.set_route_nearest_neighbor()

    all_deliveries = truck1.deliveries + truck2.deliveries

    UI = User_Interface.UI(all_deliveries, truck1, truck2)
    UI.start_ui()

'''''''''''
     for p in sorted(packages_at_hub, key = lambda x: x.package_id):
        print(p.package_id, p.time_at_hub, p.time_loaded, p.time_delivered, p.truck)
        
    for d in (sorted(all_deliveries, key = lambda x: x.time)):
        print(d)

    for d in (sorted(all_deliveries, key=lambda x: x.package.package_id)):
        print(d)

    for i in range(1, 41):
        the_package = package_hash.search(i)
        #print(the_package.package_id, the_package.time_delivered, the_package.truck)
        #print(truck1.time, truck1.distance_traveled)

    for p in sorted(packages_at_hub, key = lambda x: x.time_delivered):
        #print(p.package_id, p.time_delivered, p.truck, p.time_loaded, p.truck.distance_traveled)
        continue

    total_milage = truck1.distance_traveled + truck2.distance_traveled
    print(total_milage)

    for address in dictionary_of_addresses.values():
        #print(address.packages)
        break

    # print(dictionary_of_addresses)
    #len(load_truck1_first_time)
    #print(len(load_truck1_first_time))
    #print(len(load_truck2_first_time))
    #print(len(load_truck1_second_time))
    #print(len(load_truck2_second_time))
    print(len(all_deliveries))

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

