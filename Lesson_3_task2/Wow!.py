import os.path
import threading
import time


def read_file(data):
    while True:
        if data:
            print('Чтение файла')
            file = open(data, 'r')
            for line in file:
                if line == 'Wow!':
                    print(line, end='')
                else:
                    time.sleep(5)

            file.close()
            data_found.set()
            data_found.clear()
            break
        else:
            time.sleep(5)
            continue


def delete():
    print("Удаление файла")
    data_found.wait()
    os.remove('data')


data_found = threading.Event()

task1 = threading.Thread(target=read_file)
task2 = threading.Thread(target=delete)

task1.start()
task2.start()

task1.join()
task2.join()


if __name__ == '__main__':
    read_file(os.path.join('data'))

