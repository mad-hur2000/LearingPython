#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)
    

a=1
pr(a)
a=1
pr(a)
a=1
pr(a)
nl()

a=1
while a<3:
    pr(a)
    a += 1
nl()

for i in [0,1,3,4]:
    pr(i+5)
nl()

for i in range(3):
    pr(i+6)
nl()

for i in range(3):
    for j in range(3):
        print(i,j)
nl()
pr('break to terminate loop')
for i in range(5):
    if i==2:
        break
    print(i)
nl()
pr('continue to skip to next iteration')
for i in range(5):
    if i==2:
        continue
    print(i)
nl()
pr('pass, when there is no code . if dont want to type any code or keep it empty, use pass')
for i in range(5):
    if i==2:
        pass # if no any code, then wrie pass
    print(i)
nl()

for c in 'something':
    pr(c)

nl()

for key,value in {'a':1, 'b': 2, 'c':3}.items():
    print(key,value)
