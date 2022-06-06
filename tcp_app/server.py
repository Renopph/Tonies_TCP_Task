import socketserver

class Server(socketserver.BaseRequestHandler):
    """A simple server that accepts client connections."""

    def handle(self):
        """Test handler. This function needs to be overwritten in order for the communication to be customized."""
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())  
        
    # def run_server(self):
    #     """Tries to listen for client connections and receive data continuously."""
    #     self.socket.listen(1)
    #     connection, address = self.socket.accept()
    #     while True:
    #         try:
    #             data = connection.recv(1024)

    #             if not data:break
    #             print('Client says:' + data)
    #             connection.sendall('Server says:hi')
    #         except socket.error as e:
    #             print('Error occurred:' + str(e))
    #             break
    #     connection.close()

HOST = 'localhost'
PORT = 9999

if __name__ == '__main__':

    # Create server at the defined port on localhost
    with socketserver.TCPServer((HOST,PORT),Server) as server:
        # This will keep the server running until someone closes it (CTRL+C in the Linux terminal)
        server.serve_forever()