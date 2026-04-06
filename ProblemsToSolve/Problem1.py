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