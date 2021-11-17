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

iv, key = keygen()

with open('flag.txt', 'r') as f:
    flag = f.read().strip()

flag_enc = encrypt(flag.encode(), iv, key).hex()
while True:
    print('Enter G to get the encrypted flag, or E to Encrypt a message.')
    q = input('> ')
    if q.lower() == 'g':
        print(flag_enc)
    elif q.lower() == 'e':
        print('Enter the message you\'d like to encrypt (MUST BE 32 BYTES)')
        msg = input('> ')
        if len(msg) != 32:
            print('You dissapoint me, ;(')
            exit()
        enc = encrypt(msg.encode(), iv, key).hex()
        print('Encrypted Message: ',enc)
        print('IV:\t\t   ', iv.hex())
        print('Partial Key: \t   ','*' * 4 + key[2:].hex())

    else:
        print('You dissapoint me, ;(')
        exit()