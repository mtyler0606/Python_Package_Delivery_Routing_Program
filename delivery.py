import datetime

import truck
import Package
import Addresses


class Delivery:
    def __init__(self, truck: truck, package: Package, address: Addresses, time: datetime.time, current_mileage: float):
        self.truck = truck
        self.package = package
        self.address = address
        self.time = time
        self.current_milage = current_mileage

    def __str__(self):
        if self.package is not None:
            return ("ID: " + str(self.package.package_id) + ", " + self.address.name + ", truck no. " + str(self.truck.number) +
                    ", current mileage: " + str(self.current_milage) + " loaded: " + self.package.time_loaded.__str__() +
                    ", delivered: " + self.time.__str__() + " - " + self.package.special_notes)
        else:
            return ("Return to HUB : truck no. " + str(self.truck.number) + ", current mileage: "
                    + str(self.current_milage) + " time: " + self.time.__str__())
