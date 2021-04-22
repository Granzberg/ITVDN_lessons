class Employee(object):
    def __init__(self, name, surname, year_hiring, staff=[]):
        self.name = name
        self.surname = surname
        self.year_hiring = year_hiring
        self.staff = staff

    def employee_list(self):
        for i in range(4):
            name = input("Имя: ")
            surname = input("Фамилия: ")
            year_hiring = input("Год поступления на работу: ")
            self.staff = "Имя: {}\nФамилия:  {}\nГод поступления на работу:  {}".format(name, surname, year_hiring)
            if i == 0:
                self.staff = self.staff00
                return self.staff00
            elif i == 1:
                self.staff = self.staff01
                return self.staff01
            elif i == 2:
                self.staff = self.staff02
                return self.staff02
            elif i == 3:
                self.staff = self.staff03
                return self.staff03

    def my_list(self, s00, s01, s02, s03):
        s00 = self.staff00
        s01 = self.staff01
        s02 = self.staff02
        s03 = self.staff03
        print(s00)
        print(s01)
        print(s02)
        print(s03)

    staff00 = []
    staff01 = []
    staff02 = []
    staff03 = []
    

'''    
e = Employee
e.employee_list()


print(Employee.staff00)
print(Employee.staff01)
print(Employee.staff02)
print(Employee.staff03)
'''


