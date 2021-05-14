import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.connect(('localhost', 8000))
num1 = int(input('a= '))
num2 = int(input('b= '))
sock.send(b'num1, num2')
sock.close()
