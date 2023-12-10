import Addresses
import Package


class Truck:
    def __init__(self):
        self.packages = []
        self.current_location = None
        self.destination = None
        # self.time_departed= 0


    def load_package(self, package: Package):
        package.status = Package.PackageStatus.ON_TRUCK
        # set package load time?
        self.packages.append(package)

    def set_route_nearest_neighbor(self):
        distance_traveled = 0
        while len(self.packages) > 0:
            if isinstance(self.current_location, Addresses.Address):
                for item in self.current_location.distances:
                    for package in self.packages:
                        if package.address.name == item[1]:
                            self.current_location = package.address
                            distance_traveled += item[0]
                            package.status = Package.PackageStatus.DELIVERED
                            # set package delivered time
                            self.packages.remove(package)
                            break
                    else:
                        continue
                    break
        distance_traveled += self.current_location.edges["HUB"]
        return distance_traveled

