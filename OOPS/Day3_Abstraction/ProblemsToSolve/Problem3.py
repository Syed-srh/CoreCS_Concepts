# Practice Scenario 3: Employee System
# Complete the Employee and its subclasses.

# Employee class:
# The Employee class should be abstract.

# Features to be added to Employee class:
# Add below attributes:

# id
# name
# salary
# Add below methods:

# work() : Abstract method
# get_details() : Prints employee details
# Subclasses:
# Developer and Manager inherit from Employee.

# Features to be added:
# Add below methods:

# work() : Define role-specific work


from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    def get_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def work(self):
        print(f"{self.name} is coding")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing")

#Example
dev = Developer(1, "Alice", 50000)
mgr = Manager(2, "Bob", 70000)

dev.work()
dev.get_details()

mgr.work()
mgr.get_details()
