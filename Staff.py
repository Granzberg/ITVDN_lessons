class Employee(object):
    def __init__(self, name, surname, year_hiring):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring

    def __str__(self):
        return "Имя: {}\nФамилия:  {}\nГод поступления на работу:  {}".format(self.name, self.surname, self.year_hiring)

     
name = "Maxim"
surname = "Shishov"
year_hiring = "2020"


def up_list():
    staff = []
    while True:
        if staff == list:
            staff.append(e.__str__())
            print(staff)
        else:
            break


e = Employee(name, surname, year_hiring)
up_list()
