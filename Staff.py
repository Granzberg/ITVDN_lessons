class Employee(object):
    def __init__(self, name, surname, year_hiring):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring

    def __str__(self):
        return "Имя: {}\nФамилия:  {}\nГод поступления на работу:  {}".format(self.name, self.surname, self.year_hiring)


workers = []
staff00 = []
staff01 = []
staff02 = []
staff03 = []
for i in range(4):
    try:
        name = input("Имя: ")
        surname = input("Фамилия: ")
        year_hiring = int(input("Год постуления: "))
        e = Employee(name, surname, year_hiring)
        if i == 0:
            staff00.append(e)
            workers.append(staff00)
        elif i == 1:
            staff01.append(e)
            workers.append(staff01)
        elif i == 2:
            staff02.append(e)
            workers.append(staff02)
        elif i == 3:
            staff03.append(e)
            workers.append(staff03)

    except ValueError as error:
        print("Error: ", error)


print("*"*30)
for personal in staff00:
    print(personal)
print("*"*30)
for personal in staff01:
    print(personal)
print("*"*30)
for personal in staff02:
    print(personal)
print("*"*30)
for personal in staff03:
    print(personal)



