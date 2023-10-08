import os
import base64

def base():
    data = 'base/'
    files = os.listdir(data)
    for file in files:
        try:
            f = open(data + file)  # 返回一个文件对象
            string = f.read()  # 调用文件的 read()方法
            t3 = base64.b16decode(string)
            t2 = base64.b16decode(t3)
            t1 = base64.b32decode(t2)
            t0 = base64.b32decode(t1)
            f.close()
            print(t0)
        except Exception as e:
            f.close()
            print(file,'file error!!')

if __name__=='__main__':
    base()