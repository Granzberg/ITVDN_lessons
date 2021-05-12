def adding_to_dict(my_new_name, my_url, my_array):
    # Функция которая создает ключ/значение и проверяет его что бы не было повторений.
    try:
        while True:
            new_values = {my_new_name: my_url}
    # Проверка существует ли имя.
            check = my_array.get(my_new_name, 0)
            if check != 0:
                raise KeyError
            else:
                my_array.update(new_values)
                return my_array
    except KeyError as error:
        print("Такой ключ существует\nСоздайте другой ключ!", error)


def get_linc_from_dict(name, my_array):
    # Функия на выдачи сылки по ключу. Не импортирывать!.
    print(my_array.get(name))



