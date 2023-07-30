# 奇怪的TTL字段

## 解题思路

> 下载附件得到一个txt文本,里面是一些ttl的值,一共只出现了4个数字63,127,191,255

> 常见操作系统的TTL值:

```
UNIX 及类 UNIX 操作系统 ICMP 回显应答的 TTL 字段值为 255
Compaq Tru64 5.0 ICMP 回显应答的 TTL 字段值为 64
微软 Windows NT/2K操作系统 ICMP 回显应答的 TTL 字段值为 128
微软 Windows 95 操作系统 ICMP 回显应答的 TTL 字段值为 32
LINUX Kernel 2.2.x & 2.4.x ICMP 回显应答的 TTL 字段值为 64
```

> 把63,127,191,255转换为二进制,如下:

```
63： 00111111
127：01111111
191：10111111
255：11111111
```

> 只有最高两位不同,后面没有思路了,写一个脚本,把二进制的数转换成图片,得到的图片是个残缺的二维码图片,binwalk发现这个图片隐藏了很多其他图片,foremost进行分离,得到了其他图片碎片,拼接成完整二维码,得到key:AutomaticKey cipher:fftu{2028mb39927wn1f96o6e12z03j58002p}

> 根据key的信息得知是AutomaticKey加密,在线解密得到flag.

## flag

> flag{2028ab39927df1d96e6a12b03e58002e}

## 参考

> https://www.wishingstarmoye.com/ctf/autokey