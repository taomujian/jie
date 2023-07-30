import os 

oldtime = 2000000000
flag = ""

for i in range(0, 47): #有0~46个txt文件 就是循环47次
    file = "stego/{0}.txt".format(i)  #调用文件路径 记得复制自己的文件路径 不要搬用我的
    newtime = int(os.path.getmtime(file))  #获取最近修改的时间
    s = newtime - oldtime
    flag = flag + chr(s)
   
print(flag)