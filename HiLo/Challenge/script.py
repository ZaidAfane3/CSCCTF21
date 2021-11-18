#!/usr/local/bin/python3
import random
import time
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

print('Would you like to play a game? Y/N')
x = input('> ')
if x.lower() == 'y':
    print('Let\'s Play Higher or Lower.')
    print('I will give you a number and you have to guess if the next one is going to be higher or lower.')
    print('Let us begin.')
    score = 0
    while True:
        a = random.randint(1, 256)
        print(f'The numebr is {a}')
        print('Higher or Lower')
        ans = input('> ')
        if score % 2 == 0:
            nx  = (a * 5) % 256
        else:
            nx  = (a // 4) % 256
        if nx > a:
            t = 'higher'
        else:
            t = 'lower'
        if ans.lower() == t:
            print(f'Correct, the new number was {nx}')
            score += 1
        else:
            print(f'Wrong, the new number was {nx}')
            exit(1)
        if score == 250:
            with open('flag.txt', 'r') as f:
                print(f.read())
                exit()
        a = nx

if x.lower() == 'n':
    print('Oh okay :(')
    print('Just take the flag: ')
    time.sleep(4)
    print('CSCCTF{0bv!ou$ly_A_F4k3_0ne}')
    time.sleep(4)
    print('LOOOOL YOU THOUGHT YOU CAN GET A FREE ONE, XDDDDDDDDDDDD')
    print('GOTTA PLAY TO WIN!')
    exit(1)
else:
    print('HUH!?!?!?')
    print('WHAT?!')
    print('Just try again.')
    exit(1)