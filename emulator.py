def adding_to_dict():
    my_url = input("Ссылка которую нужно сократить: ")
    my_new_name = input("Новое имя ссылки: ")
    new_values = {my_new_name: my_url}
    emulator.update(new_values)


def get_linc_from_dict():
    while True:
        link_request = input("Хотите получить свою ссылку(y/n): ")
        if link_request == "y":
            print(emulator.get(input("Имя: ")))
        elif link_request == "n":
            break


def logic():
    adding_to_dict()
    while True:
        new_link_request = input("Хотите добавить еще ссылку?(y/n/e): ")
        if new_link_request == "y":
            adding_to_dict()
        elif new_link_request == "n":
            get_linc_from_dict()
            break


emulator = {}
logic()
