# Day 06 Tuples

# Tuple:
# A tuple is a collection of different data types which is ordered and unchangable (immutable) Once a tuple is created we cannot change its value. We cannot use add, insert, remove methods. Unlike list tuple has few methods.

# tuple(): create empty tuple
# count(): count the number of a specified item in a tuple
# index(): find the index of a specified item in a tuple
# operator(): join two or more tuples and to create a new tuple

# Create Tuple

empty_tuple = ()

# tuple constructor

empty_tuple = tuple()

tpl = ("item1", "item2")
fruits = ("banana", "orange", "mango", "lemon")

# Tuple Length
tpl = ("item1", "item2", "item3")
len(tpl)

# Accesing Tuple Items

tpl = ("item1", "item2", "item3")
first_item = tpl[0]
second_item = tpl[1]

last_index = len(tpl) - 1
last_item = tpl[last_index]
print(last_item)

# Negative index

tpl = ("item1", "item2", "item3", "item4")
first_item = tpl[-4]
print(first_item)

second_item = tpl[-3]
last_item = tpl[-1]
print(last_item)

fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

print(first_fruit)
print(second_fruit)
print(last_fruit)

# Slicing Tuples

tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]  # not include item at index 3
item2_the_rest = tpl[1:]
print(item2_the_rest)

middle_two_items = tpl[-3:-1]
print(middle_two_items)

# Changing Tuples to Lists

fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)

# Checking an Item in a Tuple

print("orange" in fruits)

# Joining Tuples

fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_vegetables = fruits + vegetables

# Deleting Tuples

tpl1 = ("item1", "item2", "item3")
del tpl1
