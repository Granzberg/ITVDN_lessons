import socket

host = socket.gethostbyname(socket.gethostname())
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

name = input('Введите псевдоним: ')


while True:
    try:
        message = input('Text: ')
        sock.send((name + ': ' + message).encode('utf-8'))
        data = sock.recv(1024)
        data = data.decode('utf-8')
        print(data)
    except KeyboardInterrupt:
        sock.close()
        print('Stop')
        break
