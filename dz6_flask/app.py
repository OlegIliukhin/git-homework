from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    book_list = [
        "Clean Code",
        "Atomic Habits",
        "The Pragmatic Programmer"
    ]
    return render_template("items.html", items=book_list)


@app.route("/about")
def about():
    return "<h2>Привіт! Це мій перший Flask-проєкт 🚀</h2>"


if __name__ == "__main__":
    app.run(debug=True)