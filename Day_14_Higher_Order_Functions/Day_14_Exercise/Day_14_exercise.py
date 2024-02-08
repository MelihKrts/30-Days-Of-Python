# Day 14 Higher Order Function Exercise Solution

# Exercise Solution

# Level 1 Solution

# 1.1

# Map function to each element of iterator and collects result.

# Filter applies function to each element of iterator and collect those elements for which function returns true.

# Reduce apllies rolling computation to sequential pair of elements in iterator. Initially it takes two elements from iterator in sequence, applies function, collect result, then take next element, in sequence from iterator, applies function and repeat this untill listhas single value


# 1.2

# Higher Order Function: A higher order function is a function that can take other functions as arguments or return functions as results.

# Closure: A closure is a function that captures the environment in which it was created, including the variables in its lexical scope, even after that scope has finished executing.

# Decorator: It wraps another function, modifying its behavior without changing its code directly


# 1.3


def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


def cube(x):
    return x**3


# 1.4
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]

for country in countries:
    print("Country:", country)


# 1.5
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]

for name in names:
    print("Name: ", name)


# 1.6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)


# ------------------------------------------------------------------------------------------------------------------


# Exercise Level 2 Solution

# Level 2 Solution

# 2.1


def upper_country(country):
    return country.upper()


uppercased_country = map(upper_country, countries)
print(list(uppercased_country))

# 2.2


def square(x):
    return x**2


squared_number = map(square, numbers)
print(list(squared_number))

# 2.3


def upper_name(name):
    return name.upper()


uppercased_name = map(upper_name, names)
print(list(uppercased_name))


# 2.4
def country_land(country):
    if "land" in country:
        return True
    else:
        return False


containing_land = filter(country_land, countries)
print(list(containing_land))

# 2.5


def six_lngth_cntry(country):
    if len(country) == 6:
        return True
    else:
        return False


six_character = filter(six_lngth_cntry, countries)
print(list(six_character))


# 2.6


def more_than_six_lngth(country):
    if len(country) >= 6:
        return True
    else:
        return False


more_than_cntry = filter(more_than_six_lngth, countries)
print(list(more_than_cntry))


# 2.7
def start_letter(country):
    if country[0] == "E":
        return True
    else:
        return False


start = filter(start_letter, countries)
print(list(start))


# 2.8

import functools

all_in = functools.reduce(
    lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**3, numbers))
)
print(all_in)

# 2.9


def get_string_list(input_list):
    return [item for item in input_list if isinstance(item, str)]


mixed_list = [1, "apple", 3, "banana", "cherry", 4]
string_list = get_string_list(mixed_list)
print(string_list)

# 2.10


def sum_numbers(num1, num2):
    return num1 + num2


total_reduce = functools.reduce(sum_numbers, numbers)
print(total_reduce)


# 2.11


def concatenate(message, country):
    return f"{message}, {country}"


joined_msg = functools.reduce(concatenate, countries) + " are north European Countries."
print(joined_msg)


# 2.12

from countries import countries


def land_country(country):
    return "land" in country


def ia_country(country):
    return "ia" in country


def island_country(country):
    return "island" in country


def stan_country(country):
    return "stan" in country


def categorize_countries(category):
    if category == "land_country":
        return filter(land_country, countries)
    elif category == "ia_country":
        return filter(ia_country, countries)
    elif category == "island_country":
        return filter(island_country, countries)
    elif category == "stan_country":
        return filter(stan_country, countries)


land_countries = categorize_countries("land_country")
ia_countries = categorize_countries("ia_country")
island_countries = categorize_countries("island_country")
stan_countries = categorize_countries("stan_country")


print("Land Countries:")
print(list(land_countries))
print()

print("IA Countries:")
print(list(ia_countries))
print()

print("Island Countries:")
print(list(island_countries))
print()

print("Stan Countries:")
print(list(stan_countries))
print()


# 2.13
from collections import defaultdict


def count_countries_starting_with_each_letter(country_names):
    country_count = defaultdict(int)
    for country in country_names:
        first_letter = country[
            0
        ].upper()  # Get the first letter of the country name and convert it to uppercase
        country_count[
            first_letter
        ] += 1  # Increment the count for the corresponding letter
    return country_count


country_dict = count_countries_starting_with_each_letter(countries)
print(country_dict)


# 2.14


def get_first_ten_countries(country):
    return country[:10]


print(get_first_ten_countries(countries))

# 2.15


def get_last_ten_countries(country):
    return country[-10:]


print(get_last_ten_countries(countries))


# ------------------------------------------------------------------------------------------------------------------


# Exercise Level 3 Solution

# Level 3 Solution

# 3.1

from countries_data import countries_data
from pprint import pprint

sorted_countries_by_name = sorted(countries_data, key=lambda x: x["name"])
pprint(sorted_countries_by_name)

sorted_countries_by_capital = sorted(countries_data, key=lambda x: x["capital"])
pprint(sorted_countries_by_capital)

sorted_countries_by_population = sorted(countries_data, key=lambda x: x["population"])
pprint(sorted_countries_by_population)

from countries_data import countries_data
from pprint import pprint

total_speakers = defaultdict(int)

for country in countries_data:
    for language in country['languages']:
        total_speakers[language] += country['population']

sorted_languages = sorted(total_speakers.items(), key=lambda x: x[1], reverse=True)[:10]

pprint(sorted_languages)


sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

top_ten_countries = sorted_countries[:10]

pprint(top_ten_countries)
