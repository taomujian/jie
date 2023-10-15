# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 28 2021, 17:39:59)
# [GCC 10.2.1 20210110]
# Embedded file name: /home/ctf/bbb.py
# Compiled at: 2017-09-02 22:35:36
import random
key = 'ctf'
strr = '186,98,180,154,139,192,114,14,102,168,43,136,52,218,85,100,43'

def func1(str1, key):
    random.seed(key)
    str2 = ''
    for c in str1:
        str2 += str(ord(c) ^ random.randint(0, 255)) + ','

    str2 = str2.strip(',')
    return str2


def func2(str2, key):
    random.seed(key)
    str1 = ''
    for i in str2.split(','):
        i = int(i)
        str1 += chr(i ^ random.randint(0, 255))

    return str1

print(func1(strr, key))
print(func2(strr, key))
# okay decompiling data.pyc