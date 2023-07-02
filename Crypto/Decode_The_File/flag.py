from string import ascii_uppercase, ascii_lowercase, digits
from Crypto.Util.number import long_to_bytes

base = ascii_uppercase + ascii_lowercase + digits + '+/'
result = []
for line in open('1a351e90fb2b476a929d1e2666d7c511', 'r').readlines():
    line = line.strip()
    if '==' in line:  # 如果是编码一个字节
        result.append(bin(base.find(line[-3]))[2:].rjust(6, '0')[2:])
    elif '=' in line:  # 如果是编码两个字节
        result.append(bin(base.find(line[-2]))[2:].rjust(6, '0')[4:])

ret = ''.join(result)
print(long_to_bytes(int(ret[:ret.rfind('1') + 1], 2), 2).decode())