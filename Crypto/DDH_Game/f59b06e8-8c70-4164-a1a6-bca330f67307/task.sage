from secret import flag
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import getRandomRange

assert flag.startswith(b'CatCTF{')
assert flag.endswith(b'}')

# BLS-12-381 but with my own G!
p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
K = GF(p)
a = K(0x00)
b = K(0x04)
E = EllipticCurve(K, (a, b))
E.set_order(0x73EDA753299D7D483339D80809A1D80553BDA402FFFE5BFEFFFFFFFF00000001 * 0x396C8C005555E1568C00AAAB0000AAAB)

G = E(3745324820672390389968901155878445437664963280229755729082200523555105705468830220374025474630687037635107257976475, 2578846078515277795052385204310204126349387494123866919108681393764788346607753607675088305233984015170544920715533)
n = G.order()

# Embedding degree of this curve
k = 12

m = Integer(bytes_to_long(flag[7:-1]))
sols = m.bits()

DDH_instances = []

for i in range(len(sols)):
    a = getRandomRange(1, n)
    b = getRandomRange(1, n)
    c = 0
    if sols[i] == True:
        c = a * b % n
    elif sols[i] == False:
        c = getRandomRange(1, n)
        assert a*b*G != c*G
    
    ins = ((a*G).xy(), (b*G).xy(), (c*G).xy())
    DDH_instances.append(ins)

with open('DDH_instances.txt', 'w') as f:
    f.write(str(DDH_instances))