import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8000))
while True:
    a = input('a =  ')
    b = input('b =  ')
    message = a + ' ' + b
    sock.send(message.encode('utf-8'))
    data = str(sock.recv(1024), 'utf-8')

    if data == 'close':
        print('closed')
        sock.close()
    else:
        print(data)
        continue
