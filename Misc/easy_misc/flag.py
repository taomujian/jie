import re

with open("data.txt", "rb") as f:
    contents = f.read()
    res = re.compile(r'0,1\),(\d+),1\)\)=(\d+),').findall(str(contents))
    dic = {}
    for a, b in res:
        if a in dic:
            if int(b) > dic[a]:
                dic[a] = int(b)
        else:
            dic[a] = int(b)
    flag = ""
    for i in range(1,40): #1~39
        flag += chr(dic[str(i)])
    print(flag)