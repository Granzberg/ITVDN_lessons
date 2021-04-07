class Bookshelf:
    def __init__(self, author, name_book, year_book, genre_book):
        self.author = author
        self.name_book = name_book
        self.year_book = year_book
        self.genre_book = genre_book

    def shelf(self):
        print(self.author)
        print(self.name_book)
        print(self.year_book)
        print(self.genre_book)


class Comment:
    def __init__(self, book_comment):
        self.book_comment = book_comment

    def comment_book(self):
        print("Отзыв: {}".format(self.book_comment))


first_book = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
second_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
third_book = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
fourth_book = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")

comment = Comment("Хорошая книга, рекомендую.")

fourth_book.shelf()
print("**************************")
second_book.shelf()
print("**************************")
third_book.shelf()
print("**************************")
fourth_book.shelf()
comment.comment_book()
