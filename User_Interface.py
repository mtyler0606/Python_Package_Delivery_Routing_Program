import truck
import Package
import Addresses
import datetime
import MyHashTable


class UI:
    def __init__(self, deliveries: list, truck1: truck, truck2: truck, package_hash: MyHashTable, package_list: list):
        self.deliveries = deliveries
        self.truck1 = truck1
        self.truck2 = truck2
        self.package_hash = package_hash
        self.package_list = package_list

    def start_ui(self):
        welcome_message = ("Enter:\n1 for Status of All Packages and Total Mileage\n2 to get status of a single package at a particular time\n"
                           "3 to get the status of all packages at a particular time\n4 to display information for packages with extra requirements\n-1 to Exit\n")
        print(welcome_message)

        while True:
            user_input = input()
            if user_input == '1':
                self.get_final_status()
            elif user_input == '2':
                self.get_one_package()
            elif user_input == '3':
                self.get_all_packages()
            elif user_input == '4':
                self.get_special_requirements()
            elif user_input == '5':
                print(welcome_message)
            elif user_input == '-1':
                break
            # elif special notes
            else:
                print("Invalid Input")
            print("\nEnter 5 to repeat menu options")

    def get_final_status(self):
        user_input = input("Enter 1 to order deliveries by package id, Anything else orders packages by delivery time\n")
        if user_input == '1':
            for d in sorted(self.deliveries, key=lambda x: x.package.package_id):
                print(d)
            total_distance = self.truck1.distance_traveled + self.truck2.distance_traveled
            print("Total distance of traveled by all trucks", round(total_distance, 5))
        else:
            for d in sorted(self.deliveries, key= lambda x: x.time):
                print(d)
            total_distance = self.truck1.distance_traveled + self.truck2.distance_traveled
            print("Total distance of traveled by all trucks", round(total_distance, 5))

    def get_one_package(self):
        package_id = None
        while True:
            try:
                user_number = int(input("Enter package id (1-40)\n"))
                if user_number < 1 or user_number > 40:
                    print("No package with that id number")
                else:
                    package_id = user_number
                    break
            except:
                print("Invalid input")
        while True:
            try:
                user_input = input("Enter time (HH:MM)\n")
                user_time = datetime.datetime.strptime(user_input, "%H:%M").time()
                break
            except:
                print("Invalid input")
        the_Package = self.package_hash.search(package_id)
        print(f"Status of Package {package_id} at {user_time}: {self.get_package_status(the_Package, user_time)}")

        # if user_input ==

    def get_all_packages(self):
        while True:
            try:
                user_input = input("Enter time (HH:MM)\n")
                user_time = datetime.datetime.strptime(user_input, "%H:%M").time()
                break
            except:
                print("Invalid input")
        for package in self.package_list:
            print(f"Status of Package {package.package_id} at {user_time}: {self.get_package_status(package, user_time)}")

    def get_package_status(self, the_package: Package, the_time: datetime.time):
        if the_time < the_package.time_loaded:
            return "At Hub"
        if the_time >= the_package.time_loaded and the_time < the_package.time_delivered:
            return f"On Truck No. {the_package.truck.number}"
        if the_time >= the_package.time_delivered:
            return "Delivered"

    def get_special_requirements(self):
        packages_with_delivery_deadlines = [1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40]
        print("--Packages with a delivery deadline--")
        for p in packages_with_delivery_deadlines:
            package = self.package_hash.search(p)
            print(f"{package.package_id}, deadline: {package.deliver_deadline} delivered: {package.time_delivered}")
        print()
        packages_that_arrive_late_to_hub = [9, 25, 28, 32]
        print("--Packages that arrive late to hub")
        for p in packages_that_arrive_late_to_hub:
            package = self.package_hash.search(p)
            print(f"{package.package_id}, arrives at hub: {package.time_at_hub} time loaded: {package.time_loaded}")
        print()
