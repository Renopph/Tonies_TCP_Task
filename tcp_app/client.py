"""The client module is only here for testing if the server does what is required."""
import socket


# class Client():
#     """A simple client to connect to the server and send messages."""

#     def __init__(self,port):
#         self.host = socket.gethostname()
#         self.port = port
#         # SOCK_STREAM -> TCP socket
#         self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
#     def connect_to_server(self):
#         self.socket.connect((self.host,self.port))
#         self.socket.sendall(b'Hello World')
#         data = self.socket.recv(1024)


HOST = 'localhost'
PORT = 9999
data=b'Hello World'

# if __name__ == '__main__':
#     client = Client(PORT)

#     client.connect_to_server()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(bytes(str(data) + '\n','utf-8'))

    received = str(sock.recv(1024),'utf-8')

print('Sent: {}'.format(data))
print('Received: {}'.format(received))