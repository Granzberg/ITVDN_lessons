sequence = int(input("Введите последовательность чисел: "))

sequence = map(int, str(sequence))
sequence = sorted(sequence)

print(sequence)
