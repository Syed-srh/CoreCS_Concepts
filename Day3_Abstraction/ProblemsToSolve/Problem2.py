# Practice Scenario 2: Vehicle System
# Complete the Vehicle and Car / Bike classes by adding new features.

# Vehicle class:
# The Vehicle class should be an abstract class.

# Features to be added to Vehicle class:
# Add below attributes:

# brand
# model
# fuel_type
# Add below methods:

# start() : Abstract method
# stop() : Abstract method
# display_details() : Prints vehicle details
# Subclasses:
# Car and Bike inherit from Vehicle.

# Features to be added to subclasses:
# Add below methods:

# start() : Define how each vehicle starts
# stop() : Define how each vehicle stops



from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")

    
class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

    def stop(self):
        print("Bike is stopping")

# Example usage
car = Car("Toyota", "Camry", "Petrol")
car.display_details()
car.start()
car.stop()

bike = Bike("Honda", "CBR", "Petrol")
bike.display_details()
bike.start()
bike.stop()