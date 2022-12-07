#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

def nl():
    print('\t')

def pr(a):
    print(a)

f=open('saag.txt','a')

for a in range(1,86):
    f.write(str(a))
    f.write('--\n')
f.close()