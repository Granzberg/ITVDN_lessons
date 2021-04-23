class Employee(object):
    def __init__(self, name, surname, year_hiring, staff):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring
        self.staff = staff

    def __str__(self):
        s = "Имя: {}\nФамилия:  {}\nГод поступления на работу:  {}".format(self.name, self.surname, self.year_hiring)
        return s

    def __eq__(self, other):
        return (self.name, self.surname, self.year_hiring) == (other.name, other.surname, other.year_hiring)

    def up_list(self):
        Employee.__str__(self.staff(name, surname, year_hiring))
        return staff


name = "Maxim"
surname = "Shishov"
year_hiring = "2020"
staff = [name, surname, year_hiring]

e = Employee(name, surname, year_hiring, staff)
print(e.up_list())



