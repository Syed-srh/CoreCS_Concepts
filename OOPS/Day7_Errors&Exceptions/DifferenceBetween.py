# Difference between instance attribute Vs class Attribute, 
# Instance method Vs class Method Vs Static Method

class Car:
    car_count = 1  # class attribute
    def __init__(self, model):
        self.model = model  # instance attribute

    @classmethod
    def increase_car_count(cls):
        cls.car_count += 1
    @staticmethod
    def display_info():
        print("This is a Car class.")
    #in static method we cannot access class attributes or instance attributes, we can only access them in class method and instance method respectively.

c1 = Car("BMW M5")
c2 = Car("Audi R8")
print(c1.model)  # Output: BMW M5
print(c2.model)  # Output: Audi R8

#the main DIfference between instance attribute and class attribute
#instance attribute is is used as self.attribute_name and it is unique to each instance of the class, while class attribute is defined at the class level and shared among all instances of the class.

#the main difference between instance method, class method and static method is that instance method takes self as the first parameter and can access instance attributes and class attributes, while class method takes cls as the first parameter and can access class attributes but not instance attributes, and static method does not take any special first parameter and cannot access either instance attributes or class attributes.

   