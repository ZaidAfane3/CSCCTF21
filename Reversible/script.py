from secret import KEY

with open('flag.txt', 'r') as f:
    flag = f.read().strip()

cipher = b''
x = 0
for i in flag:
    cipher += chr(ord(i) ^ ord(KEY[x % len(KEY)])).encode()
    x += 1

with open('cipher.enc', 'w') as f:
    f.write(cipher.decode())
