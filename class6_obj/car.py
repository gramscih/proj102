from battery import Battery

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.__year} {self.__make} {self.__model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.__odometer_reading} KM on it")

    def update_odometer(self, km):
        if km >= self.__odometer_reading:
            self.__odometer_reading = km
    
    def __private_func(self):
        print("This is a private function")

    def get_model(self):
        return self.__model

    def set_model(self, new_mode):
        self.__model = new_mode


# Inheritance
class ElectricCar(Car):
    # constructor for python2.7
    # def __init__(self, make, model, year):
    #     super(ElectricCar, self).__init__(make, model, year)

    # python 3.x
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        print(f"this car has a {self.battery_size} -kWh battery")
