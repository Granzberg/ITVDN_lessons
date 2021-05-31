import os.path
import asyncio
import time


async def read_file(data):
    if data:
        print('Чтение файла')
        file = open(data, 'r')
        a = file.read()
        for line in a.split(" "):
            print(line)
            if line == 'Wow!':
                file.close()
                await delete(data)
            else:
                time.sleep(5)
        file.close()


async def delete(data1):
    print("Удаление файла")
    os.remove(data1)


data = os.path.join('data.txt')


event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(read_file(data))]
tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()