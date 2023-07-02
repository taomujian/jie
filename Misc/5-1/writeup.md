# 5-1

## 解题思路

> 下载附件得到一个文件,binwalk没有探测出来格式.未知类型文件,用xortool尝试

> -c表示出现频率最高的字符,这个需要根据经验,比如文本内容一般是空格(20),二进制文件一般是00

```
xortool badd3e0621ff43de8cf802545bbd3ed0 -c 20
```
> 尝试出了key：GoodLuckToYou,对原文件进行异或得到flag

## flag

> wdflag{You Are Very Smart}

## 参考

> https://github.com/hellman/xortool
> https://github.com/raddyfiy/xortool-for-Windows
