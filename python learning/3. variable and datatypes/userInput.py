#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

inp=input()
pr(inp)
nl()

inp=input('enter the ip address:')
pr(inp)
nl()

while True:
    inp=input('Enter the ip:')
    pr('>>> {}'.format(inp))
    if inp=='exit':
        break
    else:
        pr('exploiting...')
        nl()
