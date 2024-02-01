# Dictionaries:
# A dictionary is a collection of unordered, modifiable(mutuable) paired (key:value) data type

# Creating Dictionary
empty_dict = {}
dct = {"key:1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],  # list
    "address": {"street": "Space street", "zipcode": "02210"},  # dict
}

# print(type(person["address"]))
print(len(person))

# The dictionary above shows that a value could be any data types:string,boolean,list,tuple,set or a dictionary

# Dictionary Length
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(len(dct))

# Accessing Dictionary Items
print(dct["key1"])
print(person["first_name"])
print(person["country"])
print(person["skills"])
print(person["skills"][0])
print(person["address"]["street"])
# print(person["city"]) error

# Adding Items to a Dictionary
dct["key5"] = "value5"
person["job_title"] = "Instructor"
person["skills"].append("HTML")
print(person)

# Modifying Items in a Dictionary
person["first_name"] = "Eyob"
person["age"] = 252

# Checking Keys in a Dictionary
print("key2" in dct)
print("key5" in dct)

# Removing Key and Value Pairs from a Dictionary

# pop(key):     removes the item with the specified key name:
# popitem():    removes the last item
# del:          removes an item with specified key name

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.pop("key1")
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.popitem()
del dct["key2"]

person.pop("first_name")
person.popitem()
del person["is_married"]
print(person)

# Changing Dictionary to a List of Items

# items() method changes dictionary to a list tuple
print(dct.items())

# Clearing a Dictionary
print(dct.clear())

# Deleting a Dictionary
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
del dct

# Copy a Dictionary
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct_copy = dct.copy()

# Getting Dictionary Keys an a List

# the keys() method gives us all the keys of a dictionary list
print(dct.keys())

# Getting Dictionary Value as a List

# the values() methods gives us all the value of a dictionary list
print(dct.values())