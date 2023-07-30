import gmpy2
import libnum
from Crypto.Util.number import *

d_p = 0xd5a225c0d41b16699c4471570eecd3dd7759736d5781aa7710b31b4a46e441d386da1345bc97d1aa913f853f850f6d4684a80e6067fb71cf213b276c2cbaed59
d_q = 0x1338c593d3b5428ce978bed7a553527155b3d138aeac084020c0c67f54b953015e55f60a5d31386505e02e6122dad7db0a05ecb552e448b347adc2c9170fa2f3
e = 65537
p = 0
q = 0
for k_p in range(1, e):
    if (e*d_p - 1) % k_p == 0:
        p = (e*d_p - 1) // k_p + 1
        if gmpy2.is_prime(p):
            break
        
for k_q in range(1, e):
    if (e*d_q - 1) % k_q == 0:
        q = (e*d_q - 1) // k_q + 1
        if gmpy2.is_prime(q):
            break

n = p * q
e = 65537

phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
with open('92d8c7449d614543a0f9da8f05e39bbe/flag.enc','rb') as f:
    flag = f.read()
    
c = bytes_to_long(flag)
m = gmpy2.powmod(c, d, n)
flag = long_to_bytes(m)
print(flag)