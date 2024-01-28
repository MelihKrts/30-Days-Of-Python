# Day 5 Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1
empty_list = []

# 1.2
items_list = ["Ankara", "Istanbul", "Izmir", "Bursa", "Edirne"]

# 1.3
print(len(items_list))

# 1.4
first_item = items_list[0]
print(first_item)

middle_item = items_list[len(items_list) // 2]
print(middle_item)

last_item = len(items_list) - 1
last_index = items_list[last_item]
print(last_index)

# 1.5
isBachelor = True
mixed_data_types = ["Melih", 23, 1.91, isBachelor, "Turkey"]

# 1.6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 1.7
print(it_companies)

# 1.8
print(len(it_companies))

# 1.9
first_compaines = it_companies[0]
print(first_compaines)

middle_compaines = len(it_companies) // 2
print(it_companies[middle_compaines])

last_compaines = it_companies[-1]
print(last_compaines)

# 1.10
it_companies[0] = "Accenture"
print(it_companies)

# 1.11
it_companies.append("Intel")
print(it_companies)

# 1.12

# find index
middle_index = len(it_companies) // 2


it_companies.insert(middle_index, "Cisco")
print(it_companies)

# 1.13
it_companies[6] = it_companies[6].upper()
print(it_companies)

# 1.14
print("#; ".join(it_companies))

# 1.15
is_checked = "Amazon" in it_companies
print(is_checked)

# 1.16
it_companies.sort()
print(it_companies)

# 1.17
it_companies.sort(reverse=True)
print(it_companies)

# 1.18
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
slice_first = it_companies[0:3]
print(slice_first)

# 1.19
slice_last = it_companies[-3:]
print(slice_last)

# 1.20

it_companies = (
    it_companies[0 : len(it_companies) // 2]
    + it_companies[len(it_companies) // 2 + 1 :]
)
print(it_companies)

# 1.21
it_companies.pop(0)

# 1.22
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
remove_middle = len(it_companies) // 2
it_companies.pop(remove_middle)
print(it_companies)

# 1.23
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[-1]
print(it_companies)

# 1.24
it_companies.clear()
print(it_companies)

# 1.25
del it_companies

# 1.26
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)

# ------------------------------------------------------------------------------------------------------------------

# Day 5 Exercise Level 2 Solution

# Level 2 Solution

# 2.1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 2.1.1
ages.sort()
print("Min age:", min(ages), "\nMax age:", max(ages))

# 2.1.2
min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)
ages.sort()

print(ages)

# 2.1.3
median_age = (ages[len(ages) // 2] + ages[~(len(ages) // 2)]) / 2
print("Median age:", int(median_age))

# 2.1.4
average = sum(ages) / len(ages)
print("Average:", average)

# 2.1.5
range = max_age - min_age
print("Range:", range)

# 2.1.6
min_diff = abs(min(ages) - average)
max_diff = abs(max(ages) - average)
print("Min diff:", min_diff, "\nMax diff:", max_diff)

# 2.2
import countries


find_middle_countries = len(countries.countries) // 2


print("Middle Country:", countries.countries[find_middle_countries])

# 2.2.1
from pprint import pprint

middle_index = len(countries.countries) // 2


if len(countries.countries) % 2 == 1:
    first_half = countries.countries[: middle_index + 1]
    second_half = countries.countries[middle_index + 1 :]
else:
    first_half = countries.countries[:middle_index]
    second_half = countries.countries[middle_index:]


print("First Half:")
pprint(first_half, width=1)
print("\nSecond Half:")
pprint(second_half, width=1)

# 2.3
country = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
first_country, second_country, third_country, *scandic = country

print("First Country:", first_country)
print("Second Country:", second_country)
print("Third Country:", third_country)
print("Scandic Country:", scandic)
