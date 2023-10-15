import base64
from Crypto.Cipher import DES3
from hashlib import md5
 
v1 = b'\x55\x75\xff\xf0\x02\xa5'
v2 = b'\x55\x75\x7c\xff\x00\xa9'
v3 = b'\x55\x75\x7d\xfc\x30\xa8'
v4 = b'\x30\x80\x03\x3f\xfd\x55\x5a\x80'
key = base64.b64encode(v1+v2+v3)
print('key:',key)
print('m:',v4)
c = DES3.new(key, DES3.MODE_ECB)
cipher = base64.b64encode(c.encrypt(v4))
sn = key + cipher
assert(md5(sn+b'Welcome/to/this/very/simple/challenge').hexdigest() == '44e4403b63620a2075d3fb2e0a6207d2')
print('sn:', sn.decode())