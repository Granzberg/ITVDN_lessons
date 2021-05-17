from socketserver import UnixStreamServer, StreamRequestHandler
import os


os.unlink('unix.sock')


class EchoTCPServer(StreamRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        data = data.decode('utf-8')
        data = int(data[0]) + int(data[-1])
        data = str(data)
        data = data.encode('utf-8')
        self.request.sendall(data)


if __name__ == '__main__':
    with UnixStreamServer('unix.sock', EchoTCPServer) as server:
        server.serve_forever()
