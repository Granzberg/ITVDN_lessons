import socket

host = 'localhost'
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
message = input('Сообщение: ')
sock.send(message.encode('utf-8'))
sock.close()
