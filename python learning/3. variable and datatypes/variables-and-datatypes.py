#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

def ty(b):
    print(type(b))

def pb(c):
    pr(c)
    ty(c)
    nl()

name='mad'
print(name)
print(type(name))
nl()

length=int('4')
print(length)
print(type(length))
nl()


list=['mad','nis','rut']
print(list)
print(type(list))
nl()


list1=[11,12,13]
print(list1)
nl()

# Assingning list values to variables

one,two,three=list1
print(one)
print(two)
print(three)
print(list1)
print(type(list1))
nl()

# this throws error
# one,two=list1
# print(one)
# print(two)

# copying list
list1=list
print(list1)
nl()

tuple=('nis','rut','mad')
print(tuple)
print(type(tuple))
nl()

dictonary={'1':'rut','2':'mad','3':'nis'}
print(dictonary)
print(type(dictonary))
nl()

bool=True
print(bool)
print(type(bool))
nl()

range=range(8)
print(range)
print(type(range))
nl()



bytes=b'mad'
print(bytes)
print(type(bytes))
