from Crypto.Util import number

key = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890{}_#&'

out = 'WhcuU0o4Vc0VUasJc08W04uJ0qd2IJpVJ02V04p'

P = 23
Q = 63

len = 67

invP = number.inverse(P , len)

def decrypt(c):
    flag = ''
    for e in c:
        print(e,key.find(e))
        pos = (key.find(e) - Q + len) % len
        tmp = pos * invP % len
        flag += key[tmp]
    return flag

print('hsct' + decrypt(out) + '}')