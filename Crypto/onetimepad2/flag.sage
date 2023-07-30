import binascii
from os import urandom
from sage.all import *

def process1(m, k):
    res = 0
    for i in bin(k)[2:]:
        res = res << 1;
        if (int(i)):
            res = res ^ m
        if (res >> 128):
            res = res ^ P
    return res

def process2(a, b):
    res = []
    res.append(process1(a[0], b[0]) ^ process1(a[1], b[2]))
    res.append(process1(a[0], b[1]) ^ process1(a[1], b[3]))
    res.append(process1(a[2], b[0]) ^ process1(a[3], b[2]))
    res.append(process1(a[2], b[1]) ^ process1(a[3], b[3]))
    return res

def nextrand(rand):
    global N, A, B
    tmp1 = [1, 0, 0, 1]
    tmp2 = [A, B, 0, 1]
    s = N
    N = process1(N, N)
    while s:
        if s % 2:
            tmp1 = process2(tmp2, tmp1)
        tmp2 = process2(tmp2, tmp2)
        s = s / 2
    return process1(rand, tmp1[0]) ^ tmp1[1]

def str2num(s):
    return int(s.hex(), 16)

def num2str(n, block=16):
    s = hex(n)[2:].strip('L')
    s = '0' * ((32-len(s)) % 32) + s
    return s.decode('hex')

def keygen():
    key = str2num(urandom(16))
    while True:
        yield key
        key = nextrand(key)
        
def encrypt(message):
    length = len(message)
    pad = '\x00' + urandom(15 - (length % 16))
    to_encrypt = message + pad
    res = ''
    generator = keygen()
    f = open('key.txt', 'w') # This is used to decrypt and of course you won't get it.
    for i, key in zip(range(0, length, 16), generator):
        f.write(hex(key)+'\n')
        res += num2str(str2num(to_encrypt[i:i+16]) ^ key)
    f.close()
    return res
 
plain = "One-Time Pad is used here. You won't know that the flag is flag{".encode()
ct = binascii.unhexlify("0da8e9e84a99d24d0f788c716ef9e99cc447c3cf12c716206dee92b9ce591dc0722d42462918621120ece68ac64e493a41ea3a70dd7fe2b1d116ac48f08dbf2b26bd63834fa5b4cb75e3c60d496760921b91df5e5e631e8e9e50c9d80350249c")
P = 0x100000000000000000000000000000087
A = 0xc6a5777f4dc639d7d1a50d6521e79bfd
B = 0x2e18716441db24baf79ff92393735345
N = str2num(urandom(16))
assert N != 0

vals = []
for i in range(0, 64, 16):
    vals.append(str2num(plain[i:i+16]) ^ str2num(ct[i:i+16]))
    print("KEY %02d" % i, hex(vals[-1]))
 
p0 = vals[0]
p1 = vals[1]
uppp = process1(p1, A ^ 1) ^ B
down = process1(p0, A ^ 1) ^ B
down = pow1(down, 2**128-2)  # inversion
AN = process1(uppp, down)
print("A^N", AN)
 
def ntopoly(npoly):
    return sum(c*X**e
        for e, c in enumerate(Integer(npoly).bits()))
 
X = GF(2).polynomial_ring().gen()
poly = ntopoly(P)
F = GF(2**128, modulus=poly, name='a')
a = F.fetch_int(A)
an = F.fetch_int(AN)
 
N = int(discrete_log(an, a))
# takes ~1 minute
# N = 76716889654539547639031458229653027958
assert a**N == an
 
def keygen2(key):
    while True:
        yield key
        key = nextrand(key)
 
K = vals[0]
print("K", K)
print("N", N)
print(encrypt(ct, keygen2(K)))