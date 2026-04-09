
class Student1:
    def __init__(self, name, rollno):
        self.name = name 
        self.rollno = rollno
    def display_stud_details(self):
        print(f"Student Name: {self.name}, Roll No: {self.rollno}")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self, student):
        print(f"{self.name} is teaching {self.subject} to {student.name}")

    def display_teacher_details(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}")

s1 = Student1("Syed", 101)
s2 = Student1("Rahil", 102)
t1 = Teacher("Varsha Sir", "OOPs")

t1.teach(s1)
t1.teach(s2)
t1.display_teacher_details()
s1.display_stud_details()
s2.display_stud_details()