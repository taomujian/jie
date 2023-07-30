from functools import reduce
import gmpy2
from Crypto.Util.number import *

p = [868019, 875543, 597263]
q = [913799, 904727, 890459]
C = [0x8D5051562B, 0x5FFA0AC1A2, 0x6008DDF867]
B = [0xFFEEE,0xFFFEE,0xFEFEF]
def CRT(moudle,a):
    M = reduce((lambda x,y : x * y),moudle)
    result = 0
    for mi in moudle:
        Mi = M // mi
        inv_Mi = gmpy2.invert(Mi,mi)
        result = (result + a[moudle.index(mi)] * Mi * inv_Mi) % M
    return result % M

for i in range(0,len(p)):
    for a1 in [m_p for m_p in range(p[i]) if (C[i] % p[i]) == (m_p * (m_p + B[i])) % p[i]]:
        # 遍历所有小于p[i]的值
        for a2 in [m_q for m_q in range(q[i]) if (C[i] % q[i]) == (m_q * (m_q + B[i])) % q[i]]:
            # 遍历所有小于q[i]的值
            x = CRT([p[i],q[i]],[a1,a2])
            try:
                if "2" not in bytes.decode(long_to_bytes(x)): # 简单过滤掉了一个不是flag的又是可见字符的字符串
                    print(bytes.decode(long_to_bytes(x)),end="")
            except:
                continue
