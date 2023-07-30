import random
from gmpy2 import invert

key = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890{}_#&'        
flag = 'hsctf{'
flag = flag[flag.find("'") + 1:]
c0 = 'WhcuU0o4Vc0VUasJc08W04uJ0qd2IJpVJ02V04p'

def encrypt(m, a, b, kt):
    c = ''
    for mt in m:
        tmp = key.find(mt)
        k = kt
        for _ in range(len(c0)):
            tmp = tmp * a if k % 2 == 0 else tmp + b
            k = k // 2
        c += key[tmp % len(key)]
    return c

def get_params(limit):
    m = flag[4:6]
    for a in range(limit):
        for b in range(limit):
            for kt in range(limit):
                if (encrypt(m, a, b, kt) == c0[:2]):
                    return a, b, kt

a, b, kt = get_params(len(key))

def decrypt(c, a, b, kt):
    m = ''
    for ct in c:
        tmp = key.find(ct)
        k = kt
        for _ in range(len(c)):
            tmp = tmp * invert(a,len(key)) if k % 2 == 0 else tmp - b
            k = k // 2
        m += key[tmp % len(key)]
    return m

print('hsct' + decrypt(c0, a, b,kt) + '}')