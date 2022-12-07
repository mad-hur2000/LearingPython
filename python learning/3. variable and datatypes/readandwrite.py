#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'
def nl():
    print('\t')

def pr(a):
    print(a)

f=open('10.txt')
pr(f)

f=open('10.txt','rt')
pr(f)

pr(f.read())
pr(f.readlines())

f.seek(0)
pr(f.readlines())
nl()

pr('for file to be redable again, seek it to 0')
nl()

f.seek(0)
for line in f:
    pr(line.strip())

f.close()
nl()

# can't perform operations on closed files
# pr(f.readlines())   

f=open('text.txt','w')
f.write('this is mad\n')
f.write('this is mad again\n\n')
f=open('text.txt','r')
pr(f.read())

f=open('text.txt','w')
f.write(' Now rewriting this is mad\n')
f.write('this is mad again') 
f=open('text.txt','r')
# f.write('this is mad after read')
# can't write when open in read mode
pr(f.read())
nl()

f=open('text.txt','a')
f.write('\t Now appending hello mad') 
f=open('text.txt','r')
pr(f.read())
f.close()
nl()

pr(f.name)
pr(f.closed)
pr(f.mode)

with open('rockyou.txt', encoding='latin-1') as f:  ## there will be encoading error if encoading not specified
    for line in f:
        print(line)