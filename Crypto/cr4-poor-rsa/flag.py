import base64
import gmpy2
from Crypto.PublicKey import RSA
import rsa

with open("bf930316910b451c94c41ce8a9d851a8/key.pub", "rb") as file:
    key = file.read()

print(key)
pub = RSA.importKey(key)
n = pub.n
e = pub.e
print("n = ", n)
print("e = ", e)

p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901
phi_n = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)
print("d = ", d)

priv = rsa.PrivateKey(n, e, d, p, q)

with open("bf930316910b451c94c41ce8a9d851a8/flag.b64", "rb") as file:
    cipher = file.read()
cipher = base64.b64decode(cipher)
flag = rsa.decrypt(cipher, priv).decode()
print(flag)