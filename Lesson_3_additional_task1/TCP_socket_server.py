import threading
import time
import socketserver


class MyTCPServer(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = str(self.request.recv(1024), 'utf-8')
        print("{}:{} wrote:".format(self.client_address[0], self.client_address[1]))
        print("Message: " + self.data)
        trigger.set()
        trigger.clear()

    def logic_calc(self, data):
        trigger.wait()
        data = int(data[0]) + int(data[-1])
        self.logic_shutdown(data)
        self.request.sendall(str(self.data).encode('utf-8'))

    def logic_shutdown(self, data):
        if data == 'close':
            socketserver.TCPServer.server_close()

    def separation(self):

        task1 = threading.Thread(target=self.handle)
        task2 = threading.Thread(target=self.logic_calc)
        started_at = time.time()

        task1.start()
        task2.start()

        task1.join()
        task2.join()


trigger = threading.Event()


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    with socketserver.TCPServer((HOST, PORT), MyTCPServer) as server:
        server.serve_forever()
