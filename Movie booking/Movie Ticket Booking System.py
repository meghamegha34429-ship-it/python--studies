from flask import Flask, request

app = Flask(__name__)

class MovieBooking:

    def book_ticket(self, name, movie, tickets):

        price = 150
        total = tickets * price

        return f"""
        <h1>Movie Ticket Booking System</h1>

        <h3>Customer Details</h3>

        Name : {name}<br>
        Movie Name : {movie}<br>
        Number of Tickets : {tickets}<br><br>

        <h3>Booking Details</h3>

        Ticket Price : ₹{price}<br>
        Total Amount : ₹{total}<br><br>

        <h3>Booking Confirmed Successfully</h3>
        """

booking = MovieBooking()

@app.route("/")
def home():

    return """
    <h1>Movie Ticket Booking System</h1>

    <form action="/book">

        Customer Name:
        <input type="text" name="name"><br><br>

        Movie Name:
        <input type="text" name="movie"><br><br>

        Number of Tickets:
        <input type="number" name="tickets"><br><br>

        <input type="submit" value="Book Ticket">

    </form>
    """

@app.route("/book")
def book():

    name = request.args.get("name")
    movie = request.args.get("movie")
    tickets = int(request.args.get("tickets"))

    return booking.book_ticket(
        name,
        movie,
        tickets
    )

app.run(debug=True)
