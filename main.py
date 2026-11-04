from flask import Flask, render_template, request, redirect
from database import Database

app = Flask(__name__)
db = Database()


@app.get("/")
def index():
    with db:
        birthdays = db.list_birthdays()

    return render_template("index.html", birthday_list=birthdays, error="")


@app.post("/birthday")
def birthday_form():
    form = request.form
    name, month, day = form.get("username"), form.get("month"), form.get("day")

    if not all((name, month, day)):
        return render_template("index.html", birthday_list=[], error="введите все поля")

    with db:
        db.add_birthday(name, month, day)

    return redirect("/")


app.run(debug=True)
