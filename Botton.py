class Figure(object):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        print("Фигура")


class Rectangle(Figure):
    def __init__(self, side02):
        self.side02 = side02

    def __str__(self):
        print("Прямоугольник(side, side02)")


class Mouse:
    def __init__(self, click):
        self.click = click

    def __str__(self):
        print("Нажатие на кнопку(click)")


Mouse.__str__(print())
Rectangle.__str__(print())


