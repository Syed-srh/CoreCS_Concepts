#Association is a relationship where two independent classes are connected, but neither depends on the other for existence.

# Both objects can exist independently
# They interact with each other
# Real-World Example
# A Teacher teaches Students
# A Customer places Orders
# In both cases:

# Teacher can exist without Student
# Student can exist without Teacher

# class Student:
#     def __init__(self, name):
#         self.name = name 

# class Teacher:
#     def __init__(self, name):
#         self.name = name 
#     def teach(self, student):
#         print(f"{self.name} is teaching OOPs to {student.name}")

# s1 = Student("Syed")
# t1 = Teacher("Mr. Varsha")
# t1.teach(s1)

#Here we pass the student object to the teacher's teach method, demonstrating the association between the two classes.
    #Teacher  --------->  Student
        # (uses)


# Aggregation is a special form of association where one class contains a reference to another class.

# Represents a "has-a" relationship
# Child object can exist independently of parent


# Real-World Example
# A Department has Teachers
# A Team has Players
# Even if:

# Department is removed → Teachers still exist


# class Teacher:
#     def __init__(self,name):
#         self.name = name 

# class Department:
#     def __init__(self, name, teachers):
#         self.name = name 
#         self.teachers = teachers

#     def show(self):
#         print(f"Department: {self.name}, teachers: {self.teachers.name}")
    
# t1 = Teacher("Varsha")
# dept = Department("Computer Science", t1)

# dept.show()

#here in this the Department is Dependent Where as the teacher is Independent. If we delete the Department object, the Teacher object still exists. This illustrates the concept of aggregation, where the Department "has-a" Teacher, but the Teacher can exist independently of the Department.
# Department contains a Teacher object
# Teacher object is created outside and passed in
# Teacher exists independently


    # Department  ------->  Teacher
        # (has-a)


#Composition is a strong form of aggregation where:

# One class owns another class
# Child object cannot exist without parent object

#  Real-World Example
# A House has Rooms
# A Car has an Engine
# If:

# House is destroyed → Rooms do not exist independently

# class Engine:
#     def __init__(self):
#         self.type = "Petrol"

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # created inside

#     def show(self):
#         print(f"Car has {self.engine.type} engine")

# c = Car()
# c.show()

# Engine object is created inside Car
# Engine cannot exist without Car in this design
# Strong ownership

# Car  =======>  Engine
# (owns completely


# Key Differences
# Feature	Association	Aggregation	Composition
# Relationship	Uses	Has-a	Owns
# Dependency	Independent	Weak dependency	Strong dependency
# Object Life	Independent	Independent	Dependent
# Example	Teacher–Student	Department–Teacher	Car–Engine