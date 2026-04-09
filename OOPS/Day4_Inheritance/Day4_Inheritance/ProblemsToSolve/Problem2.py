# Vehicle Information System
# Complete the Vehicle, Car, and Bike classes.

# Vehicle class:
# The Vehicle class should act as the base class.

# Features to be added to Vehicle class
# Add below attributes:
# brand
# speed
# Add below methods:
# show_details() : Prints brand and speed
# Car class:
# The Car class inherits from Vehicle.

# Features to be added to Car class
# Add below attributes:
# number_of_doors
# Add below methods:
# show_details() : Override parent method and include numberofdoors
# Bike class:
# The Bike class inherits from Vehicle.

# Features to be added to Bike class
# Add below attributes:
# bike_type (sports/commuter)
# Add below methods:
# show_details() : Override parent method and include bike_type

class vehicle:
    def __init__(self,  brand, speed):
        self.brand = brand
        self.speed = speed
    def show_details(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")
    
class Car(vehicle):
    def __init__(self, brand, speed, number_of_doors):
        super().__init__(brand, speed)
        self.number_of_doors = number_of_doors
    def show_details(self):
        super().show_details()
        print(f"Number of Doors: {self.number_of_doors}")
    
class Bike(vehicle):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type
    def show_details(self):
        super().show_details()
        print(f"Bike Type: {self.bike_type}")
# Example usage:
car = Car("Toyota", 180, 4)
bike = Bike("Yamaha", 120, "sports")
car.show_details()
bike.show_details()
