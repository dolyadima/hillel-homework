# version 1.0 (original: Ihor Harahatyi)
# import socket
# import threading
#
# CONNECTIONS = set()
#
#
# class SockThread(threading.Thread):
#     def __init__(self, conn, *a, **kwa):
#         self.conn = conn
#         super().__init__(*a, **kwa)
#
#     def run(self):
#         with self.conn:
#             while True:
#                 data = self.conn.recv(1024)
#                 print('Recieved message:', data)
#                 if not data:
#                     print(f'Client {self.conn} disconnected!')
#                     CONNECTIONS.remove(self.conn)
#                     break
#                 for conn in CONNECTIONS:
#                     conn.sendall(data)
#
#
# def main():
#     with socket.socket(socket.AF_INET,
#                        socket.SOCK_STREAM,
#                        proto=socket.IPPROTO_TCP) as sock:
#         sock.bind(('0.0.0.0', 8887))
#         sock.listen()
#
#         while True:
#             conn, addr = sock.accept()
#             CONNECTIONS.add(conn)
#             print(f'Client {addr} connected.')
#             sock_thread = SockThread(conn)
#             sock_thread.start()
#
#
# if __name__ == '__main__':
#     main()

# version 2.0 (
#   asyncio.get_event_loop(), loop.sock_accept(),
#   loop.sock_recv(), loop.sock_sendall()
#   )
import socket
import asyncio


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP,
        )
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        self.socket.setblocking(False)
        self.main_loop = asyncio.get_event_loop()
        self.users = []
        print(f'Server is listening <{self.host}:{self.port}>')

    async def send_data(self, data=None):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data)

    async def listen_socket(self, listened_socket=None, addr=('0.0.0.0', -1)):
        if not listened_socket:
            return

        while True:
            try:
                data = await self.main_loop.sock_recv(listened_socket, 2048)
                print(f'Recieved message <{data.decode("utf-8")}>')
                if not data:
                    print(f'Client <{addr}> disconnected')
                    self.users.remove(listened_socket)
                    return
                await self.send_data(data)
            except Exception as e:
                print(f'Error in try "listen_socket": {e}')
            # except ConnectionResetError:
            #     print(f'error, Client <{addr}> removed')
            #     self.users.remove(listened_socket)
            #     return

    async def accept_sockets(self):
        while True:
            user_socket, address = await self.main_loop.sock_accept(self.socket)
            print(f"Client <{address}> connected")
            self.users.append(user_socket)
            self.main_loop.create_task(self.listen_socket(user_socket, address))

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())

    def start(self):
        self.main_loop.run_until_complete(self.main())


if __name__ == '__main__':
    # server = Server('127.0.0.1', 8887)
    server = Server('0.0.0.0', 8887)
    server.start()

# TODO
# version 3.0
# StreamReader, StreamWriter
