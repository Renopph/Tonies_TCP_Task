"""The server script that was requested."""
import socketserver
import test_pb2 as proto

class Server(socketserver.BaseRequestHandler):
    """A simple server that accepts client connections. The read_buffer specifies how to read the protobuf-encoded messages"""

    def handle(self):
        """Test handler. This function needs to be overwritten in order for the communication to be customized."""
        # the number 4096 is arbitrary. This is the maximum size to be received in a buffer
        self.data = self.request.recv(4096).strip()
        print('{} wrote: {}'.format(self.client_address,Server.read_buffer(self.data)))
        self.request.sendall(b'Received your message.')

    @staticmethod
    def read_buffer(buffer):
        """Reads a protobuf-encoded message"""

        # Read the first 8 Bytes (unsigned long) to find out the length of the message
        # in python 3, int() should handle longints automatically
        length = int.from_bytes(buffer[0:4],'big')
        # Try unpacking all the following bytes at once
        payload = buffer[4:4+length]
        log_message = proto.LogMessage()
        log_message.ParseFromString(payload)
        return(log_message)

HOST = 'localhost'
PORT = 9999

if __name__ == '__main__':

    # Create server at the defined port on localhost
    with socketserver.TCPServer((HOST,PORT),Server) as server:
        # This will keep the server running until someone closes it (CTRL+C in the Linux terminal).
        server.serve_forever()