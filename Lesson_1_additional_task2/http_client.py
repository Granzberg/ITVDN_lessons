import socket



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))

content = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]

content = '\n'.join(content)

print(content)

sock.send(content.encode('utf-8'))
result = sock.recv(10240)
print(result.decode('utf-8'))
