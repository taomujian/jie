# Unknown-format

## 解题思路

> 下载附件得到一个pcap文件,

> 分析发现此为kindle传输数据的流量包,使用工具kindletool(https://github.com/NiLuJe/KindleTool)

```
kindletool dm usb_sniff.pcap out
```

> binwalk发现这个文件是一个gz文件,直接解压会错误,用binwalk -e解压,得到一个新的gz文件,解压得到一个文件,010 Editor text模式打开,搜索ctf,得到flag.

## flag

> ALEXCTF{Wh0_N33d5_K1nDl3_t0_3X7R4Ct_K1ND13_F1rMw4R3}