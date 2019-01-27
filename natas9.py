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

