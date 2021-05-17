import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect('unix.sock')
sock.send(b'5, 8')
result = sock.recv(1024)
result = result.decode()
print('Data:', result)
sock.close()
