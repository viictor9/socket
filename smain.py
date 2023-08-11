import pyaes
import socket
import hashlib

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
server_socket.bind(server_address)

server_socket.listen(1)


print("Server is listening for incoming connections...")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
plaintext = input("Enter message to send: ")
ciphertext = aes.encrypt(plaintext.encode())  

md5_hash = hashlib.md5(ciphertext).hexdigest()

client_socket.send(ciphertext)
client_socket.send(md5_hash.encode())

# print(f"Hash is {md5_hash}")

print("Program ended.")

# data = client_socket.recv(1024).decode()

# print(f"Message recieved from client: {data}")


client_socket.close()

server_socket.close()


#server