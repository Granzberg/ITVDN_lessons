def adding_to_dict():
    # Функция которая создает ключ/значение и проверяет его что бы не было повторений.
    try:
        while True:
            my_url = input("Ссылка которую нужно сократить: ")
            my_new_name = input("Новое имя ссылки: ")
            new_values = {my_new_name: my_url}
    # Проверка существует ли имя.
            check = emulator.get(my_new_name, 0)
            if check != 0:
                raise KeyError
            else:
                emulator.update(new_values)
                break
    except KeyError as error:
        print("Такой ключ существует\nСоздайте другой ключ!", error)


def get_linc_from_dict():
    # Функия на выдачи сылки по ключу. Не импортирывать!.
    while True:
        link_request = input("Хотите получить свою ссылку(y/n): ")
        if link_request == "y":
            print(emulator.get(input("Имя: ")))
        elif link_request == "n":
            break


def logic():
    # Функция выбора действия. Не импортировать!
    adding_to_dict()
    while True:
        new_link_request = input("Хотите добавить еще ссылку?(y/n/e): ")
        if new_link_request == "y":
            adding_to_dict()
        elif new_link_request == "n":
            get_linc_from_dict()
            break


emulator = {}

