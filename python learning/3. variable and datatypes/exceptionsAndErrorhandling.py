#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

pr(1)
pr(2)

try:
    somethskjfkj
except:
    pr('the file dosen\'t exit')
nl()

try:
    f=open('1m0.txt')
except Exception as e:
    pr(e)
nl()

try:
    f=open('1m0.txt')
except FileNotFoundError:
    pr('file dosen\'t exist')
except Exception as e:
    pr(e)
finally:
    pr('this is final mesage..!')
nl()

try:
    fjsflkaj
    f=open('1m0.txt')
except FileNotFoundError:
    pr('file dosen\'t exist')
except Exception as e:
    pr(e)
nl()

n=10  #try with different values like 0 or 'mad' etc.
if n==0:
    raise Exception('n can\'t be 0!')
if type(n) is not int:
    raise Exception('n must be int!')
print(1/n)
nl()

n=0
assert(n != 0)  #for strict error handling
pr(1/n)

