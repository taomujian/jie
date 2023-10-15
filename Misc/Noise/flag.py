
key = 'GoodLuckToYou'
flag = ''
with open('badd3e0621ff43de8cf802545bbd3ed0', 'rb') as f:
    con = f.read()
    for i in range(len(con)):
        print(con[i])
        flag += chr(con[i] ^ ord(key[i % 13]))

with open('flag.txt', 'w', encoding = 'utf-8') as f:
    f.write(flag)