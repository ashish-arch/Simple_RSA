from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


publicKey = '''-----BEGIN PUBLIC KEY-----
MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA3HqcJli0vDgMrsz4jTR5
mwdIs5qy2kK7sPqzlLqNqrz/JkkKYiCh2QFGX7UBdglDreb7JU3AVZ/e3LJPsTQz
zg63YCari+NI4Ne2LvKgJql4RFYLlwmwv2YbST00AkoEMvMeTO7uXMF/z1oB7xhy
iy+9EPRRT1BbdPC4yKbBvWol2fXJJPrj+6A48J+szd/IHgKQa14Jljs+WkTHFv5J
A1OTEdpOSh+Qj4NVtCd/xnHMY1Li7PKZffxla4Xsoo9Z9qxBfQxyN2nsmG1w82lA
QQgzCnMdw4uXdN9k2bV2FGScrO46H6NFsANFdG6MpzHCONim/aQ5J8IRLyymG38z
eBQfDjlRMWZ3uPjpe2ERmUGH+IrgAMeizkHNeXRFs/SzjMgYhxlvCwgwfcYqTWWM
zM4MkE0eeL26ynDM+J926O+jg37Pf/mUpkcRA5ZTRWwqJ7Y8db703pzK0O6EACrl
iLVCAv1V1d15JidCb5QOO8gSjDzPuRsU7Vs+b+lzaYkxAgMBAAE=
-----END PUBLIC KEY-----'''



privateKey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''


#initialising public key with RSA
Public_key = RSA.import_key(publicKey)

#initialing private Key with RSA
Private_key = RSA.import_key(privateKey)


def encrypter():
    msg = b'A message for encryption'
    encryptor = PKCS1_OAEP.new(Public_key)
    encrypted = encryptor.encrypt(msg)
    return binascii.hexlify(encrypted)


cipher = encrypter()

#print(cipher)
#the output will be in the form   b'something'  to remove b''  use  .decode('ascii') at the end 

def decrypter(cipher_text):
    decryptor = PKCS1_OAEP.new(Private_key)
    decrypted = decryptor.decrypt(cipher_text)
    return decrypted


decipher = decrypter(binascii.unhexlify(cipher))

#print(decipher)