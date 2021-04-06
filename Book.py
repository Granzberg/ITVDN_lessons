class Bookshelf:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        return (self.author, self.name) == (other.author, other.name)

    def __repr__(self):
        return "({!r}, {!r})".format(self.author, self.name)

    def __str__(self):
        return "{!r}, {!r}".format(self.author, self.name)

    def book1(self):
        print(self.author)
        print(self.name)
        print(self.year)
        print(self.genre)


book_standart = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
other_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
other_book2 = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
other_book3 = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")
book_standart.book1()
print("**************************")

other_book.book1()
print("**************************")

other_book2.book1()
print("**************************")

other_book3.book1()
print("**************************")

print(Bookshelf.__eq__(other_book, other_book2))
print(Bookshelf.__str__(book_standart))
print(Bookshelf.__repr__(other_book))


