class Editor:
    def view_document(self):
        edit_my_file = open('text.txt', 'r')
        print('открытие документа', edit_my_file.name)
        print('закрытие документа', edit_my_file.closed)
        edit_my_file.close()
        print('файл закрыт', edit_my_file.closed)

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии.")


class ProEditor(Editor):
    def view_document(self):
        edit_my_file = open('text.txt', 'w')
        edit_my_file.write('запись в файл!')
        read_text = edit_my_file.read()
        print('прочитано')
        print(read_text)
        edit_my_file.close()

    def edit_document(self):
        print("Редактирование документов разрешено")


def passw(password):
    key = "123456"
    if password == key:
        ProEditor.edit_document(self=password)
        ProEditor.view_document(self=password)
    else:
        Editor.edit_document(self=password)
        Editor.view_document(self=password)
        

password = input("Введите лицензионный ключ: ")
passw(password)

