# Latlong

## 解题思路

> 下载附件得到文件,用file命令发现是一个wav文件,修改后缀.播放后发现是一段无线波信号.

> multimon-ng是一个专门解码aprs、psk等业余无线电数字通信协议的工具

> 在使用multimon-ng前,需要先用sox把wav转为raw

```
sox -t wav 997a0b28705f4ef086acfb7e1b932336 -esigned-integer -b16 -r 22050 -t raw latlong.raw
multimon-ng -t raw -a AFSK1200 latlong.raw
```

## flag

> flag{f4ils4f3c0mms}
