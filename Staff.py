class Employee(object):
    def __init__(self, name, surname, year_hiring):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring

    def __str__(self):
        return "Имя: {}\nФамилия:  {}\nГод поступления на работу:  {}".format(self.name, self.surname, self.year_hiring)


worker = []
staff = []

while True:
    try:
        b = input("Добавить ещё одного работника(y/n): ")

        if b == "y":
            name = input("Имя: ")
            surname = input("Фамилия: ")
            year_hiring = input("Год постуления: ")
            e = Employee(name, surname, year_hiring)
            worker.append(e)
            staff.append(worker)
        else:
            break

    except ValueError as error:
        print("Error: ", error)

print(staff)
