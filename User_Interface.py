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
        """ Starts the user interface. User can select different options from the terminal to display delivery information
            When the user inputs "-1" the program concludes
        """
        welcome_message = ("Enter:\n1 for Status of All Packages and Total Mileage\n2 to get status of a single package at a particular time\n"
                           "3 to get the status of all packages_to_be_delivered at a particular time\n4 to display information for packages_to_be_delivered with extra requirements\n-1 to Exit")
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
        """Prints delivery information for all packages and total combined mileage traveled by all trucks
        """
        print("--Delivery information for each package ordered by delivery time--")
        for d in sorted(self.deliveries, key=lambda x: x.time):
            print(d)
        total_distance = self.truck1.distance_traveled + self.truck2.distance_traveled
        print("\nTotal distance of traveled by all trucks", round(total_distance, 5))

    def get_one_package(self):
        """Prints the status of one package at a specific time.
        User is first prompted to enter a package ID, and then prompted to enter a time
        """
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

    def get_all_packages(self):
        """Prints the status of all packages at a particular time of the user's choosing
        """
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
        """Helper function used by get_all_packages and get_one_package. Returns a packages status in an easily readable format

        :param the_package: a Package Type
        :param the_time: a specific time
        :return: a string representing the status of the package at the specific time in an easily readable format
        """
        if the_time < the_package.time_loaded:
            return "At Hub"
        if the_time >= the_package.time_loaded and the_time < the_package.time_delivered:
            return f"On Truck No. {the_package.truck.number}"
        if the_time >= the_package.time_delivered:
            return "Delivered"

    def get_special_requirements(self):
        """Prints the information about all the packages that have special delivery requirements or constraints
        in order to easily validate that all special requirements are met.
        """
        packages_with_delivery_deadlines = [1, 6, 13, 14, 15, 16, 20, 25, 29, 30, 31, 34, 37, 40]
        print("--Packages with a delivery deadline--")
        for p in packages_with_delivery_deadlines:
            package = self.package_hash.search(p)
            print(f"{package.package_id}, deadline: {package.deliver_deadline} delivered: {package.time_delivered}")
        print()
        packages_that_arrive_late_to_hub = [6, 9, 25, 28, 32]
        print("--Packages that arrive late to hub--")
        for p in packages_that_arrive_late_to_hub:
            package = self.package_hash.search(p)
            print(f"{package.package_id}, arrives at hub: {package.time_at_hub} time loaded: {package.time_loaded}")
        print()
        packages_required_to_be_on_Truck2 = [3, 18, 36, 38]
        print("--Packages required to be delivered on only Truck No. 2--")
        for p in packages_required_to_be_on_Truck2:
            package = self.package_hash.search(p)
            print(f"{package.package_id}, Truck No. {package.truck.number} (special notes: {package.special_notes})")
        print()
        packages_required_to_be_delivered_together = [13, 14, 15, 16, 19, 20]
        print("--Packages required to be delivered together--")
        for p in packages_required_to_be_delivered_together:
            package = self.package_hash.search(p)
            print(f"{package.package_id}, Truck No. {package.truck.number} Loaded: {package.time_loaded}")
