import csv


def create():
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['First name', 'Last name', 'Date of birth', 'Current city'])
        while True:
            first_name = input('Имя: ')
            last_name = input('Фамилия: ')
            date_of_birth = input('Дата рождения: ')
            current_city = input('Грод проживания: ')
            writer.writerow([first_name, last_name, date_of_birth, current_city])
            choice = input("Добавить еще?(y/n): ")
            if choice == 'n':
                break


def data():
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    date_of_birth = input('Дата рождения: ')
    current_city = input('Грод проживания: ')
    return [first_name, last_name, date_of_birth, current_city]


def additional_recording():
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        while True:
            first_name = input('Имя: ')
            last_name = input('Фамилия: ')
            date_of_birth = input('Дата рождения: ')
            current_city = input('Грод проживания: ')
            writer.writerow([first_name, last_name, date_of_birth, current_city])
            choice = input("Добавить еще?(y/n): ")
            if choice == 'n':
                break


def read_row():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def import_xml():
    export_data = {}
    reader = csv.DictReader(open('data.csv'))
    for row in reader:
        export_data.update(row)


#create()
#additional_recording()
read_row()
import_xml()
