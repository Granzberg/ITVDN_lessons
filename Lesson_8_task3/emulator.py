import shelve


def adding_to_dict(my_new_name, my_url, my_array):
    # Функция которая создает ключ/значение и проверяет его что бы не было повторений.
    try:
        while True:
            new_values = {my_new_name: my_url}
    # Проверка существует ли имя.
            check = my_array.get(my_new_name, 0)
            x = tuple(new_values)
            check_data = check_db()
            if x > check_data:
                return 0
            if check != 0 or check_data != 0:
                raise KeyError
            else:
                my_array.update(new_values)
                return my_array
    except (KeyError,) as error:
        print("Такой ключ существует\nСоздайте другой ключ!")


def get_linc_from_dict(name, my_array):
    # Функия на выдачи сылки по ключу. Не импортирывать!.
    print(my_array.get(name))


def check_db():
    filename = 'data'
    with shelve.open(filename) as db:
        for key in db.items():
            keys = key
    return keys

