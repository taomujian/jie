import Crypto.interesting1.flag as flag
import hashlib
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
from Crypto.Cipher import AES
import random


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
def gen_seed():
    iv=flag.iv
    key=flag.key
    evil=flag.evil
    m="token=5t43g5g2j1;admin=0;group=0"
    c="bMPWOsg+YH0eSwchPY6HTEvf3ESETSrEQ3/M1d0lUm0=".decode("base64")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    testc = cipher.encrypt(m)
    assert testc==c
    assert "admin=1" in evil
    assert "group=1" in evil
    cipher = AES.new(key, AES.MODE_CBC, iv)
    monster = cipher.encrypt(evil)
    counter=0
    for i in range(len(monster)):
        if monster[i]!=c[i]:
            counter+=1
    assert counter==2
    return int(hashlib.sha256(monster).hexdigest(),16)


def main():
    msgtemp=str(int(flag.encode(flag.flag),16))
    msg=msgtemp+"A"*(16-len(msgtemp)%16)
    seed=gen_seed()
    iv=gen_iv(seed)
    password=gen_password(seed)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    c = cipher.encrypt(msg)
    open("heheda.txt","w").write(c.encode("hex"))

if __name__ == '__main__':
    main()