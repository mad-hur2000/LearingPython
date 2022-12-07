#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)
    nl()

def ty(b):
    print(type(b))

def pb(c):
    pr(c)
    ty(c)
    nl()

stra='mad'
strb='nis'
stra='mad005'
print(stra,strb)
nl()

print("string is immutable, keeps value in heap memory's string pool. and keeps name address pair in stack")
straa='madhur'
strbb='nisarg'
strcc='madhur'
print(straa)
print(strbb)
print(strcc)
print(id(straa))
print(id(strbb))
print(id(strcc))


strc='''long
one'''
pr(strc)

strd='i\'m a string d'
pr(strd)

stre="i'm a string e"
pr(stre)

strf="I\"m a string f\nI\"m on a newline."
pr(strf)
strg='\\ \x31 \x42 \x43'
pr(strg)

strh='aaaaa'
pr(strh)
strh='a' * 10
pr(strh)
pr(len(strh))

pr('string' in strd)
pr('mad' in strd)

pr(strd.startswith('i'))
pr(strd.startswith('I'))

pr(strd.index('str'))

pr(strd.upper())
pr(strd.lower())

messy_str='   messy string '
pr(messy_str)
pr(messy_str.strip())
pr(messy_str.replace('str','string').strip())
pr(messy_str.replace('string','example').strip())

pr(messy_str.split())
pr(messy_str.split('s'))

print(strd)
print(strd.encode())
pr(strd.encode('utf-8'))

print(strd.rjust(25))
pr(strd.rjust(25,'x'))
print(strd.ljust(25))
pr(strd.ljust(25,'x'))

print('i am ' + 'string d')
# print('string d is ' + str(len(strd)) ' characters long.')  ## plus '+' missing
# print('string d is ' + len(strd) + ' characters long.')  ## cant concatenate string with int
pr('string d is ' + str(len(strd)) + ' characters long.')

print(1 + 1)
print('1'+'1')
print(type('1'+'1'))
ty(print('1'+'1')) ## something new
nl()

#format method
print('stringd is {} characters long.'.format(len(strd)))
print('{} {} {}'.format(len(strd), 5.0, 0x12))
print('{0} {2} {1}'.format(len(strd), 5.0, 0x12))
pr('{length} {two} {one}'.format(length=len(strd), two=5.0, one=0x12))
lengths=len(strd)
print(f'stringd is {lengths} characters long.')
print(f'stringd is {lengths:.2f} characters long.')
print(f'stringd is {lengths:.4f} characters long.')
print(f'stringd is {lengths:x} characters long.')
print(f'stringd is {lengths:b} characters long.')
pr(f'stringd is {lengths:o} characters long.')
 
print('stringd is %d characters long.' % len(strd))
print('stringd is %f characters long.' % len(strd))
print('stringd is %x characters long.' % len(strd))
