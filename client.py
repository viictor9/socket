import socket
import pyaes
import hashlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 8080)

aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
plaintext = input("Enter message to send: ")
ciphertext = aes.encrypt(plaintext.encode())  

md5_hash = hashlib.md5(plaintext.encode()).hexdigest()
# print(md5_hash)

client_socket.sendto(plaintext.encode(), server_address)
client_socket.sendto(ciphertext, server_address)
client_socket.sendto(md5_hash.encode(), server_address)

client_socket.close()


# UDP = sock_dgram