#Inheritance in oops 
#Where the One class acquires the properties and behavior of another class is called inheritance
#The class which acquires the properties and behavior of another class is called child class or subclass

#The class whose properties and behavior are acquired by another class is called parent class or super class

# class Vehicle:
#     def stop(self):
#         print("Vehicle is stopping")
    
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting")

# c = Car()
# c.start()
# c.stop()    
#Here the Car class is inheriting the stop method from the Vehicle class, so we can call the stop method on an instance of the Car class.
#Vehicle is parent class
#Car is child class

#Basic syntax and Working
# class Parent:
#     def greet(self):
#         print("Hello from Parent class"
#               )
# class Child(Parent):
#     def welcome(self):
#         print("Welcome to the Child class")
# c = Child()
# c.greet()
# c.welcome() 
#In this example, the Child class inherits the greet method from the Parent class. Since we haven't defined any additional methods or attributes in the Child class, it simply uses the greet method from the Parent class when we call c.greet().


#super 
#super is a built-in function in Python that allows you to call methods from a parent class. It is commonly used in the context of inheritance to access and invoke methods from the parent class within a child class.

# class Parent:
#     def greet(self):
#         print("Hello from Parent class")

# class Child(Parent):
#     def greet(self):
#         super().greet()
#         print("Welcome to the Child class")

# c = Child()
# c.greet()


# class vehicle:
#     def start(self):
#         print("Vehicle is starting")

#     def get_fuel(self):
#         print("Petrol / Diesel / Electric")
# class Car(vehicle):
#     def start(self):
#         super().start()
#         print("Car is starting")
#         # super().get_fuel()

# c = Car()
# c.start()
# c.get_fuel()


## >> Types of Inheritance
#1. Single Inheritance - parent to child class
#2. Multiple Inheritance - more than one parent class to child class
#3. Multilevel Inheritance - parent to child to grandchild class
#4. Hierarchical Inheritance - one parent class to multiple child classes


#multi-level Inheritance
# Grandparent
#      │
#      ▼
#    Parent
#      │
#      ▼
#     Child

# class Grandparent:
#     def house(self):
#         print("Grandparent's house")

# class Parent(Grandparent):
#     def car(self):
#         print("Parent's car")

# class Child(Parent):
#     def bike(self):
#         print("Child's bike")

# c = Child()
# c.house()
# c.car()
# c.bike()


# #multi-level Inheritance
# class Father:
#     def skill1(self):
#         print("Driving")
    
# class Mother:
#     def skill2(self):
#         print("Cooking")

# class Child(Father, Mother):
#     def skill3(self):
#         print("Programming")

# c = Child()
# c.skill1()
# c.skill2()
# c.skill3()

#Hierarchical Inheritance
#Here there is one parent class and multiple child classes

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")

#     def stop(self):
#         print("Vehicle is stopping")

#     def horn(self):
#         print("Vehicle is honking")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is riding")

# class Bus(Vehicle):
#     def transport(self):
#         print("Bus is transporting passengers")

# c = Car()
# c.start()
# c.stop()
# c.horn()
# c.drive()

# b = Bike()
# b.start()
# b.stop()
# b.horn()
# b.ride()

# bus = Bus()
# bus.start()
# bus.stop()
# bus.horn()
# bus.transport()


#Constructor In Inheritance
#Without the super()

# class Parent:
#     def __init__(self):
#         print("Parent class constructor")

# class Child(Parent):
#     def __init__(self):
#         print("Child class constructor")

# c = Child()
#Here it searches for the child class first then on the Parent class

# class Parent:
#     def __init__(self):
#         print("Parent class constructor")

# class child(Parent):
#     def __init__(self):
#        pass
# c = child()
#Here it searches for the child class first then on the Parent class, since there is no constructor defined in the child class


#using th super
# class Parent:
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
       
#         print("Parent class constructor")
        
# class Child(Parent):
#     def __init__(self, a, b, c):
#         super().__init__(a, b)
#         self.c = c
#         print("Child class constructor")

# c = Child(1,2,3)
# print(c.a)
# print(c.b)
# print(c.c)

#Method Resolution Order (MRO) also known as Diamond method
#MRO defines the order in which Python searches for methods.
#    A
#   / \
#  ▼   ▼
# B     C
#   \ /
#    ▼
#    D

# class A:
#     def Show(self):
#         print("Method from class A")

# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
# d = D()
# d.Show()    


class A:
    def Show(self):
        print("Method from class A")

class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

print(D.mro())
