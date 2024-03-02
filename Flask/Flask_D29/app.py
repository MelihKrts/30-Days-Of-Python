from flask import Flask, render_template, url_for, redirect, request
from collections import Counter
from flask_pymongo import PyMongo
import datetime
import re

app = Flask(__name__)


uri = "mongodb://localhost:27017/30DaysOfPython"


app.config["MONGO_URI"] = "mongodb://localhost:27017/30DaysOfPython"
mongo = PyMongo(app, uri=uri)
print(mongo.db)


@app.route("/")
def index():
    name = "30 Days Of Python Programming"
    return render_template("index.html", name=name)


@app.route("/about")
def about():
    name = "30 Days Of Python Programming"
    return render_template("about.html", name=name)


@app.route("/student")
def student():
    name = "30 Days of Python Challenge Participants"
    students = mongo.db.students.find()
    return render_template("student.html", name=name, students=students)


@app.route("/api")
def api():
    return render_template("api.html")


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form.get("name")
        birthyear = request.form.get("birthyear")
        country = request.form.get("country")
        city = request.form.get("city")
        skills = request.form.get("skills").split(",")
        bio = request.form.get("bio")

        student = {
            "name": name,
            "birthyear": birthyear,
            "country": country,
            "city": city,
            "skills": skills,
            "bio": bio,
            "created_at": datetime.datetime.utcnow(),
        }

        mongo.db.students.insert_one(student)

        return redirect(url_for("student"))
    return render_template("join.html")


@app.route("/post", methods=["GET", "POST"])
def post():
    name = "Text Analyzer"
    if request.method == "GET":
        return render_template("post.html", name=name)
    if request.method == "POST":
        content = request.form["content"]

        words = re.findall(r"\w+", content)
        num_words = len(words)
        num_chars = len(content)
        word_freq = Counter(words)
        most_frequent_word = word_freq.most_common(1)[0][0] if word_freq else None

    return render_template(
        "result.html",
        num_words=num_words,
        num_chars=num_chars,
        most_frequent_word=most_frequent_word,
        most_used_words=word_freq.most_common(),
        total_words=num_words,
    )


if __name__ == "__main__":
    app.run(debug=True)
