# Day 14 Higher Order Function


def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, lst):
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)


def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute


result = higher_order_function("square")
print(result(3))

result = higher_order_function("cube")
print(result(3))

result = higher_order_function("absolute")
print(result(-3))


# Python Closures


def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))


# Python Decorators


# Creating Decorators
def greeting():
    return "Welcome to Python"


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)
print(g())


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())

# Applying Multiple Decorators to a single Function


#  First Decorator
def uppercase_generator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# Second Decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())

# Accepting Parameters in Decorator Functions


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I Live in {}".format(para3))

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love Teach".format(first_name, last_name, country))


print_full_name("Asabeneh", "Yetayeh", "Finland")


# Built in Higher Order Function

# Map Function
# The map() function is a built-in that takes a function and iterable as parameters.
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))

numbers_str = ["1", "2", "3", "4", "5"]
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

# Filter Function
# The filter() It filters the items that satisfy the filtering criteria

numbers = [1, 2, 3, 4, 5]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))


def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]


def is_name_long(name):
    if len(name) > 7:
        return True
    else:
        return False


long_names = filter(is_name_long, names)
print(list(long_names))

# Reduce
# The reduce it does not return another iterable, instead it returns a single value.

import functools

numbers_str = ["1", "2", "3", "4", "5"]


def add_two_numbers(x, y):
    return int(x) + int(y)


total = functools.reduce(add_two_numbers, numbers_str)
print(total)
