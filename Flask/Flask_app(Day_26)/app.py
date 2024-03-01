from flask import Flask, render_template, url_for, request, redirect
from collections import Counter
from serverless_wsgi import handle_request
import re

app = Flask(__name__)


@app.route("/")
def index():
    name = "30 Days of Python Programming"
    techs = ["HTML", "CSS", "Flask", "Python"]
    return render_template("index.html", name=name, techs=techs)


@app.route("/about")
def about():
    name = "30 Days of Python Programming"
    return render_template("about.html", name=name)


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
        word_variety = len(word_freq) / num_words * 100 if num_words > 0 else 0

        return render_template(
            "result.html",
            num_words=num_words,
            num_chars=num_chars,
            most_frequent_word=most_frequent_word,
            word_variety=word_variety,
            most_used_words=word_freq.most_common(),
            total_words=num_words,
        )


if __name__ == "__main__":
    app.run(debug=True)
