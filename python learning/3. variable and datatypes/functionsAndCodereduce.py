#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

def funa():
    pr('funa')
funa()
funa()
nl()

def funb():
    return 'i\'m fun b'
funb()
b = funb()
pr(b)
nl()

def func(a):
    pr('\t{}'.format(a))
func('func')
func('func with another arg')
nl()

# two args
def fund(a, b):
    pr('{} {}'.format(a, b))
fund('its a', 'its b')
fund(a='any',b='order')
fund(b='any',a='order')
nl()

def fune(a='default arg a'):
    pr('{}'.format(a))
fune()
fune('given arg')
nl()

# multiple aregs
def funf(a, *more):
    pr('{} {}'.format(a,' '.join([a for a in more])))
funf('mad')
funf('mad','a')
funf('mad','a','b','c')
nl()

def fung(**ks):
    for a in ks:
        print(a,ks[a])
fung(a='a',b='b',c='c')
nl()
fung(a='a',b='b')
nl()

def funh(s,f,i,l):
    pr(type(s))
    pr(type(f))
    pr(type(i))
    pr(type(l))
funh('str',3.45, 4, ['hello',4,6.4])
nl()

v=100
pr(v)

def funi():
    pr(v)
funi()
nl()

def funj():
    v=5
    pr(v)
    v += 1
    pr(v)
funj()
nl()

# v can be accessed by global keyword otherwise v is only readable
def funk():
    global v
    pr(v)
    v += 1
    pr(v)
funk()
pr(v)
nl()

def funj():
    pr('hello from fun j')
def funk():
    pr('hello from fun k')
funj()
funk()
nl()

def funl():
    pr('fun l')
    funj()
    funk()
funl()
nl()

# def funm(a):
#     pr(a)
#     funm(a-1)
# funm(1)

def funn(a):
    pr(a)
    if a > 0:
        funn(a-1)
funn(5)
nl()

def funo(a):
    while a > 0:
        pr(a)
        a -= 1
funo(5)       