class Employee(object):
    def __init__(self, name, surname, year_hiring, staff=[]):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring
        self.staff = staff

    def __str__(self):
        self.staff = "Имя: {}\nФамилия: {}\nГод поступления на работу: {}"\
            .format(self.name, self.surname, self.year_hiring)
        print(self.staff)


try:
    Employee.name = input("Имя: ")
    Employee.surname = input("Фамилия: ")
    Employee.year_hiring = input("Год поступления на работу: ")
    Employee.__str__()
except TypeError as error:
    print("Ошибка: ", error)

