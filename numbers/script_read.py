numbers = []
with open('Lesson_8_task1.txt', 'r') as data:
    for line in data:
        numbers.append(int(line))

print(numbers)
