from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long 
import string 
import random 
import sys
import base64
import hashlib
from Crypto.Cipher import AES 

sys.set_int_max_str_digits(65535)

m = "token=5t43g5g2j1;admin=0;group=0" 
c = base64.b64decode("bMPWOsg+YH0eSwchPY6HTEvf3ESETSrEQ3/M1d0lUm0=")


def cbc_bit_attack_mul(c, m, position, target):
    l = len(position)
    r = c # Convert c to a mutable bytearray
    for i in range(l):
        change = position[i]-16
        tmp = bytes(chr(ord(m[position[i]])^ord(target[i])^c[change]), 'utf-8')
        r = r[0:change]+tmp+r[change+1:]
    return r

def gen_iv(seed):
    s=random.Random()
    s.seed(seed)
    while True:
        iv=long_to_bytes(s.randint(0xfffffffffffffffffffffffffffffff,0xffffffffffffffffffffffffffffffff))
        if hashlib.sha256(iv).hexdigest()[0:4]==hashlib.sha256(long_to_bytes(seed)).hexdigest()[0:4]:
            return iv
        
def gen_password(seed):
    s=random.Random()
    s.seed(seed)
    while True:
        password=long_to_bytes(s.randint(0xfffffffffffffffffffffffffffffff,0xffffffffffffffffffffffffffffffff))
        if hashlib.sha256(password).hexdigest()[4:8]==hashlib.sha256(long_to_bytes(seed)).hexdigest()[4:8]:
            return password


seed = cbc_bit_attack_mul(c, m, [23, 31], ['1','1'])
seed = int(hashlib.sha256(seed).hexdigest(), 16)
iv = gen_iv(seed)
password = gen_password(seed)
cipher = AES.new(password, AES.MODE_CBC, iv)
with open('82bad951e0684e13872c872e3fdac14d/heheda.txt', 'rb') as reader:
    flag_enc = reader.read()
    flag_enc = bytes.fromhex(flag_enc.decode('utf-8')) 
    
flag = cipher.decrypt(flag_enc)
flag = flag[:-16]
flag = int(flag)

a = long_to_bytes(flag)
b = base64.b32decode(a)
b = base64.b64decode(b)
b = base64.b64decode(b)
b = base64.b32decode(b)
b = base64.b64decode(b)
b = base64.b64decode(b)
b = base64.b64decode(b)
b = base64.b64decode(b)
b = base64.b16decode(b)
b = base64.b16decode(b)
b = base64.b64decode(b)
b = base64.b32decode(b)
b = base64.b64decode(b)
b = base64.b64decode(b)
b = base64.b64decode(b)
print(b)
