# uncompyle6 version 3.9.0
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Oct 30 2018, 23:45:53) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
# Embedded file name: pystego.py
# Compiled at: 2017-08-01 00:44:47
# Size of source mod 2**32: 1961 bytes
import sys, os, hashlib, time, base64
fllag = '9474yeUMWODKruX7OFzD9oekO28+EqYCZHrUjWNm92NSU+eYXOPsRPEFrNMs7J+4qautoqOrvq28pLU='

def crypto(string, op='encode', public_key='ddd', expirytime=0):
    ckey_lenth = 4
    public_key = public_key and public_key or ''
    key = hashlib.md5(public_key).hexdigest()
    keya = hashlib.md5(key[0:16]).hexdigest()
    keyb = hashlib.md5(key[16:32]).hexdigest()
    keyc = ckey_lenth and (op == 'decode' and string[0:ckey_lenth] or hashlib.md5(str(time.time())).hexdigest()[32 - ckey_lenth:32]) or ''
    cryptkey = keya + hashlib.md5(keya + keyc).hexdigest()
    key_lenth = len(cryptkey)
    string = op == 'decode' and base64.b64decode(string[4:]) or '0000000000' + hashlib.md5(string + keyb).hexdigest()[0:16] + string
    string_lenth = len(string)
    result = ''
    box = list(range(256))
    randkey = []
    for i in range(255):
        randkey.append(ord(cryptkey[i % key_lenth]))

    for i in range(255):
        j = 0
        j = (j + box[i] + randkey[i]) % 256
        tmp = box[i]
        box[i] = box[j]
        box[j] = tmp

    for i in range(string_lenth):
        a = j = 0
        a = (a + 1) % 256
        j = (j + box[a]) % 256
        tmp = box[a]
        box[a] = box[j]
        box[j] = tmp
        result += chr(ord(string[i]) ^ box[(box[a] + box[j]) % 256])

    if op == 'decode':
        if result[0:10] == '0000000000' or int(result[0:10]) - int(time.time()) > 0:
            if result[10:26] == hashlib.md5(result[26:] + keyb).hexdigest()[0:16]:
                return result[26:]
        return
    else:
        return keyc + base64.b64encode(result)


if __name__ == '__main__':
    while True:
        flag = input('Please input your flag:')
        if flag == crypto(fllag, 'decode'):
            print('Success')
            break
        else:
            continue
# okay decompiling 58cadd8d8269455ebc94690fd777c34a.pyc
