import asyncio


class EchoClientProtocol(asyncio.Protocol):

    try:
        def __init__(self, message, loop):
            self.message = message
            self.loop = loop

        def connection_made(self, transport):
            transport.write(self.message.encode('utf-8'))
            print('Data sent: {!r}'.format(self.message))
            if message == 'close':
                raise KeyError

    except KeyError:
        def connection_lost(exc):
            print('The server closed the connection')
            print('Stop the event loop')
            loop.stop()

    else:
        def data_received(self, data):
            data = 'Data received: {!r}'.format(data.decode('utf-8'))
            print(data)


loop = asyncio.get_event_loop()

message = input('Сообщение: ')

coro = loop.create_connection(lambda: EchoClientProtocol(message, loop), 'localhost', 8000)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
