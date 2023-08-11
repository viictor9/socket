import socket
import pyaes
import hashlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080) 
client_socket.connect(server_address)

server_data = client_socket.recv(1024)  

aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
decrypted_data = aes.decrypt(server_data).decode()  

received_md5_hash = client_socket.recv(1024).decode()

calculated_md5_hash = hashlib.md5(server_data).hexdigest()

if received_md5_hash == calculated_md5_hash:
    # print(f"Hash is: {calculated_md5_hash}")
    print("Integrity verified.")
else:
    print("Integrity compromised.")

# print("Encrypted message from the server: ", server_data)
try:
    received = server_data
    print(f"Availability verified\n Message: {decrypted_data}")
except:
    print("Availability compromised")

# aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
# message = input("Enter message: ")
# message = aes.encrypt(message.encode("UTF-8"))
# client_socket.send(message.encode())

client_socket.close()


#client