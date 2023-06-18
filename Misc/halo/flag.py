import string

from base64 import *

b = b64decode("aWdxNDs1NDFSOzFpa1I1MWliT08w").decode()
data = list(b)
for k in range(0,200):
    key=""
    for i in range(len(data)):
        key += chr(ord(data[i]) ^ k)
    print(key)