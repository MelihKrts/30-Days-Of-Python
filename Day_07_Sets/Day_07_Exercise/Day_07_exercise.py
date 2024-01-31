# Day 07 Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1

it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print(len(it_companies))

# 1.2
it_companies.add("Twitter")
print(it_companies)

# 1.3
it_companies.update(["SAP", "Kaspersky", "Norton", "Intel", "TSMC"])
print(it_companies)

# 1.4
it_companies.remove("Norton")
print(it_companies)

# 1.5
# remove() : remove method removes one value from the set. Keep is mind that if the specified value is not present in the set, a KeyError will be raised.
# discard(): If there is no value to remove in the set, the discard method will not return an error


# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 2 Solution

# Level 2 Solution

# 2.1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C)

# 2.2
common_element = A.intersection(B)
print(common_element)

# 2.3
is_subset = A.issubset(B)
print("Is A subset of B:", is_subset)

# 2.4
is_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", is_disjoint)

# 2.5
C1 = A.union(B)
print("A union B:", C1)

C2 = B.union(A)
print("B union A:", C2)

# 2.6
symmetric_difference = A.symmetric_difference(B)
print("Symmetric Difference between A and B:", symmetric_difference)

# 2.7
del A
del B
del it_companies

# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 3 Solution

# Level 3 Solution

# 3.1
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("List is age length:", len(age))

age = set(age)
print(type(age))
print("Set is age length:", len(age))

# Set age is bigger than list age

# 3.2

# string: String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation Python strings are "immutable" which means they cannot be changed after thay are created.
# list: ordered and changeable(modifiable) collection.
# tuple: ordered and unchangeable or unmodifiable (inmutable)
# set: unordered, un-indexed and unmodifiable

# 3.3
unique_words = "I am a teacher and I love to inspire and teach people."
unique_words_split = unique_words.split()

unique_words_set = set(unique_words_split)
print(unique_words_set)
