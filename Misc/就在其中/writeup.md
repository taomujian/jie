# 就在其中

## 解题思路

> 下载附件得到一个pcap文件,foremost分离,得到一个key.txt,打开是乱码,应该是加密了.wireshark打开pcap文件,发现访问了很多文件,有一个test.key文件,里面是RSA私钥,把私钥内容打开保存下来,用这个私钥解密key.txt这个文件得到flag.

```
openssl rsautl -decrypt -in key.txt -inkey private.txt -out flag.txt
```

## flag

> flag{haPPy_Use_0penSsI}
