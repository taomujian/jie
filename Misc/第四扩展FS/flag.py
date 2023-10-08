f = open("file.txt","r")
txt = f.read().replace(" ","")
f.close()
d = {}
for i in txt:
    d[i] = d.get(i,0)+1

ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse =True)
for i in ls:
    print(i[0],end="")
