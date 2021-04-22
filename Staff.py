class Employee(object):
    def __init__(self, name, surname, year_hiring):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring

    def __str__(self):
        s = "Имя: {}\nФамилия:  {}\nГод поступления на работу:  {}".format(self.name, self.surname, self.year_hiring)
        return s


def employee_list(x):
    staff00 = []
    staff01 = []
    staff02 = []
    staff03 = []
    for i in range(4):
        if i == 0:
            x = staff00
            return x
        elif i == 1:
            x = staff01
            return x
        elif i == 2:
            x = staff02
            return x
        elif i == 3:
            x = staff03
            return x


name = input("Имя: ")
surname = input("Фамилия: ")
year_hiring = input("Год поступления на работу: ")
staff = Employee(name, surname, year_hiring)

print(employee_list(staff))

