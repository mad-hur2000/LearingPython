#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

from pwn import *

def nl():
    print('\t')

def pr(a):
    print(a)
    nl()

pr(cyclic(50))
pr(cyclic_find('laa'))
pr(cyclic_find('laaa'))

pr(shellcraft.sh())
pr(hexdump(asm(shellcraft.sh())))

## to connect local process 

# p=process('/bin/sh')
# p.sendline('echo mad;')
# p.interactive()

## to connect remote process 

# r= remote('127.0.0.1', 1234)
# r.sendline('hello mad!')
# r.interactive()
# r.close()

pr(p32(0x13371337))
pr(hex(u32(p32(0x13371337))))

l=ELF('/bin/bash')

pr(hex(l.address))
pr(hex(l.entry))

pr(hex(l.got['write']))
pr(hex(l.plt['write'])) 

for address in l.search(b'/bin/sh\x00'):
    pr(hex(address))

pr(hex(next(l.search(asm('jmp esp')))))

r=ROP(l)
pr(r.rbx)

pr(xor('A','B'))
pr(xor(xor('A','B'),'A'))

pr(b64e(b'test'))
pr(b64d(b'dGVzdA=='))

pr(md5sumhex(b'hello'))
pr(sha1sumhex(b'hello'))

pr(bits(b'a'))
pr(unbits([0, 1, 1, 0, 0, 0, 0, 1]))


