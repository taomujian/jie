# running

## 解题思路

> 下载附件,看格式是个doc文档,查看属性,是自解压文件,说明其实是个zip文件,解压后得到一个exe和word文件,word文件打开后什么信息都没有,exe文件执行后,有一个tif文件,修改后缀为tif,看到是一个图片,用PS打开,去掉图层,得到一个提示.用010 Editor打开exe文件,在结尾处找到一串字符,根据提示编写脚本,得到flag.

```
bytearray=b"njCp1HJBPLVTxcMhUHDPwE7mPW"

flag="flag{"

for i in range(len(bytearray)):
    if i % 2==0:
        c=bytearray[i]
        c-=1
        flag+=chr(c)

    else:
        c=bytearray[i]
        c+=1
        flag+=chr(c)

flag+="}"
print (flag)
```

## flag

> flag{mkBq0IICOMUUwdLiTICQvF6nOX}
