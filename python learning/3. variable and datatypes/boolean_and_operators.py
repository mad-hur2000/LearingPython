#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)
    nl()

def ty(b):
    print(type(b))

def pb(c):
    pr(c)
    ty(c)
    nl()

valid=True
notValid=False    # small f in 'false' is not allowed

pr(valid)
pr(notValid)

pr(valid == True)
pr(notValid == True)

pr(valid != True)
pr(notValid != True)

pr(not valid)
pr(not notValid)

pr((9 < 8) == True)  # is same as # pr((9 < 8))     
pr((9 > 8) == True)  # is same as # pr((9 > 8))
pr((9 <= 8) == True)  # is same as # pr((9 <= 8))
pr((9 >= 8) == True)  # is same as # pr((9 >= 8))
pr((9 == 8) == True)  # is same as # pr((9 == 8))
pr((9 != 8) == True)  # is same as # pr((9 != 8))

pr('-------------')
pr(5 > 6 and 5 < 6)
pr(5 > 6 or 5 < 6)

pr(bool(0))
pr(bool(1))
pr(bool(0) == False)
pr(bool(1) == True)
pr('-------------')

pr(10 + 10)
pr(10 - 10)
pr(10 / 10)
pr(10 // 10)
pr(10 * 10)
pr(10 ** 10)
pr(10 % 10)

pr(10 / 3)
pr(10 // 3)
pr(10 % 3)

x=10
pr(x)
x = x + 1
pr(x)
x+=1
pr(x)
x-=1
pr(x)
x*=5
pr(x)
x/=5
pr(x)

x=13
pr(bin(x))
print(bin(x)[2:].rjust(4,'0'))

y=5
print(bin(y)[2:].rjust(4,'0'))

print('and')
print(bin(x & y)[2:].rjust(4,'0'))
pr(x & y)

print('or')
print(bin(x | y)[2:].rjust(4,'0'))
pr(x | y)

print('shift right')
print(bin(x >> 1)[2:].rjust(8,'0'))
pr(bin(x >> 2)[2:].rjust(8,'0'))

print('shift left')
print(bin(x << 1)[2:].rjust(8,'0'))
print(bin(x << 2)[2:].rjust(8,'0'))


