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

dicta={'a':1,'b':'2','c':'3'}
pr(len(dicta))
pb(dicta)

pr(dicta['a'])
pr(dicta.get('a'))

pr(dicta.keys())
pr(dicta.values())
pr(dicta.items())
nl()

lista=list(dicta.items())
pb(lista)

pr('''no duplicates allowed
but updation is allowed''')
dicta['a']=5
pr(dicta)
dicta.update({'a':1})
pr(dicta)


dicta['d']=4
pr(dicta)
nl()

pr('removing with pop and del ')
dicta.pop('d')
pr(dicta)
del dicta['c']
pr(dicta)
nl()

pr('nasted dictionary')
dicta['c']={'a':'mad','b':'hur'}
pr(dicta)
nl()

pr('empty dictionary')
dictb={}
pr(dictb)
dictc= dict()
pr(dictc)