import socket
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client import Client


class Server:
    def __init__(self, host="localhost", port=8080):
        self.host = host
        self.port = port
        self.clients: list["Client"] = []

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        print(f"Server started on {self.host}:{self.port}")
        self.running = True
