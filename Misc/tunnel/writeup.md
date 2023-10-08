# Tunnel

## 解题思路

> 下载附件后,得到1个pcap文件,Wireshark打开,发现很多DNS流量,结合题目名字可知是DNS隧道分析.

> 发现全是有base64的dns域名请求,使用tshark提取A记录的域名
```
tshark -Y "ip.dst==8.8.8.8  && dns.qry.type == 1" -r tunnel.pcap | awk '{print $(NF)}' | awk -F '.' '{print $1}' > b64.txt
```

> 使用脚本进行解码拼接,得到一个加密的zip：

> 但是flag.zip需要使用密码解密,猜测是base64解密,然后使用base64隐写脚本得到密码

> 得到压缩密码B@%MG"6FjbS8^c#r

> 然后解压得到flag图片

## flag

> flag{D01n't_5pY_0nmE}