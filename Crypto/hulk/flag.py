from zio import *

flag = ''
target = ('202.112.51.217', 9999)
dic = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}"

def get_payload(a, b, c):
    return ''.join(chr(ord(a[i]) ^ ord(b[i]) ^ ord(c[i])) for i in range(16))  # 使用 range 替换 xrange

def exp(i, payload):  # 在函数参数中使用 payload 替换 pay
    io = zio(target, timeout=5, print_read=COLORED(NONE, 'red'), print_write=COLORED(NONE, 'green'))  # 修改 print_read 和 print_write 的参数
    io.read_until(b'encrypt: 0x')  # 将字符串改为字节串
    pay1 = b'30' * (48 - i)  # 将字符串改为字节串
    io.writeline(pay1)
    io.read_until(b'ciphertext')
    data = io.read_until(b'Give')
    io.read_until(b'encrypt: 0x')
    ciphertext1 = data[data.find(b'0x')+2:-5]
    data1 = ciphertext1[64:96]
    tmp = (b'0' * (39 - len(flag + payload)) + flag + payload)[-16:]
    pay2 = get_payload(ciphertext1[32:64].decode('hex'), ciphertext1[-32:].decode('hex'), tmp).encode('hex')
    io.writeline(pay2)
    io.read_until(b"ciphertext")
    r2 = io.read_until(b"\n")
    ciphertext12 = r2[r2.find(b'0x')+2:r2.find(b'0x')+34]
    io.close()
    if data1 == bytes.fromhex(ciphertext12):  # 使用 bytes.fromhex 替换 decode('hex')
        return 1
    else:
        return 0

for i in range(1, 39):  # 使用 range 替换 xrange
    for pay in dic:
        if exp(i, pay):
            flag += pay
            print(flag)  # 在print语句中使用括号

print(flag)  # 在print语句中使用括号