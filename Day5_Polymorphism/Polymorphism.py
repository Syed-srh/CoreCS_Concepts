#Polymorphism means "many forms". It allows the same method name to behave differently depending on the object calling it.
#methos PverRiding is an Example of Polymorphism
# class Animal:
#     def speak(self):
#         return "Animal speaks"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
# # Create instances of Dog and Cat
# dog = Dog()
# cat = Cat()

# # Call the speak method on the instances
# print(dog.speak())  # Output: Woof!
# print(cat.speak())  # Output: Meow!

#Using super() in Method Overriding
#The super() function is used to call a method from the parent class. 

# It is useful when the child class wants to extend rather than completely replace the parent behavior.

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog barks")
# d = Dog()
# d.sound()

#Runtime Polymorphism (Method Overriding Based)
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# animals = [Dog(), Cat()]
# for a in animals:
#     a.sound()

#Duck typing means that the type of object is determined by its behavior rather than its class. 

# If an object has the required method, it can be used.
# class Dog:
#     def speak(self):
#         print("Woof!")
# class Cat:
#     def speak(self):
#         print("Meow!")
# def make_animal_speak(animal):
#     animal.speak()
# dog = Dog()
# cat = Cat()
# make_animal_speak(dog)  # Output: Woof!
# make_animal_speak(cat)  # Output: Meow!


#Singleton 
#A Singleton class ensures that only one instance of the class exists throughout the program and provides a global access point to that instance.
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)
    