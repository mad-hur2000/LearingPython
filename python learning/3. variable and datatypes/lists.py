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

items=['aaaaa','bbbbb','ccccc']
pb(items)

numbers=[18,72,3,13,19,14,45]
pb(numbers)

list1=['a', 1, 2.0, ['mad'],[], list(), ('A','b'), False]
pb(list1)
pr(list1[0])
pr(list1[1])
pr(list1[3][0])
pr(list1[3][-1]) # when only one element, 0 and -1 act similar
pr(list1[4])
pr(list1[-2])
nl()


repeat= ['join '] *5  
#is same as # repeat= ['join '] *5
pb(repeat)

item1 , item2, item3 = items
pr(item1)
pr(item2)
pr(item3)
nl()


pr(items)
pr('aaaaa' in items)
pr('ccccc' in items)
pr('ddddd' in items)
nl()

#mutable
items[0]='zzzzz'
pr(items)

pr('---------delete and insert')
del items[0]
pr(items)

items.insert(0,'aaaaa')
pr(items)
nl()

pr('-----------delete and insert differently as list1')
del items[0]
pr(items)

items=['aaaaa'] + items
pr(items)

items.append('ddddd')
pr(items)

pr(max(items))
pr(min(items))

pr(items.index('ccccc'))
pr(items[items.index('ccccc')])

pr('both methods to reverse the list1')
items.reverse()
pr(items)

items=items[::-1]
pr(items)

pr(items.count('aaaaa'))
items.append('aaaaa')
pr(items)
pr(items.count('aaaaa'))

items.pop()
pr(items)

items2=['eeeee','fffff']
pr(items2)

items.extend(items2)
pr(items)

items2.clear()
pr(items2)

pr(numbers)
numbers.sort()
pr(numbers)

numbers.sort(reverse=True)
pr(numbers)
nl()

pr(items)
items3=items
pr(items3)

items3[2]='mad'
pr(items3)
pr(items)
pr('--------now copy')

items[2]='ccccc'
items4=items.copy()
pr(items)
pr(items4)

items4[2]='mad'
pr(items)
pr(items4)

pr(numbers)

numbers2= list(map(float,numbers))
pr(numbers2)

numbers3=tuple(map(int,numbers2))
pr(numbers3)
