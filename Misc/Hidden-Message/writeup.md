# Hidden-Message

## 解题思路

> 下载附件,得到一个pcap文件,追踪UDP流,发现一串字符,没有发现可疑之处.这时查看pcap包,发现数据包都一样,就是端口不一样,怀疑端口在隐藏信息,可以用tshark或者把包导出为json用python解析得到flag.

## payload

```
tshark -r hidden-message.pcap -Tfields -e udp.srcport | while read port; do echo -n ${port: -1}; done | tr 01 10 | perl -lpe '$_=pack"B*",$_' Heisenberg
```

## flag

> Heisenberg
