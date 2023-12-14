# Student ID 010919298

import MyHashTable
import truck
import Package
import Addresses
import datetime
import User_Interface

def main():

    # Addresses.py contains code for the Address class, and the get_addresses function
    # The get_addresses function reads the address info for the distance table CSV file and converts it into Address objects
    # It then returns a dictionary of address objects the Address.name as the key
    dictionary_of_addresses = Addresses.get_addresses()

    # Package.py contains code for the Package class, and the get_packages function
    # get_packages returns reads the package information for the package CSV file
    # creates a Package object for each package, and returns both hash table and a list of packages_to_be_delivered
    packages_from_file = Package.get_packages()
    package_hash = packages_from_file[0]
    package_list = packages_from_file[1]

    # Correct address for the package with the wrong address
    wrong_address = package_hash.search(9)
    wrong_address.address = '410 S State St'
    # sets the time when address is corrected as the time when the package arrives at the Hub
    wrong_address.time_at_hub = datetime.time(10, 20, 0, 0)

    # set time_at_hub for the late packages_to_be_delivered
    late_packages_by_id = [6, 25, 28, 32]
    for package_id in late_packages_by_id:
        package_hash.search(package_id).time_at_hub = datetime.time(9, 5, 0, 0)

    # for each package set package.address to address object instead of string using dictionary_of_addresses
    for package in package_list:
        for value in dictionary_of_addresses.values():
            if package.address == value.name:
                package.address = value

    # truck.py contains the Truck class
    # Create truck1 and truck2. A third truck is not used
    # Set initial location for each truck to "HUB"
    truck1 = truck.Truck(1)
    truck1.current_location = dictionary_of_addresses["HUB"]
    truck2 = truck.Truck(2)
    truck2.current_location = dictionary_of_addresses["HUB"]

    # Load the trucks
    # Lists hold package id's used for load_package method in the Truck class
    load_truck1_first_time = [4, 40, 1, 29, 7, 2, 33, 31, 32, 17, 28, 6]
    load_truck2_first_time = [15, 16, 34, 14, 19, 36, 27, 35, 13, 39, 3, 37, 38, 30, 20, 21]
    load_truck1_second_time = [8, 9, 10, 5]
    load_truck2_second_time = [25, 26, 22, 24, 18, 11, 23, 12]

    # Set the time for truck1 to 9:05 (for later departure)
    truck1.time = datetime.datetime(2024, 1, 1, 9, 5, 0, 0)

    # load each truck for the first time
    for item in set(load_truck1_first_time):
        truck1.load_package(package_hash.search(item))
    for item in set(load_truck2_first_time):
        truck2.load_package(package_hash.search(item))

    # the Truck.set_route_nearest_neighbor method contains the nearest neighbor algorithm
    # All routing, tracking time and distance, and marking packages_to_be_delivered loaded or delivered is handled within the Truck class
    truck1.set_route_nearest_neighbor()
    truck2.set_route_nearest_neighbor()
    # Reset current_location to hub for each truck
    truck1.current_location = dictionary_of_addresses["HUB"]
    truck2.current_location = dictionary_of_addresses["HUB"]

    # truck1 must wait at the HUB for package 9 to have the correct address
    if(truck1.time.time() < datetime.time(10, 20, 0, 0 )):
        truck1.time = datetime.datetime(2024, 1,1,10, 20, 0 ,0)

    # Load trucks for second time
    for item in load_truck1_second_time:
        truck1.load_package(package_hash.search(item))
    for item in load_truck2_second_time:
        truck2.load_package(package_hash.search(item))

    # Run algorithm for second time
    truck1.set_route_nearest_neighbor()
    truck2.set_route_nearest_neighbor()

    # Delivery objects are created for each package delivery
    # deliveries for each truck are combined into one list to be passed to the ui
    all_deliveries = truck1.deliveries + truck2.deliveries

    # Create and start the user interface
    # Pass deliveries, trucks, and packages_to_be_delivered to the user interface
    ui = User_Interface.UI(all_deliveries, truck1, truck2, package_hash, package_list)
    ui.start_ui()


if __name__ == '__main__':
    main()

