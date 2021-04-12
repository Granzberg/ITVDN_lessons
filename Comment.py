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
    first_book_comment = "Не читал и не хочу, назване не нравится."
    second_book_comment = "Странное название для книги."
    third_book_comment = "Книжка хороша, рекомендую."
    fourth_book_comment = "Хорошая книга, рекомендую."

    def __init__(self, first_book_comment, second_book_comment, third_book_comment, fourth_book_comment):
        #self.list_comments = list_comments
        self.first_book_comment = first_book_comment
        self.second_book_comment = second_book_comment
        self.third_book_comment = third_book_comment
        self.fourth_book_comment = fourth_book_comment
        #self.list1 = []

    #def print_list(self):
     #   return list.append()

    def add_list(self):
        first_list_comments = [self.first_book_comment]
        second_list_comments = [self.second_book_comment]
        third_list_comments = [self.third_book_comment]
        fourth_list_comments = [self.fourth_book_comment]
        return first_list_comments, second_list_comments, third_list_comments, fourth_list_comments

    def adding_comments(self):
        return "{}\nКоментарии:  {}".format(first_book.shelf(), Comment.add_list(self))


first_book = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
second_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
third_book = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
fourth_book = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")


#first_book_comment = Comment("Не читал и не хочу, назване не нравится.")
#second_book_comment = Comment("Странное название для книги.")
#third_book_comment = Comment("Книжка хороша, рекомендую.")
#fourth_book_comment = Comment("Хорошая книга, рекомендую.")


#print(first_book.shelf())
print(Comment.adding_comments())
print("**************************")
#print(second_book.shelf())
#print(Comment.adding_comments())
print("**************************")
#print(third_book.shelf())
#print(Comment.adding_comments(third_book_comment))
print("**************************")
#print(fourth_book.shelf())
#print(Comment.adding_comments(fourth_book_comment))
