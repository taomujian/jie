from Crypto.Cipher import DES

f = open('5b8bcb28546b4423b481b13149abc99f/ciphertext', 'rb')
ciphertext = f.read()
f.close()
IV = b'13245678'
KEY = b'\x00\x00\x00\x00\x00\x00\x00\x00'
a = DES.new(KEY, DES.MODE_OFB, IV)
plaintext = a.decrypt(ciphertext)
print(plaintext.decode(errors ='ignore'))

KEY = b'\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F'
a = DES.new(KEY, DES.MODE_OFB, IV)
plaintext = a.decrypt(ciphertext)
print(plaintext.decode(errors ='ignore'))

KEY = b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"
a = DES.new(KEY, DES.MODE_OFB, IV)
plaintext = a.decrypt(ciphertext)
print(plaintext.decode(errors ='ignore'))

KEY = b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
a = DES.new(KEY, DES.MODE_OFB, IV)
plaintext = a.decrypt(ciphertext)
print(plaintext.decode(errors ='ignore'))