class Book:

    def __init__(self, title, author, price, rating):
        self.title = title
        self.price = price
        self.rating = rating

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Price: {self.price}")
        print(f"Rating: {self.rating}")
        