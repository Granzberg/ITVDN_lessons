import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8000))
client = []
print('Start')
while True:
    data, addres = sock.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in client:
        client.append(addres)

    for clients in client:
        if clients == addres:
            continue

        sock.sendto(data, clients)
