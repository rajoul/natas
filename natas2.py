import requests,re


username="natas1"
password="gtVrDuiDfck831PqWsLEZy5gyDz1clto"

url=str("http://%s.natas.labs.overthewire.org" %username)

r=requests.post(url,auth=(username,password))

print(r.text)
if re.findall('The password (.*)',r.text):
    print('good')

#<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->