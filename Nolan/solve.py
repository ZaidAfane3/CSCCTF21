import random
import time

seed1 = int(time.time())

with open('cipher.enc', 'r', encoding='utf-8') as f:
    enc = f.read().strip()

while True:
    random.seed(seed1)
    t = [random.randint(0,255) for _ in enc]
    dec = ''
    i = 0
    while i < len(enc):
        dec += chr(ord(enc[i]) ^ t[i])
        i += 1
    if 'CSCCTF' in dec:
        print(dec)
        exit()
    seed1 -= 1