import os,sys
from Crypto.Util.number import*

os.chdir(sys.path[0])

f = open('e05281b9394c4032b443f9793b76be2a/key','rb').read()
c = bytes_to_long(f)
bin_out = bin(c)[2:].zfill(12*8)   #将key文本内容转换为 2 进制数，每个字节占 8 位

R = bin_out[0:19]  #取输出序列的前19位
mask = 0b1010011000100011100

def lfsr(R,mask):
    output = (R << 1) & 0xffffffff
    i=(R&mask)&0xffffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
    output^=lastbit
    return (output,lastbit)

#根据生成规则，初始状态最后一位拼接输出序列
#我们可以猜测seed的第19位（0或1），如果seed19+R[:18]输出值等于R[:19]，那么就可以确定seed值了
def decry():
    cur = bin_out[0:19]      #前19位 2 进制数
    res = ''
    for i in range(19):
        if lfsr(int('0'+cur[0:18],2),mask)[0] == int(cur,2):
            res += '0'
            cur = '0'+cur[0:18]
        else:
            res += '1'
            cur = '1' + cur[0:18]
    return int(res[::-1],2)

r = decry()
print(bin(r))