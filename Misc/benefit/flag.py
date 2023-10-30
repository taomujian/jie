s = 'DJECQDJEARTJECRTBAARDJECRTBACQDJACRTBECRTJEARTBACQTBAARTBECRDJECQTJAARDJECQTBEAQTBACQTJECQDBECRDJACQTBACQDJACRDBACRTBECQTBACQDBEARTBEARTJACQDJACQTJEARTBACQTJECQDBEAQTJEARDJEARDJACRDBEAQTBACQTJEARTJAARTJECQDJAARDJAAQTJEARTBACQTJEARTJACRDJECQDJAARDJAARDBACRTJACQTBECQDJACQDBACQDJEAR'

def xor(s1, s2, z):
    rt = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            rt += str(z[i])
        else:
            rt += str(1 - z[i])
    return rt

cmp = 'DJECQ'
a = {}
cnt = 0

def dfs(s, dep):
    if dep == 5:
        ans = ''
        for i in range(len(s) // 5):
            ans += xor(cmp, s[i * 5:(i + 1) * 5], a)
        flag = b''
        for i in range(len(ans) // 7):
            flag += int(ans[i * 7:(i + 1) * 7], 2).to_bytes(1, byteorder='big')
        print(flag.decode('utf-8'))  # Print the flag as a UTF-8 string
        # print(int(ans, 2).to_bytes(35 * 8, byteorder='big'))  # Print the flag as bytes
        # print(len(int(ans, 2).to_bytes(35 * 8, byteorder='big')))  # Print the length of the bytes
        # print(hex(int(ans, 2))[2:])  # Print the flag as a hexadecimal string
        global cnt
        cnt += 1
        # print(cnt)
        return
    a[dep] = 1
    dfs(s, dep + 1)
    a[dep] = 0
    dfs(s, dep + 1)

print(len(s))
dfs(s, 0)
