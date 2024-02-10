# Day 17 Exception Handling

try:
    print(10 + "5")
except:
    print("Something went wrong")

try:
    name = input("Enter your name: ").capitalize()
    year_born = input("Year you were born: ")
    age = 2024 - int(year_born)
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print("Type error occured")
except ValueError:
    print("Value error occured")
except ZeroDivisionError:
    print("Zero division error occured")
else:
    print("I usually run with the try block")
finally:
    print("I alway run")

# Shorten the about code as follows:

try:
    name = input("Enter your name")
    year_born = input("Year you born:")
    age = 2024 - int(year_born)
    print(f"You are {name}. And your age is {age}")
except Exception as e:
    print(e)

# Packing and Unpacking Arguments in Python

# * tuples
# ** dictionaries

# Unpacking

# Unpacking List


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst))


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

numbers = range(2, 7)
print(list(numbers))

args = [2, 7]
numbers = range(*args)
print(numbers)

# A list or a tuple can also be unpacked
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)


# Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} year old"


dct = {"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "age": 250}
print(unpacking_person_info(**dct))


# Packing List
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))


# Packing Dictionaries


def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key}= {kwargs[key]}")
    return kwargs


print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

# Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)

country_lst_one = ["Finland", "Sweden", "Norway"]
country_lst_two = ["Denmark", "Iceland"]
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# Enumerate
for index, item in enumerate([20, 30, 40]):
    print(index, item)


for index, i in enumerate(countries):
    print("hi")
    if i == "Finland":
        print(f"The country {i} has been found at index {index}")


# Zip
fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({"fruit": f, "veg": v})
print(fruits_and_veges)