#interface in oops 
#interface is a blueprint of class which has only abstract method and no data member
#interface is used to achieve abstraction and multiple inheritance in java

# class flyable:
#     def how_it_flys(self):
#         pass

# class bird(flyable):
#     def how_it_flys(self):
#         print("Birds fly by flapping their wings")

# class Aeroplane(flyable):
#     def how_it_flys(self):
#         print("Aeroplanes fly by using engines")

# #Creating objects of the classes
# bird1 = bird()
# aeroplane1 = Aeroplane()
# #Calling the methods
# bird1.how_it_flys()
# aeroplane1.how_it_flys()

#Here
#Flyable acts like an interface
#Bird and Airplane are unrelated classes
#Both implement the fly() method in their own way


#Interface-Based Abstraction
# class vehicle:
    


#Multiple Interface Implementation
class Engine:
    def start(self):
        pass

class Gps:
    def navigate(self):
        pass

class Car(Engine, Gps):
    def start(self):
        print("Engine started")
    
    def navigate(self):
        print("Navigation started")

car = Car()
car.start()
car.navigate()