from base64 import b64decode
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

def cal_k():
    with open('640f836b07464f359526983d88ad5b69/ps','r') as f:
        ps=[int(x) for x in f.read().split('\n')[:-1]]
    with open('640f836b07464f359526983d88ad5b69/r','r') as f:
        r=int(f.read())
    pbits=[bin(x).rfind('1')-2 for x in ps]
    bc=['0']*512
    for le in range(512):
        ind=pbits.index(511-le)
        tt=bin(r)[2:].rjust(512,'0')[511-le]
        if tt=='1':
            bc[ind]='1'
            r^=ps[ind]
    return int(''.join(bc),2)

def solve():
    with open('640f836b07464f359526983d88ad5b69/ef','rb') as f:
        ef=b64decode(f.read())
    key=long_to_bytes(int(md5(long_to_bytes(cal_k())).hexdigest(),16))
    aes_obj = AES.new(key, AES.MODE_ECB)
    return aes_obj.decrypt(ef)

if __name__=='__main__':
    print(solve())
