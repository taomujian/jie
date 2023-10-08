# 恶臭的数据包

## 解题思路

> 下载附件后,得到1个pcap文件,wireshark打开,发现wifi流量包,用airdecap-ng爆破密码,然后用密码解密流量

```
aircrack-ng cacosmia.cap -w TOP300.txt

airdecap-ng cacosmia.cap -e mamawoxiangwantiequan -p 12345678
```

> 打开解密后的流量包,搜索flag等关键字符,找到了flag.txt中,隐藏在一个png图片中,提取出16进制数据,然后010 Editor打开导入数据保存为图片,foremost得到一个压缩包,尝试伪加密和爆破没有结果.

> 发现请求包里有一个Cookie,发现是jwt token,jwt解码得

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJoaW50IjoiZm9yIHNlY3VyaXR5LCBJIHNldCBteSBwYXNzd29yZCBhcyBhIHdlYnNpdGUgd2hpY2ggaSBqdXN0IHBpbmdlZCBiZWZvcmUifQ.P3xOErNrUkYqdMBoo8WvU63kUVyOkZjiTK-hwOIIS5A

{
  "hint": "for security, I set my password as a website which i just pinged before"
}
```

> 可以看到压缩包解压密码为某个域名,查找dns数据包,尝试解密,发现解压密码是26rsfb.dnslog.cn,解压得到flag

## flag

> flag{f14376d0-793e-4e20-9eab-af23f3fdc158}

## 参考

> https://blog.csdn.net/qq_29977871/article/details/125919876