#Abstraction is the process of hiding the implementation details 
# and showing only the functionality to the user. In OOP, abstraction is achieved using abstract classes and interfaces.

#Creating an abstract class
from abc import ABC, abstractmethod

class vehicle(ABC):

    def fuel_type(self):
        print("Petrol/Diesel")
    @abstractmethod
    def start(self):
        pass

#  car = vehicle() # This will raise an error because we cannot create an object of an abstract class



#Creating a concrete class that inherits from the abstract class
# class Car(vehicle):

#     def start(self):
#         print("Car is starting")
# #Creating an object of the concrete class
# car = Car()
# car.start()
# car.fuel_type()


#Subclass Car inherits from the abstract class Vehicle and provides an implementation for the abstract method start(). We can create an object of the Car class and call both the start() and fuel_type() methods.
class Bike(vehicle):
    def start(self):
        print("Bike is starting")
#Creating an object of the concrete class
bike = Bike()
bike.start()
bike.fuel_type()



