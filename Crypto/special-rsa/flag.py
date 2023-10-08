import binascii
import msgpack
import sys
sys.setrecursionlimit(10000)

def egcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return (b, 0, 1)
    else:
        d, x, y = egcd(b, (a - b * (a // b)))
        return (d, y, x - y * (a // b))
    
def modinv(a, N):
    d, x, y = egcd(N, a)
    assert d == 1
    return y % N

def npow(a, b):
    global N
    ret = 1
    if b != 0:
        if b < 0:
            ret *= modinv(pow(a, -b, N), N)
        else:
            ret *= pow(a, b, N)
    return ret

N = 23927411014020695772934916764953661641310148480977056645255098192491740356525240675906285700516357578929940114553700976167969964364149615226568689224228028461686617293534115788779955597877965044570493457567420874741357186596425753667455266870402154552439899664446413632716747644854897551940777512522044907132864905644212655387223302410896871080751768224091760934209917984213585513510597619708797688705876805464880105797829380326559399723048092175492203894468752718008631464599810632513162129223356467602508095356584405555329096159917957389834381018137378015593755767450675441331998683799788355179363368220408879117131

with open('7a407f44a073442c91fd395b20594f01/msg.enc', 'rb') as f:
    msg_enc = f.read()
    # print len(msg_enc)
    
with open('7a407f44a073442c91fd395b20594f01/msg.txt', 'r') as f:
    msg_plain = f.read()
    # print msg_plain
    
def pad_even(x):
    return ('', '0')[len(x) % 2] + x

m = []
for i in range(0, len(msg_plain), 256):
    ms = msg_plain[i:i+256]
    m.append(int(binascii.hexlify(ms.encode()), 16))
    
print('m')
print(m, len(m))

r = []
c = []
for r_s, c_s in msgpack.unpackb(msg_enc, raw=True):
    r.append(int(binascii.hexlify(r_s), 16))
    c.append(int(binascii.hexlify(c_s), 16))
    
print('r =')
print(r, len(r))
print('')
print('c =')
print(c, len(c))
print('')
_, a, b = egcd(r[0], r[1])

k1 = (modinv(m[0], N) * c[0]) % N
k2 = (modinv(m[1], N) * c[1]) % N

k = npow(k1, a) * npow(k2, b) % N

print('k =')
print(k)
print('')

flag = open("7a407f44a073442c91fd395b20594f01/flag.enc", "rb").read()
flag = msgpack.unpackb(flag, raw = True)
r3 = int(binascii.hexlify(flag[0][0]), 16)
c3 = int(binascii.hexlify(flag[0][1]), 16)
m3 = (c3 * pow(modinv(k, N), r3, N)) % N
# 将 m3 转换为字节对象
print(bytes.fromhex(hex(m3)[2:-2]))
