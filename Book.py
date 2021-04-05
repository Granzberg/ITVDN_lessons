class Bookshelf:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def book1(self):
        print(self.author)
        print(self.name)
        print(self.year)
        print(self.genre)


class Shelf:
    def __repr__(self):
        return "Bookshelf({!r}, {!r})".format(self.author, self.name)
    def __str__(self):
        return "{}{:+d}i".format(self.author, self.name)

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
AnotherClass = Bookshelf
print(AnotherClass)
print(Bookshelf == AnotherClass)
print("**************************")
my_object = Shelf(book_standart, other_book)
print(my_object)


