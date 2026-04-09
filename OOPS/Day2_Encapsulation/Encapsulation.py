#Encapsulation is the bunding the related attribute and method into single entity

# class Car:
#     def __init__(self, brand, model, engine, speed_limit):
#         self.brand = brand
#         self.model = model
#         self.engine = engine
#         self.__speed_limit = speed_limit


# user_car = Car("BMW", "X5", "V8", 250)
# print(user_car.brand)
# print(user_car.model)
# print(user_car.engine)
# print(user_car._Car__speed_limit)

#Purpose of the Encapsulation
#1. The Data is hidden from the outside world and can only be accessed through the method of the class
#2. It helps to achieve data hiding
    
    #---->Access Modifier
    #1.public access : access for EveryOne
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
    
# m1 = Mobile("Apple", "iPhone 13", 999)
# print(m1.brand)
# print(m1.model)
# print(m1.price)

    #2.private access : Restricted access for only within the class and using __ before the variable name
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.__price = price
#     def get_price(self):
#         print(self.__price)
# m1 = Mobile("Apple", "iPhone 13", 999)
# print(m1.brand)
# print(m1.model)
# m1.get_price()

  #To update 
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.__model = model
#         self.__price = price
#     def get_price(self):
#         print(self.__price)
    
#     def set_model_price(self,model, price):
#         self.__model = model
#         self.__price = price

# m1 = Mobile("Apple", "iPhone 13", 999)
# print(m1.brand)
# print(m1._Mobile__model)
# m1.get_price()  
# m1.set_model_price("iPhone 17", 1099)
# print(m1._Mobile__model)
# print(m1._Mobile__price)


  #Here to 
    #get the data - get method
    #update the data - set method


#Protection layer 
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.__model = model
#         self.__price = price
#     def get_price(self):
#         print(self.__price)
    
#     def set_model_price(self,model, price):
#         self.__model = model
#         self.__price = price

#     def set_balance(self, balance, provided_secret_key):
#         if provided_secret_key == self.__secret_key:
#             self.__balance = balance
#         else:
#             print("Invalid secret key")

# m1 = Mobile("Apple", "iPhone 13", 999)
# print(m1.brand)
# print(m1._Mobile__model)
# m1.get_price()
# m1.set_model_price("iPhone 17", 1099)
# print(m1._Mobile__model)
# print(m1._Mobile__price)




#proper Encapsulation
class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
account = BankAccount()
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
