#import start_emulator


class Emulator(object):
    def __init__(self, my_url, my_new_name, link_request, new_link_request, emulator={}):
        self.my_url = my_url
        self.my_new_name = my_new_name
        self.link_request = link_request
        self.new_link_request = new_link_request
        self.emulator = emulator

    def adding_to_dict(self, my_url, my_new_name):
        # Функция которая создает ключ/значение и проверяет его что бы не было повторений.
        try:
            while True:
                new_values = {my_new_name: my_url}
        # Проверка существует ли имя.
                check = self.emulator.get(my_new_name, 0)
                if check != 0:
                    raise KeyError
                else:
                    self.emulator.update(new_values)
                    break
        except KeyError as error:
            print("Такой ключ существует\nСоздайте другой ключ!", error)

    def get_linc_from_dict(self, link_request):
        # Функия на выдачи сылки по ключу. Не импортирывать!.
        while True:
            #start_emulator.loop2()
            if link_request == "y":
                print(self.emulator.get(input("Имя: ")))
            elif link_request == "n":
                break

    def logic(self, my_url, my_new_name, new_link_request, link_request):
        # Функция выбора действия. Не импортировать!
        self.adding_to_dict(my_url, my_new_name)
        while True:
            #start_emulator.loop()
            if new_link_request == "y":
                self.adding_to_dict(my_url, my_new_name)
            elif new_link_request == "n":
                self.get_linc_from_dict(link_request)
                break
