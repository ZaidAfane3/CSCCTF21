from Crypto.Util import number
from Crypto.Cipher import AES
import os

def keygen():
    iv, key = [os.urandom(16) for _ in range(2)]
    return iv, key

def encrypt(msg, iv, key):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(msg)

def decrypt(enc, iv, key):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(enc)

enc_flag = bytes.fromhex('3e1a7ce00863c85bf9e5fa217619cba8857e6e1356afd1a389a89ea3375a1073')
enc_text = bytes.fromhex('dbaa84bf20bc1cb6af86a26f5592fd06c1f5783a633664af0157fa068801fb0a')
iv = bytes.fromhex('66490ceda01b0f5700eb8efb299c8fc2')
key = b'\x00\x00' + bytearray.fromhex('3f4f0ab61a02891b10952fea0746')

for i in range(256):
    key = list(key)
    key[0] = i
    for j in range(256):
        key = list(key)
        key[1] = j
        key = bytes(key)
        dec = decrypt(enc_text, iv, key)
        if b'AAA' in dec:
             print(decrypt(enc_flag, iv, key).decode())
