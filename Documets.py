class Editor:
    def __init__(self):
        pass

    def view_document(self):
        e = open('text.txt', 'x')
        return e

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии.")


class ProEditor(Editor):
    def __init__(self):
        pass

    def edit_document(self):
        print("Редактирование документов разрешено")


m = Editor.view_document()
