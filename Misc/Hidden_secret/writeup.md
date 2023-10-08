# Hidden_secret

## 解题思路

> 下载附件后得到3个文件,里面是16进制字符,开头分别是03 04,01 02,05 06,这有可能是zip压缩包的三个组成部分,压缩源文件数据区,压缩源文件目录区,压缩源文件目录结束标志.只不过每个文件都缺少一个50 4B的标记.手工给加上就行了,最后合并得到一个压缩包文件.

> 解压后得到一个txt和jpg文件,txt文件里有提示,jpg文件后面隐藏了1.txt,因题目有问题,看不到,这是NTFS交换数据流隐写,用下面的命令读取即可

```
notepad.exe 1.jpg:1.txt
```

> 得到一串乱码字符,用解码得到flag.

```
K<jslc7b5'gBA&]_5MF!h5+E.@IQ&A%EExEzp\X#9YhiSHV#
```

## flag

> unctf{cca1a567c3145b1801a4f3273342c622}