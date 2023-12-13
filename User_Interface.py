import truck
import Package
import Addresses


class UI:
    def __init__(self, deliveries: list, truck1: truck, truck2: truck):
        self.deliveries = deliveries
        self.truck1 = truck1
        self.truck2 = truck2

    def start_ui(self):
        welcome_message = "Enter:\n1 for Status of All Packages and Total Mileage\n2 to get status of a single package at a particular time\n3 to get the status of all packages at a particular time\n-1 to Exit\n"
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
                print(welcome_message)
            elif user_input == '-1':
                break
            else:
                print("Invalid Input")
            print("\nEnter 4 to repeat options")

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
        pass

    def get_all_packages(self):
        pass

