from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2
def egcd(a,b):
    if b==0:
        return a,1,0
    else:
        g,x,y=egcd(b,a%b)
        return g,y,x-a//b*y

c1=bytes_to_long(open('c2d6e7158d7b4cd6a747774f0bdc5f72/cipher1.txt','rb').read())
c2=bytes_to_long(open('c2d6e7158d7b4cd6a747774f0bdc5f72/cipher2.txt','rb').read())

pub1=RSA.importKey(open('c2d6e7158d7b4cd6a747774f0bdc5f72/publickey1.pem').read())
pub2=RSA.importKey(open('c2d6e7158d7b4cd6a747774f0bdc5f72/publickey2.pem').read())
n1= pub1.n
e1= pub1.e
n2= pub2.n
e2= pub2.e

assert n1==n2


s1=gmpy2.invert(e1,e2)
s2=egcd(e1,e2)[2]

if(s1<0):
    s1=-s1
    c1=gmpy2.invert(c1,n1)
if(s2<0):
    s2=-s2
    c2=gmpy2.invert(c2,n1)
m=long_to_bytes((pow(c1,s1,n1)*pow(c2,s2,n1))%n1)
print(m)