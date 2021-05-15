from socketserver import UnixStreamServer, StreamRequestHandler
import os


os.unlink('unix.sock')


class EchoTCPServer(StreamRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        data = data.decode('utf-8')
        result = self.handling_data(data)
        print('Data: {}'.format(result))
        result_bin = data.encode(self.handling_data(data))
        self.request.sendall(result)

    def handling_data(self, data):
        res1 = int(data[0])
        res2 = int(data[-1])
        print(res1, res2)
        data = res1 + res2
        data = str(data)
        return data


if __name__ == '__main__':
    with UnixStreamServer('unix.sock', EchoTCPServer) as server:
        server.serve_forever()
