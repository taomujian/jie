import re
import os

def decode(x):  #如果按照正常算法得到的是synchsafe integer，解析成 真正的整数大小
    a = x & 0xff;
    b = (x >> 8) & 0xff;
    c = (x >> 16) & 0xff;
    d = (x >> 24) & 0xff;
    x_final = 0x0;
    x_final = x_final | a;
    x_final = x_final | (b << 7);
    x_final = x_final | (c << 14);
    x_final = x_final | (d << 21);
    return x_final
 
def encode(x): #和上边相反
    a = x & 0x7f;
    b = (x >> 7) & 0x7f;
    c = (x >> 14) & 0x7f;
    d = (x >> 21) & 0x7f;
    
    x_final = 0x0;
    x_final = x_final | a;
    x_final = x_final | (b << 8);
    x_final = x_final | (c << 16);
    x_final = x_final | (d << 24);
    return x_final

files = open('1.mp3', 'rb')   # 以二进制打开文件
result = ''
head = files.read(10)[7:]
# id3, ver, revision, flag, length  = struct.unpack("!3sBBBI",head);
mp3_size = decode(int.from_bytes(head, 'big', signed = False))  # 将字节字符串转换为十进制数字
n = mp3_size + 12
total_lenth = os.path.getsize('1.mp3')

# 提取
while n < total_lenth:  # 结束位置
    files.seek(n, 0)
    head = files.read(1)   #读取一个字节（8位）
    padding = '{:08b}'.format(ord(head))[-2]  # 该字节的倒数第一位是private的值
    private = bin(ord(head))[-1]
    result += private
    n += 418 if padding == "1" else 417

# 拼接
flag = ''
textArr = re.findall('.{' + str(8) + '}', result)
for i in textArr:
    flag = flag + chr(int(i, 2)).strip('\n')
print(flag)