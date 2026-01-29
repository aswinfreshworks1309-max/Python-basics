class MovieTicket:
    def __init__(self):
        # Store all movies in a dictionary
        self.movies = {}

    def add(self, title, price, tickets):
        # Add a new movie
        self.movies[title] = {"price": price, "available_tickets": tickets}
        print(f"Added movie '{title}' with {tickets} tickets at ₹{price} each.")

    def book_tickets(self, title, count):
        # Book tickets if available
        if title in self.movies:
            if self.movies[title]["available_tickets"] >= count:
                self.movies[title]["available_tickets"] -= count
                print(f"{count} tickets booked for '{title}'.")
            else:
                print("Not enough tickets available.")
        else:
            print("Movie not found.")

    def cancel(self, title, count):
        # Cancel tickets
        if title in self.movies:
            self.movies[title]["available_tickets"] += count
            print(f"{count} tickets cancelled for '{title}'.")
        else:
            print("Movie not found.")

    def availability(self, title):
        # Show availability
        if title in self.movies:
            print(f"Available tickets for '{title}': {self.movies[title]['available_tickets']}")
        else:
            print("Movie not found.")


# Example usage:
ticket_system = MovieTicket()
ticket_system.add("Vanamagan", 200, 10)
ticket_system.add("Dragon", 400, 20)
ticket_system.book_tickets("Vanamagan", 2)
ticket_system.book_tickets("Dragon", 1)
ticket_system.availability("Vanamagan")
ticket_system.cancel("Vanamagan", 1)
ticket_system.availability("Vanamagan")
