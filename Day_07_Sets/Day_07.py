# Sets:
# Set is a collection of items.

# Creating a Set

# st = set()

st = {"item1", "item2", "item3", "item4"}
fruits = {"banana", "orange", "mango", "lemon"}

# Set's Length

len(fruits)

# Checking an Item

st = {"item1", "item2", "item3", "item4"}
print("Does set st contain item3? ", "item3" in st)

# Adding Items to a Set

st.add("item5")

# Add Multiple items update()
# The update() takes a list argument

st = {"item1", "item2", "item3", "item4"}
st.update(["item5", "item6", "item7"])
print(st)

fruits = {"banana", "orange", "mango", "lemon"}
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
fruits.update(vegetables)
print(fruits)

# Removing Items From a Set
st = {"item1", "item2", "item3", "item4"}
st.remove("item2")

# pop methods()

fruits.pop()
print(fruits)

# Clearing Items in a Set
st.clear()

# Deleting Items in a Set
del st

# Converting List to Set
lst = ["item1", "item2", "item3"]
st = set(lst)

# Joining Set
# We can join two sets using the union() or update method
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
print(fruits.union(vegetables))

# Update method join()

st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item5", "item6", "item7", "item8"}
st1.update(st2)
print(st1)

# Finding Intersection Items

# hint: A ∩ B (Common element in set A and set B)
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3", "item4"}
common_element = st1.intersection(st2)
print(common_element)

# Intersection update
# method removes the items that is not present in both sets(or in all sets if the comparison is done between more than two sets)
x = {"item1", "item2", "item3"}
y = {"item1", "item4", "item5"}

x.intersection_update(y)

print(x)

# Checking Subset and SuperSet
# A set can be a subset or super set of other sets:

# Subset: issubset()
# super set : issuperset

st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}

is_subset = st1.issubset(st1)
is_superset = st1.issuperset(st2)
print(is_subset)
print(is_superset)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)
whole_numbers.issuperset(even_numbers)

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.issubset(dragon))

# Checking the Difference Between two sets
# It returns the difference between two set

# hint A/B,  B/A A is different from B
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item3", "item4"}
diffrence_st2 = st2.difference(st1)
difference_st1 = st1.difference(st2)
print(diffrence_st2)
print(difference_st1)

# Finding Symmetric Difference Between Two Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.symmetric_difference(st1))

# Joining Sets