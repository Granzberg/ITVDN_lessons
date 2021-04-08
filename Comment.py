class Bookshelf:
    def __init__(self, author, name_book, year_book, genre_book):
        self.author = author
        self.name_book = name_book
        self.year_book = year_book
        self.genre_book = genre_book

    def shelf(self):
        print("Автор:       {}".format(self.author))
        print("Название:    {}".format(self.name_book))
        print("Год выпуска: {}".format(self.year_book))
        print("Жанр:        {}".format(self.genre_book))


class Comment:
    def print_info(self):
        print(first_book.shelf(), "Коментарии: {}".format(self.f_comment))


first_book = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
second_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
third_book = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
fourth_book = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")

first_book_comment = Comment()
first_book_comment.f_comment = "Не читал и не хочу, назване не нравится."

'''second_book_comment.comment = ("Странное название для книги.")
third_book_comment = ("Книжка хороша, рекомендую.")
fourth_book_comment = ("Хорошая книга, рекомендую.")'''

#first_book.shelf()
first_book_comment.print_info()
print("**************************")
'''second_book.shelf()
second_book_comment.
print("**************************")
third_book.shelf()
third_book_comment.comment_book3()
print("**************************")
fourth_book.shelf()
fourth_book_comment.comment_book4()'''
