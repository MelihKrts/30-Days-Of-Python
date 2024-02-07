language = "Python"
lst = list(language)
print(type(lst))
print(lst)

# list comprehension
lst = [i for i in language]
print(type(lst))
print(lst)

# Generating Numbers
numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i * i) for i in range(11)]
print(numbers)

# If Expression

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattaned_list = [number for row in list_of_lists for number in row]
print(flattaned_list)

# Creating a Lambda Function


def add_two_numbers(a, b):
    return a + b


print(add_two_numbers(2, 3))

add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))

print((lambda a, b: a + b)(2, 3))

square = lambda x: x**2
print(square(3))

cube = lambda x: x**3
print(cube(3))

multiple_variable = lambda a, b, c: a**2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))

# Lambda function inside another function


def power(x):
    return lambda n: x**n


cube = power(2)(3)
print(cube)

two_power_of_five = power(2)(5)
print(two_power_of_five)