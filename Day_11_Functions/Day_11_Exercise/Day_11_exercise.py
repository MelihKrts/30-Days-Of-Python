# Day 11 Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1


def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


print(add_two_numbers(9, 35))

# 1.2

import math  # PI number


def area_of_circle(r):
    pi = math.pi
    area = pi * r**2
    return area


print(area_of_circle(10))

# 1.3


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, int):
            print("The value you entered is not a number")
        else:
            total += num
    return total


print(add_all_nums(2, 3, 5))
print(add_all_nums("abc"))

# 1.4


def convert_celcius_to_fahrenheit(c):
    formula = (c * 9 / 5) + 32
    return formula


print("Fahrenheit degree", convert_celcius_to_fahrenheit(12.5))

# 1.5


def check_season(month):
    if month in ("december", "january", "february"):
        return "Winter"
    elif month in ("march", "april", "may"):
        return "Spring"
    elif month in ("june", "july", "august"):
        return "Summer"
    elif month in ("september", "october", "november"):
        return "Autumn"
    else:
        return "Invalid month"


print(check_season("april"))

# 1.6


def calculate_slop(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return m


print("The slope is", calculate_slop(4, 2, 5, 4))

# 1.7
import cmath


def solve_quadratic_eqn(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4 * a * c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)

    return root1, root2


roots = solve_quadratic_eqn(1, -3, 2)
print("Roots:", roots)


# 1.8
def print_list(my_list):
    for i in my_list:
        print(i)


my_list = [1, 2, 3, 4, 5]
print_list(my_list)

# 1.9


def reverse_list(lst):
    reversed_lst = []
    for value in lst:
        reversed_lst = [value] + reversed_lst
    return reversed_lst


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# 1.10


def capitialize_list_items(lst):
    capitialize_list = [item.capitalize() for item in lst]
    return capitialize_list


original_list = ["apple", "banana", "cherry"]
result = capitialize_list_items(original_list)
print(result)


# 1.11
def add_item(my_list, item):
    updated_list = my_list + [item]
    return updated_list


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
food_staff = add_item(food_staff, "Meat")
print(food_staff)


# 1.12
def remove_item(my_list, item):
    updated_list = [value for value in my_list if value != item]
    return updated_list


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
food_staff = remove_item(food_staff, "Mango")
print(food_staff)


# 1.13
def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total


print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# 1.14


def sum_of_odds(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 1:
            total += i
    return total


print(sum_of_odds(100))


# 1.15
def sum_of_even(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return total


print(sum_of_even(100))


# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 2 Solution

# Level 2 Solution


# 2.1
def evens_and_odds(n):
    evens = sum(1 for i in range(1, n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(1, n + 1) if i % 2 != 0)

    return f"The number of odds are {odds}.\nThe number of evens are {evens + 1}."


# Example usage
print(evens_and_odds(100))

# 2.2


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result_recursive = factorial(5)
print(result_recursive)


# 2.3
def is_empty(value=None):
    if value is None or not value:
        print("The value is empty.")
    return value


result = is_empty("example")
result2 = is_empty()
print(result)
print(result2)


# 2.4
def calculate_mean(*nums):
    total = int(sum(nums) / len(nums))
    return total


print(calculate_mean(1, 2, 3, 4, 5, 6, 7, 8, 9))


def calculate_median(*nums):
    sorted_nums = sorted(nums)
    length = len(nums)
    if length % 2 == 0:
        middle1 = sorted_nums[length // 2 - 1]
        middle2 = sorted_nums[length // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_nums[length // 2]

    return median


result = calculate_median(4, 2, 7, 1, 5)
print("Median:", result)


def calculate_mode(*nums):
    num_counts = {}

    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    max_count = max(num_counts.values())
    mode = [num for num, count in num_counts.items() if count == max_count]

    return mode


# Example usage
result = calculate_mode(4, 2, 7, 1, 5, 4, 7, 4)
print("Mode:", result)


def calculate_range(*nums):
    range = max(nums) - min(nums)
    return range


print(calculate_range(15, 12, 3, 70))


def calculate_variance(*nums):
    n = len(nums)

    mean = sum(nums) / n

    squared_diff = [(num - mean) ** 2 for num in nums]

    variance = sum(squared_diff) / n

    return variance


result = calculate_variance(15, 12, 3, 70)
print("Variance:", result)


def calculate_std(*nums):
    n = len(nums)

    mean = sum(nums) / n

    squared_diff = [(num - mean) ** 2 for num in nums]

    variance = sum(squared_diff) / n

    std_deviation = math.sqrt(variance)

    return std_deviation


result = calculate_std(15, 12, 3, 70)
print("Standard Deviation:", result)


# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 3 Solution

# Level 3 Solution


# 3.1
def is_prime(num):
    if num < 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If the number is divisible by any value in the range, it's not prime

    return True


result1 = is_prime(7)
result2 = is_prime(15)

print("Is 7 prime?", result1)
print("Is 15 prime?", result2)

# 3.2


def unique(lst):
    sean = set()
    for item in lst:
        if item in sean:
            return False
        sean.add(item)
    return True


result1 = unique([1, 2, 3, 4, 5])
result2 = unique([1, 2, 3, 4, 1])

print(result1)
print(result2)


# 3.3
def are_all_same_type(lst):
    if not lst:
        return True

    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)


# Example usage
result1 = are_all_same_type([1, 2, 3, 4, 5])
result2 = are_all_same_type(["apple", "banana", "orange"])
result3 = are_all_same_type([1, "apple", 3.14])

print("Are all items of the first list of the same data type?", result1)
print("Are all items of the second list of the same data type?", result2)
print("Are all items of the third list of the same data type?", result3)


# 3.4


def is_valid_variable(variable):
    try:
        exec(f"{variable} = None")
        del locals()[variable]
        return True
    except Exception:
        return False


# Example usage
result1 = is_valid_variable("valid_variable")
result2 = is_valid_variable("123invalid_variable")
result3 = is_valid_variable("my_variable")

print("Is 'valid_variable' a valid Python variable?", result1)
print("Is '123invalid_variable' a valid Python variable?", result2)
print("Is 'my_variable' a valid Python variable?", result3)


# 3.5
import countries_data
from collections import Counter


def most_spoken_languages(data, top_n=10):
    all_languages = [language for country in data for language in country["languages"]]
    language_counts = Counter(all_languages)

    top_languages = language_counts.most_common(top_n)

    return top_languages


from countries_data import countries_data

result = most_spoken_languages(countries_data, top_n=10)
print("Top 10 Most Spoken Languages:", result)


# 3.5.1
from pprint import pprint


def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x["population"], reverse=True)

    # Get the top N most populated countries
    top_countries = sorted_countries[:top_n]

    return top_countries


from countries_data import countries_data

result = most_populated_countries(countries_data, top_n=10)
print("Top 10 Most Populated Countries:")
pprint(result)
