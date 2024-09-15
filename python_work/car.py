class Car:
    """A simple car class"""

    def __init__(self, make, model, year):
        """Init attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, miliage):
        if miliage >= self.odometer_reading:
            self.odometer_reading = miliage
        else:
            print("can't roll back f'ing odometer!!!")       
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery_size = 40
    
    def describe_battery(self):
        print(f"this car has a batter size of {self.battery_size} -- kWh Battery.")



my_leaf = ElectricCar('tesla', 'y', 2024)

print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()