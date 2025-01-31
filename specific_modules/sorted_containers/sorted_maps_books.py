from sortedcontainers import SortedDict


class Book:
    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year

    def __eq__(self, other):
        return (self.title, self.publication_year) == (
            other.title,
            other.publication_year,
        )

    def __gt__(self, other):
        return (self.title, self.publication_year) > (
            other.title,
            other.publication_year,
        )

    def __lt__(self, other):
        return (self.title, self.publication_year) < (
            other.title,
            other.publication_year,
        )

    def __hash__(self):
        return (self.title, self.publication_year)


library = SortedDict()
library[2021] = Book("Python 101", 2021)
library[2013] = Book("DDIA", 2013)
library[2024] = Book("Cook Book", 2021)
# TODO: Add another book to the library with the publication year as the key, remember the book's uniqueness comes from its title and year.
# TODO: Iterate through library and print the book title and its publication year.

for year, book in library.items():
    print(f"Publication Year: {year}, Title: {book.title}")
