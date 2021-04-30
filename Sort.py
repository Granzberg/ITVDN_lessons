fraze = input("Введите текст: ")
fraze = fraze.split()
fraze.sort(key=str.lower)
print(fraze)
