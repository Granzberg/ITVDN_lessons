import socketserver


class MyTCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = str(self.request.recv(1024), 'utf-8')
        print("{}:{} wrote:".format(self.client_address[0], self.client_address[1]))
        print("Message: " + self.data)
        self.data = int(self.data[0]) + int(self.data[-1])
        self.data = str(self.data)

        self.request.sendall(self.data.encode('utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    with socketserver.TCPServer((HOST, PORT), MyTCPServer) as server:
        server.serve_forever()
