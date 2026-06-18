class MovieBooking:

    def book_ticket(self, name, movie, tickets):

        if movie.lower() == "leo":
            price = 200
        elif movie.lower() == "jailer":
            price = 180
        else:
            price = 150

        total = tickets * price

        return {
            "name": name,
            "movie": movie,
            "tickets": tickets,
            "price": price,
            "total": total
        }
