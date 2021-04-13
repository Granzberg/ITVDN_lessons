class Bookshelf:
    def __init__(self, author, name_book, year_book, genre_book):
        self.author = author
        self.name_book = name_book
        self.year_book = year_book
        self.genre_book = genre_book
        self.comments = []

# заменить на метод str ????
    def __str__(self):
        s = "Автор:       {}\nНазвание:    {}\nГод выпуска: {}\nЖанр:        {}"
        return s.format(self.author, self.name_book, self.year_book, self.genre_book)


class Comment:
    def __init__(self, comments):
        self.comments = comments

# заменить на метод str????
    def add_list(self):
        first_list_comments = [first_book.comments]
        second_list_comments = [second_book.comments]
        third_list_comments = [third_book.comments]
        fourth_list_comments = [fourth_book.comments]
        return first_list_comments, second_list_comments, third_list_comments, fourth_list_comments

# заменить на метод str ????
    def __str__(self):
        g = "{}\nКоментарии:  {}"
        return g.format(first_book.__str__(), Comment.add_list(self))


first_book = Bookshelf("Maximilian Maxim", "Maximilian's Adventure", 1999, "adventure")
second_book = Bookshelf("some author", "some name of book", 2000, "sci-fi")
third_book = Bookshelf("Emili Bronte", "Wuthering Heights", 1998, "Novel")
fourth_book = Bookshelf("Erikh Mariya Remark", "Triumphal Arch. Borrowed life", 1988, "Novel")


first_book.comments = Comment("Не читал и не хочу, назване не нравится.")
second_book.comments = Comment("Странное название для книги.")
third_book.comments = Comment("Книжка хороша, рекомендую.")
fourth_book.comments = Comment("Хорошая книга, рекомендую.")


#print(first_book.__str__())
print(Comment.__str__(first_book.comments))
print("**************************")
#print(second_book.__str__())
#print(Comment.adding_comments())
print("**************************")
#print(third_book.__str__())
#print(Comment.adding_comments(third_book_comment))
print("**************************")
#print(fourth_book.__str__())
#print(Comment.adding_comments(fourth_book_comment))
