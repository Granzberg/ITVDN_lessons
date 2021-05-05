emulator = {}


def my_emulator():
    my_url = input("Ссылка которую нужно сократить: ")
    my_new_name = input("Новое имя ссылки: ")
    new_values = {my_new_name: my_url}
    emulator.update(new_values)


my_emulator()
link_request = input("Хотите получить свою ссылку(y/n): ")


def branching(link_request):
    while True:
        if link_request == "y":
            print(emulator.get(input("Имя: ")))
            link_request = input("Хотите получить свою ссылку(y/n): ")
        elif link_request == "n":
            new_link_request = input("Хотите добавить еще ссылку?(y/n/e): ")

            if new_link_request == "y":
                my_emulator()
            elif new_link_request == "n":
                break


branching(link_request)
