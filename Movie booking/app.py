from flask import Flask, render_template, request
from movie import MovieBooking

app = Flask(__name__)

booking = MovieBooking()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/book")
def book():

    name = request.args.get("name")
    movie = request.args.get("movie")
    tickets = int(request.args.get("tickets"))

    data = booking.book_ticket(name, movie, tickets)

    return render_template("result.html", data=data)

app.run(debug=True)
