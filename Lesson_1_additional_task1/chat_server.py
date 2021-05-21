import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8000))
sock.listen(5)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        message = client.recv(1024)
        client.close()
        print('Сообщение: ', message.decode('utf-8'))
