from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Глобальный список книг (в реальном проекте была бы БД)
books = [
    {"title": "Clean Code", "author": "Robert Martin"},
    {"title": "Python Crash Course", "author": "Eric Matthes"},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books", methods=["GET", "POST"])
def book_list():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")

        if title and author:
            books.append({"title": title, "author": author})

        return redirect(url_for("book_list"))

    return render_template("items.html", books=books)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)