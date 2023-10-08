f = open('84de1b2a1a23450ca9dec4b10bced50c.txt','r')
s = f.read()
s = bytes.fromhex(s)
flag = ''
key = '23\xffSY\x8b'
length = len(key)
for i in range(len(s)):
    flag += chr(s[i] ^ ord(key[i%length]))
    
print(flag)