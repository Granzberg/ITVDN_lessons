import emulator
import data
import shelve

my_array = {}
my_url = input("Ссылка которую нужно сократить: ")
my_new_name = input("Новое имя ссылки: ")

emulator.adding_to_dict(my_new_name, my_url, my_array)

while True:
    new_link_request = input("Хотите добавить еще ссылку?(y/n): ")
    if new_link_request == "y":
        my_url = input("Ссылка которую нужно сократить: ")
        my_new_name = input("Новое имя ссылки: ")
        emulator.adding_to_dict(my_new_name, my_url, my_array)
    elif new_link_request == "n":
        break

data.make_data(my_new_name, my_url)

while True:
    link_request = input("Хотите получить свою ссылку(y/n): ")
    if link_request == "y":
        name = input("Имя: ")
        emulator.get_linc_from_dict(name, my_array)
    elif link_request == "n":
        break

while True:
    ans = input('Показать БД?: ')
    if ans == 'y':
        with shelve.open('data') as db:
            data = dict(db.items())
            print(data)
    elif ans == 'n':
        break
