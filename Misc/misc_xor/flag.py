content = open('cipher.txt', 'r').read()
key = ord(content[0]) ^ ord('f')
print(''.join([chr(ord(i) ^ key) for i in content]))