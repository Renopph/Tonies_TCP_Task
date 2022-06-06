"""The client module is only here for testing if the server does what is required."""
import socket


class Client():
    """A simple client to connect to the server and send messages."""

    def __init__(self,port):
        self.host = socket.gethostname()
        self.port = port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    def connect_to_server(self):
        self.socket.connect((self.host,self.port))
        self.socket.sendall(b'Hello World')
        data = self.socket.recv(1024)


HOST = 'localhost'
PORT = 12345

if __name__ == '__main__':
    client = Client(PORT)

    client.connect_to_server()