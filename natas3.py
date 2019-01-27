import requests,re


username="natas2"
password="ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url=str("http://%s.natas.labs.overthewire.org/files/users.txt" %username)

r=requests.post(url,auth=(username,password))

print(r.text)

#natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14