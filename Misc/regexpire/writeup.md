# Pixel-Princess

## 解题思路

> 下载附件得到一个文件,binwalk+foremost得到一个压缩包和一张图片.

> 压缩包打开得到一张图片,上面是一个密码.

> 得到的第1张图片用Steghide隐写了,输入密码得到一个压缩包,解压得到flag.

```
steghide extract -sf 00000001.jpg
```


## flag

> flag{You_F0unD_M3}