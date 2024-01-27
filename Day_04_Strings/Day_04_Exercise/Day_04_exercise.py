# Day 4 Exercise Solution

# 1
first_word = "Thirty"
second_word = "Days"
third_word = "Of"
fourth_word = "Python"
space = " "

single_string = (
    first_word + space + second_word + space + third_word + space + fourth_word
)
print(single_string)

# 2
coding = "Coding"
for_word = "For"
all_word = "All"

single_string = coding + space + for_word + space + all_word
print(single_string)

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
company = "cODING fOR aLL"
print(company.swapcase())

# 9
company = "Coding For All"
print(company[0:6])

# 10
print(company.index("Coding"))
print(company.find("Coding"))

# 11
print(company.replace("Coding", "Python"))

# 12
print("Python for Everyone".replace("Everyone", "All"))

# 13
print(company.split())

# 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split())

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])

# 18
name = "Python For Everyone"
abbr = "".join(x[0] for x in name.split())
print(abbr)

# 19
name = "Coding For All"
abbr = "".join(x[0] for x in name.split())
print(abbr)

# 20
print(company.index("C"))

# 21
print(company.index("F"))

# 22
print(company.rfind("l"))

# 23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.find("because"))

# 24
print(sentence.rindex("because"))

# 25
print(sentence.replace("because because because", ""))

# 26
print(sentence.find("because"))

# 27
print(sentence.replace("because because because", ""))

# 28
name = "Coding For All"
print(name.startswith("Coding"))

# 29
print(name.startswith("coding"))

# 30
name_trim = "   Coding For All      "
print(name_trim.strip(" "))

# 31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" * ".join(libraries))

# 33
print("I am enjoying this challenge\nI just wonder what is next")

# 34
print("Name\tAge\tCountry\tCity")
print("Melih\t23\tTurkey\tManisa")

# 35
radius = 10
area = 3.14 * radius**2
string_format = "The area of a circle with radius %d is %d meters square" % (
    radius,
    area,
)
print(string_format)

# 36
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
