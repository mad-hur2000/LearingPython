#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

if True:
    pr('true')

if False:
    pr('false')

if not False:
    pr('not false')
nl()

if 1 < 1:
    pr('1 < 1')
elif 1 <= 0:
    pr('1 <= 0')
else:
    pr('else 1')
nl()

if 1 < 1:
    pr('1<1')
elif 1 <= 0:
    pr('1 <= 1')
elif 2 <= 2:
    pr('2 <= 2')
else:
    
    pr('else reached')


if 1 > 0 and 0 < 1 :
    pr('1 > 0 and 0 < 1')

if 1 > 0 and 0 > 1 :
    pr('1 > 0 and 0 > 1')   #will not be printed
nl()

if (1 > 0 or 0 < 1) and 1 ==  1 :
    pr('1>0 or 0<1 and 1 == 1')
    nl()
pr('ternary')

if 0 < 1 : pr('0 < 1')
pr('1 >= 1') if 1 >= 1 else pr('1 < 1')












