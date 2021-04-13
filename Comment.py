class Bookshelf:
    def __init__(self, author, name_book, year_book, genre_book, comments=[]):
        self.author = author
        self.name_book = name_book
        self.year_book = year_book
        self.genre_book = genre_book
        self.comments = comments

    def __str__(self):
        s = "Автор:       {}\nНазвание:    {}\nГод выпуска: {}\nЖанр:        {}"\
            .format(self.author, self.name_book, self.year_book, self.genre_book)
        return s + "\n{}".format(self.comments)


class Comment:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Коментарии:  {}".format(self.text)


first_book = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
second_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
third_book = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
fourth_book = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")


first_book.comments = Comment("Не читал и не хочу, назване не нравится.")
second_book.comments = Comment("Странное название для книги.")
third_book.comments = Comment("Книжка хороша, рекомендую.")
fourth_book.comments = Comment("Хорошая книга, рекомендую.")


print(first_book.__str__())
print("**************************")
print(second_book.__str__())
print("**************************")
print(third_book.__str__())
print("**************************")
print(fourth_book.__str__())
