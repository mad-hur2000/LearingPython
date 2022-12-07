#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

def nl():
    print('\t')

def pr(a):
    print(a)

import sys

pr(sys.version)
pr(sys.executable)
pr(sys.platform)

# for line in sys.stdin:
#     if line.strip() == 'exit':
#         break
#     sys.stdout.write('>> {}'.format(line))

for i in range(1,5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

for i in range(1,5):
    print(i)

import time 

for i in range(0,51):
    time.sleep(0.01)
    sys.stdout.write('{} [{}{}]\r'.format(i, '#'*i,'.'*(50-i)))
    sys.stdout.flush()
sys.stdout.write('\n')
nl()

pr(sys.argv)

if len(sys.argv) !=3:
    pr('[x] to run {} enter username and password as cmd line arguments'.format(sys.argv[0]))
    sys.exit(5)
nl()

username = sys.argv[1]
password = sys.argv[2]

pr('username is "{}" and password is "{}"'.format(username, password))
nl()

pr(sys.path) 
nl()
# pr(sys.modules)
sys.exit(0)