with open("enc/enc.txt", 'rb') as f:
    c = f.read().hex()
print(c)
flag = [int(str(c)[i:i+2], 16) for i in range(0, len(c), 2)] #16进制转换为10进制
print(flag)

key = 'hello world'
s = [i for i in range(256)]
t = [key[i % len(key)] for i in range(256)]

j = 0
for i in range(256):
    j = (j + int(s[i]) + int(ord(t[i]))) % 256
    s[i], s[j] = s[j], s[i]

i = 0
j = 0
x = 0
for m in range(37):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i], s[j] = s[j], s[i]
    x = (s[i] + (s[j] % 256)) % 256
    flag[m] = flag[m] ^ s[x]

print(flag)
print(''.join(chr(c) for c in flag))
