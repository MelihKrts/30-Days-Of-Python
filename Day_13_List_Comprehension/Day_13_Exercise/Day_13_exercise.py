# Day 13 List Comprehension Exercise Solution

# Exercise Solution

# Exercise 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_and_negative = [number for number in numbers if number <= 0]
print(zero_and_negative)


# Exercise 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattaned_list = [
    number for sublist in list_of_lists for row in sublist for number in row
]
print(flattaned_list)


# Exercise 3
numbers = [(i, 1, i**2, i**3, i**4, i**5) for i in range(11)]
for number in numbers:
    print(number)


# Exercise 4
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
flattaned_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for sublist in countries
    for country, city in sublist
]
print(flattaned_countries)


# Exercise 5
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
flattaned_dic = [
    {"country": country.upper(), "city": city.upper()}
    for sublist in countries
    for country, city in sublist
]
print(flattaned_dic)


# Exercise 6
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
flattaned_name = [" ".join(name) for sub_name in names for name in sub_name]
print(flattaned_name)

# Exercise 7

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda slope, x, y: y - slope * x
print(slope(1, 2, 3, 4))
print(y_intercept(1, 2, 3))
