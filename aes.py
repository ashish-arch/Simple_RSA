import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b"password"
salt = b'\xdf\x05fB\xdf\x9d\xa2\xe7\x99V\xe5f+*\xb3\xfc'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
 )
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

def aesEncrypt():
    return f.encrypt(b'Put the text to be encrypted')

def aesDecrypt():
    return f.decrypt(cipher_text)

token = f.encrypt(b"Secret message!")
print(token)

red = f.decrypt(token)

print(red)