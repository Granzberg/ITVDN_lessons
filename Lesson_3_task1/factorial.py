import threading
import time


def handler(started=1, finished=0):
    result = 1
    for i in range(started, finished+1):
        result *= i
    print('Факториал числа ' + str(a) + ' будет: ' + str(result))


a = int(input('Факторил числа: '))
params = {'finished': a}

task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print('RESULT 1')
task.start()
task.join()
print('Time: {}'.format(time.time() - started_at))

started_at = time.time()
print('RESULT 2')
handler(**params)
print('Time: {}'.format(time.time() - started_at))
