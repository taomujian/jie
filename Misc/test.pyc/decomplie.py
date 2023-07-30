import base64

str = 'jYygTOy' + 'cmNycWNyYmM1Ujf'

def flag1():
    code = str[::-3]
    result = ''
    for i in code:
        ss = ord(i) - 1
        result += chr(ss)
    
    print(result[::-1])


def flag2():
    code = str[::-2]
    result = ''
    for i in code:
        ss = ord(i) - 1
        result += chr(ss)
    
    print(result[::-2])


def flag3():
    pass
# WARNING: Decompyle incomplete

flag1()
flag2()