import base64
import string
from Crypto.Util.strxor import strxor

dict = string.ascii_letters + string.digits + ".?!'\",;: ()-" + chr(10)

with open('2d9f626b97254c7b8c56c3e311ac6be6/cipher.txt', 'r') as f:
    cipher = base64.b64decode(f.read())

def enc(data, key):
    key = (key * (len(data) / len(key) + 1))[:len(data)]
    return strxor(data, key)

def getkey(i,j):
    list=[]
    for a in dict:
        for b in dict:
            if ord(a) ^ cipher[i] == ord(b) ^ cipher[j]:
                list.append(chr(ord(a) ^ cipher[i]))
    return set(list)

key = ''
for a in range(1,30):
    key_len = a
    group = len(cipher) // key_len   #组数
    key = ""
    for i in range(key_len):
        k = getkey(0 * key_len + i, 1 * key_len + i)    #第一组
        for j in range(1, group - 1):
            k = k & getkey(j * key_len + i, j * key_len + key_len + i)     #每次取交集
        key += ''.join(list(k))
        
    if key:
        break
    
