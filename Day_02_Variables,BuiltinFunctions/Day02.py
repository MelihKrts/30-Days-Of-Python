# Variables in Python
first_name = "Melih"
last_name = "Karatas"
country = "Turkey"
city = "Manisa"
age = 239
is_married = False
skills = ["HTML", "CSS", "JS", "React", "Python"]
person_info = {
    "firstName": "Melih",
    "lastName": "Karatas",
    "country": "Turkey",
    "city": "Manisa",
}

print("Hello, World!")
print("Hello", ",", "World", "!")
print(len("Hello, World!"))


print("First name:", first_name)
print("First name length:", len(first_name))
print("Last name:", last_name)
print("Last Name length:", len(last_name))
print("Country:", country)
print("Age:", age)
print("Married:", is_married)
print("Skills: ", skills)
print("Person information: ", person_info)

first_name, last_name, country, age, is_married = (
    "Asabeneh",
    "Yetayeh",
    "Helsinki",
    250,
    True,
)

print(first_name, last_name, country, age, is_married)
print("First name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
print("Married", is_married)

# Input

first_name = input("What is your name: ")
age = input("How old are you?: ")

print(first_name)
print(age)

# Different Python Types

first_name = "Aasabeneh"
last_name = "Yetayeh"
country = "Finland"
city = "Helsinki"
age = 239


# Printing out types
print(type("Asabeneh"))
print(type(first_name))
print(type(10))
print(type(3.14))
print(type(1 + 1j))
print(type(True))
print(type([1, 2, 3, 4]))
print(type({"name": "Asabeneh", "age": 239, "is_married": 250}))
print(type((1, 2)))
print(type(zip([1, 2], [3, 4])))

# Casting: Converting one data type to another data type.

# int to float
num_int = 10
print("num_int", num_int)

num_float = float(num_int)
print("num_float", num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)

num_str = str(num_int)
print(num_str)

# str to int or float
num_str = "10.6"
# print("num_str", int(num_str)) ValueError: invalid literal for int() with base 10: '10.6'

num_float = float(num_str)
print("num_float:", num_float)

# Value error, first float then float to int conversion to prevent error

num_int = int(num_float)
print("num_int:", num_int)

# str to list
first_name = "Asabeneh"
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)
