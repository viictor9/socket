import socket
import struct

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
client_socket.connect(server_address)

# Send the first message
message1 = "Hello, server! This is message 1."
length1 = len(message1)
client_socket.send(struct.pack('!I', length1))
client_socket.send(message1.encode())

# Send the second message
message2 = "Hello again, server! This is message 2."
length2 = len(message2)
client_socket.send(struct.pack('!I', length2))
client_socket.send(message2.encode())

client_socket.close()
