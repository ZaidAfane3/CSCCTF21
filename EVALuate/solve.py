from pwn import *

conn = remote('127.0.0.1', 1234)

print(conn.recvuntil('SOW!'))
print(conn.recvline())

while True:
    eq = conn.recvline().strip().decode()
    print(eq)
    ans = eval(eq)
    print(ans)
    conn.recvuntil('> ')
    conn.sendline(str(ans))
