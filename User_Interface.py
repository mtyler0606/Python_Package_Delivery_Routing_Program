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
        welcome_message = ("Enter:\n1 All Deliveries and Total Mileage\n2 to get status of a single package at a particular time\n"
                           "3 to get the status of all packages at a particular time\n"
                           "4 to get the status of all packages at a particular time sorted by status\n"
                           "5 to display information for packages with extra requirements\n-1 to Exit")
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
                self.get_all_packages_sorted()
            elif user_input == '5':
                self.get_special_requirements()
            elif user_input == '6':
                print(welcome_message)
            elif user_input == '-1':
                break
            # elif special notes
            else:
                print("Invalid Input")
            print("\nEnter 6 to repeat menu options")

    def get_final_status(self):
        """Prints delivery information for all packages and total combined mileage traveled by all trucks
        """
        print("--Delivery information for each package ordered by delivery time--")
        for d in sorted(self.deliveries, key=lambda x: x.time):
            print(d)
        total_distance = self.truck1.distance_traveled + self.truck2.distance_traveled
        print("\nTruck 1 distance traveled:", round(self.truck1.distance_traveled, 5), "Truck 2 distance traveled:",
              round(self.truck2.distance_traveled, 5), "\nTotal distance of traveled by all trucks", round(total_distance, 5))

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

    def get_all_packages_sorted(self):
        """Prints the status of all packages at a particular time of the user's choosing, sorted by category
                """
        while True:
            try:
                user_input = input("Enter time (HH:MM)\n")
                user_time = datetime.datetime.strptime(user_input, "%H:%M").time()
                break
            except:
                print("Invalid input")
        package_status_strings = []
        for package in self.package_list:
            # package_status_strings.append(f"Status of Package {package.package_id} at {user_time}: {self.get_package_status(package, user_time)}")
            package_status_strings.append(self.lookup_package_status(package.package_id, user_time))
        print("--Packages at Hub:")
        for package_status in package_status_strings:
            if "At Hub" in package_status:
                print(package_status)
        print("\n--Packages on Truck 1:")
        for package_status in package_status_strings:
            if "En Route, on truck no. 1" in package_status:
                print(package_status)
        print("\n--Packages on Truck 2:")
        for package_status in package_status_strings:
            if "En Route, on truck no. 2" in package_status:
                print(package_status)
        print("\n--Packages Delivered")
        for package_status in package_status_strings:
            if "Delivered" in package_status:
                print(package_status)


    def get_package_status(self, the_package: Package, the_time: datetime.time):
        """Helper function used by get_all_packages and get_one_package. Returns a packages status in an easily readable format

        :param the_package: a Package Type
        :param the_time: a specific time
        :return: a string representing the status of the package at the specific time in an easily readable format
        """
        if the_time < the_package.time_loaded:
            return "At Hub"
        if the_time >= the_package.time_loaded and the_time < the_package.time_delivered:
            return f"En Route, on truck no. {the_package.truck.number}"
        if the_time >= the_package.time_delivered:
            return f"Delivered ({the_package.time_delivered})"

    def get_special_requirements(self):
        """Prints the information about all the packages that have special delivery requirements or constraints
        in order to easily validate that all special requirements are met.
        """
        packages_with_delivery_deadlines = [1, 6, 13, 14, 15, 16, 20, 25, 29, 30, 31, 34, 37, 40]
        print("--Packages with a delivery deadline--")
        for p in packages_with_delivery_deadlines:
            package = self.package_hash.search(p)
            print(f"{package.package_id}, deadline: {package.delivery_deadline} delivered: {package.time_delivered}")
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

    def lookup_single_package_at_time(self, package_id:int, time_string: str):
        """
        Returns information about a single package in self.package_hash at a particular time
        :param package_id: package_id: integer, the package id of a packaged in the package hash
        :param time_string: a string representing a specific time in "%H: %M" format,
        converted by function into a time object, and used as a parameter in the get_package_method to retrieve
        a string representing the package's status at the specific time given
        :return: the package's address, delivery deadline, city, zip code weight, time delivered, and status at time given
        """
        converted_time = datetime.datetime.strptime(time_string, "%H:%M").time()
        the_package = self.package_hash.search(package_id)
        return (the_package.address.name, the_package.delivery_deadline, the_package.city, the_package.zip_code,
                the_package.weight, the_package.time_delivered,
                f"Status of Package {package_id} at {time_string}: {self.get_package_status(the_package, converted_time)}")

    def lookup_package_status(self, package_id:int, time: datetime.time):
        """
                Returns information about a single package in self.package_hash at a particular time as a formatted string
                :param package_id: package_id: integer, the package id of a packaged in the package hash
                :param time: a datetime.time object, the function looks up a package's status at this time
                :return: the package's address, delivery deadline, city, zip code weight,
                time delivered, and status at time given as a formatted sting
                """
        the_package = self.package_hash.search(package_id)
        return (f"ID {the_package.package_id} ({the_package.address.name}, {the_package.city}, {the_package.zip_code}), "
                f"Deadline: {the_package.delivery_deadline}, Wt: {the_package.weight}, "
                f"---- Status at {time.__str__()}: {self.get_package_status(the_package, time)}")

