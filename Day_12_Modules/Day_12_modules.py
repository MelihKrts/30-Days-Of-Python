# Modules

# Creating Module

# Import Module

import mymodule

print(mymodule.generate_fullname("Asabeneh", "Yetayeh"))

# Import Functions from a Module

from mymodule import generate_fullname, sum_two_nums, person, gravity

print(generate_fullname("Asabeneh", "Yetayeh"))
print(sum_two_nums(1, 9))

mass = 100
weight = mass * gravity
print(weight)
print(person["firstname"])

# Import Functions from a Module and Renaming
from mymodule import (
    generate_fullname as fullname,
    sum_two_nums as total,
    person as p,
    gravity as g,
)

print(fullname("Asabeneh", "Yetayeh"))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p["firstname"])

# Import Built-in Modules

# OS Module

import os

# Creating a directory
# os.mkdir("c:/test/30_Days_Python")

# Changing the current directory
# os.chdir("path")

# Getting currnet working directory
# os.getcwd()

# Removing directory
# os.remove()

# Some useful sys commands
import sys

# to exit sys
# sys.exit()

# To know the largest integer variable it takes
sys.maxsize

# To know environment path
sys.path
# print(sys.path)

# To know the version of python you are using
# print(sys.version)


# Statistics Module

from statistics import *  # importing all the statistics modules

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# Math module
import math

print(math.pi)  # 3.141592653589793, pi constant
print(math.sqrt(2))  # 1.4142135623730951, square root
print(math.pow(2, 3))  # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))  # 2, logarithm with 10 as base

from math import pi

print(pi)

from math import pi, sqrt, pow, floor, ceil, log10

print(pi)  # 3.141592653589793
print(sqrt(2))  # 1.4142135623730951
print(pow(2, 3))  # 8.0
print(floor(9.81))  # 9
print(ceil(9.81))  # 10
print(math.log10(100))  # 2

from math import *

print(pi)  # 3.141592653589793, pi constant
print(sqrt(2))  # 1.4142135623730951, square root
print(pow(2, 3))  # 8.0, exponential
print(floor(9.81))  # 9, rounding to the lowest
print(ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))  # 2

from math import pi as PI

print(PI)

# String Module
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# Random Module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive