import asyncio


class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode('utf-8')
        print('Data received: {!r}'.format(message))
        message = self.calculation(message)

        print('Send: {!r}'.format(message))
        self.transport.write(str(message).encode('utf-8'))

        print('Close the client socket')
        self.transport.close()

    def calculation(self, data):
        if data != 'close':
            number = list(data)
            number = int(number[0]) + int(number[-1])
            return number
        else:
            raise KeyboardInterrupt


loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol, 'localhost', 8000)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
