from Crypto.Util.number import *
from secret import flag
import  random
import hashlib
import os

key=os.urandom(8)
def rand(rng):
    return rng - random.randrange(rng)
m=[]
random.seed(int(hashlib.md5(key).hexdigest(), 16))
for i in range(len(flag)):
    rand(256)
    xor=flag[i]^rand(256)
    m.append(xor)
print(m)
print(bytes_to_long(key)>>12)

# [140, 96, 112, 178, 38, 180, 158, 240, 179, 202, 251, 138, 188, 185, 23, 67, 163, 22, 150, 18, 143, 212, 93, 87, 209, 139, 92, 252, 55, 137, 6, 231, 105, 12, 65, 59, 223, 25, 179, 101, 19, 215]
# 2669175714787937