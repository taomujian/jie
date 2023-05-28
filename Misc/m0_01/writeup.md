# M0_01

## 解题思路

> 附件为流量包,发现属于usb键鼠流量.发现data数据为8字节,4字节为鼠标流量,8字节为键盘流量.运行下面的命令提取数据:

```
tshark -r 12.pcapng -T fields -e usb.capdata > out.txt
```

> 只有01248，猜测为云影加密,解密得到flag

## flag

> flag{THISISFLAG}