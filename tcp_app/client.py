"""The client module is only here for testing if the server does what is required."""
import socket
import struct
from message_generator import ProtobufWriter

HOST = 'localhost'
PORT = 9999

# What to simulate:
# up to 100 clients (have to look into how to simulate this)
# Send multiple messages with arbitrarily long pauses in between
# Either close at arbitrary times, even while sending a message
# stay open forever and keep sending


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    payload = ProtobufWriter.encode_info()
    sent_data = struct.pack('>L',len(payload)) + payload
    sock.sendall(sent_data)
    print(sent_data)

    received = str(sock.recv(1024),'utf-8')

print('Sent: {}'.format(payload))
print('Received: {}'.format(received))