# 流量分析

## 解题思路

> 下载附件得到一个pcap文件

> wireshark打开,过滤http协议包,发现是sql注入,使用tshark提取flag相关数据

```
tshark -r 4d7c14206a5c4b74a0af595992bbf439.pcapng -T fields -e http.request.uri | grep flag > data.txt
```

> 编写脚本得到flag数据

## flag

> flag{c2bbf9cecdaf656cf524d014c5bf046c}