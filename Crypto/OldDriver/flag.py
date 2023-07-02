import gmpy2
import libnum
import json
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt

file = open("enc.txt", "r")
data = json.load(file)

list = []
for i in data:
    c = i['c']
    n = i['n']
    list.append((c, n))

c = []
n = []
e = 10
for cip_key in data:
    c.append(cip_key['c'])
    n.append(cip_key['n'])
    
resultant, mod = crt(n, c)
value, is_perfect = gmpy2.iroot(resultant, e)
print(long_to_bytes(value))