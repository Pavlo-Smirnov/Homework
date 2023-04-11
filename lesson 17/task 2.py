class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"{self.__class__.__name__}(name: '{self.name}', country: '{self.country}', birthday: '{self.birthday}')"

    def __str__(self):
        return f"{self.name} ({self.birthday}), from {self.country}"


class Book:
    total_books = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"(name: '{self.name}', year: {self.year}, author: {self.author})"

    def __str__(self):
        return f"'{self.name}' ({self.year}), by {self.author.name}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', books={self.books}, authors={self.authors})"

    def __str__(self):
        return f"{self.name} has {Book.total_books} books in total"


a1 = Author("Stephen King", "USA", "September 21, 1947")
a2 = Author("J.K. Rowling", "UK", "July 31, 1965")
a3 = Author("Agatha Christie", "UK", "September 15, 1890")

library = Library("My Library")


b1 = library.new_book("The Shining", 1977, a1)
b2 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, a2)
b3 = library.new_book("Murder on the Orient Express", 1934, a3)
b4 = library.new_book("It", 1986, a1)

print(library)
print("***" * 10)


stephen_king_books = library.group_by_author(a1)
print("Stephen King's books:", stephen_king_books)
j_k_rowling_books = library.group_by_author(a2)
print("J.K. Rowling's books:", j_k_rowling_books)
agatha_christie_books = library.group_by_author(a3)
print("gatha Christie's books:", agatha_christie_books)

print("***" * 10)

books_of_30s = library.group_by_year(b3.year)
print(f"Murder on the Orient Express was written in {b3.year}")
books_of_70s = library.group_by_year(b1.year)
print(f"The Shining was written in {b1.year}")
books_of_80s = library.group_by_year(b4.year)
print(f"It was written in {b4.year}")
books_of_90s = library.group_by_year(b2.year)
print(f"Harry Potter and the Philosopher's Stone was written in {b2.year}")
