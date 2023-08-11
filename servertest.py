import socket
import struct

def recv_all(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
server_socket.bind(server_address)

server_socket.listen(1)

print("Server is listening for incoming connections...")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive and print the first message
length1 = struct.unpack('!I', client_socket.recv(4))[0]
message1 = recv_all(client_socket, length1).decode()
print(f"Received message 1: {message1}")

# Receive and print the second message
length2 = struct.unpack('!I', client_socket.recv(4))[0]
message2 = recv_all(client_socket, length2).decode()
print(f"Received message 2: {message2}")

client_socket.close()
server_socket.close()
