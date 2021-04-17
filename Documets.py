class Editor:
    def view_document(self):
        e = open('text.txt', 'r')
        return e

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии.")


class ProEditor(Editor):
    def edit_document(self):
        print("Редактирование документов разрешено")


def passw():
    key = "123456"
    if password == key:
        ProEditor.edit_document()
    else:
        Editor.edit_document(e)
        Editor.view_document(e)
        

password = input("Введите лицензионный ключ: ")
e = Editor
print(e.view_document(e))
