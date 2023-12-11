import Addresses
import Package
import datetime
#from datetime import datetime, timedelta, time


class Truck:
    def __init__(self, truck_number):
        self.packages = []
        self.current_location = None
        self.destination = None
       #self.time= datetime.datetime(2024, 1, 1, 8, 0, 0, 0)
        self.time = datetime.datetime(2024, 1, 1, 8, 0, 0, 0)
        self.distance_traveled = 0
        self.number = truck_number

    def load_package(self, package: Package):
        package.status = Package.PackageStatus.ON_TRUCK
        package.time_loaded = self.time.time()
        package.truck = self
        self.packages.append(package)

    def set_route_nearest_neighbor(self):
        # distance_traveled = 0
        while len(self.packages) > 0:
            if isinstance(self.current_location, Addresses.Address):
                for item in self.current_location.distances:
                    for package in self.packages:
                        if package.address.name == item[1]:
                            self.current_location = package.address
                            self.advance_time_and_distance(item[0])
                            package.status = Package.PackageStatus.DELIVERED
                            package.time_delivered = self.time.time()
                            self.packages.remove(package)
                            break
                    else:
                        continue
                    break
        self.advance_time_and_distance(self.current_location.edges["HUB"])
        self.current_location = "HUB"

    def advance_time_and_distance(self, miles: float):
        self.time += miles * datetime.timedelta(hours=1/18)
        self.distance_traveled += miles

    def __str__(self):
        return "Truck No. " + str(self.number)
