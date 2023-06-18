import random
import hashlib
from Crypto.Util.number import *

def rand(rng):
    return rng - random.randrange(rng)

okey = 2669175714787937 << 12
c = [140, 96, 112, 178, 38, 180, 158, 240, 179, 202, 251, 138, 188, 185, 23, 67, 163, 22, 150, 18, 143, 212, 93, 87, 209, 139, 92, 252, 55, 137, 6, 231, 105, 12, 65, 59, 223, 25, 179, 101, 19, 215]

for kk in range(2**12):
    key = long_to_bytes(okey + kk)
    flag = []
    random.seed(int(hashlib.md5(key).hexdigest(), 16))
    for i in range(len(c)):
        rand(256)
        f = c[i]^rand(256)
        flag.append(f)
    if all(c < 256 for c in flag):
        flag = bytes(flag)
        if(flag.startswith(b'flag')):
            print(flag, kk)
