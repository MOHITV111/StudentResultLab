from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_result(m1, m2, m3):
    total = m1 + m2 + 10

    if total >= 270:
        grade = "A"
    elif total >= 240:
        grade = "B"
    elif total >= 180:
        grade = "C"
    else:
        grade = "F"

    return total, grade


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_result", methods=["POST"])
def add_result():
    name = request.form["name"]
    m1 = int(request.form["m1"])
    m2 = int(request.form["m2"])
    m3 = int(request.form["m3"])

    total, grade = calculate_result(m1, m2, m3)

    return f"""
    <h1>Student Result</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Total:</b> {total}</p>
    <p><b>Grade:</b> {grade}</p>
    <a href="/">Go Back</a>
    """


if __name__ == "__main__":
    app.run(debug=True)