import os.path
from asyncio.coroutines import iscoroutine
import asyncio
import time


def read_file(data):
    while True:
        if data:
            print('Чтение файла')
            file = open(data, 'r')
            for line in file:
                if line == 'Wow!\n':
                    print(line, end='')
                else:
                    yield from time.sleep(5)
            file.close()
            break
        else:
            time.sleep(5)


async def delete():
    print("Удаление файла")
    os.remove('data')


data = os.path.join('data')


event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(read_file('data')),
    event_loop.create_task(delete()),

]
tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()



