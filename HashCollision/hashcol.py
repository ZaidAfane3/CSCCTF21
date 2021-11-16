from Crypto.Util.number import *
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

rand_state = b'\x85H5\xc9*\xb1\xaai\x8a\x89DzZ\xe7J\xb7'
rand_prod = b'\x82\xc5\x8f_#eXI\x03\xcd\xdc>\xae\xdf@\xcd'
BLOCKSIZE = 8

def SIU5(m):
    assert len(m) % BLOCKSIZE == 0
    init = m[:8]
    prod = m[8:]
    # print(prod)
    if init == b'\x00\x00\x00\x00\x00\x00\x00\x00':
        init = rand_state
    if prod == b'':
        prod = rand_prod
    fin = [0 for _ in range(BLOCKSIZE)]
    x = 0
    for i in prod:
        if i == 0 or i == 1:
            i = init[x]
        fin[x] = init[x] * i
        fin[x] %= 256
        x += 1
        x %= BLOCKSIZE
    hsh = ''.join(chr(x) for x in fin).encode()
    return hsh.hex()

print("Check out my Kickass Secure Hashing Algorithm 😎😎")

h1 = bytes.fromhex(input("> ").strip())
h2 = bytes.fromhex(input("> ").strip())

print(SIU5(h1))
print(SIU5(h2))
assert h1 != h2
assert SIU5(h1) == SIU5(h2)
with open('flag.txt', 'r') as f:
    print(f.read())