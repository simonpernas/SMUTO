import socket
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .server import Server


    


class Client():
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.sock = None