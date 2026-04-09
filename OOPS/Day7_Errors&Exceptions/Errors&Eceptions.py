#Errors in Pyhton 
# Syntax Error
# The Error in  the Syntax of the code is called Syntax Error
# Example of Syntax Error
# # print("Hello World  # This will give Syntax Error because of missing closing quotation mark"
      
# Output:
# SyntaxError: unexpected EOF while parsing
# Explanation
# The closing parenthesis is missing
# Python cannot interpret incomplete syntax

#Runtime Error(Exception)
#Here the Syntax is correct but the code gives an error when we run it
# Example of Runtime Error
# # a = 10
# # b = 0
# # print(a/b)#   # This will give Runtime Error because division by zero is not allowed
# Output:
# ZeroDivisionError: division by zero
# Explanation
# The code is syntactically correct but it tries to perform an illegal operation (division by
# zero), which causes a runtime error.

# Logical Errors
# Logical errors occur when the program runs without crashing but produces incorrect results
# These errors are harder to detect because no error message is shown
# They occur due to incorrect logic or formula
#Example
# # def calculate_area(length, breadth):
# #     return length + breadth
# # print(calculate_area(5, 3))
# Output:
# 8
# Explanation   
# The correct formula should be multiplication
# The program executes successfully but produces wrong output

# Understanding Exceptions
# An exception is an event that disrupts the normal flow of execution
# Python creates an exception object when an error occurs
# If not handled, the program terminates
# If handled, the program continues execution
# Common built-in exceptions include
# ZeroDivisionError --> Raised when division by zero is attempted
# ValueError --> Raised when a function receives an argument of the right type but inappropriate value
# TypeError --> Raised when an operation is applied to an object of inappropriate type
# IndexError --> Raised when a sequence subscript is out of range
# FileNotFoundError --> Raised when trying to open a file that does not exist

# Basic Structure
# Python uses try and except blocks to handle exceptions
# Syntax

# try:
#     # code that may cause error
# except:
#     # code to handle error

# --> The try block contains risky code
#-->  The except block contains handling logic

# number = int(input("Enter a number: "))
# list_a = [1, 2, 3, 4, 5]
# try:
#     print(list_a[number])
# except IndexError:
#     print("Index is out of bounds.")
# print("Program continues after handling the exception.")

#finally block
# The finally block is used to execute code regardless of whether an exception occurred or not
# Syntax
# try:
#     # code that may cause error
# except:
#     # code to handle error
# finally:
#     # code that will always execute
#Examole 
# number = int(input("Enter a number: "))
# list_a = [1, 2, 3, 4, 5]
# try:
#     print(list_a[number])
# except IndexError:
#     print("Index is out of bounds.")
# finally:
#     print("Program continues after handling the exception.")

#raise 
#when we want to manually raise an exception, we can use the raise keyword
#Syntax
# raise ExceptionType("Error message")

#Example
# age = int(input("Enter age: "))
# if age < 18:
#     raise Exception("Age must be 18 or above")
# print("Access granted")

# Custom Exceptions
#      Definition
# Custom exceptions are user-defined error types
# They help represent domain-specific problems

# class InsufficientBalance:
#     pass
# balance = 1000
# withdraw = int(input("Enter amount: "))
# if withdraw > balance:
#     raise InsufficientBalanceError("Insufficient balance")
# print("Transaction successful")