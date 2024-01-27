# Multiline

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python"""
print(multiline_string)

# String Concatenation
first_name = "Asabeneh"
last_name = "Yetayeh"
space = " "
full_name = first_name + space + last_name
print(full_name)

# Escape Sequences in Strings
# \n --> new line
# \t --> Tab means (8 lines)
# \\ --> backslash
# \' --> single quotes
# \" --> double quotes

print("I hope everyone is enjoying the Python Challange. \nAre you ?")
print("Days\tTopics\tExercises")
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("Day 3\t5\t23")
print("Day 4\t1\t35")
print("This is a backslash symbol (\\)")
print('In every programming language it starts with "Hello World!"')

# Old Style String Formatting (% Operator)

#  %s --> String
#  %d --> integer
#  %f --> Floating point numbers
#  %. unmber of digits --> floating point numbers with fixed precision

first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am %s %s. I teach %s" % (first_name, last_name, language)
print(formated_string)

# String and Numbers
radius = 10
pi = 3.14
area = pi * radius * 2
formated_string = "The area of circle with a radius %d is %.2f" % (radius, area)

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formated_string = "The following are python libraries:%s" % (python_libraries)
print(formated_string)

# New Style String Formating (str.format) Python version 3
first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am {} {}. I teach {}".format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a**b))

radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of a circle with a radius {} is {:2f}.".format(radius, area)
print(formated_string)

# String Interpolation
a = 4
b = 3

print(f"{a} + {b} = {a +b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

# Unpacking Characters
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

language = "Python"
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

language = "Python"
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

#  Slicing Python Strings
language = "Python"
first_three = language[0:3]
print(first_three)

last_three = language[3:6]
print(last_three)

last_three = language[-3:]
print(last_three)

last_three = language[3:]
print(last_three)

# Reversing a string

greeting = "Hello World!"
print(greeting[::-1])

# Skipping Character
language = "Python"
pto = language[0:6:2]
print(pto)

# String Methods
challange = "thirty days of python"
print(challange.capitalize())  # capitalize

# count
print(challange.count("y"))  # how many timnes letter
print(
    challange.count("y", 7, 14)
)  # Counts how many times the letter x occurs in the interval starting at index 7 and excluding 14
print(
    challange.count("th")
)  # Counts the number of occurrences of character sequence xy

# endwith
print(challange.endswith("on"))  # Checks if a string ends with a specified ending

# extendtabs space tabs special (?)
challange = "thirty\tdays\tof\tpython"
print(challange.expandtabs())
print(challange.expandtabs(10))

# find return index number
print(challange.find("y"))
print(challange.find("j"))

# rfind last return index number character find() different last find index
print(challange.rfind("y"))
print(challange.rfind("j"))

# format()
age = 250
job = "teacher"
country = "Finland"
sentence = "I am {} {}. I am a {}. I am {} years old. I live in {}.".format(
    first_name, last_name, job, age, country
)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius**2
result = "The area of a circle with radius {} is {}".format(str(radius), str(area))
print(result)

# index()
sub_string = "da"
print(challange.index(sub_string))

# rindex()
print(challange.rindex(sub_string))

# isalnum alfa numeric character control

challange = "ThirtyDaysPython"
print(challange.isalnum())

challange = "thirty days of python"
print(challange.isalnum())

# isalpha (az-AZ control)
challange = "ThirtyDaysPyhton"
print(challange.isalpha())

challange = "thirty days of python"
print(challange.isalpha())

# is decimal  all character decimal(0-9) control
challange = "thirty days of python"
print(challange.isdecimal())

challange = "129"
print(challange.isdecimal())

# isdigit all character (0-9 and unicode character) control

challange = "Thirty"
print(challange.isdigit())

challange = "\u00B2"
print(challange.isdigit())

#  isnumeric

num = "10"
print(num.isnumeric())

num = "\u00BD"  # ½
print(num.isnumeric())

num = "10.5"
print(num.isnumeric())

# isidentifier

challange = "30DaysOfPython"
print(challange.isidentifier())

challange = "thirty_days_of_python"
print(challange.isidentifier())

# islower
challange = "thirty days of python"
print(challange.islower())

challange = "Thirty days of python"
print(challange.islower())

# isupper
challange = "thirty days of python"
print(challange.isupper())

#  join
web_tech = ["HTML", "CSS", "JavaScript"]
result = " ".join(web_tech)
print(result)

result = "# ".join(web_tech)
print(result)

# strip
challange = "thirty days of pythoooonnnnnn"
print(challange.strip("noth"))

# change()
challange = "thirty days of python"
print(challange.replace("python", "coding"))

#  split
print(challange.split())
print(challange.split(", "))

# title
print(challange.title())

# swapcase Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
print(challange.swapcase())
challange = "THIRTY DAYS OF PYTHON"
print(challange.swapcase())

# startswith
challange = "thirty days of python"
print(challange.startswith("thirty"))

challange = "30 days of python"
print(challange.startswith("thirty"))
