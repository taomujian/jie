# 工业协议分析1

## 解题思路

> 下载附件,得到了一个pcap文件,用wireshark打开,搜索字符串flag,搜索时要注意,在最左边可以搜索类型,是搜索包内容还是其他.搜索包内容关键字flag,得到了一个长度为10120的TCP流量包

> 然而通过多次分析与flag.txt相对应的流量包中,没有发现flag.txt的内容,于是换一个思路,对流量包进行关键字jpg、png、zip、rar、flag搜索,查看是否存在其他的文件。在linux系统中使用grep指令,可以对文件进行指定关键字搜索。我们使用指令进行关键字搜索

```
grep "flag" -a test.pacp
grep ".zip" -a test.pacp
grep ".jpg" -a test.pacp
grep ".png" -a test.pacp
```

> 最终,发现存在base64加密的png图片码,将图片码进行base64解码,解码后得到写有Flag的图片

> 也可以通过异常的命令或响应,异常的数据包长度,不常见的协议使用等思路直接筛选出这个图片,查看长度就可以直接看到.


## flag

> flag{ICS-mms104}