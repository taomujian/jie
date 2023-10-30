from sage.groups.generic import bsgs
 
K = GF(2^255-19)
e = K.gen()
 
base = e * 38377684164112914669201831650756813551072223314592288217929947158283532270268
ans = e * 0x66
 
bsgs(base, ans, (0, 25**11))