import socket


host = socket.gethostbyname(socket.gethostname())
port = 8000

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)

print('Start')

client, addr = sock.accept()

while True:
    try:
        print(addr[0], addr[1])
        if addr not in clients:
            clients.append(addr)

    except KeyboardInterrupt:
        sock.close()
        print('Stop')
        break

    else:
        result = client.recv(1024)
        print(result.decode('utf-8'))
        for client in clients:
            sock.sendto(result, client)
            print('Sanded.')

sock.close()
