import pyaes
from pyDes import *
import rsa
from cryptography.fernet import Fernet


def AES():
    aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    plaintext = input("Enter plain text for aes: ")
    ciphertext = aes.encrypt(plaintext)
    print("Encrypted text: ", ciphertext)
    aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    plaintext = aes.decrypt(ciphertext)
    print("Decrypted text: ", plaintext)

# AES()

def DES():
    data = input("Enter plain text for des: ")
    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5) 
    d=k.encrypt(data)
    print("Encrypted : %r" % d)
    print("Decrypted : %r" % k.decrypt(d))
      
# DES()

def symmetric():

    plaintext = input(b"Enter plain text: ")

    key = Fernet.generate_key()

    f = Fernet(key)

    message = plaintext.encode()

    token = f.encrypt(message)

    print(token)

    d = f.decrypt(token)

    print(d)


# symmetric()

def RSA():
    (pubkey, privkey) = rsa.newkeys(512)
    message = input("Enter plain text for RSA: ").encode('utf8')
    crypto = (rsa.encrypt(message, pubkey))
    print(str(crypto)[:150]+"\n"+str(crypto)[150:])
    message = rsa.decrypt(crypto, privkey)
    print(message.decode('utf8'))


# RSA()


cryp = int(input("Enter the type of cryptography: \n 1:Symmetric \n 2:Asymmetric \n"))



if cryp == 1:

    algo = int(input("Enter the technique to encrypt: \n 1:AES\n 2:DES\n 3:Fernet"))

    if algo == 1:
        AES()

    elif algo == 2:
        DES()

    else:
        symmetric()

else:
    RSA()





# cryptography = input("Enter type of cryptgraphy: ")


