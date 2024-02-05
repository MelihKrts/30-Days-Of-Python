# Functions
# Function without parameters


def generate_full_name():
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()


def generate_full_name():
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())

# Function with Parameters

# Single parameters


def greetings(name):
    message = name + ", welcome to Python for Everyonee!"
    return message


print(greetings("Asabeneh"))


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90))


def square_number(x):
    return x * x


print(square_number(2))


def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area


print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        # if i % 2 == 0: even number
        total += i
    return total


print(sum_of_numbers(10))
print(sum_of_numbers(100))


# Two Parameter
def generate_full_name(first_name, last_name):
    space = " "
    full_name = first_name + space + last_name
    return full_name


print("Full Name :", generate_full_name("Asabeneh", "Yetayeh"))


def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum


print("Sum of two numbers: ", sum_two_numbers(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print("Age:", calculate_age(2023, 1821))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity)
    return weight


print("Weight of an object in Newtons:", weight_of_object(100, 9.81))


# Passing Arguments with Key and Value
def print_fullname(firstname, lastname):
    space = " "
    full_name = firstname + space + lastname
    print(full_name)


print(print_fullname(firstname="Asabeneh", lastname="Yetayeh"))


def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)


add_two_numbers(num2=3, num1=2)


# Fuction returning a value Part 2


# string
def print_name(firstname):
    return firstname


print_name("Asabeneh")


def print_full_name(firstname, lastname):
    space = " "
    full_name = firstname + space + lastname
    return full_name


print(print_full_name(firstname="Asabeneh", lastname="Yetayeh"))

# Number


def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print(calculate_age(2023, 1819))


# Returning boolean
def is_even(n):
    if n % 2 == 0:
        print("even")
        return True
    return False


print(is_even(10))
print(is_even(7))


# Returning a list
def find_even_number(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_number(10))


# Function with Default Parameters
def greetings(name="Peter"):
    message = name + ", welcome to Python for Everyone!"
    return message


print(greetings())
print(greetings(name="Asabeneh"))


def generate_full_name(first_name="Asabeneh", last_name="Yetayeh"):
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
print(generate_full_name("David", "Smith"))


def calculate_age(birty_year, current_year=2023):
    age = current_year - birty_year
    return age


print("Age: ", calculate_age(1821))


def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity) + " N"
    return weight


print(
    "Weight of an object in Newtons: ", weight_of_object(100)
)  # 9.81 - average gravity on Earth's surface
print(
    "Weight of an object in Newtons: ", weight_of_object(100, 1.62)
)  # gravity on the surface of the Moon


# Arbitary Number of Arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_nums(2, 3, 5))


# Default and Arbitary Number of Parameters in Functions


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


print(generate_groups("Team-1", "Asabeneh", "Brook", "David", "Eyob"))


# Function as a parameter of Another Function
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))


def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))
