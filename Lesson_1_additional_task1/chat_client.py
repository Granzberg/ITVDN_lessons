import socket
import threading


def read_sock():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


server = 'localhost', 8000
name = input('Введите псевдоним: ')
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto((name + 'Connect to server').encode('utf-8'), server)
potok = threading.Thread(target=read_sock)
potok.start()


while True:
    mensahe = input()
    sor.sendto(('[' + name + ']' + mensahe).encode('utf-8'), server)
