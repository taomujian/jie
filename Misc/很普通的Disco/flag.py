#!/usr/bin/python3

s ='110011011011001100001110011111110111010111011000010101110101010110011011101011101110110111011110011111101'
flag = ''
for i in range(0,len(s),7):
    c_flag = s[i:i+7]
    flag += chr(int(c_flag,2))
    
print(flag)