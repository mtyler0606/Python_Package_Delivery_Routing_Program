import Addresses
import Package
import datetime
import delivery


# Each truck tracks its own time and distance traveled
class Truck:
    def __init__(self, truck_number):
        self.packages_to_be_delivered = []
        self.current_location = None
        self.destination = None
        self.time = datetime.datetime(2024, 1, 1, 8, 0, 0, 0)
        self.distance_traveled = 0
        self.number = truck_number
        self.deliveries = []

    # For the package passed in this method changes its status, sets its time_loaded, sets its truck
    # the package is then added to the truck's packages_to_be_delivered list
    def load_package(self, package: Package):
        package.status = Package.PackageStatus.ON_TRUCK
        package.time_loaded = self.time.time()
        package.truck = self
        self.packages_to_be_delivered.append(package)

    # Finds route using nearest neighbor algorithm
    def set_route_nearest_neighbor(self):
        # while there are still packages to be delivered
        while len(self.packages_to_be_delivered) > 0:
            # current_location must be an Address object
            if isinstance(self.current_location, Addresses.Address):
                # iterates through all Addresses adjacent to current Address
                for item in self.current_location.ordered_distances:
                    # iterates all packages_to_be_delivered
                    # nested loops: worst case runtime is number of Addresses times number of Packages or N^2
                    for package in self.packages_to_be_delivered:
                        # if the package address is matched, the new address is set to the package address
                            # the time and distance are advanced, the package status is set to DELIVERED
                            # the package.time_delivered is set and the package is removed from the trucks packages_to_be_delivered list
                        if package.address.name == item[1]:
                            self.current_location = package.address
                            self.advance_time_and_distance(item[0])
                            package.status = Package.PackageStatus.DELIVERED
                            package.time_delivered = self.time.time()
                            self.packages_to_be_delivered.remove(package)

                            # a new delivery object is created, and appended to the truck's list of deliveries
                            # both for loops are exited
                            new_delivery = delivery.Delivery(self, package, package.address, self.time.time(), round(self.distance_traveled, 5))
                            self.deliveries.append(new_delivery)
                            break
                    else:
                        continue
                    break
        # once the packages_to_be_delivered list is empty the truck returns to the hub
        self.advance_time_and_distance(self.current_location.distance_lookup["HUB"])
        self.current_location = "HUB"

    # adds the appropriate amount to the time and distance traveled based on the distance between locations
    def advance_time_and_distance(self, miles: float):
        self.time += miles * datetime.timedelta(hours=1/18)
        self.distance_traveled += miles

    def __str__(self):
        return "Truck No. " + str(self.number)
