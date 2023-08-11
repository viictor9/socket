import socket
import pyaes
import hashlib

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 8080)
server_socket.bind(server_address)

print("\n\tServer is listening for incoming messages...")

plain, client_address = server_socket.recvfrom(1024)
plain = plain.decode()

data, client_address = server_socket.recvfrom(1024)
# print(f"Received message 1 from {client_address}: {data}\n")

aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
decrypted_data = aes.decrypt(data).decode()  

print(f"\t{server_address}\n")

if decrypted_data == plain:
    print("\tConfidentiality verified: Decrypted message matches original plaintext.\n")
else:
    print("\tConfidentiality compromised: Decrypted message does not match original plaintext.\n")

# data, client_address = server_socket.recvfrom(1024)
# print(data)

received_md5_hash, client_address = server_socket.recvfrom(1024)
received_md5_hash = received_md5_hash.decode()

calculated_md5_hash = hashlib.md5(decrypted_data.encode()).hexdigest()

# print(f"Received message 2 from {client_address}: {data.decode()}")

if received_md5_hash == calculated_md5_hash:
    # print(f"Hash is: {calculated_md5_hash}")
    print("\tIntegrity verified: Hash value matches.\n")
else:
    print("\tIntegrity compromised: Hash values do not match.\n")


if decrypted_data:
    print("\tAvailability verified: Message received properly.\n")
    print(f"\tMessage from client: {decrypted_data}\n")
else:
    print("\tAvailability compromised: Message not received properly.\n")

server_socket.close()


#udp = sock_dgram