# Day 27 Python with MongoDB

# Connecting Flask application to MongoDB Cluster

from bson.objectid import ObjectId
from flask import Flask, render_template
import pymongo
import os

MONGODB_URI = "mongodb+srv://melihkaratas1281:yourpassword@30daysofpython.yj12jsx.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGODB_URI)

# Creating a Database and Collection

# Creating Database
db = client.thirty_days_of_python

# Creating students collection and inserting a document
db.students.insert_one(
    ({"name": "Asabeneh", "Country": "Finland", "City": "Helsinki", "age": 250})
)
print(client.list_database_names())

print("----------------------")

# Inserting many documents

students = [
    {"name": "David", "Country": "UK", "city": "London", "age": 34},
    {"name": "John", "Country": "Sweden", "city": "Stockholm", "age": 28},
    {"name": "Sami", "Country": "Finland", "city": "Helsinki", "age": 25},
]

for student in students:
    db.students.insert_one(student)

# MongoDB Find

db = client["thirty_days_of_python"]  # accessing the database
student = db.students.find_one()
print(student)

print("----------------------")

# The above query returns the first entry

# Specific Find Document

student = db.students.find_one({"_id": ObjectId("65d3119afa46c0b9672ffab6")})
print(student)

print("----------------------")

# Find

# find(): returns all the occurence from a collection if we don't pass a query object.

students = db.students.find()
for student in students:
    print(student)

print("----------------------")

# We can specify which fields to return by passing second object in the find({}, {}) 0 means not include and 1 means include

students = db.students.find(
    {}, {"_id": 0, "name": 1, "Country": 1}
)  # 0 means not include and 1 means include
for student in students:
    print(student)

print("----------------------")

# Find with Query

query = {"Country": "Finland"}
students = db.students.find(query)

for student in students:
    print(student)


print("----------------------")

# Query with modifiers

query = {"city": "Helsinki"}
students = db.students.find(query)
for student in students:
    print(student)

print("----------------------")


# Find Query with Modifier

query = {"Country": "Finland", "city": "Helsinki"}
students = db.students.find(query)
for student in students:
    print(student)

print("----------------------")

query = {"age": {"$gt": 30}}
students = db.students.find(query)

for student in students:
    print(student)

print("----------------------")

# Limiting Documents

# We can limit the number of documents we return using the limit() method.
query = db.students.find().limit(3)
for student in query:
    print(student)

print("----------------------")

# Find with Sort

# Ascending Order

students = db.students.find().sort("name")
for student in students:
    print(student)

print("-------------------")

# Descending Order

students = db.students.find().sort("name", -1)
for student in students:
    print(student)

print("-------------------------")


# Ascending Order

students = db.students.find().sort("age")
for student in students:
    print(student)

print("----------------------")

# Descending Order

students = db.students.find().sort("age", -1)
for student in students:
    print(student)

print("----------------------")


# Update with query

query = {"age": 250}
new_value = {"$set": {"age": 38}}

db.students.update_one(query, new_value)
for student in students:
    print(student)

print("----------------------")


# Delete Document

# The method delete_one() deletes one document. The delete_one() takes a query object parameter. It only removes the first occurence.

query = {"name": "John"}
db.students.delete_one(query)
for student in db.students.find():
    print(student)

print("----------------------")

for student in db.students.find():
    print(student)

print("----------------------")

# When we want to delete many documents we use delete_many() method, it takes a query object. If we pass an empty query object to delete_many({}) it will delete all the documents in the collection


# Drop a Collection

# Using the drop method we can delete a collection from a database.

query = db.students.drop()
print(query)

app = Flask(__name__)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
