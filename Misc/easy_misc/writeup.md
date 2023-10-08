# Easy_Misc

## 解题思路

> 下载附件得到一个zip文件,直接解压提示要密码,binwalk无果,看来是真加密,爆破zip文件得到密码,解压后得到一个图片,是一个百度网盘链接,但是没有提取码,说明图片有问题(爆破百度网盘提取码是不太可能的),爆破CRC得到完整的图片,下载文件得到一个流量包文件

> wireshark打开,过滤http协议包,发现是sql注入,使用tshark提取flag相关数据

```
tshark -r file.pcap -T fields -e urlencoded-form.value | grep flag > data.txt
```

> 编写脚本得到flag数据

## flag

> flag{cd2c3e2fea463ded9af800d7155be7aq}
