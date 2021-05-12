my_array = {}


def adding_to_dict(my_new_name, my_url):
    # Функция которая создает ключ/значение и проверяет его что бы не было повторений.
    try:
        while True:
            new_values = {my_new_name: my_url}
    # Проверка существует ли имя.
            check = my_array.get(my_new_name, 0)
            if check != 0:
                raise KeyError
            else:
                print("Повторений нет")
                my_array.update(new_values)
                print(my_array)
                break
    except KeyError as error:
        print("Такой ключ существует\nСоздайте другой ключ!", error)


def get_linc_from_dict(name):
    print(my_array)
    # Функия на выдачи сылки по ключу. Не импортирывать!.
    my_array.get(name)



