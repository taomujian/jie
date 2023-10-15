from PIL import Image

img = Image.open('00000001.png')
m1 = m2 = ''
# 取大图二进制
for y in range(0, img.size[0], 19):
    for x in range(0, img.size[1], 19):
        r,g,b,a = img.getpixel((x,y))
        m1 += str(r & 1)
# 取中间隐写图二进制
for y in range(171, 171 + 19):
    for x in range(171, 171 + 19):
        r,g,b,a = img.getpixel((x,y))
        m2 += str(a & 1)
# 二进制串取异或
xor = ''.join(str(int(A)^int(B)) for A,B in zip(m1,m2))
# 二进制转字符串并输出
print(''.join(chr(int(xor[i:i+8], 2)) for i in range(0, len(xor), 8)))