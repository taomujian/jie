# coding=utf-8
import gmpy2
import libnum
import os
import base64
import re


def rsa(c,m):
    #print(type(c),16)
    c = int(c, 16)
    m = int(m, 16)
    n1 = 1696206139052948924304948333474767
    e = 0x10001
    d1 = 37191940763524230367308693117833
    n2 = 3104649130901425335933838103517383
    d2 = 1427000713644866747260499795119265
    a1 = pow(m, e ,n1)
    a2 = pow(c, d2, n2)
    a1 = libnum.n2s(a1)
    a2 = libnum.n2s(a2)
    return a1, a2

datas = []
flag = []

for i in open("data.txt","r").readlines():
    i = base64.b64decode(i)
    datas.append(i)
    
parsed_data = []
for item in datas:
    seq = int(item.split(b'SEQ = ')[1].split(b';')[0])
    parsed_data.append((seq, item))

# 按照 SEQ 值进行排序
sorted_data = sorted(parsed_data, key=lambda x: x[0])
for line in sorted_data:
    line = line[1]
    data = line.split(b'DATA = ')[1].split(b'L; SIG')[0]
    sig = line.split(b'SIG = ')[1].split(b'L')[0]
    result = rsa(data, sig)
    flag.append(result)
    
flag1 = b""
for i in flag:
    if i[0] == i[1]:
        flag1 += i[0]
        
print(flag1.decode())