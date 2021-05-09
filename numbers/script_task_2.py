import array
import random

numbers = [random.randint(-100000, 100000)for _ in range(10000)]

numbers_array = array.array('i', numbers)
with open('Lesson_8_task2.bin', 'wb') as data:
    data.write(numbers_array)
