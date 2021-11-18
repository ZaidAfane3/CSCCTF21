from Crypto.Util.number import *
import os
from Generator import generateKeys
os.chdir(os.path.abspath(os.path.dirname(__file__)))

e,n,d = generateKeys()
priv = (d,n)
pub = (e,n)

def encrypt(pub, msg):
        e, n = pub
        i = bytes_to_long(msg.encode())
        return int(pow(i, e, n))

def decrypt(priv, cipher):
        d, n = priv
        return long_to_bytes(pow(cipher, d, n))



with open('flag.txt', 'r') as f:
        msg = f.read().strip()
cipher = encrypt(pub, msg)

print(f'e = {pub[0]}\nn = {pub[1]}')
print('-' * 185)
print(f'c = {cipher}')
print('-' * 185)
