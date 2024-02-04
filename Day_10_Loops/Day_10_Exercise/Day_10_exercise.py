# Day 10 Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1

# for number in range(11):
#     print("For loop number", number)

# number = 0
# while number < 11:
#     print("While loop number", number)
#     number += 1

# 1.2
# for number in range(11, -1, -1):
#     print("Iterate 10 to 0 For loop", number)

# number = 10
# while number > -1:
#     print("Iterate 10 to 0 While loop", number)
#     number -= 1

# 1.3
n = 7
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("#", end="")
#     print()

# 1.4
a = 8
# for i in range(0, a):
#     for b in range(0, a):
#         print("# ", end="")
#     print()

# 1.5

# for i in range(0, 11):
#     print(i, "*", i, "=", i * i)

# 1.6
# pyt = ["Python", "Numpy", "Pandas", "Django", "Flask"]
# for pythons in pyt:
#     print(pythons)

# 1.9
# for i in range(0, 101, 2):
#     print(i)


# 1.10
# for i in range(0, 101, 1):
#     if i % 2 == 1:
#         print(i)


# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 2 Solution

# Level 2 Solution

# 2.1
total = 0
for i in range(total, 101):
    total += i
print("The sum of all numbers is", total)

# 2.2
even_number = 0
odd_number = 0
for i in range(101):
    if i % 2 == 0:
        even_number += i
    else:
        odd_number += i
print(
    "The sum of all evens is",
    even_number,
    "." + "And the sum of all odds is",
    odd_number,
)


# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 3 Solution

# Level 3 Solution

import sys

sys.path.append("../")

from data import countries
from data import countries_data

countries_with_land = [
    country for country in countries.countries if "land" in country.lower()
]
for country in countries_with_land:
    print(country)

# 3.2
fruit_list = ["banana", "orange", "mango", "lemon"]
reversed_list = []
for value in fruit_list:
    reversed_list = [value] + reversed_list
print("Reversed fruit list", reversed_list)

# 3.3.1
data_list = countries_data.countries_data
all_languages = []
for country_info in data_list:
    langugaes = country_info.get("languages", [])
    all_languages.extend(langugaes)

unique_language = set(all_languages)
total_language = len(unique_language)

print("Total number of languages in the data:", total_language)

# 3.3.2
all_languages = []
for country_info in countries_data.countries_data:
    languages = country_info.get("languages", [])
    all_languages.extend(languages)


language_counts = {}
for language in all_languages:
    language_counts[language] = language_counts.get(language, 0) + 1

sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)

top_ten_languages = sorted_languages[:10]

for language, count in top_ten_languages:
    print(f"Top ten most spoken languages: {language}: {count}")

# 3.3.3
sorted_countries = sorted(countries_data.countries_data, key=lambda x: x.get("population", 0), reverse=True)
top_ten_countries = sorted_countries[:10]
print("Top ten most populated countries:")
for country_info in top_ten_countries:
    name = country_info.get("name", "Unknown")
    population = country_info.get("population", "Unknown")
    print(f"{name}: {population}")