import socket

class Server():
    """A simple server that accepts client connections."""

    def __init__(self,host,port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((host,port))     
        
    def run_server(self):
        """Tries to listen for client connections and receive data continuously."""
        self.socket.listen(1)
        connection, address = self.socket.accept()
        while True:
            try:
                data = connection.recv(1024)

                if not data:break
                print('Client says:' + data)
                connection.sendall('Server says:hi')
            except socket.error as e:
                print('Error occurred:' + str(e))
                break
        connection.close()

HOST = 'localhost'
PORT = 12345

if __name__ == '__main__':

    server = Server(HOST,PORT)
    server.run_server()