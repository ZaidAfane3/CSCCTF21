#!/usr/local/bin/python3
import random
import time
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

x = os.urandom(16)
random.seed(x)

operations = ['+', '-', '*', '//']

print('NEED TO SOLVE SOME MATH RN!!!!!')
print('SOLVE AS MUCH AS YOU CAN AND YOU WILL REAP WHAT YOU SOW!')
score = 0
while True:
    a = random.randint(1,10e6)
    b = random.randint(1,10e6)
    operand = random.choice(operations)
    eq = str(a) + ' ' + operand + ' ' + str(b)
    x = eval(eq)
    print(eq)
    start = time.time()
    try:
        ans = int(input('> '))
    except:
        print('YOU\'RE DOING SOMETHING WRONG!\nTRY AGAIN LATER!')
        exit(1)
    end = time.time()
    if end - start > 3:
        print('TOO SLOW!\nTRY AGAIN LATER!')
        exit(1)
    if ans != x:
        print('WRONG!\nTRY AGAIN LATER!')
        exit(1)
    if score == 700:
        with open('flag.txt', 'r') as f:
            print(f.read())
            exit(0)
    score += 1
