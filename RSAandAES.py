from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC







# Run this function as soon as backend receive the post data

def keyGeneration():
    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()
    publicKey = pubKeyPEM.decode('ascii')  # This is public Key store this directly to database
    privateKey = privKeyPEM.decode('ascii') # This is private Key store this after AES encrypting it with the hotelien admin password
    return [publicKey,privateKey]


#########  publicKey = pubKeyPEM.decode('ascii')  ##########
#use this key to encrypt every email and phone no of user who checkin in that particular hotel



Keys = keyGeneration()
#Keys[0] is public key
#keys[1] is private key

#print(Keys)






########## Encrypt the privateKey in AES using the below function#########

#AES  
def aesEncryptKeyGeneration():
    password = b"put the custom admin password here"  #password form the sign up form
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
    return f



cipherSuitKey = aesEncryptKeyGeneration()


def aesEncrypt(cipherSuitKey,privateKey):
    return cipherSuitKey.encrypt(privateKey.encode('utf-8'))

cipher_text = aesEncrypt(cipherSuitKey,Keys[1])             #Keys[1] is the private key above
# this will be the encrypted private key to be store in the database
#the output will be in the form   b'something'  to remove b''  use  .decode('ascii') at the end 



#print(cipher_text)     



def aesDecrypt(cipherSuitKey, cipher_text):
    return cipherSuitKey.decrypt(cipher_text)

decrypted_text = aesDecrypt(cipherSuitKey,cipher_text)


#print(decrypted_text)