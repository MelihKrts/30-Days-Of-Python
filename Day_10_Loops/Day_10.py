# Day 10 Loops

# While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# For Loop

# For loop list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# For loop string
language = "python"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# for loop tuple

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space Street", "zipcode": "02210"},
}

#  key of the dictionary
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # keys and values

for value in person.items():  # values
    print(value)

#  loops in set

it_compaines = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_compaines:
    print(company)

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be", number + 1) if number != 5 else print("Loop's end")
print("outside loops")

# Range Function
lst = list(range(11))
print(lst)

st = set(range(1, 11))
print(st)

lst = list(range(0, 11, 2))
print(lst)

st = set(range(0, 11, 2))
print(st)

# Nested Loops
for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

# For Else
for number in range(11):
    print(number)
else:
    print("The loop stops at", number)

# Pass
for number in range(6):
    pass
