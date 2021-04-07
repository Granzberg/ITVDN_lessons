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
    def __init__(self, first_book_comment, second_book_comment, third_book_comment, fourth_book_comment):
        self.first_book_comment = first_book_comment
        self.second_book_comment = second_book_comment
        self.third_book_comment = third_book_comment
        self.fourth_book_comment = fourth_book_comment

    def comment_book1(self):
        print("Отзыв: {}".format(self.first_book_comment))

    def comment_book2(self):
        print("Отзыв: {}".format(self.second_book_comment))

    def comment_book3(self):
        print("Отзыв: {}".format(self.third_book_comment))

    def comment_book4(self):
        print("Отзыв: {}".format(self.fourth_book_comment))


first_book = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
second_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
third_book = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
fourth_book = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")

first_book_comment = Comment("Не читал и не хочу, назване не нравится.")
second_book_comment = Comment("Странное название для книги.")
third_book_comment = Comment("Книжка хороша, рекомендую.")
fourth_book_comment = Comment("Хорошая книга, рекомендую.")

first_book.shelf()
first_book_comment.comment_book1()
print("**************************")
second_book.shelf()
second_book_comment.comment_book2()
print("**************************")
third_book.shelf()
third_book_comment.comment_book3()
print("**************************")
fourth_book.shelf()
fourth_book_comment.comment_book4()
