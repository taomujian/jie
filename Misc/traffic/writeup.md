# traffic

## 解题思路

> 下载附件得到一个pcapng文件,wireshark打开,分析协议发现只有简单的icmp、dns和tls包,icmp只有heiheihei!!和不定长的aaa,判断是icmp包在长度上有问题

> tshark提取出相应的长度,看着像是ascii码,发现是乱码,那可能是需要偏移下,爆破得到flag.

```
tshark -r d0a836756fbb48509f0f51f1f5d4dca4.pcapng -Y "icmp" -T fields -e frame.len | tr "\n" ","
```

## flag

> flag{1CmPG@M3}
