# Day 09 Conditions Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1
legal_age = 18
age = int(input("Enter your age: "))
incomplete_year = legal_age - age

if age >= legal_age:
    print("You are old enough to learn to drive")
elif legal_age - age:
    print(f"You need {incomplete_year} more years to learn to drive")
else:
    print("Wrong value enter")

# 1.2
my_age = 23
your_age = int(input("Enter your age: "))
age_different = abs(my_age - your_age)

if age_different == 1:
    print("1 year difference in age")
elif age_different > 1:
    if your_age > my_age:
        print(f"You are {age_different} years older than me")
    elif your_age < my_age:
        print(f"I am {age_different} years older than you")
    else:
        print("We are the same age")
else:
    print("Wrong Value")

# 1.3

get_number_one = int(input("Enter number one: "))
get_number_two = int(input("Enter number two: "))
if get_number_one > get_number_two:
    print(f"{get_number_one} greater than {get_number_two}")
elif get_number_one < get_number_two:
    print(f"{get_number_one} is less {get_number_two}")
else:
    print(f"{get_number_one} is equal to {get_number_two}")


# ------------------------------------------------------------------------------------------------------------------


# Exercise Level 2 Solution

# Level 2 Solution

# 2.1

score = int(input("Enter your Score: "))

if 80 <= score <= 100:
    print("Grades: A")
elif 70 <= score <= 79:
    print("Grades: B")
elif 60 <= score <= 69:
    print("Grades: C")
elif 50 <= score <=59:
    print("Grades: D")
elif 0 <= score <=49:
    print("Grades: F")


# 2.2
month_input = input("Enter a month name: ").capitalize()
if month_input in ("September", "October", "December"):
    season = "Autumn"

elif month_input in ("December", "January", "February"):
    season = "Winter"

elif month_input in ("March", "April", "May"):
    season = "Spring"

elif month_input in ("June", "July", "August"):
    season = "Summer"
else:
    print("Wrong Value")

print("Season is a:", season)

# 2.3
fruits = ["banana", "orange", "mango", "lemon"]
fruit_input = input("Enter fruit name: ")

if fruit_input.lower() not in fruits:
    fruits.append(fruit_input.lower())
    print(f"{fruit_input} added to the list. Modified list:{fruits}")
else:
    print(f"That fruit already exits in the list")


# ------------------------------------------------------------------------------------------------------------------


# Exercise Level 3 Solution

# Level 3 Solution

# 3.1

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

if "skills" in person:
    skill_list = person["skills"]
    if skill_list:
        middle_index = len(skill_list) // 2
        middle_skill = skill_list[middle_index]
        print(f"Middle Skill: {middle_skill}")
else:
    print("The person dictionary does not have a 'skills' key.")

# 3.2
if "skills" in person:
    skill_list = person["skills"]
    if skill_list:
        skill_control = "Python" in skill_list
        print("Result: ", skill_control)
else:
    print("The person dictionary does not have a 'skills' key.")

# 3.3
if "skills" in person:
    skill_list = person["skills"]

    if "JavaScript" in skill_list and "React" in skill_list and len(skill_list) == 2:
        print("He is a front end developer")

    elif "Node" in skill_list and "Python" in skill_list and "MongoDB" in skill_list:
        print("He is a backend developer")

    elif "React" in skill_list and "Node" in skill_list and "MongoDB" in skill_list:
        print("He is a fullstack developer")
    else:
        print("Unknown title")
else:
    print("The person dictionary does not have a 'skills' key.")

# 3.4
if "is_married" in person and "country" in person:
    married = person["is_married"]
    country_fin = person["country"]

    if married  and country_fin  == "Finland":
        print(
            person["first_name"],
            person["last_name"],
            "lives in",
            person["country"],
            ". He is married",
        )
    else:
        print("He is not married and does not live in Finland.")
else:
    print("No contact information found ")

