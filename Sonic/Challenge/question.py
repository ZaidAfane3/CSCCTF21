#!/usr/local/bin/python3
import random
import base64
from Crypto.Util.number import *
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

with open('wordlist.txt', 'r') as f:
    ls = [line.strip() for line in f.readlines()]

chall = ['base64', 'rot', 'hex', 'long']

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

print('Quick I need you to decode the following messages.')
print('If you can help me, I\'ll give you a prize!')

score = 0
while True:
    plaintxt = "_".join(random.choices(ls, k=4))
    encoding = random.choice(chall)
    if encoding == 'base64':
        print(encoding,base64.b64encode(plaintxt.encode()).decode(),sep=':')

    if encoding == 'rot':
        n = random.randint(1, 25)
        print(encoding,rot_alpha(n)(plaintxt), n,sep=':')

    if encoding == 'hex':
        print(encoding,plaintxt.encode().hex(),sep=':')

    if encoding == 'long':
        print(encoding,bytes_to_long(plaintxt.encode()),sep=':')

    decoded = input('> ')
    if decoded == plaintxt:
        score += 1
    else:
        print('WRONG DECODED MESSAGE!')
        exit(1)

    if score == 200:
        with open('flag.txt', 'r') as f:
            print('Congratulations, For your assistance, you will be rewarded with a flag!!')
            print(f.read())
            exit()