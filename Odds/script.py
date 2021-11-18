import random
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

odds = ['H','T']

init = random.choice(odds)

print('This should be easy.')

score = 0
while True:
    print('[H]eads or [T]ails')
    choice = input('> ')
    if init.lower() == choice.lower():
        print('Nice')
        score += 1
    else:
        print('Wrong')
        exit(1)

    if init == 'H':
        init = 'T'
    elif init == 'T':
        init = 'H'
    
    if score == 500:
        with open('flag.txt', 'r') as f:
            print(f.read())
            exit()
    
