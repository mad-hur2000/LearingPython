#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')


def pr(a):
    print(a)
    nl()


lista = ['a', 'b', 'c']
pr(lista)

listb = [x for x in lista]
pr(listb)

listc = [x for x in lista if x == 'b']
pr(listc)

listd = [x for x in range(5)]
pr(listd)

liste = [hex(x) for x in range(5)]
pr(liste)

listf = [hex(x) if x > 0 else 'x' for x in range(5)]
pr(listf)

listg = [x*x for x in range(5)]
pr(listg)

listh = [a for a in range(5) if a == 0 or a == 1]
pr(listh)

listi = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
pr(listi)

listj = [b for a in listi for b in a]
pr(listj)
# think for listj like below for loop
# print b for a in listi , for b in a
for a in listi:
    for b in a:
        print(b)

# also available for lists and set and string etc.

seta={x+x for x in range(5)}
pr(seta)

listk=[m for m in 'Mad005']
pr(listk)

pr(''.join(listk))
pr('-'.join(listk))
# pr(''.join(seta))
# join is allowed on strings

# longer form
listl=[]
for a in 'string':
    listl.append(a)
pr(listl)