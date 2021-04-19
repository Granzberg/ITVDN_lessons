class Editor:
    def view_document(self):
        print("Просмотр доступен")

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии.")


class ProEditor(Editor):
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

