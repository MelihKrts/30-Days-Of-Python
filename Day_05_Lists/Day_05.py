# Lists

# List:  ordered and changeable(modifiable) collection. Allows duplicate members
# Tuple: ordered and unchangeable oor unmodifiable (immutable)
# Set:   unordered, un-indexed and unmodifiable. can add new items to the set
# Dictionary: unordered changeable(modifiable) No duplicate members

# Create List

# Built-in function
lst = list()

# Square brackets []
lst = []

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yoghurt"]
web_techs = ["HTML", "CSS", "JS", "React", "Redux", "Node", "MongoDB"]
countries = ["Finland", "Estonia", "Denmark", "Sweden", "Norway"]

print("Fruits: ", fruits)
print("Number of fruits: ", len(fruits))
print("Vegetables:", vegetables)
print("Number of vegetables:", len(vegetables))
print("Animal products:", animal_products)
print("Number of animal products:", len(animal_products))
print("Web technologies:", web_techs)
print("Number of web technologies:", len(web_techs))
print("Countries:", countries)
print("Number of countries:", len(countries))

# lists can have items of different data types

lst = ["Asabeneh", 250, True, {"country": "Finland", "city": "Helsinki"}]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)

#  last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

# Negative Indexing
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_last)

# Unpacking List Items
lst = ["item1", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries = [
    "Germany",
    "France",
    "Belgium",
    "Sweden",
    "Denmark",
    "Finland",
    "Norway",
    "Iceland",
    "Estonia",
]
gr, fr, bg, sw, *scandic, es = countries

print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing Items List

# fruits = ['banana', 'orange', 'mango', 'lemon']

all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]  # starts first index third index not included
orange_mango_lemon = fruits[1:]  # starts first index
orange_and_lemon = fruits[
    ::2
]  # according to index multiples of the specified number (0,2,4,6) (?)

# print(all_fruits)
# print(all_fruits)
# print(orange_and_mango)
# print(orange_mango_lemon)
# print(orange_and_lemon)

# Negative indexing
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]  # starts third last index not include last first index
orange_mango_lemon = fruits[-3:]  # starts third last index
reverse_fruits = fruits[::-1]  # reverse list = banana = -4 lemon = 1

print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(reverse_fruits)

# Modifying list

# list is a mutable or modifiable ordered collection of items.
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)

fruits[1] = "apple"
print(fruits)

last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)

# Checking Items list
fruits = ["banana", "orange", "mango", "lemon"]

does_exist = "banana" in fruits
print(does_exist)

does_exist = "lime" in fruits
print(does_exist)

# Adding Items List

# end of an existing list we use the method append
lst = list()
print(lst)
lst.append("item")
print(lst)


fruits.append("apple")
print(fruits)
fruits.append("lime")
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]

fruits.insert(0, "melon")
print(fruits)

fruits.insert(2, "Peach")
print(fruits)

# Removing Items List
fruits = ["banana", "orange", "mango", "lemon", "banana"]
fruits.remove("banana")
print(fruits)

# Removing Items Pop List,
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()  # last item if index is not specified
print(fruits)

fruits = ["banana", "orange", "mango", "lemon", "banana"]
fruits.pop(4)
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop(0)
print(fruits)

# Removing Items Using Del
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
del fruits[0]
print(fruits)

del fruits[1]
print(fruits)

del fruits[1:3]
print(fruits)

# Clearing List Items
fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)

# Copying List
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)
fruits_copy.append("melon")
print(fruits_copy)
print(fruits)

# Joining List
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]

integers = negative_numbers + zero + positive_numbers
print(integers)

# Extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numbers: ", num1)

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers: ", negative_numbers)

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]

fruits.extend(vegetables)
print("Fruits and Vegetables: ", fruits)

# Count
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# Finding Index of an Item
print(ages.index(24))

# Reverse List
ages.reverse()
print(ages)

# Sorting List Items
fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)

fruits = ["banana", "orange", "mango", "lemon"]
print(sorted(fruits))

fruits = ["banana", "orange", "mango", "lemon"]
fruits = sorted(fruits, reverse=True)
print(fruits)
