import gmpy2
from Crypto.Util.number import bytes_to_long
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

flag_enc = base64.b64decode(open('4ad2e982a9014053bc65a0785dcd4f8c/flag.enc', 'rb').read())
c = bytes_to_long(flag_enc)
pub = RSA.importKey(open('4ad2e982a9014053bc65a0785dcd4f8c/pubkey.pem').read())
n = pub.n
e = pub.e

# p和q的顺序有影响,长时间解不出来换下顺序
q = 184333227921154992916659782580114145999
p = 336771668019607304680919844592337860739

while True:
    try:
        n = p * q
        phi = (p-1)*(q-1)
        d = int(gmpy2.invert(e, phi))
        privkey = RSA.construct((int(n), int(e), int(d), int(p), int(q)))
        key = PKCS1_v1_5.new(privkey)
        enc = key.decrypt(flag_enc, b"")
        print(enc)
        break
    except ValueError:
        print("generating new primes")
        p = gmpy2.next_prime(p**2 + q**2)
        q = gmpy2.next_prime(2*p*q)
        e = gmpy2.next_prime(e**2)