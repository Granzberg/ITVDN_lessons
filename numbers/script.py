import random

numbers = [random.randint(-100000, 100000)for _ in range(10000)]

with open('Lesson_8_task1.txt', 'w') as data:
    for number in numbers:
        data.write('{}\n'.format(number))

