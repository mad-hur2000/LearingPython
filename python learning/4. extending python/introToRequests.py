#!/bin/python3
# import nl,pr,ty,pb from '/basic.py'

import requests

def nl():
    print('\t')

def pr(a):
    print(a)
    nl()

a = requests.get('http://httpbin.org/get')

pr(a.headers)
pr(a.headers['Server'])
pr(a.status_code)

if a.status_code == 200:
    pr('success')
if a.status_code == 404:
    pr('not found!')

pr(a.elapsed)
pr(a.cookies)
pr(a.content)
pr(a.text)

a= requests.get('http://httpbin.org/get', params={'id':'1'})
pr(a.url)

a= requests.get('http://httpbin.org/get?id=2')
pr(a.url)

a= requests.get('http://httpbin.org/get', params={'id':'3'}, headers={'Accept':'application/json', 'test_header':'test'})
pr(a.url)
pr(a.text)

a= requests.delete('http://httpbin.org/delete', params={'id':'4'})
pr(a.text)

a= requests.post('http://httpbin.org/post', data={'a':'b','c':'d'})
pr(a.text)

img={'image':open('image.jpeg','rb')}
a= requests.post('http://httpbin.org/post', files=img)
pr(a.text)

a=requests.get('http://httpbin.org/get', auth=('username','password'))
pr(a.text)

a= requests.get('https://expired.badssl.com', verify=False)
pr(a.text)

a=requests.get('http://github.com')
pr(a.headers)
# try to verify with curl

a=requests.get('http://github.com', allow_redirects=False)
pr(a.headers)

# a=requests.get('http://httpbin.org/get', timeout=0.01)
# pr(a.content)

a=requests.get('http://httpbin.org/cookies' , cookies={'mad': 'madmad'})
pr(a.content)
pr(a.text)
# pr(a.get('http://httpbin.org/cookies').text)

a=requests.Session()
a.cookies.update({'a':'b'})
pr(a.get('http://httpbin.org/cookies').text)
pr(a.get('http://httpbin.org/cookies').text)

a= requests.get('https://api.github.com/events')
pr(a.json())

a=requests.get('https://thumbs.dreamstime.com/b/beautiful-rain-forest-ang-ka-nature-trail-doi-inthanon-national-park-thailand-36703721.jpg')
with open('image2.jpeg','wb') as f:
    f.write(a.content)
f.close()