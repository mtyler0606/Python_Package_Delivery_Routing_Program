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
        self.hub = None

    def load_package(self, package: Package):
        """load_package: adds package object to a truck's packages_to_be_delivered list
        changes package's status to ON_TRUCK, Set packages time_loaded at truck's current time
        :param package: Package object
        """
        package.status = Package.PackageStatus.ON_TRUCK
        package.time_loaded = self.time.time()
        package.truck = self
        self.packages_to_be_delivered.append(package)

    def set_route_nearest_neighbor(self):
        """set_route_nearest_neighbor: Paths route through to deliver all packages in truck's packages_to_be_delivered list
        Uses nearest-neighbor algorithm to route deliveries

        For each delivery: adds delivery time to self.time and distance to self.distance_traveled,
            changes package's status to DELIVERED, sets package's time_delivered
            removes package from self.packages_to_be_delivered,
            creates a new Delivery object, adds it to self.deliveries

        After all packages are delivered return truck to HUB

        Time Complexity: O(N^2) - nested FOR loops
        Space: O(N)
        """
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
        self.current_location = self.hub
        new_delivery = delivery.Delivery(self, None, self.hub, self.time.time(), round(self.distance_traveled, 5))
        self.deliveries.append(new_delivery)

    # adds the appropriate amount to the time and distance traveled based on the distance between locations
    def advance_time_and_distance(self, miles: float):
        """
        adds param miles to self.distance_traveled representing distance traveled by truck,
        adds the trucks time to represent time elapsing while truck is travelling (truck travels at 18 miles per hour)
        :param miles: float
        """
        self.time += miles * datetime.timedelta(hours=1/18)
        self.distance_traveled += miles

    def __str__(self):
        return "Truck No. " + str(self.number)
