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

items=('itema','itemb','itemc')
pb(items)

numbers=(1,2,3)
pb(numbers)

repeat= ('join ',) *5
pb(repeat)
repeat= ('join ') *5  #this will be string * 5 if no comma 
pb(repeat)              

mixed=('abc', 12 , ('abcd',56))
pb(mixed[0])
pb(mixed[1])
pb(mixed[2])
pb(mixed[2][0])
pb(mixed[2][1])

item1 , item2, item3 = items
pr(item1)
pr(item2)
pr(item3)
nl()

pr(items)
pr('itema' in items)
pr('itemc' in items)
pr('itemd' in items)

pr(items)
pr(items[0])
pr(items[1])
pr(items[2])
pr(items[-1])
pr(items[-2])
pr(items)
pr(items[0-3])
pr(items[0:2])
pr(items[:1])
pr(items[:2])
pr(items[-3:-1])
pr(items[-2:])

## strings can be done same way