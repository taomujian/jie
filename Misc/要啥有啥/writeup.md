# 要啥有啥

## 解题思路

> 下载附件得到1个pcapng文件,分析发现存在各种协议的流量.

> 分析FTP流量,发现利用proftp的洞：CVE2015-3306，获得了192.168.138.136的shell，写到web目录下一个1.php一句话。

> 继续分析HTTP流量,发现通过另外一台机器连菜刀，down下来了两个文件：xor.jpg和whoami.jpg。名字提示很明显，xor，没有挖坑，所以两个文件xor一下得到可运行的python代码，逆向这段代码可获得AES_KEY{}

> 将xor.jpg异或后得到

```
encrypt="cc90b9054ca67557813694276ab54c67aa93092ec87dd7b539"
```

> 脚本解密AES得到key值

```
AES_key{FK4Lidk7TwNmRWQd}
```

> 发现dns流量较多，存在部分异常，tshark提取，将其中base64部分进行重组

```
tshark -r aaca5ef838e04ee085c8c30a35cf336a.pcapng -T fields -e dns.qry.name|tr -s '\n'|awk -F '.' '{if
($1~/\S{19}/) print $1}'
```

> 得到

```
shell OYzmTh2MGNclc5gALl+ 2lJ/xu58d4dAtidJc2w 4dRhB1cuh/pXAt17QSj EIFMPiSE6w+DXpXJk9z m0FD39MGvwL4ZNpr2Yn dIPnjnb0W3xNeP+e5r/ /GhTYkNTdPo4xpT4d+H MihDB1mZNcQ8Gib69l5 NlqC8PFjEeABWPfJezq G0LozsEjukHJOCMhVlR rirtkI7/ExFZAgH+G1i /gaw84nJ0DbGXQEpA2w ySh6/iXeJD1ZYgt7jRg KLCL6CGggxsAEP9+m3Q Mvw3nE7h3GtoC0xqGKm jboBW7h+WyH+QhJRd1E L+Qc7cgRAaVNYwWrWDM ByHOIlSig+MvEg0GTih cnuNdgRpD4fgmEgjvAv ScqJkQUes+Mxbi4NNkC v6YANnbGFbZSUVs3Ybu lPu6Xzj+/nBmJcOsti9 4BHja8Cjym4l2qpmIkj R6kONAs2e7uAkduLR1z
```

> AES解密，并将上述base64补充完整得到flag.

## flag

> LCTF{CVE20153306A11_1n_0ne_Pcap}
