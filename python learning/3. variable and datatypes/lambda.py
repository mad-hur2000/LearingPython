#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

def add_5(x): return x+5
pr(add_5(5))
nl()

def add(a, b): return a+b
pr(add(3,4))
nl()
# similar results as lambda function add
def addfun(a,b):
    return a+b
pr(addfun(3,4))
nl()
# lambda in one line directly 
pr((lambda a,b : a + b )(3,4))
nl()

is_even = lambda a:a%2==0
pr(is_even(2))
pr(is_even(3))
nl()

# understanding of blocks.
pr([i for i in range (1,6,2)])
for i in range(0,5,2):
    pr(i)
blocks = lambda x, y : [x[i:i+y] for i in range(0,len(x), y)]
pr(blocks('string',2))
nl()

# ord is comprihension function which shows integer representation of characters
to_ord = lambda a: [ord(i) for i in a]
pr(to_ord('ABCD'))
nl()
#doing same as to_ord in other way
def to_ordfun(a):
    list=[]
    for i in a:
        list.append(ord(i))
    return list
pr(to_ordfun('abcd'))
# lambda can be harder to understand and maintain but can do everything in one line