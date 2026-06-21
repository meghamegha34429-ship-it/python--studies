from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search", methods=["POST"])
def search():

    name = request.form["name"]
    movie = request.form["movie"]
    tickets = int(request.form["tickets"])

    if movie.lower() == "leo":
        show_time = "10:00 AM"
    elif movie.lower() == "goat":
        show_time = "2:00 PM"
    elif movie.lower() == "vikram":
        show_time = "6:00 PM"
    else:
        show_time = "9:00 PM"

    price = 150
    total = tickets * price

    return render_template(
        "booking.html",
        name=name,
        movie=movie,
        tickets=tickets,
        show_time=show_time,
        total=total
    )


@app.route("/confirm", methods=["POST"])
def confirm():

    name = request.form["name"]
    movie = request.form["movie"]
    tickets = request.form["tickets"]
    show_time = request.form["show_time"]
    total = request.form["total"]

    return render_template(
        "success.html",
        name=name,
        movie=movie,
        tickets=tickets,
        show_time=show_time,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)
