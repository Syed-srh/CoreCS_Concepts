# 3: School Hierarchy System
# Complete the Person, Student, and Teacher classes.

# Person class:
# The Person class acts as the base class.

# Features to be added to Person class
# Add below attributes:
# name
# age
# Add below methods:
# display_info() : Prints name and age
# Student class:
# The Student class inherits from Person.

# Features to be added to Student class
# Add below attributes:
# grade
# Add below methods:
# display_info() : Override and include grade
# Teacher class:
# The Teacher class inherits from Person.

# Features to be added to Teacher class
# Add below attributes:
# subject
# Add below methods:
# display_info() : Override and include subject



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade_level = grade 
    def display_info(self):
        super().display_info()
        print(f"Grade: {self.grade_level}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject 
    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

# Example usage:
student = Student("Alice", 20, "A")
student.display_info()
teacher = Teacher("Bob", 35, "Math")
teacher.display_info()
