#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)
    

def ty(b):
    print(type(b))

def pb(c):
    print(c)
    ty(c)
    nl()
pr('''sets are not ordered
so, no index values are there
so 
seta[2] cannot be printed
they do not have duplicates
also they can have multiple datatypes\n''')

seta={'a','b','c'}
pb(seta)

setb={'a','a', 'a'}
pr(setb)
pr(len(setb))
nl()
setc={'a',1,0.5,True}
pb(setc)

setd=set(('b',5,True))
pb(setd)

seta.add('d')
print(seta)
nl()

setc.update(setd)
pr(setc)  #0 is equal to False and 1 is equal to True
nl()

lista=['a','b','c']
setd={4,5,6}
print(lista,setd)
setd.update(lista)
pr(setd)
nl()
sete={1,2,3}
print(setd,sete)
setf=setd.union(sete)
pr(setf)
nl()
pr('can\'t remove second time with remove method, instead use discard')
setf.remove(4)
pr(setf)
# setf.remove(4)
# pr(setf)

setf.discard(5)
pr(setf)
setf.discard(5)
pr(setf)
pr('only use pop method if you dont care about order')

setf.pop()
pr(setf)