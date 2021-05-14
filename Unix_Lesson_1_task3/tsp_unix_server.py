import socket

sock = socket.socket(socket., socket.SOCK_DGRAM)
sock.bind(('localhost', 8000))
sock.listen(3)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))
