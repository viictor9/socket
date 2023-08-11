import pyaes
import socket 
import rsa
import hashlib

print("1: symmetric \n2: asymmetric ")
choice = int(input("Enter the type of cryptography: "))
# print("1: symmetric \n2: asymmetric ")

mainmessage = input("Enter the message: ")


def AES():
    aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    # plaintext = input("Enter plain text for aes: ")
    ciphertext = aes.encrypt(mainmessage)
    print("Encrypted text: ", ciphertext)

    #decryption
    # aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    # plaintext = aes.decrypt(ciphertext)
    # print("Decrypted text: ", plaintext)


def RSA():
    (pubkey, privkey) = rsa.newkeys(512)
    message = mainmessage.encode("UTF-8")
    crypto = (rsa.encrypt(message, pubkey))
    finalMessage = print(str(crypto)[:150]+"\n"+str(crypto)[150:])
    # message = rsa.decrypt(crypto, privkey)
    # print(message.decode('utf8'))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 8080)  
    server_socket.bind(server_address)

    server_socket.listen(1)

    print("Server is listening for incoming connections...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    message = finalMessage.encode("UTF-8")
    client_socket.send(message)

    data = client_socket.recv(1024).decode()
    print(f"Received from client: {data}")

    client_socket.close()

    server_socket.close()

if choice == 1:
    AES()

else:
    RSA()

