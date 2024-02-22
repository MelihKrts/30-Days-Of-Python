from flask import Flask, Response, jsonify, request
import json, os
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
import pymongo

app = Flask(__name__)

uri = "mongodb+srv://melihkaratas1281:Mx7ZgHdGR0jGIewS@30daysofpython.yj12jsx.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython"

client = pymongo.MongoClient(uri)

db = client["thirty_days_of_python"]

students = [
    {"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "age": 38},
    {"name": "David", "country": "UK", "city": "London", "age": 34},
    {"name": "Sami", "country": "Finland", "city": "Helsinki", "age": 25},
]

# for student in students:
#     db.students.insert_one(student)


@app.route("/api/v1.0/students", methods=["GET"])
def students():
    students = db.students.find({}, {"_id": 0})  # Exclude _id field
    students_list = list(students)
    return jsonify(students_list)


@app.route("/api/v1.0/students/<id>", methods=["GET"])
def single_student(id):
    student = db.students.find_one({"_id": ObjectId(id)}, {"_id": 0})
    return jsonify(student)


@app.route("/api/v1.0/students", methods=["POST"])
def create_student():
    data = request.get_json()
    name = data["name"]
    country = data["country"]
    city = data["city"]
    skills = data["skills"]
    bio = data["bio"]
    birthyear = data["birthyear"]
    created_at = datetime.now()
    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "created_at": created_at,
    }
    db.students.insert_one(student)
    return Response(
        json.dumps({"message": "Student created successfully"}),
        status=201,
        mimetype="application/json",
    )


@app.route("/api/v1.0/students/<id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    name = data["name"]
    country = data["country"]
    city = data["city"]
    skills = data["skills"]
    bio = data["bio"]
    birthyear = data["birthyear"]
    updated_at = datetime.now()
    updated_student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "updated_at": updated_at,
    }
    db.students.update_one({"_id": ObjectId(id)}, {"$set": updated_student})
    return Response(
        json.dumps({"message": "Student updated successfully"}),
        status=200,
        mimetype="application/json",
    )


@app.route("/api/v1.0/students/<id>", methods=["DELETE"])
def delete_student(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(
        json.dumps({"message": "Student deleted successfully"}),
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
