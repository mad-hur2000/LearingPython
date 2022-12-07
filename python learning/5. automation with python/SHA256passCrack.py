#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

from pwn import *
import sys

def nl():
    print('\t')


def pr(a):
    print(a)

if len(sys.argv) != 3:
    pr('Invalid number of arguments')
    pr('>> {} <sha256sum>'.format(sys.argv[0]))

hash_from_user=sys.argv[1]
password_file=sys.argv[2]
attemps=0

with log.progress('Attempting to crack: {}!\n'.format(hash_from_user)) as p:
    with open(password_file,'r',encoding='latin-1') as passowrd_list:
        for password in passowrd_list:
            password = password.strip('\n').encode('latin-1')
            password_hash = sha256sumhex(password)
            p.status('[{}] {} == {}'.format(attemps,password.decode('latin-1'),password_hash))
            if password_hash == hash_from_user:
                p.success('Password hash found!! attemps [{}] , {} hashes to  {}'.format(attemps,password.decode('latin-1'), password_hash))
                exit()
            attemps += 1
        p.failure('Password hash not found!')
