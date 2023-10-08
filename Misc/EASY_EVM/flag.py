from functools import reduce
from Crypto.Util.number import long_to_bytes,bytes_to_long

def egcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q

def chinese_remainder(pairs):
    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product//x for x in mod_list]
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x

if __name__=='__main__':
    result = chinese_remainder([(231412341286754812414291, 193913535844325315514675), (126381254785148123414597, 59349569214207838388981), (438712649816519864511367, 153559101645126489682469)])
    Least_common_multiple = 231412341286754812414291 * 126381254785148123414597 * 438712649816519864511367
    for i in range(1, 100000):
        print(i)
        flag = Least_common_multiple * i + result
        flag = long_to_bytes(flag)
        if b'flag{' in flag:
            print(flag)
            break