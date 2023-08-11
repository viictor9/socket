import hashlib

value = input("Enter text to hash: ")

hashh = hashlib.sha512(value.encode("UTF-8"))

print("SHA512 hash: ", hashh.hexdigest(), "\n")

hashmd5 = hashlib.md5(value.encode("UTF-8"))

print("MD5 hash: ",hashmd5.hexdigest(), "\n")

hash256 = hashlib.sha256(value.encode("UTF-8"))

print("SHA256 hash: ", hash256.hexdigest(), "\n")