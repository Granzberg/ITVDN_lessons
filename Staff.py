class Employee(object):
    def __init__(self, name, surname, year_hiring):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring

    def __str__(self):
        return "Имя: {}\nФамилия:  {}\nГод поступления на работу:  {}".format(self.name, self.surname, self.year_hiring)


workers = []

how_many_workers = int(input("Скольок работников добавить?: "))
for i in range(how_many_workers):
    try:
        name = input("Имя: ")
        surname = input("Фамилия: ")
        year_hiring = int(input("Год постуления: "))
        e = Employee(name, surname, year_hiring)
        workers.append(e)
        workers.append(workers[0] + workers[i])

    except (ValueError, TypeError) as error:
        print("Error: ", error)


print("*"*30)
for personal in workers:
    print(personal)
    print("*" * 30)



