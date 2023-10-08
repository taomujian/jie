import base64

dec = b""

with open("b64.txt","r") as f:
    for line in f.readlines():
        tmp = line.strip()
        missing_padding = len(tmp) % 4
        if missing_padding != 0:
            tmp += '='* (4 - missing_padding)
        dec += base64.b64decode(tmp.encode())

print(len(dec))

with open('flag.zip', 'wb') as f:
    f.write(dec)

with open("b64.txt", "r") as f:
    x = f.readlines()

for i in x:
    i = i.strip()
    l = 4 - len(i) % 4
    if l != 4:
        i += "="* l
        with open('flag.txt', 'a') as writer:
            writer.write(i + '\n')

def inttobin(a, n):
    ret = bin(a)[2:]
    while len(ret) < n:
        ret = '0' + ret
    return ret

table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
f = open("flag.txt", "r")
tmpbin = ''
res = ''
line = f.readline()
while line:
    if line[-2] == '=':
        if line[-3] == '=':
            tmpbin += inttobin(table.index(line[-4]), 6)[2:]
        else:
            tmpbin += inttobin(table.index(line[-3]), 6)[4:]
    line = f.readline()
quotient = int(len(tmpbin)/8)
for i in range(quotient):
    res += chr(int(tmpbin[8*i:8*i+8], 2))

print(res)