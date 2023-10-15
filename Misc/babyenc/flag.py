tmp = ""
with open('babyenc\\out.txt', 'r') as f:
    tmp = f.read()
    
test = list(map(ord, tmp))
for i in range(len(test) - 5):
    lis = list(map(ord, "RCTF{"))
    tmpi = i
    for j in range(len(test) - 5 - i):
        tmp = lis[j] ^ lis[j + 1] ^ lis[j + 4] ^ test[tmpi]
        tmpi += 1
        if chr(tmp) == "}":
            lis.append(tmp)
            print(str(i) + " results:" + ''.join(map(chr, lis)))
            break
        elif chr(tmp) == "\n":
            break
        elif tmp < 43:
            break
        else:
            lis.append(tmp)
# RCTF{te1l_mE_tHe_wAy_you_so1ve_thIs}
