import socket

host = 'localhost'
port = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        message = sock.recv(1024).strip()
        print(message.decode('utf-8'))
        client.close()
