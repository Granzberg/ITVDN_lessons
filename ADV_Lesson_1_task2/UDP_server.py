import socketserver


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print('Address: {}\nData: {}'.format(self.client_address[0], data.decode()))
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    with socketserver.UDPServer(('localhost', 8000), UDPHandler) as server:
        server.serve_forever()
