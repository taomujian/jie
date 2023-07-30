import binascii
from Crypto.Util.strxor import strxor

def supa_encryption(s1, s2):
    res = [chr(0)]*12
    for i in range(len(res)):
        q = s1[i]
        d = s2[i]
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

def add_pad(msg):
    L = 24 - len(msg)%24
    msg += chr(L)*L
    return msg

with open('beginners-luck-40/BITSCTFfullhd.png', 'rb') as reader:
    enc_data = reader.read()

png_header = binascii.unhexlify(b'89504E470D0A1A0A0000000D494844520000078000000438')

key = strxor(enc_data[0:24], png_header)

png_data = b''
for i in range(0, len(enc_data), 24):
    enc = strxor(enc_data[i:i+24], key)
    png_data += enc
    
with open('flag.png', 'wb') as f:
    f.write(png_data)
