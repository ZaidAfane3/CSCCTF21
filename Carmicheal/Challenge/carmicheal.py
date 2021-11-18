#!/usr/local/bin/python3
from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
e = 65537
n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
print(f'e = {e}\nd = {d}\nn = {n}\n')

d_ = int(input('> '))
assert d_ != d
assert 0 <= d_ < phi

with open('flag.txt') as f:
    msg = f.read().strip().encode()

msg = bytes_to_long(msg)
enc = pow(msg, e, n)
dec1 = pow(enc, d, n)
dec2 = pow(enc, d_, n)
assert dec1 == dec2
print(long_to_bytes(dec2).decode())