import emulator


#my_url = input("Ссылка которую нужно сократить: ")
#my_new_name = input("Новое имя ссылки: ")
my_url = 'sdsdsdsdsd'
my_new_name = 'da'

print(emulator.adding_to_dict(my_new_name, my_url))

while True:
    new_link_request = input("Хотите добавить еще ссылку?(y/n): ")
    if new_link_request == "y":
        my_url = input("Ссылка которую нужно сократить: ")
        my_new_name = input("Новое имя ссылки: ")
        emulator.adding_to_dict(my_new_name, my_url)
        print(emulator.my_array)
    elif new_link_request == "n":
        break

while True:
    link_request = input("Хотите получить свою ссылку(y/n): ")
    if link_request == "y":
        name = input("Имя: ")
        print(emulator.get_linc_from_dict(name))
    elif link_request == "n":
        break
