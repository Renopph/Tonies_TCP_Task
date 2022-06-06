import socketserver
import test_pb2 as proto
import struct

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
        # print(buffer)
        length = int.from_bytes(buffer[0:4],'big')
        # Try unpacking all the following bytes at once
        payload = buffer[4:4+length]
        log_message = proto.LogMessage()
        message = log_message.ParseFromString(payload)
        # print(log_message)
        return(log_message)



HOST = 'localhost'
PORT = 9999

if __name__ == '__main__':
    # testing formatting of bytes
    # data = b'\n\x05ERROR\x12\x04main\x1a\x06\x13]\xcbBq\xdf"\x16Insufficient resources'
    # data = struct.pack('>L',len(data)) + data
    # print(Server.read_buffer(data))

    # Create server at the defined port on localhost
    with socketserver.TCPServer((HOST,PORT),Server) as server:
        # This will keep the server running until someone closes it (CTRL+C in the Linux terminal)
        server.serve_forever()