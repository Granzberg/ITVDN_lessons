import emulator


my_url = input("Ссылка которую нужно сократить: ")
my_new_name = input("Новое имя ссылки: ")
#my_url = 'sdsdsdsdsd'
#my_new_name = 'da'

print(emulator.Emulator.logic(my_url, my_new_name))
print(emulator.Emulator.adding_to_dict(my_url, my_new_name))


def loop():
    new_link_request = input("Хотите добавить еще ссылку?(y/n/e): ")
    print(emulator.Emulator.logic(new_link_request))

def loop2():
    link_request = input("Хотите получить свою ссылку(y/n): ")
    print(emulator.Emulator.get_linc_from_dict(link_request))


