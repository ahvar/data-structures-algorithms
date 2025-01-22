from sortedcontainers import SortedDict


class Book:
    def __init__(self, author, title):
        self._title = title
        self._author = author

    def __lt__(self, other):
        return self._author < other.author

    def __gt__(self, other):
        return self._author > other.author

    def __eq__(self, other):
        return self._author == other.author

    def __hash__(self):
        return hash((self._title, self.author))

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author


# TODO: Define the Book class with a constructor for 'author' and 'title', and implement the logic to sort books by the author's name.

# Initialize the sorted map with books sorted by author's name
library = SortedDict(
    {Book("Orwell", "1984"): 1000, Book("Huxley", "Brave New World"): 2000}
)
dsa = Book("Author Name", "DSA")
ddia = Book("Ham Bone", "DDIA")
library[dsa] = 3000
library[ddia] = 4000

# TODO: Add at least two Book instances to 'library' with different authors and titles. Each book should be mapped to its price (integer).

# TODO: Write a loop to print all books in 'library', displaying each book's title and author.
for book, price in library.items():
    print("Title: {}, Author: {}".format(book.title, book.author))
