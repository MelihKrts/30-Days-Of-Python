# Day 8 Dictionaries Exercise Solution

# Exercise Solution

# 1
dog = {}

# 2
dog = {"name": "Lucky", "breed": "Golden Retreiver", "legs": 4, "age": 3}

# 3
student = {
    "first_name": "Daphne",
    "last_name": "Cameron",
    "gender": "female",
    "age": 26,
    "marital_status": False,
    "skills": ["Swim", "Java", "PHP", "C#"],
    "country": "Brazil",
    "city": "Rio de Janeiro",
    "address": "Avenida Croton 1737",
}

# 4
print("Length:", len(student))

# 5
print("Student Skills:", student["skills"])
print("Skills types:", type(student["skills"]))

# 6
student["skills"] += ["Instrument playing", "Fitness", "Caligraphy"]

# Alternative 2
# student["skills"].extend(["Instrument playing", "Fitness", "Caligraphy"])

print(student)

# 7

convert_list_keys = list(student.keys())

print("Converted List:", convert_list_keys)
print(type(convert_list_keys))

# 8
convert_list_values = list(student.values())
print("Values:", convert_list_values)
print(type(convert_list_values))

# 9
cvrt_dic_to_list = list(student.items())
print(cvrt_dic_to_list)
print(type(cvrt_dic_to_list))

# 10
student.pop("marital_status")
print(student)

# 11
del student
