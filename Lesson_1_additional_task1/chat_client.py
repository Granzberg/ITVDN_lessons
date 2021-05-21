import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8000))
message = input('Сообщение: ')
sock.send(message.encode('utf-8'))
sock.close()
