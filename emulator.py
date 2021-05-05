my_url = input("Ссылка которую нужно сократить: ")
my_new_name = input("Новое имя ссылки: ")

emulator = {my_new_name: my_url}

link_request = input("Хотите получить свою ссылку(y/n): ")

if link_request == "y":
    print(emulator.get(my_new_name))
else:
    print("Спасибо. До свидания")

