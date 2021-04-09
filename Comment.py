class Bookshelf:
    def __init__(self, author, name_book, year_book, genre_book):
        self.author = author
        self.name_book = name_book
        self.year_book = year_book
        self.genre_book = genre_book

    def shelf(self):
        return "Автор:       {}\nНазвание:    {}\nГод выпуска: {}" \
               "\nЖанр:        {}".format(self.author, self.name_book, self.year_book, self.genre_book)


class Comment:
    def __init__(self, first_book_comment, list1):
        self.first_book_comment = first_book_comment
    list1 = []

    def __add__(self, other):
        return first_book.shelf(), "\nКоментарии: {}".format(other.list1)


    #def print_list(self):
        #list1.
        #return


first_book = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
second_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
third_book = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
fourth_book = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")


first_book_comment = Comment("Не читал и не хочу, назване не нравится.")

'''second_book_comment.comment = ("Странное название для книги.")
third_book_comment = ("Книжка хороша, рекомендую.")
fourth_book_comment = ("Хорошая книга, рекомендую.")'''


print(first_book.shelf())
print(Comment.__add__())
print("**************************")
print(second_book.shelf())
#second_book_comment.
print("**************************")
print(third_book.shelf())
#third_book_comment.comment_book3()
print("**************************")
print(fourth_book.shelf())
#fourth_book_comment.comment_book4()
