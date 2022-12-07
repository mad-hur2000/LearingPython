#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

def ty(b):
    print(type(b))

def pb(c):
    pr(c)
    ty(c)
    nl()

int=1
pb(int)

float=1.0
pb(float)

complexnum=3.5j
pb(complexnum)

hexa=0xa
pb(hexa)

octal=0o12
pb(octal)

binary=0b11101
pb(binary)

addition=int+hexa+octal
pb(addition)

absolute=abs(-5.9)
pb(absolute)

pr(round(4.6))
pr(round(4.5))  # even round off to lower
pr(round(3.5))  # odd round off to upper
pr(round(4.4)) 

pr(bin(8))   # to print binary of number
pr(hex(18))   # to print hex of number
pr(oct(8))   # to print octal of number