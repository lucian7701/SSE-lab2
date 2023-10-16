from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    year_born = 2023 - int(input_age)
    return render_template("hello.html", name=input_name, age=input_age, year_born=year_born)
