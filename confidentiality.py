import pyaes
from pyDes import *
import rsa
from cryptography.fernet import Fernet


def AES():
    aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    plaintext = input("Enter plain text for aes: ")
    ciphertext = aes.encrypt(plaintext)
    print(ciphertext)
    aes = pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
    plaintext = aes.decrypt(ciphertext)
    print(plaintext)

AES()

def DES():
    data = input("Enter plain text for des: ")
    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5) 
    d=k.encrypt(data)
    print("Encrypted: %r" % d)
    print("Decrypted: %r" % k.decrypt(d))
      
DES()

def symmetric():

    plaintext = input("Enter plain text: ")

    key = Fernet.generate_key()

    f = Fernet(key)

    token = f.encrypt(b"hello")

    print(token)

    d = f.decrypt(token)

    print(d)


symmetric()

def RSA():
    (pubkey, privkey) = rsa.newkeys(512)
    message = input("Enter plain text for RSA: ").encode('utf8')
    crypto = (rsa.encrypt(message, pubkey))
    print(str(crypto)[:150]+"\n"+str(crypto)[150:])
    message = rsa.decrypt(crypto, privkey)
    print(message.decode('utf8'))


RSA()

# cryptography = input("Enter type of cryptgraphy: ")


