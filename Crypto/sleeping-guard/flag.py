import base64
import binascii
from Crypto.Util.strxor import strxor

data = open('data.txt', 'r').read()

cipher_data = base64.b64decode(data)

png_header = binascii.unhexlify(b'89504E470D0A1A0A0000000D')

key = strxor(cipher_data[0:12], png_header)
png_data = b''

for i in range(len(cipher_data) // len(key)):
    png_data = png_data + strxor(cipher_data[i * len(key) : (i + 1) * len(key)], key)

with open('flag.png', 'wb') as writer:
    writer.write(png_data)