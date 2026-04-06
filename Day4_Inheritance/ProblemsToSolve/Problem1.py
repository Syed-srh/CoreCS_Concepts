# 1: Employee Management System
# Complete the Employee, Developer, and Manager classes by adding required features.

# Employee class:
# The Employee class should act as the parent class.

# Features to be added to Employee class
# Add below attributes:
# id
# name
# salary
# Add below methods:
# display_details() : Prints employee id, name, and salary
# Developer class:
# The Developer class inherits from Employee.

# Features to be added to Developer class
# Add below attributes:
# programming_language
# Add below methods:
# display_details() : Override parent method and include programming language
# Manager class:
# The Manager class inherits from Employee.

# Features to be added to Manager class
# Add below attributes:
# team_size
# Add below methods:
# display_details() : Override parent method and include team size


class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, id, name, salary, programming_language):
        super().__init__(id, name, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")


class Manager(Employee):
    def __init__(self, id, name, salary,team_size):
        super().__init__(id, name, salary)
        self.team_size = team_size
    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")
