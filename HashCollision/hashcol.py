from crypto.util.number import *
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

BLOCKSIZE = 8

def SIU5(m):
    assert len(m) % BLOCKSIZE == 0
    init = m[:8]
    prod = m[8:]
    x = 0
    for i in prod:
        init[x] *= bytes_to_long(i)
        x %= BLOCKSIZE
        x += 1
        x %= BLOCKSIZE
    
    return init.hex()

print("Check out my Kickass Secure Hashing Algorithm 😎😎")

h1 = bytes.fromhex(input("> ").strip())
h2 = bytes.fromhex(input("> ").strip())

print(SIU5(h1))
print(SIU5(h2))
assert h1 != h2
assert SIU5(h1) == SIU5(h2)
# with open('flag.txt', 'r') as f:
#     print(f.read())