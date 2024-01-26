# Day 3 Exercise Solution

# Exercise Solution

# 1
my_age = 23
print(type(my_age))

# 2
my_height = 1.91
print(type(my_height))

# 3
complex_number = 1 + 1j
print(type(complex_number))

# 4
base = int(input("Enter base: "))
height = int(input("Enter height: "))
triangle = 0.5 * base * height
convert_triangle = int(triangle)
print("The area of the triangle is", convert_triangle)

# 5
first_side = int(input("Enter first side: "))
second_side = int(input("Enter second side: "))
third_side = int(input("Enter third side: "))
perimeter = first_side + second_side + third_side
print("The perimeter of triangle is: ", perimeter)

# 6

length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
area = length * width
perimeter = 2 * (length + width)
print("Rectangle area: ", area)
print("Rectangle perimeter:", perimeter)

# 7
import math

radius = int(input("Enter a radius: "))
circle_area = math.pi * radius * radius
circle_ference = 2*math.pi*radius
print("Circle area:", circle_area)
print("Circle ference: ", circle_ference)

# 8
slope = 2
y_intercept = 2
x_intercept = 1
print(f"Slope: (m): {slope}")
print(f"Y-intercept (b): {y_intercept}")

# 9
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_calculate = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Slope (m): {int(slope_calculate)}")
print(f"Euclidean disatnce (d): {distance}")

# 10
# checked


# 11
def quadratic_equation(x):
    return x**2 + 6 * x + 9


x_values = [-3, -2, -1, 0, 1, 2, 3]

for x in x_values:
    y = quadratic_equation(x)
    print(f"For x = {x}, y = {y}")

    a = 1
b = 6
c = 9


discriminant = b**2 - 4 * a * c

if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print(f"Solutions for x: {x1}, {x2}")
else:
    print("No real solutions for x (discriminant is negative)")

# 12
word_one = "python"
word_two = "dragon"

print(len(word_one) != len(word_two))

# 13
print("on" in word_one and "on" in word_two)

# 14
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

# 15
print("on" in word_one and "on" in word_two)

# 16
find_length = len(word_one)
print(find_length, type(find_length))

# 16.1
convert_float = float(find_length)
print(type(convert_float))

# 16.2
convert_string = str(find_length)
print(type(convert_string))

# 17
number = 4

print(number % 2 == 0)

# 18

number_one = 7
number_two = 3
floor_division = number_one // number_two

converted_value = int(2.7)
print(floor_division == converted_value)

# 19
print(10 == "10")

# 20
print(int(9.8) == 10)

# 21
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
earning = hours * rate
print("Your weekly earning is: ", earning)

# 22
year = int(input("Enter number of years you have lived: "))
day = 365
hour = 24
minute = 60
second = 60

one_year_second = second * minute * hour * day
all_second = one_year_second * year
print(f"You have lived for {all_second} seconds ")

# 23
for number in range(1, 6):
    print(number, number**0, number**1, number**2, number**3)
