# Day 6 Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1

empty_tuple = ()

# 1.2

sister_sibling = ("Daphne", "Emma")
brother_sibling = ("James", "Leonardo")

# 1.3
sibling = sister_sibling + brother_sibling
print(sibling)

# 1.4
print(len(sibling))

# 1.5
family_members = list(sibling)
family_members.insert(0, "Maria")
family_members.insert(1, "Robert")

print(family_members)

# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 2 Solution

# Level 2 Solution

# 2.1
mother, father, *sibling = family_members

print("Mother Parent:", mother)
print("Father Parent:", father)
print("Siblings:", sibling)

# 2.2
fruits = ("apple", "melon", "tangerine")
vegetables = ("cabbage", "zucchini", "aubergine")
animal_product = ("milk", "honey", "meat")

food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

# 2.3
food_stuff_lt = list(food_stuff_tp)

# 2.4
middle_tuple_item = len(food_stuff_tp) // 2

middle_item = food_stuff_tp[middle_tuple_item - 1 : middle_tuple_item + 1]
print("Middle item(s):", middle_item)

# 2.5
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[-3:]


print("Slice out first three:", first_three_items)
print("Slice out last three:", last_three_items)


# 2.6
del food_stuff_tp

# 2.7
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
