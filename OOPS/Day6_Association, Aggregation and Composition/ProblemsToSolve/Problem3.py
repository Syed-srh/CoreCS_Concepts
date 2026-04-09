# 3: Company–Employee System (Aggregation)
# Design Employee and Company classes.

# Features to be added to Employee class
# Add below attributes:
# name
# salary
# Add below methods:
# display_employee() : Prints employee details
# Features to be added to Company class
# Add below attributes:
# company_name
# employees (list of Employee objects)
# Add below methods:
# show_employees() : Prints all employee details
# Additional Requirements
# Create multiple Employee objects independently
# Pass them into Company
# Demonstrate that employees exist even if Company is not used


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Company:

    #To show the (list of Employee objects)
    def __init__(self, company_name, employees):
        self.company_name = company_name
        self.employees = employees
    def show_employees(self):
        print(f"Company: {self.company_name}")
        for emp in self.employees:
            emp.display_details()

        ##Additional Requirements
# Create multiple Employee objects independently
# Pass them into Company
# Demonstrate that employees exist even if Company is not used

# Create Employee objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 55000)
# Create Company object with list of employees
company = Company("Tech Solutions", [emp1, emp2, emp3])
# Show employees in the company
company.show_employees()
# Show that employees exist even if Company is not used
emp1.display_details()
emp2.display_details()
emp3.display_details()
