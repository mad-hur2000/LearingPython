#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

def nl():
    print('\t')

def pr(a):
    print(a)

alist=[]
blist=[]
clist=[]
count=0
total=0

c=open('saagcir.txt','r')
h=open('heightSaag.txt','r')

for a in c:
    alist +=[int(a)]
for b in h:
    blist +=[int(b)]

if len(alist)==len(blist):
    for x in alist:
        # pr("no.{}  c={}  h={}  vol={}")
        clist= alist[x]*alist[x]*blist[x]/1808.64
        total= total + clist
        count+=1
        pr(f'no.{count}     c={alist[x]}    h={blist[x]}    vol= {clist:.2f}')
print(f'\ntotal volume:{total:.2f}')
 
    # vol_cubeft=(cir*cir*height)/2304
    # pr(vol_cubeft)  




# 0.0004340   2304
# 0.0005530   1808
# 4.340
# 5.530