# Exercise Level 1 Solution

# 1.2
# Day 2: 30 Days of python programming

# 1.3

first_name = "Melih"

# 1.4
last_name = "Karatas"

# 1.5
fullName = first_name + " " + last_name

# 1.6
country = "Turkey"

# 1.7
city = "Manisa"

# 1.8
age = 23

# 1.9
year = 2024

# 1.10
is_married = False

# 1.11
is_true = True

# 1.12
is_light_on = False

# 1.13
first_name, last_name, country, city, age, is_married = (
    "Melih",
    "Karatas",
    "Turkey",
    "Manisa",
    23,
    False,
)


# Exercise Level 2 Solution

# 2.1
print(type(first_name))
print(type(last_name))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2.2
print("First name length:", len(first_name))

# 2.3
print("Last name length:", len(last_name))
print(len(first_name) < len(last_name))

# 2.4
num_one = 5
num_two = 4

# 2.4.1
total = num_one + num_two
print(total)

# 2.4.2
diff = num_two - num_one
print(diff)

# 2.4.3
product = num_two * num_one
print(product)

# 2.4.4
division = num_one / num_two
print(division)

# 2.4.5
remainder = num_two % num_one
print(remainder)

# 2.4.6
exp = num_one**num_two
print(exp)

# 2.4.7
Floor_division = num_one // num_two
print(Floor_division)

# 2.5
import math  # PI number
radius = 30

# 2.5 (circle area and circumference calculate)
radius = int(input("Enter a radius: "))

area_of_circle = math.pi * radius * radius
circum_of_circle = 2 * math.pi * radius
print("Circle area:", area_of_circle)
print("Circle circumference:", circum_of_circle)

# 2.6
user_first_Name = input("Enter a first name: ")
user_last_name = input("Enter a last name: ")
user_country = input("Enter a Country: ")
user_age = int(input("Enter a age: "))

print("----------------------")
print("First name: ", user_first_Name)
print("Last name: ", user_last_name)
print("Country: ", user_country)
print("Age: ", user_age)

# 2.7
help("keywords")
