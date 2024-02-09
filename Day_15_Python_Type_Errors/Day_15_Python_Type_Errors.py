# Day 15 Python Type Errors

# SyntaxError
# print "hello world" # Programming language syntax missue

print("Hello World")

# NameError
print(age)  # age named variable is undefined
age = 25
print(age)

# IndexError
numbers = [1, 2, 3, 4, 5]
numbers[5] # List index starts from zero. There is no 5th index in the list

# ModuleNotFoundError
# import maths  # Ther is no maths module in the python programming language
# maths.pi
# There is no maths module in

# AttributeError
import math

# math.PI   # This function is not available in the module

math.pi

# KeyError
users = {"name": "Asab", "age": 250, "country": "Finland"}
print(users["name"])
print(users["county"])  # The key name used to retrieve the dictonary value is incorrect

print(users["country"])

# TypeError
sum = 4 + "3"
print(sum) # int data type and str data type cannot be combined

sum = 4 + int(3)
print(sum)

# ImportError
# from math import power # There is no function named power in math function

# ValueError
int("12a") # A Valueerror in python is a type of exception that occurs when a function receives an argument of the correct type but an inappropriate value

# ZeroDivisionError
print(1/0) #  A number is not divisible by zero